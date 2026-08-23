# Issue #42 — Rencana Menentukan Jumlah Sampel dan Cluster

## 1. Tujuan

Issue ini akan menentukan berapa siswa, kelas, dan sekolah yang perlu direkrut untuk studi tiga gelombang.

Prinsipnya sederhana: **jumlah sampel mengikuti model dan data pilot, bukan angka baku seperti 200 atau 300.**

## 2. Status

Rencana simulasi sudah dapat disiapkan sekarang. **Final N belum boleh dikunci** karena parameter utama masih menunggu hasil #40–#41.

Status Issue #42: **POWER PLAN READY — FINAL N PENDING PILOT**.

## 3. Apa yang dibutuhkan dari pilot

Kita hanya memakai parameter yang memang penting:

- reliability/loading konstruk utama;
- korelasi SEC–BPNS;
- stabilitas engagement dari waktu ke waktu yang masuk akal berdasarkan literatur/pilot;
- perkiraan hubungan PTS/DPM dengan mediator dan engagement;
- ICC kelas/sekolah bila tersedia;
- perkiraan attrition per gelombang;
- jumlah siswa per kelas/sekolah yang realistis;
- apakah secondary interaction DPM × PTS tetap ingin diuji.

Jika pilot belum bisa mengestimasi satu parameter dengan baik, gunakan rentang konservatif dari literature dan tandai sebagai asumsi.

## 4. Tiga skenario saja

Tidak perlu puluhan skenario. Gunakan tiga skenario utama:

### Konservatif

- effect lebih kecil;
- reliability lebih rendah;
- attrition lebih tinggi;
- clustering lebih kuat.

### Realistis

- menggunakan nilai tengah dari pilot/literature yang paling masuk akal.

### Optimistis

- effect/reliability sedikit lebih baik;
- attrition lebih rendah.

Tambahkan satu stress test hanya jika perlu, misalnya school dropout atau cluster size sangat tidak seimbang.

## 5. Outcome utama untuk power

Prioritaskan analisis yang benar-benar menjadi kontribusi utama:

1. prospective PTS → engagement;
2. prospective SEC/BPNS → engagement setelah baseline engagement;
3. perbandingan indirect pathway melalui SEC vs BPNS;
4. selected DPM strategy pathways yang memang didukung teori.

Interaction DPM × PTS tidak boleh menentukan seluruh ukuran sampel bila interaction itu membuat studi menjadi tidak realistis. Jika power interaction buruk tetapi analisis utama cukup kuat, interaction diturunkan menjadi secondary/exploratory.

## 6. Apa yang dinilai dari simulasi

Jangan hanya melihat “power > .80”. Periksa juga:

- apakah model sering convergent;
- apakah estimasi bias berlebihan;
- apakah interval kepercayaan cukup masuk akal;
- apakah indirect effect dapat diestimasi dengan precision yang layak;
- apakah attrition membuat jumlah T3 terlalu kecil;
- apakah cluster count cukup untuk standard error yang stabil.

Untuk komunikasi proposal, hasil akhirnya cukup dijelaskan dengan bahasa biasa: “dengan asumsi X, Y, dan Z, target ini memberikan peluang yang memadai untuk mendeteksi hubungan utama dan tetap menyisakan peserta setelah attrition.”

## 7. Prosedur mencari N

1. Ambil parameter dari #40–#41.
2. Mulai dari ukuran sampel/cluster yang realistis secara lapangan.
3. Simulasikan tiga skenario.
4. Jika hasil utama belum cukup stabil, naikkan N/cluster.
5. Ulangi sampai primary analyses mempunyai precision/power yang memadai.
6. Tambahkan allowance attrition untuk menentukan target recruitment T1.
7. Cocokkan dengan kemampuan #43 memperoleh sekolah/kelas.
8. Jika angka tidak feasible, sederhanakan secondary analysis sebelum menurunkan kualitas core design.

## 8. Output yang harus dihasilkan nanti

| Output | Arti sederhana |
|---|---|
| Minimum analyzable N | jumlah siswa yang dibutuhkan pada analysis wave akhir |
| Target T1 recruitment | jumlah siswa yang harus direkrut di awal setelah memperhitungkan attrition |
| School/class target | berapa cluster yang perlu direkrut |
| Expected cluster size | rata-rata siswa per kelas/sekolah |
| Interaction decision | confirmatory / exploratory / drop |
| Assumption table | parameter apa yang diasumsikan dan sumbernya |

## 9. Aturan keputusan

### Primary model

Target internal: hasil simulasi menunjukkan estimasi primary path/indirect effects cukup stabil dan power/coverage memadai pada skenario realistis, serta tidak runtuh total pada skenario konservatif.

### Secondary interaction

Pertahankan confirmatory hanya bila power dan precision cukup tanpa membuat recruitment tidak realistis.

### RI-CLPM/sensitivity

Tidak digunakan untuk menentukan minimum N utama. Jika model tersebut membutuhkan sampel jauh lebih besar atau tidak stabil, tetap sebagai sensitivity analysis dan boleh tidak dijalankan bila data tidak mendukung.

## 10. Menghindari over-engineering

Tidak perlu:

- membandingkan puluhan estimator pada tahap power;
- mensimulasikan setiap kemungkinan loading per item secara unik tanpa alasan;
- membuat sample-size justification berdasarkan software tertentu;
- mengklaim satu N “ideal” universal.

Yang dibutuhkan adalah **angka recruitment yang masuk akal dan dapat dijelaskan**.

## 11. Skeleton parameter untuk simulasi

Parameter final akan menggantikan placeholder berikut setelah pilot:

```text
waves = 3
N_T1 = candidate
schools = candidate
students_per_school = from sampling plan
attrition_T2 = from pilot/literature
attrition_T3 = from pilot/literature
reliability_SEC = from pilot
reliability_BPNS = from pilot
reliability_engagement = from pilot
stability_SEC = literature/pilot
stability_BPNS = literature/pilot
stability_engagement = literature/pilot
PTS_to_BPNS = literature/pilot range
SEC_to_engagement = literature/pilot range
BPNS_to_engagement = literature/pilot range
DPM_paths = strategy-specific range
ICC = pilot/literature
replications = sufficient for stable Monte Carlo estimates
```

Tidak ada angka placeholder yang boleh masuk manuscript sebagai final sebelum simulasi dijalankan.

## 12. Definition of Done

Issue #42 baru ditutup bila:

- final battery #41 tersedia;
- parameter pilot/literature masuk ke simulasi;
- Monte Carlo benar-benar dijalankan;
- target T1 N dan cluster ditentukan;
- attrition allowance eksplisit;
- secondary analyses yang underpowered sudah diturunkan statusnya.

Sampai itu terjadi, issue tetap **OPEN**.
