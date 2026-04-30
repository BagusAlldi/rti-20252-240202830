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

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

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

**Nama Peneliti:** Bagus Alldiansyah  
**Tanggal:** 11 April 2026

1. **Ketika membaca klaim "metode X 95% akurat":**
   - [cite_start]**Pertanyaan pertama saya:** Apakah efisiensi alur kerja yang dihasilkan benar-benar konsisten di seluruh unit (tiket, parkir, restoran) atau hanya pada satu bagian saja? [cite: 10, 15]
   - [cite_start]**Data yang dibutuhkan untuk verifikasi:** Hasil pengujian komparatif antara sistem lama dan sistem baru, serta data penurunan *error rate* dari pengguna lapangan[cite: 15, 187].

2. **Posisi paradigma:**
   - **Pendekatan:** [X] Design Science Research (DSR)
   - [cite_start]**Alasan:** Penelitian ini membangun **artefak** berupa desain antarmuka *high fidelity* dan prototipe sistem informasi pariwisata untuk memecahkan masalah efisiensi operasional[cite: 41, 155].

3. **Identifikasi distorsi:**
   - [cite_start]**Asumsi tersembunyi:** Dianggap bahwa operator sistem memiliki keterampilan dasar komputer yang cukup untuk mengoperasikan sistem baru[cite: 108].
   - [cite_start]**Sumber bias potensial:** Jumlah responden uji coba yang terbatas (hanya 6 orang), yang mungkin belum merepresentasikan seluruh variasi perilaku pengguna[cite: 15].
   - [cite_start]**Langkah mitigasi:** Melakukan evaluasi berkelanjutan dengan teknik *System Usability Scale* (SUS) pada penelitian selanjutnya untuk cakupan yang lebih luas[cite: 215].

---

## Latihan 1 — Identifikasi Distorsi

**Paper yang dipilih:**
> [cite_start]**Judul:** Implementasi Double Diamond Model pada Pengembangan User Interface User Experience Sistem Informasi Pariwisata Terintegrasi [cite: 2, 3]  
> [cite_start]**Penulis (Tahun):** Riyan Abdul Aziz (2025) [cite: 4, 1]  
> [cite_start]**Sumber/Link DOI:** JURTI, Vol.9 No.3 [cite: 1]

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| **Reality → Data** | [cite_start]Observasi lapangan dan FGD dengan operator, akuntan, dan pengelola di Janti Park[cite: 83]. | [cite_start]**Sampling Bias:** Data hanya diambil dari satu objek wisata (Janti Park), sehingga masalah di tempat lain mungkin berbeda[cite: 20]. |
| **Data → Processing** | [cite_start]Mengelompokkan poin permasalahan menggunakan teknik *affinity diagram*[cite: 135]. | [cite_start]**Subjective Bias:** Pengelompokan kategori masalah sangat bergantung pada interpretasi peneliti terhadap hasil FGD[cite: 149]. |
| **Processing → Analysis** | [cite_start]Membandingkan sistem lama (Versi A) dan sistem baru (Versi B) melalui *A/B Testing*[cite: 185]. | [cite_start]**Testing Bias:** Responden mungkin cenderung memberikan penilaian positif karena mengetahui sedang menguji sistem baru yang "lebih baik"[cite: 183]. |
| **Analysis → Inference** | [cite_start]Menyimpulkan peningkatan kepuasan 64% dan penurunan kesalahan 83%[cite: 15]. | [cite_start]**Confirmation Bias:** Fokus hanya pada indikator yang meningkat secara signifikan[cite: 200]. |
| **Inference → Knowledge** | [cite_start]Menyatakan bahwa *Double Diamond Model* memberikan struktur desain yang sistematis untuk sistem pariwisata[cite: 47]. | [cite_start]**Overgeneralization:** Keberhasilan pada satu platform web belum tentu otomatis berlaku sama efektifnya pada platform *mobile*[cite: 42]. |

[cite_start]**Distorsi paling besar di tahap:** Reality → Data (karena keterbatasan jumlah responden pengujian)[cite: 15, 213].

---

## Latihan 2 — Analisis Kasus Etika

[cite_start]**Skenario:** Menemukan kegagalan transaksi saat lonjakan pengunjung (1.500-2.000 orang) pada sistem lama[cite: 23, 24].

| Perspektif | Analisis |
|------------|---------|
| **Kejujuran ilmiah** | [cite_start]Peneliti harus melaporkan secara jujur bahwa sistem lama mengalami *crash* dan memaksa petugas kembali ke cara manual[cite: 87, 88]. |
| **Transparansi** | [cite_start]Mengakui adanya ketidaksinkronan data pemasukan bulanan yang ditemukan saat observasi[cite: 29]. |
| **Peer review** | [cite_start]Menyajikan data perbandingan waktu penyelesaian tugas (6,5 menit vs 3,2 menit) secara objektif agar dapat divalidasi peneliti lain[cite: 187]. |

**Keputusan akhir dan justifikasi:**
> Melaporkan seluruh kelemahan sistem lama tanpa menutup-nutupi data kegagalan transaksi. [cite_start]Justifikasi ini penting agar pengembangan sistem baru (artefak) benar-benar didasarkan pada *problem statement* yang valid dan nyata dari lapangan[cite: 150, 171].

---

## Latihan 3 — Posisi Paradigma

[cite_start]**Topik riset:** Sistem Informasi Pariwisata Terintegrasi[cite: 3, 16].

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| **Kesesuaian (1–5)** | [cite_start]4 [cite: 15] | [cite_start]3 [cite: 83] | [cite_start]5 [cite: 42] |
| **Jenis data** | [cite_start]Persentase penurunan kesalahan dan waktu tugas[cite: 15, 187]. | [cite_start]Hasil FGD dan perasaan operator terhadap sistem[cite: 83, 193]. | [cite_start]Prototipe *High Fidelity* dan hasil *Blackbox Testing*[cite: 155, 172]. |
| **Limitasi** | Kurang menangkap sisi emosi pengguna. | Data sulit dikuantifikasi secara matematis. | Terlalu fokus pada penyelesaian fungsional artefak. |

[cite_start]**Paradigma yang dipilih:** Design Science Research (DSR)[cite: 42, 47].  
[cite_start]**Alasan:** Penelitian ini bertujuan menghasilkan solusi praktis melalui pembuatan artefak digital yang diuji secara sistematis lewat empat tahap: *discover, define, develop,* dan *deliver*[cite: 43, 205].

---

## Refleksi

**Jawaban:**
> Sebelumnya, saya hanya melihat UI/UX sebagai keindahan tampilan. [cite_start]Namun, melalui studi kasus sistem terintegrasi ini, saya belajar bahwa klaim "lebih baik" harus dibuktikan dengan rantai transformasi yang valid, seperti penurunan waktu penyelesaian tugas hingga 50%[cite: 14, 212]. [cite_start]Sekarang, pertanyaan utama saya saat membaca paper adalah: *"Bagaimana metode ini memitigasi distorsi pada tahap pengumpulan kebutuhan pengguna (Discover)?"*[cite: 61, 209].
---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> ___________________________________________________
> ___________________________________________________
