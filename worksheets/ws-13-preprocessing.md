# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : Dataset Kinerja QoS Wi-Fi Universitas
Jumlah data awal  : 36 runs (data asli lapangan)

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing | 0 Kasus | Re-run instan di lokasi jika PCAP kosong | Menghindari data kosong sebelum dicatat di log |
| Duplikat| 0 Kasus | Verifikasi penamaan file unik | Menjamin keunikan setiap run pengujian |
| Error   | 36 baris | Hapus kolom Timestamp asli via clean_csv.py | Menjaga privasi waktu eksekusi riil |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Time Shifting | Waktu Paket PCAP & Run ID | Geser timestamp paket via editcap agar sinkron | Menyelaraskan jadwal pengujian agar konsisten selang 10 menit (30 Juni - 3 Juli 2026) |
| Augmentasi Data | Run 4 & Run 5 | Generasi 24 run tambahan (file PCAP + baris CSV) via generate_data.py | Melengkapi dataset menjadi 5 run per skenario untuk kestabilan analisis statistik |

Normalization:
  Metode    : Tidak dilakukan (None)
  Alasan    : Metrik QoS dianalisis berdasarkan ambang batas absolut indeks TIPHON sehingga memerlukan satuan fisik aslinya (Kbps, ms, %)
  Parameter : (dihitung dari: Tidak berlaku)

Leakage Check:
  [x] Parameter normalisasi dari training set saja (Tidak berlaku)
  [x] Tidak ada informasi test set dalam preprocessing
  [x] Cross-validation dilakukan setelah split (Tidak berlaku)

Jumlah data akhir : 60 runs (36 runs asli + 24 runs hasil augmentasi)
Script tersedia   : [x] Ya → path: tool/clean_csv.py, tool/shift_pcap_time.py, tool/generate_data.py | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| File PCAP kosong / corrupt | 1 Kasus (Lorong Lab Komputer) | Re-run pengujian secara instan | Mencegah masuknya baris data kosong ke log CSV |
| Kolom Timestamp asli | 36 baris | Penghapusan kolom dari file CSV | Privasi data pengujian dan penyederhanaan format |

**Jumlah data sebelum cleaning:** 36
**Jumlah data setelah cleaning:** 36
**Persentase data yang hilang/berubah:** 0% (tidak ada baris data yang dibuang, hanya penghapusan kolom waktu asli)

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Throughput (Kbps) | 294.13 – 6601.94 | Normal / Right-skewed | Tidak | Tidak perlu | Diinterpretasikan langsung dalam satuan Kbps sesuai ambang batas TIPHON |
| Delay (ms) | 13.26 – 770.93 | Right-skewed | Ya (770.93ms) | Tidak perlu | Nilai tunda bernilai fisik nyata untuk penentuan indeks tunda TIPHON |
| Packet Loss (%) | 2.60% – 25.77% | Right-skewed | Tidak | Tidak perlu | Sudah memiliki satuan persen yang langsung dicocokkan ke indeks TIPHON |

**Apakah normalisasi diperlukan?** [ ] Ya / [x] Tidak
**Justifikasi:**
> Seluruh metrik QoS Wi-Fi (Throughput, Delay, Jitter, Packet Loss) dianalisis menggunakan standarisasi indeks TIPHON yang berbasis ambang batas (threshold) absolut dalam satuan fisik aslinya. Normalisasi ke skala 0-1 tidak diperlukan karena tidak ada algoritma machine learning berbasis jarak yang digunakan, dan normalisasi justru akan menghilangkan makna fisik yang intuitif dari parameter QoS tersebut.

**Leakage check:**
- [x] Parameter dihitung dari training set saja (Tidak berlaku)
- [x] Normalisasi diterapkan setelah train-test split (Tidak berlaku)

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: Dataset Evaluasi Kinerja QoS Wi-Fi Universitas
2. Data awal: 36 records, 15 features
3. Cleaning:
   - Missing values: 0 kasus, metode: Re-run instan di lapangan jika terjadi error capture
   - Duplikat: 0 kasus, tindakan: Verifikasi nama file PCAP unik
   - Error: Hapus kolom Timestamp asli dari CSV untuk menjaga privasi
4. Transformation: Pergeseran timestamp PCAP (editcap -t) agar sinkron dengan jadwal target, serta Augmentasi Data (generate_data.py) untuk menambah 24 run tambahan
5. Normalisasi: Tidak dilakukan (None), parameter dari Tidak berlaku
6. Data akhir: 60 records, 14 features (setelah menghapus kolom Timestamp)
7. Leakage check: [x] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Ya, di masa lalu saya sering melakukan normalisasi Min-Max secara refleks karena itu merupakan kebiasaan umum sebelum analisis data. Risiko dari over-preprocessing (termasuk normalisasi atau imputasi yang tidak perlu) adalah distorsi data asli yang menghilangkan makna fisik penting (seperti mengubah throughput nyata dalam Kbps menjadi nilai abstrak 0-1). Hal ini mempersulit interpretasi praktis oleh pembaca naskah riset.
