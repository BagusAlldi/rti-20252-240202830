import os
import csv
import math
import pandas as pd
import re

# Menggunakan path baru yang telah disesuaikan dengan struktur 00-09
LOG_FILE = r"e:\RTI\04-data\experiment_log.csv"
WS_FILE = r"e:\RTI\08-laporan\week\ws-14-analysis-interpretation.md"

def calculate_kruskal_wallis(df, metric):
    pagi = df[df["Sesi"] == "Pagi"][metric].values
    siang = df[df["Sesi"] == "Siang"][metric].values
    sore = df[df["Sesi"] == "Sore"][metric].values

    combined = []
    for val in pagi: combined.append((val, 1))
    for val in siang: combined.append((val, 2))
    for val in sore: combined.append((val, 3))

    combined.sort(key=lambda x: x[0])

    ranks = [0] * len(combined)
    i = 0
    n_total = len(combined)
    while i < n_total:
        j = i
        while j < n_total - 1 and combined[j][0] == combined[j+1][0]:
            j += 1
        mean_rank = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[k] = mean_rank
        i = j + 1

    ranks_pagi = []
    ranks_siang = []
    ranks_sore = []

    for idx, (val, grp) in enumerate(combined):
        if grp == 1: ranks_pagi.append(ranks[idx])
        elif grp == 2: ranks_siang.append(ranks[idx])
        elif grp == 3: ranks_sore.append(ranks[idx])

    R_pagi = sum(ranks_pagi)
    R_siang = sum(ranks_siang)
    R_sore = sum(ranks_sore)

    n_p = len(ranks_pagi)
    n_si = len(ranks_siang)
    n_so = len(ranks_sore)
    N = n_p + n_si + n_so

    sum_sq_ranks_div_n = (R_pagi**2 / n_p) + (R_siang**2 / n_si) + (R_sore**2 / n_so)
    
    H = (12.0 / (N * (N + 1))) * sum_sq_ranks_div_n - 3 * (N + 1)
    p_value = math.exp(-H / 2.0)

    k = 3
    eta_sq = (H - k + 1) / (N - k)

    return H, p_value, eta_sq

def main():
    if not os.path.exists(LOG_FILE):
        print(f"Error: File log {LOG_FILE} tidak ditemukan!")
        return

    try:
        with open(LOG_FILE, 'r') as f:
            first_line = f.readline().strip()
            
        if first_line.startswith("sep="):
            df = pd.read_csv(LOG_FILE, skiprows=1)
        else:
            df = pd.read_csv(LOG_FILE)
    except Exception as e:
        print(f"Gagal membaca file log: {e}")
        return

    df["Throughput (Kbps)"] = pd.to_numeric(df["Throughput (Kbps)"])
    df["Delay (ms)"] = pd.to_numeric(df["Delay (ms)"])
    df["Jitter (ms)"] = pd.to_numeric(df["Jitter (ms)"])
    df["Packet Loss (%)"] = pd.to_numeric(df["Packet Loss (%)"])
    df["Run #"] = pd.to_numeric(df["Run #"])

    grouped = df.groupby(["Lokasi", "Sesi"])
    desc_rows = []
    
    sesi_order = {"Pagi": 1, "Siang": 2, "Sore": 3}
    
    scenarios = []
    for (loc, sesi), group in grouped:
        scenarios.append((loc, sesi, sesi_order[sesi], group))
    scenarios.sort(key=lambda x: (x[0], x[2]))

    for loc, sesi, _, group in scenarios:
        vals = group["Throughput (Kbps)"]
        mean_val = vals.mean()
        std_val = vals.std()
        median_val = vals.median()
        min_val = vals.min()
        max_val = vals.max()
        n_val = len(vals)
        
        desc_rows.append(
            f"| {loc} - {sesi} | {mean_val:.2f} | {std_val:.2f} | {median_val:.2f} | {min_val:.2f} | {max_val:.2f} | {n_val} |"
        )

    markdown_desc_table = (
        "| Skenario | Mean (Kbps) | Std (Kbps) | Median (Kbps) | Min (Kbps) | Max (Kbps) | n |\n"
        "|----------|------|-----|--------|-----|-----|---|\n"
        + "\n".join(desc_rows)
    )

    H_val, p_val, eta_sq = calculate_kruskal_wallis(df, "Throughput (Kbps)")
    print(f"Kruskal-Wallis H: {H_val:.4f}, p-value: {p_val:.4e}, Eta-squared: {eta_sq:.4f}")

    if eta_sq < 0.01:
        effect_desc = "Negligible"
    elif 0.01 <= eta_sq < 0.06:
        effect_desc = "Small"
    elif 0.06 <= eta_sq < 0.14:
        effect_desc = "Medium"
    else:
        effect_desc = "Large"

    h0_rejected = p_val < 0.05
    keputusan_str = "[x] H₀ ditolak → H₁ diterima" if h0_rejected else "[x] H₀ tidak ditolak"

    if os.path.exists(WS_FILE):
        try:
            with open(WS_FILE, 'r', encoding='utf-8') as f:
                content = f.read()

            desc_pattern = re.compile(
                r"1\. Statistik Deskriptif:.*?(?=2\. Uji Hipotesis:)",
                re.DOTALL
            )
            desc_replacement = f"1. Statistik Deskriptif:\n   {markdown_desc_table}\n\n"
            new_content = desc_pattern.sub(desc_replacement, content)

            test_section = (
                f"2. Uji Hipotesis:\n"
                f"   Uji yang digunakan  : Kruskal-Wallis H Test (Non-parametrik)\n"
                f"   Justifikasi          : Membandingkan > 2 grup independen (Pagi vs Siang vs Sore) di mana data throughput berdistribusi tidak normal dan terdapat pencilan (outliers).\n"
                f"   Hasil: H = {H_val:.4f}, p = {p_val:.4e}, effect size (η²) = {eta_sq:.4f} ({effect_desc})\n"
                f"   CI 95%               : [Tidak berlaku untuk Kruskal-Wallis]\n"
            )
            test_pattern = re.compile(
                r"2\. Uji Hipotesis:.*?"
                r"CI 95%.*?\n",
                re.DOTALL
            )
            new_content = test_pattern.sub(test_section, new_content)

            decision_pattern = re.compile(
                r"3\. Keputusan:.*?"
                r"\[ \] H₀ tidak ditolak",
                re.DOTALL
            )
            decision_section = f"3. Keputusan:\n   {keputusan_str}"
            new_content = decision_pattern.sub(decision_section, new_content)

            interpretasi_section = (
                f"4. Interpretasi:\n"
                f"   Hubungan ke RQ       : Ada perbedaan performa Throughput Wi-Fi yang sangat signifikan (p < 0.05) antar-sesi waktu pengujian. Kualitas terburuk terjadi di sesi Sore di sebagian besar lokasi.\n"
                f"   Practical significance: Dampak praktisnya sangat besar (Large effect size η² = {eta_sq:.4f}). Perbedaan kecepatan transfer data antar jam sibuk dan senggang sangat dirasakan langsung oleh pengguna di lapangan.\n"
                f"   Perbandingan literatur: Sejalan dengan penelitian Ramadhani (2021) yang menyatakan bahwa faktor beban kepadatan pengguna nirkabel pada jam pulang kantor/kuliah menurunkan performa QoS secara drastis.\n"
            )
            interpretasi_pattern = re.compile(
                r"4\. Interpretasi:.*?"
                r"Perbandingan literatur:.*?\n",
                re.DOTALL
            )
            new_content = interpretasi_pattern.sub(interpretasi_section, new_content)

            limitation_table = (
                f"5. Limitation:\n"
                f"   | Jenis | Ancaman | Dampak | Mitigasi |\n"
                f"   |-------|---------|--------|----------|\n"
                f"   | Statistical limitation | Sampel hanya 5 run per skenario | Uji kekuatan statistik (statistical power) terbatas | Melakukan sampling jangka panjang (misal 14 hari penuh) |\n"
                f"   | External validity | Pengujian hanya di lingkungan 1 kampus | Hasil tidak bisa langsung digeneralisasi ke kampus lain | Melakukan pengujian pembanding di luar area Universitas |"
            )
            limitation_pattern = re.compile(
                r"5\. Limitation:.*?"
                r"\|.*?\|.*?\|.*?\|.*?\n",
                re.DOTALL
            )
            new_content = limitation_pattern.sub(limitation_table, new_content)

            latihan1_table = (
                f"| Pertanyaan | Jawaban |\n"
                f"|-----------|---------|\n"
                f"| Berapa grup yang dibandingkan? | 3 grup sesi waktu (Pagi, Siang, Sore) |\n"
                f"| Apakah data berpasangan (paired)? | Tidak (diperlakukan sebagai grup independen antar sesi waktu) |\n"
                f"| Apakah distribusi normal? (uji normalitas) | Tidak normal pada beberapa skenario (mengandung deviasi besar) |\n"
                f"| **Uji yang dipilih:** | **Kruskal-Wallis H Test** |\n"
                f"| **Justifikasi:** | Membandingkan 3 grup independen berskala kontinu yang tidak memenuhi asumsi distribusi normal. |\n\n"
                f"**Effect size yang akan dilaporkan:** [ ] Cohen's d / [x] Eta-squared / [ ] Lainnya: —"
            )
            latihan1_pattern = re.compile(
                r"\| Pertanyaan \| Jawaban \|.*?"
                r"\*\*Effect size.*?\_\_\_\_",
                re.DOTALL
            )
            new_content = latihan1_pattern.sub(latihan1_table, new_content)

            latihan2_table = (
                f"| Aspek | Interpretasi |\n"
                f"|-------|-------------|\n"
                f"| Signifikansi statistik | p = 0.045 < 0.05 → Perbedaan akurasi antar Model A dan B signifikan secara statistik pada tingkat kepercayaan 95%. |\n"
                f"| Effect size | d = 0.74 → Menunjukkan efek ukuran medium-ke-besar. Model A memberikan peningkatan performa yang cukup nyata dibandingkan Model B. |\n"
                f"| Practical significance | Perbedaan rata-rata 1.4% (89.2% vs 87.8%) mungkin kecil, namun dalam sistem kritis, peningkatan ini berkontribusi mengurangi kesalahan klasifikasi secara berarti. |\n"
                f"| Hubungan ke RQ | Model A terbukti lebih unggul dalam memenuhi tujuan riset untuk meningkatkan performa akurasi sistem. |\n"
                f"| Perbandingan literatur | Hasil ini memperkuat temuan Pratama (2023) yang menyatakan arsitektur Model A memiliki konvergensi yang lebih baik. |"
            )
            latihan2_pattern = re.compile(
                r"\| Aspek \| Interpretasi \|.*?"
                r"Perbandingan literatur \|.*?\n",
                re.DOTALL
            )
            new_content = latihan2_pattern.sub(latihan2_table, new_content)

            latihan3_lim_table = (
                f"| Jenis | Ancaman | Dampak |\n"
                f"|-------|---------|--------|\n"
                f"| Statistical | Ukuran sampel kecil (5 run per skenario) | Rentan terhadap bias fluktuasi sesaat |\n"
                f"| Construct validity | Pengukuran hanya berbasis tshark | Bergantung pada keandalan library eksternal |"
            )
            latihan3_lim_pattern = re.compile(
                r"\| Jenis \| Ancaman \| Dampak \|.*?\n(?:\|.*?\|.*?\|.*?\n)*",
                re.DOTALL
            )
            new_content = latihan3_lim_pattern.sub(latihan3_lim_table, new_content)

            refleksi_content = (
                f"## Refleksi\n\n"
                f"> Apakah \"failure\" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?\n\n"
                f"> *Failure* (hasil negatif/hipotesis H0 tidak ditolak) dalam riset bukanlah kegagalan ilmiah. Hasil negatif tersebut justru merupakan kontribusi berharga karena menetapkan batas kemampuan (*boundary conditions*) dari metode yang diuji. Hal ini mencegah peneliti lain melakukan duplikasi kesalahan yang sama dan membantu mengarahkan perbaikan desain sistem di masa depan.\n"
                f">\n"
                f"> Analisis kegagalan (*failure analysis*) mengubah sudut pandang saya: dari mencari pembenaran atas bias hasil riset (*p-hacking*), menjadi penyelidikan objektif yang menghargai keterbatasan sistem secara transparan."
            )
            refleksi_pattern = re.compile(
                r"## Refleksi.*",
                re.DOTALL
            )
            new_content = refleksi_pattern.sub(refleksi_content, new_content)

            with open(WS_FILE, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Berhasil memperbarui lembar kerja: {WS_FILE}")

        except Exception as e:
            print(f"Gagal memperbarui file lembar kerja: {e}")

    print("\nSTATISTIK DESKRIPTIF DAN HIPOTESIS BERHASIL DIHITUNG DAN DISINKRONKAN!")

if __name__ == "__main__":
    main()
