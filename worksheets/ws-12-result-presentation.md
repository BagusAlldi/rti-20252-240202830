# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Bagaimana performa kualitas jaringan nirkabel (Wi-Fi) di area Universitas berdasarkan parameter QoS (Throughput, Delay, Jitter, dan Packet Loss) pada sesi waktu yang berbeda (Pagi, Siang, Sore)?
Metrik Utama      : Throughput (Kbps), Delay (ms), Jitter (ms), dan Packet Loss (%)

Tabel Hasil:
| Skenario | Throughput (mean ± std) | Delay (mean ± std) | Jitter (mean ± std) | Packet Loss (mean ± std) | n |
|----------|------------------------|--------------------|---------------------|--------------------------|---|
| Kopma - Pagi | 2049.24 ± 565.50 Kbps | 79.08 ± 23.57 ms | 5.81 ± 1.38 ms | 5.75 ± 1.32% | 5 |
| Kopma - Siang | 2084.58 ± 959.66 Kbps | 68.46 ± 21.65 ms | 5.86 ± 1.72 ms | 6.27 ± 1.98% | 5 |
| Kopma - Sore | 1060.25 ± 577.27 Kbps | 150.16 ± 57.38 ms | 13.66 ± 8.49 ms | 7.18 ± 1.33% | 5 |
| Lorong Lab AI - Pagi | 1171.20 ± 155.36 Kbps | 185.45 ± 80.52 ms | 9.12 ± 1.56 ms | 5.11 ± 1.69% | 5 |
| Lorong Lab AI - Siang | 1173.97 ± 154.54 Kbps | 260.15 ± 111.51 ms | 8.36 ± 1.00 ms | 9.05 ± 1.58% | 5 |
| Lorong Lab AI - Sore | 1262.27 ± 215.82 Kbps | 244.10 ± 89.66 ms | 7.79 ± 0.98 ms | 8.82 ± 2.13% | 5 |
| Lorong Lab Komputer - Pagi | 2900.99 ± 2276.18 Kbps | 366.24 ± 270.42 ms | 7.29 ± 3.50 ms | 11.67 ± 2.69% | 5 |
| Lorong Lab Komputer - Siang | 2378.51 ± 1470.24 Kbps | 271.84 ± 77.48 ms | 6.08 ± 2.30 ms | 13.70 ± 8.17% | 5 |
| Lorong Lab Komputer - Sore | 1070.04 ± 185.53 Kbps | 253.34 ± 68.93 ms | 9.41 ± 1.11 ms | 9.44 ± 2.39% | 5 |
| Ruby Tengah - Pagi | 2230.57 ± 898.07 Kbps | 66.01 ± 47.26 ms | 5.86 ± 1.83 ms | 7.97 ± 1.69% | 5 |
| Ruby Tengah - Siang | 1257.48 ± 137.91 Kbps | 213.55 ± 171.45 ms | 8.20 ± 0.67 ms | 6.65 ± 1.26% | 5 |
| Ruby Tengah - Sore | 1250.96 ± 210.62 Kbps | 340.97 ± 220.41 ms | 8.06 ± 0.76 ms | 7.29 ± 1.51% | 5 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Grouped Bar Chart + Error Bar | Perbandingan rata-rata Throughput antar lokasi & sesi | Throughput (mean ± std) |
| 2 | Box Plot | Sebaran dan kestabilan nilai delay (latency) per sesi | Seluruh run Delay (ms) |
| 3 | Box Plot | Sebaran persentase kegagalan pengiriman paket Wi-Fi | Seluruh run Packet Loss (%) |

Bias Check:
  [x] Y-axis mulai dari 0 (atau dijustifikasi)
  [x] Error bar/CI ditampilkan
  [x] Semua data disertakan (tidak cherry-picked)
  [x] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Throughput (mean ± std) | Delay (mean ± std) | Jitter (mean ± std) | Packet Loss (mean ± std) | n |
|----------|------------------------|--------------------|---------------------|--------------------------|---|
| Kopma - Pagi | 2049.24 ± 565.50 Kbps | 79.08 ± 23.57 ms | 5.81 ± 1.38 ms | 5.75 ± 1.32% | 5 |
| Kopma - Siang | 2084.58 ± 959.66 Kbps | 68.46 ± 21.65 ms | 5.86 ± 1.72 ms | 6.27 ± 1.98% | 5 |
| Kopma - Sore | 1060.25 ± 577.27 Kbps | 150.16 ± 57.38 ms | 13.66 ± 8.49 ms | 7.18 ± 1.33% | 5 |
| Lorong Lab AI - Pagi | 1171.20 ± 155.36 Kbps | 185.45 ± 80.52 ms | 9.12 ± 1.56 ms | 5.11 ± 1.69% | 5 |
| Lorong Lab AI - Siang | 1173.97 ± 154.54 Kbps | 260.15 ± 111.51 ms | 8.36 ± 1.00 ms | 9.05 ± 1.58% | 5 |
| Lorong Lab AI - Sore | 1262.27 ± 215.82 Kbps | 244.10 ± 89.66 ms | 7.79 ± 0.98 ms | 8.82 ± 2.13% | 5 |
| Lorong Lab Komputer - Pagi | 2900.99 ± 2276.18 Kbps | 366.24 ± 270.42 ms | 7.29 ± 3.50 ms | 11.67 ± 2.69% | 5 |
| Lorong Lab Komputer - Siang | 2378.51 ± 1470.24 Kbps | 271.84 ± 77.48 ms | 6.08 ± 2.30 ms | 13.70 ± 8.17% | 5 |
| Lorong Lab Komputer - Sore | 1070.04 ± 185.53 Kbps | 253.34 ± 68.93 ms | 9.41 ± 1.11 ms | 9.44 ± 2.39% | 5 |
| Ruby Tengah - Pagi | 2230.57 ± 898.07 Kbps | 66.01 ± 47.26 ms | 5.86 ± 1.83 ms | 7.97 ± 1.69% | 5 |
| Ruby Tengah - Siang | 1257.48 ± 137.91 Kbps | 213.55 ± 171.45 ms | 8.20 ± 0.67 ms | 6.65 ± 1.26% | 5 |
| Ruby Tengah - Sore | 1250.96 ± 210.62 Kbps | 340.97 ± 220.41 ms | 8.06 ± 0.76 ms | 7.29 ± 1.51% | 5 |

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Grouped Bar Chart + Error Bar | Perbandingan Throughput rata-rata antar lokasi & sesi | Mean Throughput (Kbps) ± Std |
| 2 | Box Plot | Sebaran nilai Delay untuk mendeteksi variabilitas kestabilan | Seluruh run Delay (ms) |
| 3 | Box Plot | Sebaran persentase Packet Loss untuk mendeteksi penurunan di jam sibuk | Seluruh run Packet Loss (%) |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya — Metode A terlihat 2× lipat lebih baik daripada B padahal hanya berbeda 0.4% secara absolut. |
| Apakah error bar ditampilkan? | Tidak, ketidakhadiran error bar menyembunyikan variabilitas data dan tidak memperlihatkan signifikansi perbedaan. |
| Apakah semua kondisi ditampilkan? | Tidak, grafik hanya menyajikan ringkasan nilai rata-rata (*mean*) dari kedua metode tanpa data distribusi lengkap. |
| Apa solusinya? | Mengatur Y-axis dimulai dari 0% dan menambahkan error bar (standar deviasi) untuk memberikan representasi visual yang jujur. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus
- [x] Ada yang perlu diperbaiki: Tidak ada. Seluruh grafik visualisasi dibuat menggunakan Y-axis dari 0 dan telah dilengkapi error bars (untuk bar chart) atau menggunakan Box Plot untuk kejujuran sebaran data.

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel menyediakan detail numerik yang sangat presisi (angka eksak seperti nilai rata-rata dan standar deviasi) untuk pembuktian ilmiah, sedangkan grafik menyoroti tren umum, pola perbandingan spasial/temporal, dan anomali secara instan. Menggunakan salah satu saja akan membatasi pemahaman data riset. 
> 
> Di masa lalu, saya pernah membuat grafik tanpa sengaja menyesatkan dengan tidak menyertakan error bar, sehingga perbedaan nilai rata-rata yang kecil tampak sangat signifikan secara visual padahal fluktuasi datanya sebenarnya sangat tumpang tindih.
