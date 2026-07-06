# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [x] Problem → Gap: masalah terdokumentasi di literatur
  [x] Gap → RQ: pertanyaan menjawab gap spesifik
  [x] RQ → Hypothesis: hipotesis memprediksi jawaban
  [x] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [x] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [x] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [x] Istilah sama di semua bagian
  [x] Variabel di RQ = variabel di hipotesis = metrik di desain
  [x] Scope tidak berubah dari masalah ke eksperimen

Cognitive Trap Checklist:
  [x] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [x] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [x] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [x] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [x] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria     | 1 (Lemah)                                        | 2 (Cukup)                                     | 3 (Baik)                                           | Skor |
|------------- |--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|------|
| Koherensi    | >2 koneksi vertikal terputus                     | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, red thread jelas        | 3    |
| Specificity  | Variabel/metrik masih abstrak, tidak ada angka   | Sebagian metrik terdefinisi numerik           | Semua metrik + threshold + unit pengukuran jelas   | 3    |
| Feasibility  | Timeline >6 bulan tanpa memperhitungkan sumber   | Timeline 3-6 bulan dengan asumsi tertentu     | Timeline 1-3 bulan realistis dengan rencana detail | 3    |
| Rigor        | Baseline tidak jelas atau straw man              | 1-2 baseline dengan justifikasi partial       | 2+ baseline SOTA + justifikasi pemilihan lengkap   | 3    |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Wi-Fi UPB kerap mengalami degradasi performa logis (QoS) pada jam sibuk perkuliahan, namun monitoring internal hanya berfokus pada status aktif/mati perangkat keras tanpa mengevaluasi kualitas layanan riil di sisi pengguna (end-to-end). |
| Gap | WS-03 | Kebanyakan studi terdahulu berfokus pada objek kecil homogen (sekolah/rumah) dengan sampling temporal sangat sempit (1-3 hari), mengabaikan arsitektur enterprise multi-building dan fluktuasi jangka panjang siklus mingguan perkuliahan. |
| RQ | WS-04 | Bagaimanakah pemetaan capaian indeks kualitas layanan internet nirkabel yang ditinjau dari parameter throughput, packet loss, delay, dan jitter bersandarkan standarisasi TIPHON jika dikomparasikan terhadap nilai ambang batas kelayakan performa minimum jaringan pada jam sibuk perkuliahan dengan memanfaatkan basis data rekaman lalu lintas paket (traffic capture) Wireshark di lingkungan kampus Universitas Putra Bangsa (UPB)? |
| Hipotesis | WS-04 | H₁: Terdapat penurunan kualitas layanan internet nirkabel (QoS) yang signifikan di bawah nilai ambang batas kelayakan minimum standar TIPHON (skor indeks < 3 / kategori Cukup atau Buruk) pada jam sibuk perkuliahan di lingkungan kampus UPB. |
| Variabel & Metrik | WS-05 | IV: 4 titik spasial (Ruby Tengah, Kopma, Lab Komputer, Lab AI) & 3 sesi temporal (07.50, 13.00, 16.00). DV: Throughput, Packet Loss, Delay, Jitter, & Indeks MOS. CV: Durasi capture 5 menit, NIC homogen, Wireshark versi seragam. |
| Sistem | WS-06 | Terdiri atas Modul Sniffer (capture biner .pcap), Modul Exporter (pcap to csv), Modul Scoring Engine (kalkulasi metrik & indeks TIPHON), dan Modul Dashboard Reporter (visualisasi grafis komparatif). |
| Desain Eksperimen | WS-07 | Tipe: Comparison Study. Control: Hasil evaluasi QoS di objek sekolah homogen (Safitri dkk., 2025) dan kampus bandwidth statis (Nisa dkk., 2024). Treatment: Pengujian spasial-temporal di 4 lokasi dan 3 sesi waktu perkuliahan UPB dengan capture 5 menit. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Gap kontekstual & temporal diidentifikasi langsung dari ketiadaan studi terdahulu yang meneliti performa logis end-to-end pada arsitektur universitas yang dinamis. |
| Gap → RQ | ✅ | RQ secara langsung menguji pemetaan spasial (4 titik) dan temporal (3 sesi perkuliahan) di kampus UPB yang merupakan wujud arsitektur enterprise. |
| RQ → Hypothesis | ✅ | H₁ memprediksi kualitas logis bernilai di bawah threshold kelayakan minimum standar TIPHON (indeks < 3) pada jam-jam sibuk perkuliahan. |
| Hypothesis → Metric | ✅ | Parameter throughput, delay, jitter, packet loss, dan indeks MOS TIPHON mengukur variabel dalam hipotesis secara presisi. |
| Metric → System | ✅ | Modul Data Exporter mengekstrak metrik kuantitatif dan Modul Scoring Engine mengkonversinya ke dalam indeks MOS 0-4 secara otomatis. |
| System → Experiment | ✅ | Pengambilan sampel data capture di lapangan menggunakan Modul Sniffer dengan konfigurasi yang terkunci (durasi 5 menit). |

**Koneksi mana yang paling lemah?** Metric → System (Variabilitas performa NIC laptop penguji yang berpotensi membiaskan sensitivitas penangkapan paket data).
**Bagaimana cara memperkuatnya?**
> Melakukan kalibrasi awal hardware NIC laptop penguji di area sepi (noise minimal) sebelum eksekusi eksperimen utama.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [x] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? —

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Seluruh 6 koneksi vertikal terhubung erat dari penentuan masalah hingga metodologi eksperimen. |
| Specificity | 3 | Semua metrik kuantitatif teknis, threshold kelayakan (MOS >= 3), lokasi, dan waktu terdefinisi numerik. |
| Feasibility | 3 | Rencana capture data modular 5 menit per sesi sangat realistis diselesaikan dalam waktu 1 bulan. |
| Rigor | 3 | Menggunakan studi rujukan SOTA terbitan 2024-2025 dengan standardisasi TIPHON yang tepercaya. |

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [x] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? —

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Mendefinisikan metrik dan variabel (karena parameter QoS TIPHON sudah memiliki rumus kalkulasi dan batas threshold kelayakan yang baku dari ETSI).
**Bagian tersulit:** Mengidentifikasi distorsi metodologi dan gap riset dari literatur secara presisi (memisahkan mana yang sekadar limitasi engineering dan mana yang merupakan celah riset ilmiah).
**Yang akan dilakukan berbeda:**
> Melakukan tinjauan pustaka secara concept-centric sejak awal menggunakan query Boolean yang lebih sempit agar pencarian paper baseline lebih efisien dan terfokus.
> Mengunci environment kerja dan durasi capture (5 menit) lebih awal untuk mempercepat repeatability test.
