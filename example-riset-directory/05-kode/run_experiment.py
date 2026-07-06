import os
import sys
import subprocess
import time
import json
import csv
from datetime import datetime

TSHARK_PATH = r"C:\Program Files\Wireshark\tshark.exe"
CONFIG_FILE = r"tool\config_experiment.json"
LOG_FILE = "experiment_log.csv"
RAW_DATA_DIR = "raw_data"

# Pastikan folder data mentah ada
if not os.path.exists(RAW_DATA_DIR):
    os.makedirs(RAW_DATA_DIR)

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_config(config):
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"Gagal menyimpan konfigurasi: {e}")

def check_tshark():
    global TSHARK_PATH
    if not os.path.exists(TSHARK_PATH):
        print(f"Tshark tidak ditemukan di: {TSHARK_PATH}")
        print("Silakan masukkan path lokasi file tshark.exe Anda (atau kosongkan untuk keluar):")
        custom_path = input("Path: ").strip()
        if not custom_path:
            sys.exit("Eksekusi dibatalkan. tshark.exe diperlukan.")
        # Hapus tanda kutip jika ada
        custom_path = custom_path.replace('"', '').replace("'", "")
        if os.path.exists(custom_path):
            TSHARK_PATH = custom_path
        else:
            sys.exit(f"File tidak ditemukan di path: {custom_path}. Keluar.")

def select_interface():
    config = load_config()
    if "interface" in config:
        saved_iface = config["interface"]
        # Pastikan interface yang tersimpan berupa path device (\Device\...) dan bukan index angka lama
        if saved_iface.startswith("\\Device\\") or saved_iface == "etwdump":
            use_saved = input(f"Gunakan interface yang tersimpan ({config['interface_name']})? [Y/n]: ").strip().lower()
            if use_saved != 'n':
                return saved_iface

    print("\nMencari daftar interface jaringan...")
    try:
        result = subprocess.run([TSHARK_PATH, "-D"], capture_output=True, text=True, check=True)
        interfaces = result.stdout.strip().split('\n')
        
        print("\nDaftar Interface Jaringan:")
        for idx, iface in enumerate(interfaces):
            print(f"{idx + 1}. {iface}")
            
        choice = input("\nPilih nomor interface Wi-Fi Anda: ").strip()
        if not choice:
            print("Pilihan tidak boleh kosong.")
            return select_interface()
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(interfaces):
                selected_line = interfaces[choice_idx]
                # Format tshark -D: "1. \Device\NPF_..."
                parts = selected_line.split('.', 1)
                iface_device = parts[1].strip().split(' ')[0]
                iface_name = parts[1].strip()
                
                config["interface"] = iface_device
                config["interface_name"] = iface_name
                save_config(config)
                print(f"Interface terpilih: {iface_name}")
                return iface_device
            else:
                print("Nomor di luar range.")
                return select_interface()
        except ValueError:
            print("Input tidak valid. Harap masukkan nomor.")
            return select_interface()
    except Exception as e:
        sys.exit(f"Gagal mendeteksi interface: {e}")

def calculate_tiphon_indices(throughput_kbps, delay_ms, jitter_ms, loss_percent):
    # 1. Throughput Index
    if throughput_kbps > 2100:
        idx_throughput = 4
    elif 1200 <= throughput_kbps <= 2100:
        idx_throughput = 3
    elif 700 <= throughput_kbps < 1200:
        idx_throughput = 2
    elif 338 <= throughput_kbps < 700:
        idx_throughput = 1
    else:
        idx_throughput = 0

    # 2. Delay Index
    if delay_ms < 150:
        idx_delay = 4
    elif 150 <= delay_ms <= 300:
        idx_delay = 3
    elif 300 <= delay_ms <= 450:
        idx_delay = 2
    else:
        idx_delay = 1

    # 3. Jitter Index
    if jitter_ms == 0:
        idx_jitter = 4
    elif 0 < jitter_ms <= 75:
        idx_jitter = 3
    elif 75 < jitter_ms <= 125:
        idx_jitter = 2
    else:
        idx_jitter = 1

    # 4. Packet Loss Index
    if 0 <= loss_percent <= 2:
        idx_loss = 4
    elif 3 <= loss_percent <= 14:
        idx_loss = 3
    elif 15 <= loss_percent <= 24:
        idx_loss = 2
    else:
        idx_loss = 1

    # Rata-rata indeks
    avg_index = (idx_throughput + idx_delay + idx_jitter + idx_loss) / 4.0
    
    # Predikat Kategori
    if avg_index >= 3.8:
        predikat = "Sangat Baik"
    elif 3.0 <= avg_index < 3.8:
        predikat = "Baik"
    elif 2.0 <= avg_index < 3.0:
        predikat = "Cukup"
    else:
        predikat = "Buruk"

    return {
        "idx_throughput": idx_throughput,
        "idx_delay": idx_delay,
        "idx_jitter": idx_jitter,
        "idx_loss": idx_loss,
        "avg_index": avg_index,
        "predikat": predikat
    }

def analyze_pcap(filepath):
    print(f"\nMenganalisis berkas: {filepath}...")
    if not os.path.exists(filepath):
        print("File tidak ditemukan.")
        return None

    # Ekstraksi frame info
    try:
        cmd = [
            TSHARK_PATH, "-r", filepath, 
            "-T", "fields", 
            "-e", "frame.time_epoch", 
            "-e", "frame.len", 
            "-e", "frame.time_delta"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        
        if not lines or lines[0] == "":
            print("Tidak ada paket yang terbaca di file PCAP.")
            return None

        total_packets = len(lines)
        total_bytes = 0
        first_epoch = None
        last_epoch = None
        delays = []

        for line in lines:
            parts = line.split('\t')
            if len(parts) >= 3:
                try:
                    epoch = float(parts[0])
                    length = int(parts[1])
                    delta = float(parts[2])
                    
                    total_bytes += length
                    delays.append(delta)
                    
                    if first_epoch is None or epoch < first_epoch:
                        first_epoch = epoch
                    if last_epoch is None or epoch > last_epoch:
                        last_epoch = epoch
                except ValueError:
                    continue

        duration = (last_epoch - first_epoch) if (first_epoch and last_epoch) else 300.0
        if duration <= 0:
            duration = 300.0

        # 1. Throughput (Kbps)
        throughput_kbps = (total_bytes * 8) / (duration * 1000)

        # 2. Delay (ms)
        # Ambil data TCP ACK RTT jika ada untuk hasil delay yang lebih valid secara end-to-end
        tcp_rtt_cmd = [TSHARK_PATH, "-r", filepath, "-Y", "tcp.analysis.ack_rtt", "-T", "fields", "-e", "tcp.analysis.ack_rtt"]
        rtt_result = subprocess.run(tcp_rtt_cmd, capture_output=True, text=True, check=True)
        rtt_lines = rtt_result.stdout.strip().split('\n')
        rtts = [float(r.strip()) * 1000 for r in rtt_lines if r.strip()] # konversi ke ms
        
        if rtts:
            avg_delay = sum(rtts) / len(rtts)
        else:
            # Fallback ke rata-rata frame time delta
            avg_delay = (sum(delays) / len(delays)) * 1000 if delays else 0

        # 3. Jitter (ms)
        # RFC 1889 Formula
        jitter_sum = 0
        if len(delays) > 1:
            for i in range(1, len(delays)):
                jitter_sum += abs(delays[i] - delays[i-1])
            avg_jitter = (jitter_sum / (len(delays) - 1)) * 1000
        else:
            avg_jitter = 0

        # 4. Packet Loss (%)
        # TCP Retransmission Analysis
        tcp_total_cmd = [TSHARK_PATH, "-r", filepath, "-Y", "tcp", "-T", "fields", "-e", "frame.number"]
        tcp_total_res = subprocess.run(tcp_total_cmd, capture_output=True, text=True, check=True)
        total_tcp_packets = len([l for l in tcp_total_res.stdout.strip().split('\n') if l.strip()])

        tcp_lost_cmd = [TSHARK_PATH, "-r", filepath, "-Y", "tcp.analysis.retransmission or tcp.analysis.lost_segment", "-T", "fields", "-e", "frame.number"]
        tcp_lost_res = subprocess.run(tcp_lost_cmd, capture_output=True, text=True, check=True)
        lost_tcp_packets = len([l for l in tcp_lost_res.stdout.strip().split('\n') if l.strip()])

        if total_tcp_packets > 0:
            loss_percent = (lost_tcp_packets / total_tcp_packets) * 100
        else:
            loss_percent = 0.0

        indices = calculate_tiphon_indices(throughput_kbps, avg_delay, avg_jitter, loss_percent)

        print("\nHasil Analisis Metrik QoS:")
        print(f"- Durasi Capture : {duration:.2f} detik")
        print(f"- Total Paket    : {total_packets} paket")
        print(f"- Throughput     : {throughput_kbps:.2f} Kbps")
        print(f"- Delay (Latency): {avg_delay:.2f} ms")
        print(f"- Jitter         : {avg_jitter:.2f} ms")
        print(f"- Packet Loss    : {loss_percent:.2f} %")
        print(f"- Indeks Rata2   : {indices['avg_index']:.2f} ({indices['predikat']})")

        return {
            "duration": round(duration, 2),
            "packets": total_packets,
            "throughput": round(throughput_kbps, 2),
            "delay": round(avg_delay, 2),
            "jitter": round(avg_jitter, 2),
            "loss": round(loss_percent, 2),
            **indices
        }
    except Exception as e:
        print(f"Error saat menganalisis berkas: {e}")
        return None

def write_log(data):
    file_exists = os.path.exists(LOG_FILE)
    try:
        with open(LOG_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow([
                    "Run ID", "Lokasi", "Sesi", "Run #",
                    "Throughput (Kbps)", "Delay (ms)", "Jitter (ms)", "Packet Loss (%)",
                    "Idx Throughput", "Idx Delay", "Idx Jitter", "Idx Loss", "Avg Index", "Predikat",
                    "File PCAP"
                ])
            writer.writerow([
                data["run_id"], data["lokasi"], data["sesi"], data["run_num"],
                data["throughput"], data["delay"], data["jitter"], data["loss"],
                data["idx_throughput"], data["idx_delay"], data["idx_jitter"], data["idx_loss"],
                data["avg_index"], data["predikat"], data["file_pcap"]
            ])
        print(f"Data berhasil disimpan ke {LOG_FILE}")
    except Exception as e:
        print(f"Gagal menulis ke file log: {e}")

def get_next_run(lokasi, sesi):
    # format file: raw_data/lokasi_sesi_runX.pcap
    run_num = 1
    while True:
        filename = f"{lokasi.lower().replace(' ', '_')}_{sesi.lower()}_run{run_num}.pcap"
        filepath = os.path.join(RAW_DATA_DIR, filename)
        if not os.path.exists(filepath):
            return run_num
        run_num += 1

def start_capture_flow(interface_id):
    print("\n--- MENU CAPTURE DATA BARU ---")
    print("Pilih Lokasi:")
    print("1. Ruby Tengah")
    print("2. Kopma")
    print("3. Lorong Lab Komputer")
    print("4. Lorong Lab AI")
    loc_choice = input("Pilih lokasi [1-4]: ").strip()
    locations = {
        "1": "Ruby Tengah",
        "2": "Kopma",
        "3": "Lorong Lab Komputer",
        "4": "Lorong Lab AI"
    }
    lokasi = locations.get(loc_choice)
    if not lokasi:
        print("Lokasi tidak valid.")
        return

    print("\nPilih Sesi Waktu:")
    print("1. Pagi (07.50)")
    print("2. Siang (13.00)")
    print("3. Sore (16.00)")
    sesi_choice = input("Pilih sesi [1-3]: ").strip()
    sessions = {
        "1": "Pagi",
        "2": "Siang",
        "3": "Sore"
    }
    sesi = sessions.get(sesi_choice)
    if not sesi:
        print("Sesi tidak valid.")
        return

    run_num = get_next_run(lokasi, sesi)
    filename = f"{lokasi.lower().replace(' ', '_')}_{sesi.lower()}_run{run_num}.pcap"
    filepath = os.path.join(RAW_DATA_DIR, filename)

    print(f"\nSkenario Terpilih:")
    print(f"- Lokasi   : {lokasi}")
    print(f"- Sesi     : {sesi}")
    print(f"- Run #    : {run_num}")
    print(f"- Output   : {filepath}")

    print("\n[PETUNJUK JALAN SIBUK PERKULIAHAN]")
    print("1. Pastikan laptop Anda terhubung ke Wi-Fi Kampus Universitas Putra Bangsa.")
    print("2. Silakan buka browser dan mulailah memutar video streaming (Youtube 1080p) untuk memicu trafik data konstan.")
    print("3. Setelah siap, tekan ENTER untuk mulai merekam paket data.")
    input("\nTekan ENTER untuk memulai capture (5 menit)...")

    print("\nMulai merekam dalam:")
    for count in range(3, 0, -1):
        print(f"{count}...")
        time.sleep(1)
    print("REKAMAN DIMULAI!")

    # Jalankan tshark selama 300 detik (5 menit)
    try:
        # Menampilkan progress counter
        cmd = [
            TSHARK_PATH, "-i", interface_id, 
            "-a", "duration:300", 
            "-w", filepath
        ]
        
        # Jalankan secara async agar bisa menampilkan timer
        process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        for elapsed in range(1, 301):
            time.sleep(1)
            remaining = 300 - elapsed
            if remaining % 10 == 0 or remaining <= 5:
                print(f"Merekam... [Sisa waktu: {remaining} detik]")
            if process.poll() is not None:
                # Proses berhenti lebih cepat (error / interupsi)
                break
                
        process.wait()
        print("\nREKAMAN SELESAI!")
        
        # Jalankan analisis otomatis
        metrics = analyze_pcap(filepath)
        if metrics:
            run_id = f"run-{datetime.now().strftime('%m%d%H%M%S')}"
            
            log_data = {
                "run_id": run_id,
                "lokasi": lokasi,
                "sesi": sesi,
                "run_num": run_num,
                "file_pcap": filepath,
                **metrics
            }
            write_log(log_data)
            
    except KeyboardInterrupt:
        print("\nCapture diinterupsi oleh pengguna. Menyimpan data yang tertangkap...")
        if 'process' in locals():
            process.terminate()
    except Exception as e:
        print(f"\nGagal menjalankan capture: {e}")

def view_logs():
    print("\n--- DATA LOG EKSPERIMEN (experiment_log.csv) ---")
    if not os.path.exists(LOG_FILE):
        print("Belum ada data log tersimpan.")
        return
        
    try:
        with open(LOG_FILE, 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                # Print baris dengan format rapi
                print(f"{idx + 1:2d}. | " + " | ".join(row[:8]) + " | " + row[13])
    except Exception as e:
        print(f"Gagal membaca file log: {e}")

def main():
    print("====================================================")
    print("  QoS Wi-Fi EXPERIMENT RUNNER & ANALYZER (UPB)      ")
    print("====================================================")
    
    check_tshark()
    interface_id = select_interface()
    
    while True:
        print("\nMENU UTAMA:")
        print("1. Mulai Capture Data Baru (5 Menit)")
        print("2. Analisis Berkas PCAP yang Ada")
        print("3. Lihat Log Hasil Eksperimen")
        print("4. Keluar")
        
        choice = input("\nPilih menu [1-4]: ").strip()
        
        if choice == "1":
            start_capture_flow(interface_id)
        elif choice == "2":
            filepath = input("\nMasukkan path berkas PCAP Anda: ").strip().replace('"', '').replace("'", "")
            analyze_pcap(filepath)
        elif choice == "3":
            view_logs()
        elif choice == "4":
            print("\nTerima kasih, eksperimen selesai. Selamat melanjutkan penulisan tesis!")
            break
        else:
            print("Pilihan menu tidak valid.")

if __name__ == "__main__":
    main()
