# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

  Contoh config YAML dengan feature toggles:
  ```yaml
  model:
    type: cnn          # IV: ganti "rf" untuk kondisi baseline
  features:
    use_temporal: true  # toggle komponen temporal
    use_normalization: true  # toggle preprocessing
  experiment:
    seed: 42
    runs: 5
  ```
  Dengan pendekatan ini, berbeda kondisi eksperimen = berbeda satu baris config, **tanpa mengubah kode**.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel... di lingkungan kampus Universitas Putra Bangsa (UPB)?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Titik Spasial & Temporal | IV | Modul Packet Sniffer (Komponen I) | Memindahkan posisi fisik gawai penerima dan mengatur penjadwalan waktu capture. |
| Parameter QoS & Indeks | DV | Modul Data Exporter (Komponen II) & Modul Scoring Engine (Komponen III) | Mengekstrak berkas .pcap menjadi .csv dan menghitung nilai metrik QoS berdasar rumus TIPHON. |
| Durasi, Software, Device | CV | Script konfigurasi locked di Modul Packet Sniffer | Menetapkan runtime 5 menit, Wireshark versi seragam, dan keseragaman hardware laptop. |

4 Prinsip Desain:
  [x] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [x] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [x] Measurement Integration — Pengukuran DV built-in
  [x] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : Paket data nirkabel mentah (raw traffic capture) format berkas biner .pcap.
  Parameter      : Durasi capture 5 menit per sesi, 4 lokasi spasial (Ruby Tengah, Kopma, Lorong Lab Komputer, Lorong Lab AI), 3 sesi temporal harian (07.50, 13.00, 16.00).
  Output format  : File data tabular metrik (.csv) dan Laporan visual diagram batang komparatif di Dashboard Reporter (Komponen IV).
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel... di lingkungan kampus Universitas Putra Bangsa (UPB)?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Titik Spasial & Temporal | IV | Modul Packet Sniffer (Komponen I) | Ganti parameter lokasi capture dan jadwal waktu capture |
| Metrik QoS & Indeks MOS | DV | Modul Data Exporter & Modul Scoring Engine | Pemrosesan ekstraksi .pcap -> .csv dan kalkulasi indeks TIPHON |
| Durasi, Software, Hardware | CV | Script config sniffer & spesifikasi laptop homogen | Kunci durasi 5 menit, lock Wireshark version, gunakan 1 laptop yang sama |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? —

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ | Setiap modul (sniffer, exporter, scoring engine) melayani manipulasi/pengukuran variabel tertentu. |
| Modularity | ✅ | Modul Scoring Engine dapat diganti (Excel -> Pandas) tanpa memengaruhi modul Packet Sniffer. |
| Controllability | ✅ | Parameter durasi capture dan interface NIC dikunci dalam script configurasi. |
| Measurability | ✅ | Dashboard Reporter otomatis mengumpulkan data hasil perhitungan dan menyajikannya secara grafis. |

**Prinsip mana yang paling sulit dipenuhi?** Controllability (mengontrol background noise/interferensi dari trafik nirkabel pengguna lain di sekitar titik).
**Strategi untuk mengatasinya:**
> Melakukan pencatatan trafik latar belakang (background noise) selama durasi capture untuk mengidentifikasi anomali/pencilan data (outlier).

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✅ Pandas Exporter | ✅ Scoring Engine TIPHON | ✅ Dashboard Reporter | Sistem berjalan otomatis menghasilkan data terstruktur beserta visualisasi predikat MOS |
| – A | ❌ (Excel Exporter) | ✅ | ✅ | Pengolahan lambat, rentan kesalahan input manual |
| – B | ✅ | ❌ (Tanpa Scoring Engine) | ✅ | Dashboard hanya menyajikan angka mentah (delay, throughput) tanpa predikat kelayakan |
| – C | ✅ | ✅ | ❌ (Tanpa Dashboard) | Hasil analisis disajikan dalam bentuk file log teks di konsol |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen B (Scoring Engine)
**Mengapa?**
> Karena tanpa standardisasi TIPHON (Scoring Engine), metrik teknis rasio yang diekstraksi tidak memiliki makna predikat kelayakan bagi pengguna akhir.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risiko membangun sistem riset secara monolitik (seperti produk) adalah kesulitan dalam melakukan isolasi variabel. Ketika performa logis menurun, peneliti tidak dapat membuktikan apakah degradasi tersebut disebabkan oleh variabel riset (IV) yang diuji atau karena overhead dari fitur tambahan yang tidak relevan dengan RQ. Arsitektur modular penting untuk memastikan variable isolation dan reproducibility eksperimen.
