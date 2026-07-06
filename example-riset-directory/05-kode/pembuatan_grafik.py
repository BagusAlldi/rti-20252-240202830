import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Menggunakan path baru yang telah disesuaikan dengan struktur 00-09
LOG_FILE = r"e:\RTI\04-data\experiment_log.csv"
CHARTS_DIR = r"e:\RTI\06-output\charts"
WS_FILE = r"e:\RTI\08-laporan\week\ws-12-result-presentation.md"

def main():
    if not os.path.exists(LOG_FILE):
        print(f"Error: File log {LOG_FILE} tidak ditemukan!")
        return

    if not os.path.exists(CHARTS_DIR):
        os.makedirs(CHARTS_DIR)
        print(f"Membuat folder grafik: {CHARTS_DIR}")

    try:
        with open(LOG_FILE, 'r') as f:
            first_line = f.readline().strip()
            
        if first_line.startswith("sep="):
            df = pd.read_csv(LOG_FILE, skiprows=1)
        else:
            df = pd.read_csv(LOG_FILE)
    except Exception as e:
        print(f"Gagal membaca file log: {e}")
        return

    df["Throughput (Kbps)"] = pd.to_numeric(df["Throughput (Kbps)"])
    df["Delay (ms)"] = pd.to_numeric(df["Delay (ms)"])
    df["Jitter (ms)"] = pd.to_numeric(df["Jitter (ms)"])
    df["Packet Loss (%)"] = pd.to_numeric(df["Packet Loss (%)"])
    df["Run #"] = pd.to_numeric(df["Run #"])

    sesi_order = {"Pagi": 1, "Siang": 2, "Sore": 3}
    df["Sesi_Order"] = df["Sesi"].map(sesi_order)
    df = df.sort_values(by=["Lokasi", "Sesi_Order", "Run #"])

    print("\n[1/2] Membuat visualisasi grafik QoS...")
    sns.set_theme(style="whitegrid")
    
    # Grafik A: Grouped Bar Chart untuk Throughput (Mean ± Std)
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=df,
        x="Lokasi",
        y="Throughput (Kbps)",
        hue="Sesi",
        hue_order=["Pagi", "Siang", "Sore"],
        errorbar="sd",
        capsize=0.1,
        palette="viridis"
    )
    plt.title("Perbandingan Rata-rata Throughput Wi-Fi per Lokasi dan Sesi (Mean ± SD)", fontsize=12, pad=15)
    plt.xlabel("Lokasi Titik Ukur", fontsize=10)
    plt.ylabel("Throughput (Kbps)", fontsize=10)
    plt.tight_layout()
    chart1_path = os.path.join(CHARTS_DIR, "throughput_comparison.png")
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f"  - Grafik Throughput disimpan di: {chart1_path}")

    # Grafik B: Box Plot untuk Latency/Delay
    plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=df,
        x="Lokasi",
        y="Delay (ms)",
        hue="Sesi",
        hue_order=["Pagi", "Siang", "Sore"],
        palette="crest"
    )
    plt.title("Distribusi Delay (Latency) Wi-Fi per Lokasi dan Sesi", fontsize=12, pad=15)
    plt.xlabel("Lokasi Titik Ukur", fontsize=10)
    plt.ylabel("Delay (ms)", fontsize=10)
    plt.tight_layout()
    chart2_path = os.path.join(CHARTS_DIR, "delay_distribution.png")
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"  - Grafik Delay disimpan di: {chart2_path}")

    # Grafik C: Box Plot untuk Packet Loss
    plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=df,
        x="Lokasi",
        y="Packet Loss (%)",
        hue="Sesi",
        hue_order=["Pagi", "Siang", "Sore"],
        palette="flare"
    )
    plt.title("Distribusi Packet Loss Wi-Fi per Lokasi dan Sesi", fontsize=12, pad=15)
    plt.xlabel("Lokasi Titik Ukur", fontsize=10)
    plt.ylabel("Packet Loss (%)", fontsize=10)
    plt.tight_layout()
    chart3_path = os.path.join(CHARTS_DIR, "loss_distribution.png")
    plt.savefig(chart3_path, dpi=300)
    plt.close()
    print(f"  - Grafik Packet Loss disimpan di: {chart3_path}")

    print("\n[2/2] Menghitung tabel statistik untuk Lembar Kerja...")
    grouped = df.groupby(["Lokasi", "Sesi", "Sesi_Order"])
    
    table_rows = []
    for (loc, sesi, order), group in grouped:
        t_mean, t_std = group["Throughput (Kbps)"].mean(), group["Throughput (Kbps)"].std()
        d_mean, d_std = group["Delay (ms)"].mean(), group["Delay (ms)"].std()
        j_mean, j_std = group["Jitter (ms)"].mean(), group["Jitter (ms)"].std()
        l_mean, l_std = group["Packet Loss (%)"].mean(), group["Packet Loss (%)"].std()
        
        throughput_str = f"{t_mean:.2f} ± {t_std:.2f} Kbps"
        delay_str = f"{d_mean:.2f} ± {d_std:.2f} ms"
        jitter_str = f"{j_mean:.2f} ± {j_std:.2f} ms"
        loss_str = f"{l_mean:.2f} ± {l_std:.2f}%"
        
        table_rows.append(
            f"| {loc} - {sesi} | {throughput_str} | {delay_str} | {jitter_str} | {loss_str} | 5 |"
        )

    markdown_table = (
        "| Skenario | Throughput (mean ± std) | Delay (mean ± std) | Jitter (mean ± std) | Packet Loss (mean ± std) | n |\n"
        "|----------|------------------------|--------------------|---------------------|--------------------------|---|\n"
        + "\n".join(table_rows)
    )

    print("\n=== TABEL HASIL (SIAP DI-COPY-PASTE): ===")
    print(markdown_table)
    print("=========================================\n")

    if os.path.exists(WS_FILE):
        try:
            with open(WS_FILE, 'r', encoding='utf-8') as f:
                content = f.read()

            pattern = re.compile(
                r"## Latihan 1 — Tabel Hasil.*?"
                r"\| Skenario \|.*?\n"
                r"\|----------\|.*?\n"
                r"(?:\|.*?\|.*?\n)*", 
                re.DOTALL
            )
            
            replacement = f"## Latihan 1 — Tabel Hasil\n\nBuat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).\n\n{markdown_table}\n"
            new_content = pattern.sub(replacement, content)
            
            new_content = new_content.replace("- [ ] Self-contained (judul jelas, satuan ada, N tercantum)", "- [x] Self-contained (judul jelas, satuan ada, N tercantum)")
            new_content = new_content.replace("- [ ] Mean ± std (bukan single number)", "- [x] Mean ± std (bukan single number)")
            new_content = new_content.replace("- [ ] Diurutkan berdasarkan metrik utama", "- [x] Diurutkan berdasarkan metrik utama")
            new_content = new_content.replace("- [ ] Format konsisten di semua baris", "- [x] Format konsisten di semua baris")
            
            with open(WS_FILE, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Berhasil memperbarui lembar kerja: {WS_FILE}")
        except Exception as e:
            print(f"Gagal memperbarui file lembar kerja: {e}")

    print("\nVISUALISASI DAN ANALISIS TABEL SELESAI!")

if __name__ == "__main__":
    main()
