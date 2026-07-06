# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : Intel Core i5 / i7 (sesuai spesifikasi gawai penguji)
  RAM     : 8 GB / 16 GB DDR4/DDR5
  GPU     : CPU-only (tidak memerlukan akselerasi grafis GPU)
  Storage : SSD 512 GB

Software:
  OS        : Windows 11 Home/Pro (Build 22631 atau terbaru)
  Runtime   : Python 3.13.5
  Framework : Wireshark/Tshark (v4.2.0 atau terbaru) + Pandas Library

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
| pandas  | 2.2.0   | PyPI   | sha256:0d69ab... |
| numpy   | 1.26.0  | PyPI   | sha256:b1d821... |
| fpdf2   | 2.8.7   | PyPI   | sha256:fe98a1... |
| pypdf   | 6.14.0  | PyPI   | sha256:7c9e10... |
| openpyxl| 3.1.0   | PyPI   | sha256:4a0210... |

Konfigurasi:
  Config file     : config_experiment.json (untuk menyimpan Wi-Fi interface terpilih)
  Random seed     : 42 (untuk operasi Pandas/NumPy deterministik)
  Hyperparameters : capture_duration = 300 (5 menit), locations = 4, sessions = 3

Reproducibility Check:
  [x] Dependency terdokumentasi (requirements.txt / lock file)
  [x] Seed ditetapkan di semua level (Python, NumPy, framework)
  [x] Config di version control
  [x] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Intel Core i5/i7 (homogen) |
| RAM | 8 GB / 16 GB |
| GPU | CPU-only |
| OS | Windows 11 |
| Runtime | Python 3.13.5 |
| Framework | Wireshark/Tshark (v4.2.0) |
| Random Seed | 42 |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| pandas | 2.2.0 | Manipulasi dan analisis data tabular hasil ekstraksi PCAP. |
| numpy | 1.26.0 | Kalkulasi matematis rata-rata delay dan deviasi jitter. |
| fpdf2 | 2.8.7 | Otomasi ekspor laporan analisis QoS menjadi berkas PDF. |
| pypdf | 6.14.0 | Pembacaan teks file PDF literatur untuk screening otomatis. |
| openpyxl | 3.1.0 | Dukungan format file Excel untuk kompatibilitas data log. |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | 42 | Throughput (Kbps) | — |
| 2 | 42 | Throughput (Kbps) | [x] Ya / [ ] Tidak |
| 3 | 42 | Throughput (Kbps) | [x] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**
> Hasil pembacaan file PCAP tidak akan berubah karena parsing data biner bersifat sepenuhnya deterministik. Namun, jika ada variasi minor dalam kalkulasi delay pada run dinamis, hal itu disebabkan oleh cache memory internal yang menyimpan state eksekusi runtime sebelumnya.

**Checklist kontrol yang sudah diterapkan:**
- [x] Random seed di-set di semua level
- [x] Tidak ada background process yang mengganggu
- [x] Cache dibersihkan antar-run
- [x] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Evaluasi QoS Wi-Fi Universitas Putra Bangsa (UPB)

## 1. Environment
- CPU: Intel Core i5/i7 Homogen
- RAM: 8 GB / 16 GB
- OS: Windows 11
- Runtime: Python 3.13.5
- Tool capture: Wireshark/Tshark v4.2.0

## 2. Installation
Langkah instalasi dependencies:
`pip install pandas numpy fpdf2 pypdf openpyxl`

## 3. Data
- Sumber: Rekaman penangkapan paket nirkabel (sniffing) melalui tshark.
- Format: Biner `.pcap`.
- Ukuran: Variatif tergantung traffic, rata-rata 10-50 MB per 5 menit capture.

## 4. Execution
Command untuk menjalankan skrip eksperimen capture & analisis otomatis:
`python run_experiment.py`

## 5. Configuration
- File konfigurasi: `config_experiment.json`
- Parameter kunci: ID interface kartu jaringan (NIC) Wi-Fi yang dikunci setelah inisialisasi pertama.

## 6. Expected Output
- File capture: `raw_data/[lokasi]_[sesi]_run[X].pcap`
- File log kumulatif: `experiment_log.csv` (berisi metrik throughput, delay, jitter, loss, dan indeks MOS TIPHON).
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [x] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Kontainerisasi menggunakan Docker untuk mengunci environment dependensi OS nirkabel sehingga dapat dijalankan 100% identik di luar platform OS Windows (seperti Linux/MacOS).
