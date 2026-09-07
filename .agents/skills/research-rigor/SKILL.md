---
name: research-rigor
description: Guardrail lintas-skill untuk mengurangi kegagalan agent dalam riset: asumsi tersembunyi, kompleksitas berlebih, perubahan di luar scope, klaim tanpa verifikasi, dan konfirmasi sepihak.
license: MIT
---

# Research Rigor

Meta-skill ini mengatur cara agent bekerja pada seluruh tahap riset. Ia mengadaptasi empat prinsip eksekusi dari [Karpathy Guidelines](https://github.com/multica-ai/andrej-karpathy-skills) ke konteks penelitian: berpikir sebelum mengklaim, memilih kompleksitas minimum yang cukup, membuat perubahan secara surgical, dan bekerja menuju kriteria keberhasilan yang dapat diverifikasi.

Gunakan prinsip ini bersama skill akademik yang relevan. Untuk tugas rutin yang jelas, terapkan secara proporsional; untuk keputusan substantif, ambigu, sulit dibalik, atau berdampak pada inferensi, terapkan secara penuh.

## 1. Think Before Claiming

Jangan menyelesaikan ketidakpastian epistemik secara diam-diam.

Sebelum klaim atau keputusan substantif, bedakan:

- **KNOWN** — informasi yang benar-benar diberikan atau diamati.
- **SUPPORTED** — klaim yang didukung bukti yang telah diperiksa.
- **INFERRED** — kesimpulan yang ditarik dari bukti, dengan logika dan batasnya.
- **ASSUMED** — asumsi kerja yang belum diverifikasi.
- **UNKNOWN** — informasi yang belum diketahui atau belum dapat diakses.
- **DECISION NEEDED** — pilihan yang memerlukan keputusan peneliti atau bukti tambahan.

Jika beberapa interpretasi masuk akal dan pilihan tersebut memengaruhi hasil, tampilkan alternatifnya. Jangan mengubah ketiadaan hasil pencarian menjadi research gap, korelasi menjadi sebab-akibat, keberadaan sitasi menjadi dukungan klaim, atau model yang tampak masuk akal menjadi teori yang telah teruji.

## 2. Parsimony First

Gunakan kompleksitas konseptual dan metodologis minimum yang cukup untuk menjawab pertanyaan penelitian.

Jangan menambah teori, konstruk, variabel, mediator, moderator, metode, robustness check, atau lapisan abstraksi hanya agar studi terlihat lebih canggih. Setiap elemen harus mempunyai fungsi yang dapat dijelaskan.

Untuk elemen baru, tanyakan:

1. Apakah elemen ini diperlukan untuk menjawab pertanyaan penelitian?
2. Apakah ia menambah daya jelas, validitas, atau kemampuan membedakan penjelasan alternatif?
3. Apakah bukti dan sumber daya yang tersedia cukup untuk mendukungnya?
4. Apakah desain yang lebih sederhana dapat menghasilkan inferensi yang sama atau lebih defensible?

Kompleksitas diperbolehkan ketika diperlukan oleh pertanyaan dan bukti, bukan sebagai indikator mutu doktoral.

## 3. Surgical Research Changes

Sentuh hanya bagian yang diperlukan untuk memenuhi tujuan tugas. Jangan melakukan perbaikan samping yang tidak diminta.

Setiap perubahan substantif harus dapat ditelusuri ke setidaknya satu dari berikut:

- tujuan atau acceptance criterion pada issue;
- bukti baru yang diverifikasi;
- keputusan penelitian yang dicatat;
- temuan review/audit;
- inkonsistensi yang secara langsung menghalangi tugas.

Jangan mengubah pertanyaan, teori, metode, definisi konstruk, sampel, atau klaim lain hanya karena agent melihat peluang untuk "memperbaiki" bagian berdekatan. Jika perubahan yang diminta menciptakan artefak yatim atau inkonsistensi langsung, perbaiki hanya konsekuensi yang dibuat oleh perubahan tersebut.

Uji sederhana: setiap perubahan penting harus mempunyai alasan yang dapat ditunjukkan pada diff, issue, decision log, atau bukti.

## 4. Goal-Driven Research

Ubah instruksi luas menjadi tujuan yang dapat diperiksa sebelum mengerjakan perubahan.

Untuk tugas nontrivial, tetapkan secara ringkas:

1. **Objective** — keadaan akhir yang ingin dicapai.
2. **Scope** — bagian yang boleh dan tidak boleh diubah.
3. **Evidence required** — bukti minimum yang diperlukan.
4. **Success criteria** — kondisi yang dapat diperiksa.
5. **Verification** — cara memastikan kondisi tersebut benar-benar terpenuhi.

Contoh:

```
Objective:
Menentukan apakah kandidat kontribusi teoretis dapat dipertahankan.

Success criteria:
[ ] Konstruk utama didefinisikan dari sumber terverifikasi.
[ ] Studi terdekat telah dibandingkan.
[ ] Bukti yang bertentangan dicatat.
[ ] Penjelasan alternatif diperiksa.
[ ] Keputusan retain / narrow / defer / reject dicatat.
```

Jika kriteria tidak dapat dipenuhi karena data, sumber, izin, atau keputusan peneliti belum tersedia, nyatakan **BLOCKED** atau **BELUM DIVERIFIKASI**. Jangan mengisi kekosongan dengan asumsi.

## 5. Falsification Before Affirmation

Untuk klaim penting, jangan hanya mencari dukungan.

Urutan default:

1. rumuskan kandidat klaim secara terbatas;
2. cari bukti yang mendukung;
3. cari secara sengaja bukti tandingan;
4. periksa penjelasan alternatif;
5. identifikasi boundary conditions dan batas inferensi;
6. baru tentukan kekuatan klaim.

Ketiadaan falsifikasi bukan bukti bahwa klaim benar. Bila bukti tandingan belum dicari atau akses literatur terbatas, turunkan tingkat kepastian.

## 6. Verification Loop

Agent boleh mengulang pekerjaan sampai kriteria keberhasilan terpenuhi, tetapi tidak boleh memperluas scope diam-diam.

Loop:

```
inspect
  ↓
identify failure
  ↓
make minimum justified change
  ↓
verify
  ↓
pass / blocked
  ↓
checkpoint
```

Verification lokal berbeda dari quality gate. Sebuah PR dapat memenuhi acceptance criteria tetapi tahap akademik tetap `PERLU REVISI` atau `BELUM DINILAI`.

## 7. Kontrak dengan workflow Git

Pada mode RESEARCH, issue adalah bounded context untuk satu unit pekerjaan. Issue sebaiknya menyimpan objective, known/unknown, scope, evidence required, success criteria, keputusan, blocker, dan checkpoint.

Hubungan kerja:

```
Issue objective
    ↓
Assumptions / unknowns
    ↓
Evidence required
    ↓
Minimum justified change
    ↓
Verification
    ↓
Checkpoint
    ↓
PR
    ↓
Quality gate tetap dinilai terpisah
```

Jangan menggunakan percakapan sebagai satu-satunya memori kerja. Jangan mengklaim bahwa merge PR membuktikan mutu ilmiah, validitas inferensi, atau persetujuan institusi.

## Atribusi

Prinsip eksekusi awal diadaptasi dari `multica-ai/andrej-karpathy-skills`, khususnya gagasan Think Before Coding, Simplicity First, Surgical Changes, dan Goal-Driven Execution. Implementasi di sini ditulis ulang untuk workflow penelitian dan menambahkan disiplin epistemik, falsifikasi, evidence traceability, serta pemisahan acceptance criteria dari academic quality gates.
