# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [x] Semua skenario tercakup
  [x] Jumlah run sesuai rencana
  [x] Tidak ada file output hilang
  Missing: 0 dari 60 data points

Format Consistency:
  [x] Semua file format sama (CSV/JSON/...)
  [x] Header konsisten
  [x] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [x] Nilai dalam range masuk akal
  [x] Tidak ada waktu negatif
  [x] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: Tidak ada anomali fatal. Perekaman awal yang sempat menghasilkan file kosong (<1KB) langsung ditangani di lokasi dengan melakukan re-run secara instan untuk menjamin kualitas data.

Cross-Validation:
  [x] Run identik → hasil mendekati
  [x] Trend konsisten dengan ekspektasi teori

Keputusan:
  [x] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: —)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Ruby Tengah - Pagi/Siang/Sore | 15 | 15 | 0 | — (Target Rencana) |
| Kopma - Pagi/Siang/Sore | 15 | 15 | 0 | — (Target Rencana) |
| Lorong Lab Komputer - Pagi/Siang/Sore | 15 | 15 | 0 | — (Target Rencana) |
| Lorong Lab AI - Pagi/Siang/Sore | 15 | 15 | 0 | — (Target Rencana) |

**Total expected:** 60 | **Total actual:** 60 | **Missing:** 0

**Keputusan untuk data missing:**
> Tidak ada data missing. Jika terjadi kegagalan atau file PCAP kosong saat pengambilan data di lapangan, proses perekaman (run) akan segera diulangi kembali di tempat pada waktu sesi tersebut guna memastikan keutuhan dataset lengkap 60 run terkumpul.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Run | Accuracy (%) |
|-----|-------------|
| 1 | *91.2* |
| 2 | *90.8* |
| 3 | *91.5* |
| 4 | *78.3* |
| 5 | *91.0* |

**Deteksi outlier (Metode IQR Persentil):**
*Urutan data: 78.3, 90.8, 91.0, 91.2, 91.5*
- Q1 = 90.8 | Q3 = 91.2 | IQR = 0.4
- Batas bawah (Q1 - 1.5×IQR) = 90.2
- Batas atas (Q3 + 1.5×IQR) = 91.8
- Outlier terdeteksi: Run 4 (78.3%) karena nilainya berada di bawah batas minimum 90.2%

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| Run 4 | 78.3% | Terjadi gangguan transmisi sesaat (interferensi nirkabel) atau putusnya koneksi jaringan di tengah pengujian | Melakukan perekaman ulang (re-run) pada skenario bersangkutan untuk mendapatkan pembacaan yang stabil |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data direncanakan terkumpul (60/60 runs berhasil dicatat)
**2. Format:** [x] Konsisten / [ ] Ada inkonsistensi: — (seluruh log menggunakan struktur format CSV yang seragam)
**3. Range check (anomali):** Semua nilai metrik QoS berada pada batas positif yang logis. File PCAP kosong (<1KB) dideteksi secara langsung dan diganti lewat re-run.
**4. Logic check:** [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian: — (durasi perekaman konstan 300 detik per run)

**Kesimpulan:** [x] Data siap analisis / [ ] Perlu tindakan: —

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> **Data yang benar** adalah data mentah (raw data) apa adanya yang terekam oleh program capture nirkabel tanpa dimodifikasi. Sedangkan **data yang dipercaya** adalah data yang telah melewati proses pembersihan dari anomali sistem (seperti pembacaan 0 paket akibat salah memilih adapter) sehingga valid dan andal untuk analisis statistik.
> 
> Validasi formal sangat penting karena pengumpulan data secara otomatis tidak menjamin kebenaran hasilnya. Gangguan eksternal seperti crash pada driver Npcap, pergeseran nomor indeks interface jaringan, atau hilangnya koneksi secara tidak sengaja dapat menghasilkan data rusak yang dapat mengacaukan kesimpulan penelitian jika tidak divalidasi terlebih dahulu.
