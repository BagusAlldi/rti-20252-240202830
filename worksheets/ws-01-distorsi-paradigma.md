# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : ____________________
Tanggal          : ____________________

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: ____________________
   - Data yang dibutuhkan untuk verifikasi: ____________________

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: ____________________

3. Identifikasi distorsi:
   - Asumsi tersembunyi: ____________________
   - Sumber bias potensial: ____________________
   - Langkah mitigasi: ____________________

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: ____________________
   - Batasan yang diakui sejak awal: ____________________
```

---

# ✅ **Latihan 1 **

**Paper yang dipilih:**

> Judul: *Evaluasi Algoritma Machine Learning untuk Klasifikasi dan Prediksi Penggunaan Lahan*
> Penulis (Tahun): Fajar Nugraha et al. (2024) ([Jurnal UGM][1])

📌 Kenapa ini bagus:

* Penelitian Indonesia (IPB, UGM context)
* Mengandung klaim performa (akurasi & kappa)
* Cocok banget untuk analisis distorsi

---

## 📊 Analisis Research Trust Model

| Tahap                     | Apa yang Dilakukan                                    | Potensi Distorsi                                                 |
| ------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------- |
| **Reality → Data**        | Menggunakan data penggunaan lahan (Sub DAS Tanralili) | Data terbatas geografis (tidak representatif global)             |
| **Data → Processing**     | Klasifikasi citra dengan algoritma (kNN, SVM, GMM)    | Preprocessing bisa mempengaruhi hasil (misalnya pemilihan fitur) |
| **Processing → Analysis** | Evaluasi model dengan metrik **kappa & accuracy**     | Overfitting atau tuning parameter berlebihan                     |
| **Analysis → Inference**  | Menyimpulkan SVM memiliki performa terbaik            | Tidak semua kondisi diuji (generalization issue)                 |
| **Inference → Knowledge** | Klaim metode terbaik untuk klasifikasi lahan          | Overgeneralization ke wilayah lain                               |

📌 Paper ini memang menunjukkan bahwa:

* SVM memiliki kinerja rata-rata terbaik (kappa tinggi) ([Jurnal UGM][1])

---

## 🎯 Distorsi paling besar:

➡️ **Reality → Data**

---

## ⚠️ Dua distorsi spesifik:

### 1. **Sampling Bias (Geographical Bias)**

* Dataset hanya dari **satu wilayah (Sub DAS Tanralili)**
* Tidak mencerminkan kondisi wilayah lain di Indonesia
  👉 Dampak: hasil tidak bisa digeneralisasi luas

---

### 2. **Metric Bias (Kappa vs Real-world Performance)**

* Menggunakan **kappa & accuracy**
* Belum tentu mencerminkan performa di kondisi nyata (misalnya perubahan lahan dinamis)

---

# ✅ **Latihan 2 — Analisis Etika (Versi Lebih Akademik)**

| Perspektif           | Analisis                                                |
| -------------------- | ------------------------------------------------------- |
| **Kejujuran ilmiah** | Menghapus outlier tanpa alasan = manipulasi             |
| **Transparansi**     | Harus dijelaskan apakah outlier error atau fenomena     |
| **Peer review**      | Reviewer akan meminta uji statistik (IQR, Z-score, dll) |

---

### ✅ Keputusan akhir:

> Outlier **tidak boleh dihapus hanya untuk mendapatkan hasil signifikan**.
>
> Praktik yang benar:
>
> * Laporkan hasil dengan & tanpa outlier
> * Jelaskan alasan penghapusan
>
> Ini penting untuk menghindari bias dan praktik seperti **HARKing**.

---

# ✅ **Latihan 3 — Posisi Paradigma**

**Topik riset:**
➡️ *Evaluasi algoritma machine learning untuk klasifikasi penggunaan lahan*

| Kriteria   | Positivis                     | Interpretivis          | Design Science           |
| ---------- | ----------------------------- | ---------------------- | ------------------------ |
| Kesesuaian | 5                             | 1                      | 4                        |
| Jenis data | Data numerik (akurasi, kappa) | Tidak relevan          | Model ML sebagai artefak |
| Limitasi   | Abaikan konteks sosial        | Tidak cocok eksperimen | Fokus artefak            |

---

### 🎯 Paradigma:

➡️ **Positivis + Design Science**

---

### 📌 Alasan:

* Positivis → karena berbasis pengukuran objektif
* Design Science → karena membangun & menguji model ML

---

# ✅ **Refleksi **

> Sebelumnya saya cenderung menerima hasil seperti “akurasi tinggi” sebagai indikator keberhasilan metode.
>
> Namun setelah memahami Research Trust Model, saya menyadari bahwa hasil tersebut sangat bergantung pada:
>
> * kualitas dataset
> * metode preprocessing
> * metrik evaluasi
>
> Pada paper ini, misalnya, penggunaan dataset yang terbatas secara geografis berpotensi menimbulkan bias dalam generalisasi hasil.
>
> Oleh karena itu, saya kini akan lebih kritis dengan mempertanyakan:
>
> * apakah data representatif
> * apakah metode evaluasi sesuai
> * apakah hasil dapat diterapkan di konteks lain

---
