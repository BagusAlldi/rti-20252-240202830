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
   - **Pertanyaan pertama saya:** Apakah efisiensi alur kerja yang dihasilkan benar-benar konsisten di seluruh unit (tiket, parkir, restoran) atau hanya pada satu bagian saja?.
   - **Data yang dibutuhkan untuk verifikasi:** Hasil pengujian komparatif antara sistem lama dan sistem baru, serta data penurunan *error rate* dari pengguna lapangan.

2. **Posisi paradigma:**
   - **Pendekatan:** [X] Design Science Research (DSR)
   - **Alasan:** Penelitian ini membangun **artefak** berupa desain antarmuka *high fidelity* dan prototipe sistem informasi pariwisata untuk memecahkan masalah efisiensi operasional.

3. **Identifikasi distorsi:**
   - **Asumsi tersembunyi:** Dianggap bahwa operator sistem memiliki keterampilan dasar komputer yang cukup untuk mengoperasikan sistem baru.
   - **Sumber bias potensial:** Jumlah responden uji coba yang terbatas (hanya 6 orang), yang mungkin belum merepresentasikan seluruh variasi perilaku pengguna.
   - **Langkah mitigasi:** Melakukan evaluasi berkelanjutan dengan teknik *System Usability Scale* (SUS) pada penelitian selanjutnya untuk cakupan yang lebih luas.

---

## Latihan 1 — Identifikasi Distorsi

**Paper yang dipilih:**
> **Judul:** Implementasi Double Diamond Model pada Pengembangan User Interface User Experience Sistem Informasi Pariwisata Terintegrasi .  
> **Penulis (Tahun):** Riyan Abdul Aziz (2025).  
> **Sumber/Link DOI:** JURTI, Vol.9 No.3 .

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| **Reality → Data** | Observasi lapangan dan FGD dengan operator, akuntan, dan pengelola di Janti Park. |**Sampling Bias:** Data hanya diambil dari satu objek wisata (Janti Park), sehingga masalah di tempat lain mungkin berbeda. |
| **Data → Processing** | Mengelompokkan poin permasalahan menggunakan teknik *affinity diagram*. | **Subjective Bias:** Pengelompokan kategori masalah sangat bergantung pada interpretasi peneliti terhadap hasil FGD. |
| **Processing → Analysis** | Membandingkan sistem lama (Versi A) dan sistem baru (Versi B) melalui *A/B Testing*. | **Testing Bias:** Responden mungkin cenderung memberikan penilaian positif karena mengetahui sedang menguji sistem baru yang "lebih baik". |
| **Analysis → Inference** | Menyimpulkan peningkatan kepuasan 64% dan penurunan kesalahan 83%. | **Confirmation Bias:** Fokus hanya pada indikator yang meningkat secara signifikan. |
| **Inference → Knowledge** | Menyatakan bahwa *Double Diamond Model* memberikan struktur desain yang sistematis untuk sistem pariwisata. | **Overgeneralization:** Keberhasilan pada satu platform web belum tentu otomatis berlaku sama efektifnya pada platform *mobile*. |

**Distorsi paling besar di tahap:** Reality → Data (karena keterbatasan jumlah responden pengujian).

---

## Latihan 2 — Analisis Kasus Etika

**Skenario:** Menemukan kegagalan transaksi saat lonjakan pengunjung (1.500-2.000 orang) pada sistem lama.

| Perspektif | Analisis |
|------------|---------|
| **Kejujuran ilmiah** | Peneliti harus melaporkan secara jujur bahwa sistem lama mengalami *crash* dan memaksa petugas kembali ke cara manual. |
| **Transparansi** |Mengakui adanya ketidaksinkronan data pemasukan bulanan yang ditemukan saat observasi. |
| **Peer review** | Menyajikan data perbandingan waktu penyelesaian tugas (6,5 menit vs 3,2 menit) secara objektif agar dapat divalidasi peneliti lain. |

**Keputusan akhir dan justifikasi:**
> Melaporkan seluruh kelemahan sistem lama tanpa menutup-nutupi data kegagalan transaksi. Justifikasi ini penting agar pengembangan sistem baru (artefak) benar-benar didasarkan pada *problem statement* yang valid dan nyata dari lapangan.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Sistem Informasi Pariwisata Terintegrasi.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| **Kesesuaian (1–5)** | 4  | 3  | 5  |
| **Jenis data** | Persentase penurunan kesalahan dan waktu tugas | Hasil FGD dan perasaan operator terhadap sistem. | Prototipe *High Fidelity* dan hasil *Blackbox Testing*. |
| **Limitasi** | Kurang menangkap sisi emosi pengguna. | Data sulit dikuantifikasi secara matematis. | Terlalu fokus pada penyelesaian fungsional artefak. |

**Paradigma yang dipilih:** Design Science Research (DSR).  
**Alasan:** Penelitian ini bertujuan menghasilkan solusi praktis melalui pembuatan artefak digital yang diuji secara sistematis lewat empat tahap: *discover, define, develop,* dan *deliver*.

---

## Refleksi

**Jawaban:**
> Sebelumnya, saya hanya melihat UI/UX sebagai keindahan tampilan. Namun, melalui studi kasus sistem terintegrasi ini, saya belajar bahwa klaim "lebih baik" harus dibuktikan dengan rantai transformasi yang valid, seperti penurunan waktu penyelesaian tugas hingga 50%. Sekarang, pertanyaan utama saya saat membaca paper adalah: *"Bagaimana metode ini memitigasi distorsi pada tahap pengumpulan kebutuhan pengguna (Discover)?"*.

