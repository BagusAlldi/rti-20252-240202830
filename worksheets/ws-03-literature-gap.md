# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Analisis Kualitas Layanan (Quality of Service - QoS) Jaringan Nirkabel Menggunakan Parameter TIPHON
Database   : Google Scholar & ResearchGate
Query      : ("Quality of Service" OR "QoS") AND ("TIPHON" OR "ETSI") AND ("Wi-Fi" OR "wireless" OR "campus")
Tahun      : 2024–2026
Hasil awal : 24 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Safitri dkk. | 2025 | Kuantitatif, Wireshark, TIPHON | Jaringan SMK Dharma Bahari (5 ruangan) | Parameter throughput bervariasi | Spasial kecil (1 gedung homogen) & temporal pendek (1 hari capture). |
| Nisa dkk. | 2024 | Kuantitatif, Wireshark, TIPHON | Kampus 1 Unjaya (6 area spasial) | Rata-rata indeks QoS kategori "Medium" (skor 3) | Pengukuran bandwidth statis, tidak mengevaluasi fluktuasi temporal harian. |
| Fitriya | 2026 | Kuantitatif, Wireshark, TIPHON | MA Futuhiyyah (5 lokasi, 3 sesi) | Kualitas baik (rata-rata indeks 3.13) | Bandwidth kecil (20 Mbps), infrastruktur homogen. |
| Anissabilla & Kusumarani | 2025 | Kuantitatif, Wireshark, TIPHON | Jaringan rumahan RunNet 10 Mbps | Penilaian throughput & packet loss video conference | Skala mikro (5-6 gawai rumah). |
| Ardiansyah & Pamuji | 2025 | Action research, Wireshark, TIPHON | Jaringan Alfanet (3 hari pengujian) | Analisis kestabilan throughput & delay | Temporal sangat sempit (3 hari). |

Pola yang ditemukan:
  Metode dominan     : Deskriptif Kuantitatif menggunakan Wireshark untuk penangkapan paket data secara real-time dan standar TIPHON.
  Dataset umum       : Rekaman aktivitas data nirkabel pada gawai penerima tunggal/kelompok kecil.
  Limitasi berulang  : Skala jaringan homogen/kecil dan keterbatasan sampel waktu (snapshot bias).

GAP IDENTIFICATION

Gap 1: [Jenis: context]
  Deskripsi    : Mayoritas studi mengevaluasi objek dengan infrastruktur kecil homogen (sekolah menengah, rumah) dengan beban terprediksi.
  Bukti        : Safitri dkk. (2025) di SMK (5 ruangan), Fitriya (2026) di MA, Anissabilla (2025) di rumah. Belum menyentuh arsitektur enterprise multi-building seperti universitas.
  Signifikansi : Memetakan QoS pada kampus membutuhkan pendekatan dinamis karena sebaran gedung dan kepadatan gawai pengguna berubah drastis antartitik spasial.

Gap 2: [Jenis: data]
  Deskripsi    : Mayoritas studi merekam aktivitas jaringan dalam rentang waktu sangat sempit (1-3 hari).
  Bukti        : Safitri dkk. (2025) hanya merekam 1 hari (Kamis, 13 Nov 2025), Ardiansyah (2025) merekam data akumulatif 3 hari.
  Signifikansi : Mengabaikan fluktuasi jangka panjang siklus mingguan perkuliahan yang heterogen.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| Safitri dkk. (2025) | Menguji jaringan sekolah menggunakan parameter logis TIPHON | Mewakili common practice analisis QoS dengan Wireshark | [Analisis QoS ... Surabaya.pdf](file:///e:/RTI/literatur/Analisis+QoS+Menggunakan+Standar+TIPHON+pada+Jaringan+Wi-Fi+SMK+Dharma+Bahari+Surabaya.pdf) |
| Nisa dkk. (2024) | Menguji pada lingkup universitas (Kampus 1 Unjaya) | Mewakili evaluasi pada objek berskala kampus | [pwcahyo, ... Unjay.pdf](file:///e:/RTI/literatur/pwcahyo,+Analisis+Quality+of+Service+(QoS)+Menggunakan+Standar+Parameter+Tiphon+pada+Jaringan+Internet+Berbasis+Wi-Fi+Kampus+1+Unjay.pdf) |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Analisis Kualitas Layanan (Quality of Service - QoS) Jaringan Wi-Fi Kampus tipe Enterprise Multi-Building
**Query pencarian:** ("Quality of Service" OR "QoS") AND ("TIPHON" OR "ETSI") AND ("Wi-Fi" OR "wireless" OR "campus")
**Database:** Google Scholar & ResearchGate

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Safitri dkk. | 2025 | Kuantitatif, Wireshark, TIPHON | Jaringan SMK Dharma Bahari (5 ruangan) | Parameter throughput bervariasi | Spasial kecil & temporal pendek (1 hari). |
| 2 | Nisa dkk. | 2024 | Kuantitatif, Wireshark, TIPHON | Kampus 1 Unjaya (6 area spasial) | Rata-rata indeks QoS kategori "Medium" (skor 3) | Pengukuran bandwidth statis, general. |
| 3 | Fitriya | 2026 | Kuantitatif, Wireshark, TIPHON | MA Futuhiyyah (5 lokasi, 3 sesi) | Kualitas baik (rata-rata indeks 3.13) | Bandwidth kecil (20 Mbps), homogen. |
| 4 | Anissabilla & Kusumarani | 2025 | Kuantitatif, Wireshark, TIPHON | Jaringan rumahan RunNet 10 Mbps | Penilaian video conference | Skala mikro (5-6 gawai rumah). |
| 5 | Ardiansyah & Pamuji | 2025 | Action research, Wireshark, TIPHON | Jaringan Alfanet (3 hari pengujian) | Analisis kestabilan throughput | Temporal sangat sempit (3 hari). |

**Pola yang terlihat — Metode dominan:** Deskriptif Kuantitatif menggunakan Wireshark untuk penangkapan paket data secara real-time dan klasifikasi standar TIPHON.
**Limitasi yang berulang:** Objek berskala kecil homogen dan bias sampling waktu durasi pendek (snapshot bias).

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [ ] Ya / [x] Tidak | — |
| Method Gap | [ ] Ya / [x] Tidak | — |
| Data Gap | [x] Ya / [ ] Tidak | Mayoritas studi mengalami bias temporal dengan durasi sampling 1-3 hari saja. |
| Context Gap | [x] Ya / [ ] Tidak | Belum ada evaluasi di lingkungan kampus enterprise multi-building yang dinamis. |

**Gap utama yang dipilih:** Context Gap dikombinasikan dengan Temporal Sampling Gap.
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena sebaran pengguna dan lalu lintas data pada kampus enterprise bersifat sangat dinamis dan heterogen di berbagai gedung dan jam sibuk perkuliahan. Mengabaikan fluktuasi spasial-temporal ini menyebabkan kegagalan sistem monitoring dalam mendeteksi bottle neck jaringan secara riil.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Safitri dkk. (2025) | Evaluasi jaringan akademis menggunakan parameter TIPHON | Mewakili common practice pemetaan QoS Wi-Fi dengan Wireshark | Ya, merupakan studi rujukan utama 2025 | [Analisis QoS ... Surabaya.pdf](file:///e:/RTI/literatur/Analisis+QoS+Menggunakan+Standar+TIPHON+pada+Jaringan+Wi-Fi+SMK+Dharma+Bahari+Surabaya.pdf) |
| 2 | Nisa dkk. (2024) | Menguji di lingkungan universitas dengan parameter yang sama | Mewakili baseline komparatif berskala kampus | Ya, studi rujukan kampus 2024 | [pwcahyo, ... Unjay.pdf](file:///e:/RTI/literatur/pwcahyo,+Analisis+Quality+of+Service+(QoS)+Menggunakan+Standar+Parameter+Tiphon+pada+Jaringan+Internet+Berbasis+Wi-Fi+Kampus+1+Unjay.pdf) |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Kedua baseline adalah studi akademis terbaru yang menerapkan metodologi analisis QoS secara ketat dengan parameter TIPHON.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Klaim "belum ada yang meneliti" adalah pernyataan tanpa dasar bukti pencarian sistematis. Sementara research gap yang valid adalah kesenjangan pengetahuan yang didefinisikan secara metodologis dan dibuktikan dengan analisis literatur yang transparan (concept-centric). Cara membuktikannya adalah dengan mendokumentasikan query pencarian secara jujur, mendefinisikan kriteria inklusi/ekklusi, dan memetakan limitasi studi terdahulu ke dalam matriks perbandingan.
