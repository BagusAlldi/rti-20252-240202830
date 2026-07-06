# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Jaringan Komputer / Analisis Kualitas Layanan (Quality of Service - QoS)
  Konteks  : Jaringan internet nirkabel (Wi-Fi) di lingkungan kampus Universitas Putra Bangsa (UPB) pada area perkuliahan yang padat aktivitas.

System Context
  Input       : Aliran paket data mentah (raw data traffic) dari aktivitas nirkabel gawai penerima dalam format berkas biner .pcap yang ditangkap menggunakan Wireshark.
  Process     : Penyadapan data (sniffing), ekspor biner .pcap ke .csv (Modul Data Exporter), kalkulasi metrik QoS (throughput, delay, jitter, packet loss) dan konversi ke skala indeks TIPHON (Modul Scoring Engine), serta pelaporan visual komparatif spasial-temporal di Dashboard Reporter.
  Output      : Nilai kuantitatif throughput (Kbps), packet loss (%), delay (ms), jitter (ms), dan indeks MOS kelayakan versi TIPHON (skala 0-4).
  Outcome     : Peta sebaran kualitas layanan Wi-Fi kampus sebagai rekomendasi empiris yang objektif bagi pengelola IT kampus untuk alokasi bandwidth dan penempatan Access Point.
  Constraints : Durasi capture dibatasi 5 menit per sesi, lokasi spasial dibatasi pada 4 area (Ruby Tengah, Kopma, Lorong Lab Komputer, Lorong Lab AI), sesi temporal dibatasi pada jam sibuk perkuliahan (07.50, 13.00, 16.00), spesifikasi perangkat NIC penerima homogen, dan versi Wireshark dikunci.
  Stakeholders: Pengelola IT/Network Administrator Kampus UPB, Dosen, Mahasiswa.

Fenomena → Problem
  Fenomena yang diamati             : Keluhan subjektif pengguna (mahasiswa/dosen) mengenai kelambatan koneksi internet Wi-Fi kampus UPB.
  Gejala (symptom) yang terukur     : Penurunan performa logis jaringan (throughput rendah, packet loss tinggi) di area tertentu pada jam sibuk perkuliahan.
  Masalah yang didiagnosis          : Monitoring internal IT hanya memantau status aktif/mati perangkat keras (hardware-centric), sehingga kegagalan alokasi bandwidth dan kemacetan trafik (traffic congestion) logis dari sudut pandang gawai pengguna (user-centric end-to-end) tidak terdeteksi.
  Masalah riset (researchable)      : Belum ada pemetaan kualitas layanan internet nirkabel (end-to-end QoS) menggunakan standar TIPHON pada arsitektur enterprise multi-building (seperti Kampus UPB) pada jam sibuk perkuliahan.
  Variabel yang terukur             : Throughput (Kbps), Packet Loss (%), Delay (ms), Jitter (ms), dan Nilai Indeks MOS.

Problem Quality Check
  [x] Clarity — Apakah satu orang membaca akan paham?
  [x] Measurability — Apakah ada metrik kuantitatif?
  [x] Relevance — Apakah penting untuk domain?
  [x] Testability — Apakah bisa gagal?
  [x] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Jaringan internet nirkabel (Wi-Fi) di lingkungan Universitas Putra Bangsa (UPB) kerap mengalami degradasi performa logis (Quality of Service) pada jam-jam aktif perkuliahan, namun sistem monitoring infrastruktur internal kampus saat ini hanya berfokus pada status aktif/mati perangkat nirkabel (hardware-centric) tanpa mengukur kualitas layanan riil dari sisi gawai pengguna (user-centric end-to-end). Ketiadaan data performa logis berkala ini mengakibatkan administrator jaringan kesulitan mendeteksi titik degradasi (bottleneck) akibat kegagalan alokasi kapasitas (bandwidth) dan kepadatan lalu lintas (traffic congestion) lokal secara spasial-temporal. Guna mengatasi kesenjangan informasi tersebut, penelitian ini bertujuan untuk memetakan capaian indeks QoS internet nirkabel di 5 lokasi strategis kampus UPB pada 3 interval waktu perkuliahan menggunakan parameter standar TIPHON berbasis rekaman paket data (traffic capture) Wireshark, guna menyediakan landasan keputusan yang objektif bagi optimasi infrastruktur jaringan bertipe enterprise multi-building.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Analisis Kualitas Layanan (Quality of Service - QoS) Jaringan Wi-Fi Kampus tipe Enterprise Multi-Building

| Tahap | Hasil |
|-------|-------|
| Reality | Pengguna Wi-Fi UPB sering merasakan kelambatan akses internet saat berada di area kampus. |
| Observed Issue (Symptom) | Sering terjadi request time out (RTO) dan kegagalan memuat SIA pada jam perkuliahan aktif. |
| Diagnosed Problem (Root Cause) | Sistem monitoring IT Helpdesk hanya mengamati ketersediaan perangkat keras nirkabel (up/down time), sehingga penumpukan pengguna dinamis (traffic congestion) di area tertentu gagal dideteksi secara logis. |
| Researchable Problem | Belum ada pemetaan performa logis Wi-Fi secara end-to-end menggunakan standar TIPHON yang meninjau variasi spasial (4 area observasi) dan temporal (3 sesi waktu) secara kuantitatif di UPB. |
| Measurable Variable | Throughput (Kbps), Packet Loss (%), Delay (ms), Jitter (ms), dan Indeks MOS TIPHON (0-4). |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> Jika ya, kembali ke tahap mana? —

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | File capture data paket biner (.pcap) berdurasi 5 menit dari Wireshark. |
| Process | Penyadapan data (sniffing) -> Ekspor PCAP ke CSV -> Perhitungan parameter QoS TIPHON -> Visualisasi dashboard. |
| Output | Angka metrik QoS riil dan nilai indeks MOS (kategori TIPHON). |
| Outcome | Basis data rekomendasi penataan Access Point dan alokasi bandwidth. |
| Constraints | 5 menit durasi capture, 4 titik spasial (Ruby Tengah, Kopma, Lorong Lab Komputer, Lorong Lab AI), 3 sesi waktu temporal (07.50, 13.00, 16.00), NIC homogen. |
| Stakeholders | IT Helpdesk UPB, Dosen, Mahasiswa. |

**Komponen mana yang paling relevan dengan masalah riset?** Process dan Constraints

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Masalah didefinisikan dengan jelas mencakup gap monitoring, parameter standar, dan batasan spasial-temporal. |
| Measurability | 5 | Diukur secara kuantitatif lewat throughput (Kbps), delay (ms), jitter (ms), dan packet loss (%) terstandar TIPHON. |
| Relevance | 5 | Sangat relevan bagi kestabilan pembelajaran digital sivitas akademika UPB. |
| Testability | 4 | Sangat dapat diuji dan dibuktikan salah (falsifiable) jika performa QoS tetap stabil di atas ambang batas. |
| Impact | 4 | Memberikan rekomendasi penataan bandwidth dan Access Point secara empiris. |

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
> Jaringan internet nirkabel (Wi-Fi) di lingkungan Universitas Putra Bangsa (UPB) kerap mengalami degradasi performa logis (Quality of Service) pada jam-jam aktif perkuliahan, namun sistem monitoring infrastruktur internal kampus saat ini hanya berfokus pada status aktif/mati perangkat nirkabel (hardware-centric) tanpa mengukur kualitas layanan riil dari sisi gawai pengguna (user-centric end-to-end). Ketiadaan data performa logis berkala ini mengakibatkan administrator jaringan kesulitan mendeteksi titik degradasi (bottleneck) akibat kegagalan alokasi kapasitas (bandwidth) dan kepadatan lalu lintas (traffic congestion) lokal secara spasial-temporal. Guna mengatasi kesenjangan informasi tersebut, penelitian ini bertujuan untuk memetakan capaian indeks QoS internet nirkabel di 4 lokasi strategis kampus UPB pada 3 interval waktu perkuliahan (07.50, 13.00, 16.00) menggunakan parameter standar TIPHON berbasis rekaman paket data (traffic capture) Wireshark selama 5 menit, guna menyediakan landasan keputusan yang objektif bagi optimasi infrastruktur jaringan bertipe enterprise multi-building.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan fundamental terletak pada sifat ketidakpastian dan tujuan akhirnya. Bug/error coding adalah masalah tertutup (closed problem) dengan kondisi benar yang sudah pasti dan diselesaikan secara deterministik melalui rekayasa/perbaikan kode (solve). Sementara itu, masalah riset adalah kesenjangan dalam tubuh pengetahuan (open problem) yang didekati secara ilmiah melalui pengujian hipotesis dan pembuktian empiris yang dapat direplikasi (understand & prove).
