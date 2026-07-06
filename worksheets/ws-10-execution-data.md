# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     |          |      |           |        |       |             |
| 2     |          |      |           |        |       |             |
| 3     |          |      |           |        |       |             |
| ...   |          |      |           |        |       |             |

Jumlah runs per skenario : ____
Total runs               : ____

DATA LOG (per run):
  Run ID    : ____________________
  Timestamp : ____________________
  Skenario  : ____________________
  Input     : ____________________
  Output    : ____________________
  Anomali   : ____________________
  Catatan   : ____________________
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1-5 | Ruby Tengah - Pagi | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 6-10 | Ruby Tengah - Siang | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 11-15 | Ruby Tengah - Sore | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 16-20 | Kopma - Pagi | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 21-25 | Kopma - Siang | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 26-30 | Kopma - Sore | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 31-35 | Lorong Lab Komputer - Pagi | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 36-40 | Lorong Lab Komputer - Siang | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 41-45 | Lorong Lab Komputer - Sore | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 46-50 | Lorong Lab AI - Pagi | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 51-55 | Lorong Lab AI - Siang | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |
| 56-60 | Lorong Lab AI - Sore | N/A (Live Wi-Fi) | 5 Menit, Wi-Fi UPB | Planned |

**Total skenario:** 12 skenario (4 lokasi kampus x 3 sesi waktu)
**Run per skenario:** 5 kali pengulangan
**Total run keseluruhan:** 60 kali pengulangan run

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh / Deskripsi |
|-------|--------|
| Run ID | run-0623083523 (ID unik acak berbasis timestamp) |
| Timestamp | 2026-06-23T08:35:23 (ISO 8601) |
| Lokasi | Ruby Tengah, Kopma, Lorong Lab Komputer, Lorong Lab AI |
| Sesi | Pagi, Siang, Sore |
| Run # | Pengulangan ke- (1 s.d. 5) |

**Konfigurasi:**
| Field | Contoh / Deskripsi |
|-------|--------|
| Interface ID | \Device\NPF_{B5ACA46D-0E95-4F54-A66E-30E4FCAB4CA5} (GUID kartu Wi-Fi) |
| Interface Name | Intel(R) Wi-Fi 6 AX201 160MHz (Nama adapter di Windows) |
| Durasi Capture | 300 (durasi dalam detik / 5 menit) |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Throughput | float | >= 0.0 Kbps |
| Delay (Latency) | float | >= 0.0 ms |
| Jitter | float | >= 0.0 ms |
| Packet Loss | float | 0.0 – 100.0 % |
| Idx Throughput | integer | 0 – 4 (TIPHON Index) |
| Idx Delay | integer | 1 – 4 (TIPHON Index) |
| Idx Jitter | integer | 1 – 4 (TIPHON Index) |
| Idx Loss | integer | 1 – 4 (TIPHON Index) |
| Avg Index | float | 1.0 – 4.0 |
| Predikat | string | Sangat Baik, Baik, Cukup, Buruk |
| File PCAP | string | Path file pcap (e.g., raw_data\ruby_tengah_pagi_run2.pcap) |

**Format output:** [x] CSV / [ ] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Koneksi tshark terputus atau driver Npcap crash | Buka PowerShell/Terminal dengan akses Administrator, jalankan ulang driver lewat perintah `net start npcap`, lalu jalankan kembali skrip. |
| Hasil ekstrem | Packet Loss terdeteksi 100% atau delay > 5000ms | Verifikasi apakah laptop terputus (*disconnect*) dari Wi-Fi kampus saat perekaman berjalan. Catat kejadian ini di log, lalu lakukan perekaman ulang (*re-run*). |
| File PCAP kosong | Ukuran file PCAP kurang dari 1 KB (0 packets) | Cek apakah nomor indeks adapter Wi-Fi Anda bergeser di Windows. Jalankan skrip, pilih ulang nomor kartu Wi-Fi Anda agar ID GUID terbarui, pastikan browser Anda sedang aktif memutar YouTube, lalu ulangi perekaman. |
| Log tidak tersimpan | Skrip terhenti secara paksa sebelum menulis ke CSV | Catat nomor run bersangkutan sebagai "Failed" dan lakukan re-run baru untuk menggantikannya agar jumlah data tetap genap 60. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Ya, sebelumnya sering menggunakan satu run karena dinilai praktis dan cepat. Namun, hal ini sangat berisiko karena kualitas jaringan nirkabel (Wi-Fi) kampus sangat fluktuatif dan dipengaruhi oleh jumlah mahasiswa aktif di sekitar area Access Point yang berubah tiap menit.

**Yang akan dilakukan berbeda:**
> Di penelitian ini, saya menerapkan 5 kali pengulangan (runs) untuk setiap skenario. Dengan multiple runs, saya dapat menghitung nilai rata-rata metrik QoS yang stabil secara statistik sehingga hasil konversi ke predikat TIPHON menjadi andal dan tepercaya secara akademis.
