# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel... di lingkungan kampus Universitas Putra Bangsa (UPB)?
Hypothesis        : Terdapat penurunan kualitas layanan internet nirkabel (QoS) yang signifikan di bawah nilai ambang batas kelayakan minimum standar TIPHON (skor indeks < 3 / kategori Cukup atau Buruk) pada jam sibuk perkuliahan di lingkungan kampus UPB.
Tipe Eksperimen   : [x] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Hasil evaluasi QoS di objek sekolah homogen (Safitri dkk., 2025) dan kampus dengan pembagian bandwidth statis (Nisa dkk., 2024). | Pengukuran homogen/statis dari literatur | Parameter data dan software Wireshark yang dikontrol sama. |
| Treatment | Pemetaan spasial-temporal QoS nirkabel secara dinamis di 4 area (Ruby Tengah, Kopma, Lorong Lab Komputer, Lorong Lab AI) dan 3 sesi waktu perkuliahan (07.50, 13.00, 16.00) UPB. | Variasi spasial-temporal jam sibuk perkuliahan aktif | capture duration 5 menit, 1 gawai penerima homogen, versi software locked. |

Fairness Checklist:
  [x] Dataset identik untuk semua kondisi
  [x] Preprocessing setara
  [x] Tuning effort setara
  [x] Environment identik
  [x] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Fluktuasi lalu lintas background data yang mendadak saat capture. | Melakukan pengulangan sampling capture di hari perkuliahan aktif yang berbeda dan merata-ratakannya. |
| External    | Karakteristik topologi fisik dan bandwidth kampus UPB yang unik/spesifik. | Mendokumentasikan secara detail spesifikasi jaringan UPB (bandwidth shared, tipe AP) sebagai prasyarat replikasi. |
| Construct   | Ketidakakuratan penangkapan paket oleh NIC laptop penguji. | Mengunci penggunaan unit laptop dan NIC homogen yang sama untuk seluruh sesi pengukuran. |
| Conclusion  | Ukuran sampel data yang terlalu kecil sehingga uji statistik tidak reliabel. | Melakukan pengambilan sampel capture terdistribusi merata selama 5 hari perkuliahan penuh. |

Statistical Plan:
  Uji statistik   : Uji One-Way ANOVA (jika berdistribusi normal) atau Kruskal-Wallis, dilanjutkan Post-Hoc Tukey HSD.
  Justifikasi      : Membandingkan variansi rata-rata indeks QoS TIPHON antar-lokasi (spasial) dan antar-jam sibuk (temporal) untuk membuktikan signifikansi perbedaan kualitas.
  Alpha            : 0.05
  Effect size min  : Cohen's f = 0.25 (efek sedang)
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel... di lingkungan kampus Universitas Putra Bangsa (UPB)?
**Tipe eksperimen:** [x] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Hasil evaluasi QoS di objek sekolah homogen (Safitri dkk., 2025) dan kampus dengan pembagian bandwidth statis (Nisa dkk., 2024). | Pengukuran homogen/statis dari literatur | Parameter data dan software Wireshark yang dikontrol sama. |
| Treatment | Pemetaan spasial-temporal QoS nirkabel secara dinamis di 4 area (Ruby Tengah, Kopma, Lorong Lab Komputer, Lorong Lab AI) dan 3 sesi waktu perkuliahan (07.50, 13.00, 16.00) UPB. | Variasi spasial-temporal jam sibuk perkuliahan aktif | capture duration 5 menit, 1 gawai penerima homogen, versi software locked. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Seluruh metode pembanding dievaluasi menggunakan raw data capture yang sama. |
| Preprocessing setara | ✅ | Berkas PCAP diekstrak menggunakan script parser exporter dengan filter parameter yang sama. |
| Tuning effort setara | ✅ | Seluruh data dipetakan menggunakan formula standardisasi TIPHON yang seragam. |
| Environment identik | ✅ | Penyadapan data dilakukan menggunakan 1 unit laptop penguji yang sama. |
| Metrik evaluasi sama | ✅ | Menggunakan metrik QoS TIPHON (Throughput, Delay, Jitter, Packet Loss, Indeks MOS). |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? —

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Fluktuasi lalu lintas background data pengguna riil yang mendadak saat capture. | Melakukan pengulangan sampling capture di hari perkuliahan aktif yang berbeda dan merata-ratakannya. |
| External | Karakteristik topologi fisik dan bandwidth kampus UPB yang spesifik. | Mendokumentasikan secara detail spesifikasi jaringan UPB (bandwidth shared, tipe AP) sebagai prasyarat replikasi. |
| Construct | Ketidakakuratan penangkapan paket oleh NIC laptop penguji. | Mengunci penggunaan unit laptop dan NIC homogen yang sama untuk seluruh sesi pengukuran. |
| Conclusion | Ukuran sampel data yang terlalu kecil sehingga kekuatan uji statistik rendah. | Melakukan pengambilan sampel capture terdistribusi merata selama 5 hari perkuliahan penuh. |

**Ancaman mana yang paling sulit dimitigasi?** _____________
**Mengapa?**
> ___________________________________________________

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah perbandingan dilakukan pada kondisi yang benar-benar adil (fairness), seperti menggunakan dataset dan perangkat keras penerima yang identik?
2. Apakah parameter hyperparameter pada metode baseline telah dituning secara optimal, ataukah baseline dibiarkan menggunakan konfigurasi default sementara metode yang diusulkan dituning secara maksimal (straw man)?
3. Apakah perbedaan keunggulan tersebut signifikan secara statistik, dan bagaimana ukuran efek (effect size) serta pengujian signifikansinya dilaporkan?
