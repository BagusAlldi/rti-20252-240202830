# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Mayoritas riset terdahulu rentan terhadap bias data temporal dan kontekstual karena menguji QoS Wi-Fi pada objek homogen skala kecil dengan durasi sampling pendek (1-3 hari).

Research Question:
  Tipe         : [x] Comparison  [ ] Improvement  [x] Exploratory
  Formulasi    : Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel yang ditinjau dari parameter throughput, packet loss, delay, dan jitter bersandarkan standarisasi TIPHON jika dikomparasikan terhadap nilai ambang batas kelayakan performa minimum jaringan pada jam sibuk perkuliahan dengan memanfaatkan basis data rekaman lalu lintas paket (traffic capture) Wireshark di lingkungan kampus Universitas Putra Bangsa (UPB)?
  Variabel IV  : Lokasi spasial (4 area observasi: Ruby Tengah, Kopma, Lorong Lab Komputer, Lorong Lab AI) dan interval waktu (3 sesi harian: 07.50, 13.00, 16.00).
  Variabel DV  : Throughput (Kbps), Packet Loss (%), Delay (ms), Jitter (ms), dan Indeks MOS TIPHON.
  Metrik       : Kuantitatif teknis logis transport layer dan skala indeks.
  Dataset      : Rekaman lalu lintas paket (traffic capture) Wireshark kampus UPB.
  Baseline     : Safitri dkk. (2025) dan Nisa dkk. (2024).

Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Karakteristik pemetaan performa logis jaringan internet nirkabel end-to-end secara spasial dan temporal pada lingkungan kampus enterprise multi-building UPB.
  Jenis kontribusi        : [ ] Improvement  [x] Comparison  [ ] Novel approach
  Gap yang diisi          : Context Gap dan Temporal Sampling Gap.

Hypothesis Pair:
  H₀ : Tidak ada penurunan kualitas layanan internet nirkabel (QoS) yang signifikan di bawah nilai ambang batas kelayakan minimum standar TIPHON (skor indeks < 3 / kategori Cukup atau Buruk) pada jam sibuk perkuliahan di lingkungan kampus UPB.
  H₁ : Terdapat penurunan kualitas layanan internet nirkabel (QoS) yang signifikan di bawah nilai ambang batas kelayakan minimum standar TIPHON (skor indeks < 3 / kategori Cukup atau Buruk) pada jam sibuk perkuliahan di lingkungan kampus UPB.
  Threshold              : Indeks Kelayakan >= 3 (Kategori "Baik" / "Good" atau "Sangat Baik" / "Satisfactory").
  Justifikasi threshold  : Standar TIPHON menetapkan nilai indeks 3 sebagai batas minimal performansi transmisi data logis agar fungsionalitas jaringan dirasakan memadai oleh pengguna akhir.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Context Gap & Temporal Sampling Gap.

**RQ versi pertama (tulis bebas):**
> Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel yang ditinjau dari parameter throughput, packet loss, delay, dan jitter bersandarkan standarisasi TIPHON jika dikomparasikan terhadap nilai ambang batas kelayakan performa minimum jaringan pada jam sibuk perkuliahan dengan memanfaatkan basis data rekaman lalu lintas paket (traffic capture) Wireshark di lingkungan kampus Universitas Putra Bangsa (UPB)?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | Analisis QoS dengan traffic capture Wireshark dan standardisasi TIPHON |
| Metrik terukur | Ya | Throughput (Kbps), Packet Loss (%), Delay (ms), Jitter (ms), dan Indeks MOS TIPHON |
| Baseline | Ya | Safitri dkk. (2025) dan Nisa dkk. (2024) |
| Dataset/konteks | Ya | Rekaman paket data Wireshark di lingkungan kampus UPB |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [x] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel yang ditinjau dari parameter throughput, packet loss, delay, dan jitter bersandarkan standarisasi TIPHON jika dikomparasikan terhadap nilai ambang batas kelayakan performa minimum jaringan pada jam sibuk perkuliahan dengan memanfaatkan basis data rekaman lalu lintas paket (traffic capture) Wireshark di lingkungan kampus Universitas Putra Bangsa (UPB)?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada penurunan kualitas layanan internet nirkabel (QoS) yang signifikan di bawah nilai ambang batas kelayakan minimum standar TIPHON (skor indeks < 3 / kategori Cukup atau Buruk) pada jam sibuk perkuliahan di lingkungan kampus UPB. |
| H₁ | Terdapat penurunan kualitas layanan internet nirkabel (QoS) yang signifikan di bawah nilai ambang batas kelayakan minimum standar TIPHON (skor indeks < 3 / kategori Cukup atau Buruk) pada jam sibuk perkuliahan di lingkungan kampus UPB. |
| Metrik | Nilai Indeks Mean Opinion Score (MOS) berskala 0 hingga 4 versi TIPHON |
| Threshold | Indeks kelayakan >= 3.00 (Kategori "Baik" / "Good") |
| Justifikasi threshold | Standar TIPHON menetapkan nilai indeks 3 sebagai batas minimal performansi transmisi data logis agar fungsionalitas jaringan dirasakan memadai oleh pengguna akhir. |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Jika hasil pengujian empiris menunjukkan bahwa pada seluruh titik spasial dan temporal jam sibuk perkuliahan, rata-rata indeks kualitas layanan (QoS) tetap stabil >= 3.00 (kategori "Baik"), maka H1 ditolak dan H0 diterima.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel... |
| Variable (IV) | Lokasi spasial (4 area observasi: Ruby Tengah, Kopma, Lorong Lab Komputer, Lorong Lab AI) dan interval waktu (3 sesi harian: 07.50, 13.00, 16.00). |
| Variable (DV) | Throughput, Packet Loss, Delay, Jitter, Indeks MOS. |
| Metric | Kbps, %, ms, ms, Skor Indeks 0-4. |
| Data source | File rekaman biner PCAP Wireshark. |
| Analysis method | Ekstraksi biner ke CSV, kalkulasi formula TIPHON, komparasi visual dashboard, dan pengujian statistika deskriptif komparatif. |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? —

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** "Analisis Kualitas Layanan Jaringan Internet Berbasis Wireless LAN Menggunakan Metode TIPHON" (Kehi & Belalawe, 2025)
**RQ yang diekstrak:** "Bagaimana kualitas jaringan internet berbasis WLAN di SMK Negeri 6 Kupang?"
**Komponen yang hilang:** RQ tersebut tidak mendefinisikan metrik kuantitatif secara spesifik dalam pertanyaan, tidak menyebutkan baseline pembanding, dan tidak membatasi kondisi waktu pengujian (jam sibuk/tidak).
