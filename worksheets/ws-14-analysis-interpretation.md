# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean (Kbps) | Std (Kbps) | Median (Kbps) | Min (Kbps) | Max (Kbps) | n |
|----------|------|-----|--------|-----|-----|---|
| Kopma - Pagi | 2049.24 | 565.50 | 1966.84 | 1415.08 | 2946.81 | 5 |
| Kopma - Siang | 2084.58 | 959.66 | 1886.59 | 1328.82 | 3746.48 | 5 |
| Kopma - Sore | 1060.25 | 577.27 | 905.69 | 294.13 | 1778.07 | 5 |
| Lorong Lab AI - Pagi | 1171.20 | 155.36 | 1195.15 | 937.94 | 1367.04 | 5 |
| Lorong Lab AI - Siang | 1173.97 | 154.54 | 1106.77 | 1045.58 | 1437.60 | 5 |
| Lorong Lab AI - Sore | 1262.27 | 215.82 | 1233.75 | 1053.62 | 1554.57 | 5 |
| Lorong Lab Komputer - Pagi | 2900.99 | 2276.18 | 2859.12 | 961.36 | 6601.94 | 5 |
| Lorong Lab Komputer - Siang | 2378.51 | 1470.24 | 2079.08 | 1328.15 | 4901.36 | 5 |
| Lorong Lab Komputer - Sore | 1070.04 | 185.53 | 953.55 | 918.25 | 1314.42 | 5 |
| Ruby Tengah - Pagi | 2230.57 | 898.07 | 2227.59 | 1335.71 | 3681.01 | 5 |
| Ruby Tengah - Siang | 1257.48 | 137.91 | 1246.42 | 1129.20 | 1454.28 | 5 |
| Ruby Tengah - Sore | 1250.96 | 210.62 | 1297.00 | 1022.33 | 1515.09 | 5 |

2. Uji Hipotesis:
   Uji yang digunakan  : Kruskal-Wallis H Test (Non-parametrik)
   Justifikasi          : Membandingkan > 2 grup independen (Pagi vs Siang vs Sore) di mana data throughput berdistribusi tidak normal dan terdapat pencilan (outliers).
   Hasil: H = 11.4502, p = 3.2631e-03, effect size (η²) = 0.1658 (Large)
   CI 95%               : [Tidak berlaku untuk Kruskal-Wallis]

3. Keputusan:
   [x] H₀ ditolak → H₁ diterima

4. Interpretasi:
   Hubungan ke RQ       : Ada perbedaan performa Throughput Wi-Fi yang sangat signifikan (p < 0.05) antar-sesi waktu pengujian. Kualitas terburuk terjadi di sesi Sore di sebagian besar lokasi.
   Practical significance: Dampak praktisnya sangat besar (Large effect size η² = 0.1658). Perbedaan kecepatan transfer data antar jam sibuk dan senggang sangat dirasakan langsung oleh pengguna di lapangan.
   Perbandingan literatur: Sejalan dengan penelitian Ramadhani (2021) yang menyatakan bahwa faktor beban kepadatan pengguna nirkabel pada jam pulang kantor/kuliah menurunkan performa QoS secara drastis.

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | Statistical limitation | Sampel hanya 5 run per skenario | Uji kekuatan statistik (statistical power) terbatas | Melakukan sampling jangka panjang (misal 14 hari penuh) |
   | External validity | Pengujian hanya di lingkungan 1 kampus | Hasil tidak bisa langsung digeneralisasi ke kampus lain | Melakukan pengujian pembanding di luar area Universitas |
   | Construct validity | Pengukuran hanya berbasis tshark | Bergantung pada keandalan library eksternal | Melakukan korelasi silang dengan data speedtest/iPerf |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : ____________________
   Boundary condition   : ____________________
   Insight              : ____________________
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 3 grup sesi waktu (Pagi, Siang, Sore) |
| Apakah data berpasangan (paired)? | Tidak (diperlakukan sebagai grup independen antar sesi waktu) |
| Apakah distribusi normal? (uji normalitas) | Tidak normal pada beberapa skenario (mengandung deviasi besar) |
| **Uji yang dipilih:** | **Kruskal-Wallis H Test** |
| **Justifikasi:** | Membandingkan 3 grup independen berskala kontinu yang tidak memenuhi asumsi distribusi normal. |

**Effect size yang akan dilaporkan:** [ ] Cohen's d / [x] Eta-squared / [ ] Lainnya: —

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| A | 89.2 ± 1.5 | 10 |
| B | 87.8 ± 2.1 | 10 |

p = 0.045, Cohen's d = 0.74, CI 95% = [0.03, 2.77]

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | p = 0.045 < 0.05 → Perbedaan akurasi antar Model A dan B signifikan secara statistik pada tingkat kepercayaan 95%. |
| Effect size | d = 0.74 → Menunjukkan efek ukuran medium-ke-besar. Model A memberikan peningkatan performa yang cukup nyata dibandingkan Model B. |
| Practical significance | Perbedaan rata-rata 1.4% (89.2% vs 87.8%) mungkin kecil, namun dalam sistem kritis, peningkatan ini berkontribusi mengurangi kesalahan klasifikasi secara berarti. |
| Hubungan ke RQ | Model A terbukti lebih unggul dalam memenuhi tujuan riset untuk meningkatkan performa akurasi sistem. |
| Perbandingan literatur | Hasil ini memperkuat temuan Pratama (2023) yang menyatakan arsitektur Model A memiliki konvergensi yang lebih baik. |---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | *Contoh: Bukan gagal total — hipotesis tidak terdukung adalah temuan yang valid dan bisa menjadi kontribusi.* |
| Kemungkinan penyebab? | *Contoh: Metode baru menambah kompleksitas komputasi (+40% waktu) tanpa peningkatan F1 yang cukup — overhead tidak sebanding.* |
| Boundary condition? | *Contoh: Metode ini hanya efektif ketika data ≥ 10.000 record; di dataset kecil (<1.000), baseline lebih stabil.* |
| Insight yang bisa diambil? | *Contoh: Ada trade-off ukuran data vs kompleksitas — rekomendasikan hybrid approach yang adaptif berdasarkan ukuran dataset.* |
| Apakah layak dilaporkan? Mengapa? | *Contoh: Ya — negative result + boundary condition analysis adalah kontribusi riset yang diakui komunitas (ex: ACL, SIGIR). Mencegah riset duplikasi yang berulang.* |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| Statistical | Ukuran sampel kecil (5 run per skenario) | Rentan terhadap bias fluktuasi sesaat |
| Construct validity | Pengukuran hanya berbasis tshark | Bergantung pada keandalan library eksternal |---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> *Failure* (hasil negatif/hipotesis H0 tidak ditolak) dalam riset bukanlah kegagalan ilmiah. Hasil negatif tersebut justru merupakan kontribusi berharga karena menetapkan batas kemampuan (*boundary conditions*) dari metode yang diuji. Hal ini mencegah peneliti lain melakukan duplikasi kesalahan yang sama dan membantu mengarahkan perbaikan desain sistem di masa depan.
>
> Analisis kegagalan (*failure analysis*) mengubah sudut pandang saya: dari mencari pembenaran atas bias hasil riset (*p-hacking*), menjadi penyelidikan objektif yang menghargai keterbatasan sistem secara transparan.