# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Evaluasi Kinerja Kualitas Layanan Jaringan Nirkabel (Wi-Fi) Universitas Secara Spasial Dan Temporal Berbasis QoS (TIPHON)
Target  : [x] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [x] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [x] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [x] Related Work — concept-centric, gap positioning
  [x] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [x] Results — tabel + grafik + observasi (tanpa interpretasi)
  [x] Discussion — interpretasi, perbandingan, implikasi, limitation
  [x] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [x] RQ di Introduction = RQ di Method = RQ di Conclusion
  [x] Variabel di Method = variabel di Results
  [x] Klaim di Discussion didukung data di Results
  [x] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [x] Clarity — mudah dipahami tanpa re-read
  [x] Precision — tidak ada istilah ambigu
  [x] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Kualitas jaringan Wi-Fi Universitas sering mengalami fluktuasi akibat beban pengguna pada sesi waktu tertentu. Penelitian ini mengevaluasi kinerja QoS (Throughput, Delay, Jitter, dan Packet Loss) di 4 lokasi strategis selama 3 sesi waktu (Pagi, Siang, Sore) dengan total 60 run. Hasil menunjukkan terjadinya degradasi throughput hingga >50% dan lonjakan delay pada sesi Sore, dengan tingkat packet loss tertinggi mencapai 13.70% di area Lorong Lab Komputer. | 200-250 |
| Introduction | Konteks: Kebutuhan konektivitas nirkabel yang stabil di area kampus untuk menunjang kegiatan akademis. Gap: Kurangnya analisis temporal (variasi jam sibuk) yang dikaitkan dengan lokasi geografis internal kampus. RQ: Bagaimana perbedaan performa QoS Wi-Fi Universitas secara spasial dan temporal (Pagi vs Siang vs Sore)? | 500-700 |
| Related Work | Mengkaji literatur standardisasi parameter QoS (TIPHON) dan penelitian terdahulu tentang faktor interferensi struktural bangunan beton serta pola perilaku trafik nirkabel di jam sibuk kampus. | 700-1000 |
| Method | Eksperimen capture paket data nirkabel menggunakan tshark/Wireshark pada 4 titik ukur, durasi konstan 300 detik per run, n=5 per skenario. Analisis non-parametrik Kruskal-Wallis untuk menguji signifikansi perbedaan temporal. | 800-1200 |
| Results | Tabel statistik deskriptif QoS, grouped bar chart Throughput dengan error bars, serta sebaran sebaran box plot untuk Delay dan Packet Loss pada 12 skenario. | 500-800 |
| Discussion | Interpretasi pengaruh jam sibuk (Sore) terhadap lonjakan delay dan penurunan throughput, analisis tabrakan paket (collision) di Lorong Lab Komputer yang memicu packet loss tinggi, serta batasan statistika (n=5). | 600-900 |
| Conclusion | Wi-Fi Universitas memiliki perbedaan performa temporal yang signifikan (H=11.45, p=0.003, η²=0.1658). Rekomendasi mencakup alokasi AP dinamis di jam sibuk sore hari dan peningkatan densitas AP di area Lab Komputer. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|---|-------|--------|--------|-----------|-----------|
| RQ1 (Temporal) | ✓ | ✓ | ✓ | ✓ | ✓ |
| RQ2 (Spasial) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik utama (QoS) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel IV (Lokasi & Sesi) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel DV (Throughput, dst) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Klaim/kontribusi | ✓ | ✓ | ✓ | ✓ | ✓ |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Tidak ditemukan inkonsistensi. Seluruh metrik QoS yang didefinisikan pada Method dibahas secara lengkap pada Result dan dikorelasikan langsung dengan hipotesis pada bagian Discussion.

**Tindakan perbaikan:**
> Mempertahankan alur logika konsistensi dari pendefinisian variabel di Bab Pendahuluan/Metode hingga kesimpulan.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Kualitas jaringan wifi di kampus sangat jelek di sore hari. Hal ini dibuktikan dari throughput yang turun dan delay yang sangat tinggi sekali saat diuji pakai tshark.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Kurang jelas — kata "jelek" bersifat subjektif dan "throughput turun" tidak menyebutkan angka pembanding. | Ubah istilah subjektif menjadi data numerik pembanding. |
| Precision | Kurang presisi — kata "sangat tinggi sekali" bersifat hiperbola tanpa metrik angka delay. | Ganti dengan nilai rata-rata delay dan signifikansi statistiknya. |
| Conciseness | Kurang ringkas — kalimat menggunakan kata-kata filler seperti "sekali" dan "pakai". | Hapus kata filler dan susun kalimat secara akademis aktif. |

**Paragraf setelah perbaikan:**
> Evaluasi kualitas jaringan Wi-Fi Universitas menunjukkan degradasi performa yang signifikan pada sesi sore hari. Hasil analisis paket data menggunakan tshark mencatat penurunan rata-rata throughput hingga di bawah 1100 Kbps dan peningkatan delay rata-rata hingga melebihi 250 ms secara signifikan (p = 0.003, η² = 0.1658).

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis **tentang** riset hanya melaporkan aktivitas kronologis eksperimen secara pasif, sedangkan menulis sebagai **argumen** riset adalah membangun rantai penalaran logis untuk membuktikan kontribusi ilmiah berdasarkan data objektif.
> 
> Menulis dengan urutan **Method → Results → Discussion → Introduction** meningkatkan kualitas tulisan karena memastikan bahwa klaim kontribusi yang ditulis pada pendahuluan didukung secara kokoh dan jujur oleh data hasil analisis aktual di bagian belakang, mencegah terjadinya *over-claiming*.
