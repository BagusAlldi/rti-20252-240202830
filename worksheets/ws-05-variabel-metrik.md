# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel... di lingkungan kampus Universitas Putra Bangsa (UPB)?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Titik Spasial | IV | Area observasi | 4 lokasi strategis (Ruby Tengah, Kopma, Lorong Lab Komputer, Lorong Lab AI) | Nominal | — | Penempatan fisik laptop penguji | Mewakili sebaran gedung dan jangkauan Access Point. |
| Interval Waktu | IV | Sesi waktu temporal | Sesi Pagi, Siang, Sore | Ordinal | Jam | Waktu mulai capture (07.50, 13.00, 16.00) | Mewakili fluktuasi kepadatan pengguna sesuai jadwal kuliah. |
| Throughput | DV | Kecepatan data riil | Volume data per detik | Ratio | Kbps | Ekstraksi statistik Wireshark | Mengukur lebar pita transfer data riil di sisi pengguna. |
| Packet Loss | DV | Kegagalan transmisi | Rasio paket data hilang | Ratio | % | Analisis deret paket Wireshark | Indikator degradasi transmisi akibat kemacetan. |
| Delay | DV | Latensi pengiriman | Waktu tunda paket | Ratio | ms | Rata-rata selisih waktu kirim-terima | Mengukur kelambatan transmisi data logis. |
| Jitter | DV | Variasi latensi | Deviasi waktu tunda | Ratio | ms | Selisih variasi delay antar-paket | Mengukur kestabilan koneksi transport layer. |
| Indeks MOS | DV | Kategori kelayakan | Indeks kepuasan (0-4) | Ordinal | Skala | Konversi metrik utama ke standar TIPHON | Standardisasi evaluasi kenyamanan jaringan (ETSI). |
| Durasi Capture | CV | Waktu penyadapan | Durasi capture 5 menit | Ratio | menit | Timer program capture | Menjamin keadilan sampel statistik di tiap titik. |
| Perangkat Uji | CV | Hardware NIC | Laptop & NIC homogen | Nominal | — | Penggunaan 1 unit laptop yang sama | Menghilangkan bias sensitivitas antena penerima. |
| Versi Software | CV | Analisis paket | Software Wireshark homogen | Nominal | — | Mengunci versi software seragam | Menghindari perbedaan kalkulasi oleh parser. |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [x] Setiap langkah terdokumentasi
  [x] Tidak ada "lompatan logis"
  [x] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel... di lingkungan kampus Universitas Putra Bangsa (UPB)?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Titik Spasial | IV | Area observasi nirkabel | 4 lokasi strategis kampus (Ruby Tengah, Kopma, Lorong Lab Komputer, Lorong Lab AI) | Nominal | — |
| Interval Waktu | IV | Kepadatan temporal | Sesi Pagi, Siang, Sore (07.50, 13.00, 16.00) | Ordinal | Jam |
| Parameter QoS | DV | Kualitas teknis logis | Throughput, Packet Loss, Delay, Jitter | Ratio | Kbps, %, ms |
| Indeks MOS | DV | Standardisasi kelayakan | Nilai indeks 0-4 versi TIPHON | Ordinal | Skala |
| Durasi Capture | CV | Batas waktu sampel | Capture konstan 5 menit | Ratio | menit |
| Perangkat NIC | CV | Homogenitas alat | 1 unit laptop penguji | Nominal | — |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? —

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Metrik QoS TIPHON mewakili standar industri telekomunikasi (ETSI) untuk evaluasi performansi logis. |
| Sensitive | 4 | Menggunakan data rasio (milidetik dan persentase) untuk menangkap anomali/penurunan kinerja kecil. |
| Feasible | 5 | Data sangat mudah diperoleh melalui software sniffing gratis Wireshark. |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Indeks MOS TIPHON (0-4) digunakan sebagai metrik sekunder untuk mengonversi data teknis ratio menjadi klasifikasi kelayakan keluhan pengguna secara komparatif.

**Contoh kasus ceiling effect untuk metrik ini:**
> Parameter Packet Loss bernilai 0% pada saat jaringan tidak digunakan (idle), sehingga tidak dapat mendeteksi potensi penurunan kinerja lainnya seperti peningkatan delay akibat antrian router.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | Ya, data terekam penuh selama 10 menit | Batasi buffer capture agar tidak terjadi packet drop di NIC. |
| Consistency | *Apakah ada kontradiksi internal?* | Format file PCAP seragam di semua sesi | Gunakan versi aplikasi Wireshark yang sama di semua titik. |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | Ya, data paket logis end-to-end di gawai pengguna | Kunci posisi laptop penguji secara konsisten di setiap sesi. |
| Representativeness | *Apakah sampel mewakili populasi target?* | Ya, mewakili siklus mingguan perkuliahan | Lakukan sampling berulang pada hari perkuliahan aktif yang berbeda. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data (p-hacking) memicu bias konfirmasi karena peneliti cenderung memilih metrik yang hanya menguntungkan dan mendukung hipotesis mereka. Eksplorasi data yang sah dilakukan untuk menemukan hubungan baru tanpa klaim pembuktian, dan hasilnya dilaporkan secara transparan sebagai temuan exploratory, bukan hasil konfirmatori hipotesis.
