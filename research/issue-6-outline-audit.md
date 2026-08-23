# Issue #6 — Audit dan Lock Outline Canonical Manuscript Gemma

## Keputusan

Canonical working outline Bab 1 Gemma dikunci sebagai **project decision** berikut:

1.1 Latar Belakang  
1.2 Penelitian Terdahulu  
1.3 Masalah dan Pertanyaan Penelitian  
1.4 Kesenjangan Penelitian  
1.5 Tujuan Penelitian  
1.6 Ruang Lingkup Penelitian

Keputusan ini **bukan** klaim bahwa keenam subbagian tersebut diwajibkan secara universal oleh Universitas Indonesia atau PPIM. Struktur tersebut dipilih sebagai working baseline karena konsisten dengan requirement UI-wide dan precedent Ilmu Manajemen/PPIM yang dapat diverifikasi.

## Evidence hierarchy

### Level A — Official UI-wide requirement

Sumber resmi UI/FEB UI: Keputusan Rektor Universitas Indonesia Nomor 2143/SK/R/UI/2017, *Pedoman Teknis Penulisan Tugas Akhir Mahasiswa Universitas Indonesia*.

URL: https://feb.ui.ac.id/uploads/2022/06/SK-Pedoman-Penulisan-Karya-Akhir-2017-UPDATE.pdf

Temuan yang dapat dipastikan:

- Tugas akhir UI mencakup disertasi.
- Bagian isi disampaikan dalam sejumlah bab.
- Pembagian bab dari pendahuluan sampai kesimpulan **ditentukan oleh fakultas sesuai kebutuhan**.
- Bagian akhir memuat Daftar Referensi dan Lampiran jika ada.
- Tingkatan subbab maksimal tiga tingkat.

Implikasi: pedoman UI mengatur struktur makro dan format, tetapi tidak memberikan dasar untuk mengklaim satu set subjudul Bab 1 tertentu sebagai kewajiban universal UI.

### Level B — Official PPIM/FEB UI context

Sumber resmi:

- https://feb.ui.ac.id/doktor-ilmu-manajemen/
- https://ppim.feb.ui.ac.id/program-doktor/

Yang dapat dipastikan:

- PPIM FEB UI menyelenggarakan Program Doktor Ilmu Manajemen.
- Program menekankan kemampuan merumuskan permasalahan manajemen, menggunakan teori dan metode empiris secara komprehensif, serta menghasilkan kontribusi ilmiah.
- Halaman program publik yang diverifikasi tidak menetapkan struktur chapter-by-chapter untuk proposal/disertasi.

### Level C — Dissertation precedent

Precedent yang digunakan secara hati-hati: ringkasan disertasi Whony Rofianto, Program Pascasarjana Ilmu Manajemen UI (2014), tersedia melalui mirror publik.

URL mirror: https://adoc.pub/universitas-indonesia-disertasi.html

Daftar isi yang dapat diverifikasi memuat Bab 1:

- 1.1 Latar Belakang
- 1.2 Penelitian Terdahulu
- 1.3 Masalah dan Pertanyaan Penelitian
- 1.4 Kesenjangan Penelitian
- 1.5 Tujuan Penelitian
- 1.6 Ruang Lingkup Penelitian

Status epistemik: **precedent**, bukan regulasi. Mirror publik bukan sumber normatif institusi.

## Before/after mapping

| Current scaffold | Canonical working outline | Status keputusan |
|---|---|---|
| `# Bab 1. Latar Belakang` | `# BAB 1 — PENDAHULUAN` | Gemma project decision informed by precedent |
| `1.1 Konteks Penelitian` | `1.1 Latar Belakang` | Precedent + project decision |
| `1.2 Masalah Penelitian` | `1.2 Penelitian Terdahulu` | Precedent + project decision |
| `1.3 Rumusan Masalah` | `1.3 Masalah dan Pertanyaan Penelitian` | Precedent + project decision |
| `1.4 Tujuan Penelitian` | `1.4 Kesenjangan Penelitian` | Precedent + project decision |
| `1.5 Kontribusi Penelitian` | `1.5 Tujuan Penelitian` | Precedent + project decision |
| — | `1.6 Ruang Lingkup Penelitian` | Precedent + project decision |

Kontribusi penelitian tidak dihapus secara substantif; kontribusi harus muncul sebagai konsekuensi dari gap dan kemudian dapat dikembangkan pada bagian/bab yang relevan. Ia tidak dipertahankan sebagai subjudul Bab 1 hanya karena scaffold generik sebelumnya memuatnya.

## Lock rules

1. Jangan menyebut outline ini sebagai “wajib UI” atau “wajib PPIM”.
2. Jika ditemukan pedoman PPIM/FEB UI yang lebih spesifik dan lebih baru, buat issue verifikasi sebelum mengubah baseline.
3. Instruksi promotor yang terdokumentasi dapat mengganti project decision sepanjang tidak bertentangan dengan requirement institusional yang berlaku.
4. Perubahan struktur berikutnya tetap melalui Issue -> Branch -> PR -> Review -> Merge.
5. `manuscript/` tetap canonical source; file ini hanya audit trail.

## Open question untuk promotor

- Apakah proposal seminar diwajibkan memakai susunan Bab 1 yang identik dengan disertasi final?
- Apakah promotor menghendaki subbagian kontribusi/manfaat sebagai heading tersendiri di Bab 1?
- Apakah terdapat handbook PPIM internal yang tidak tersedia pada halaman publik?

## Status

**LOCKED AS WORKING BASELINE** setelah merge Issue #6; dapat direvisi hanya dengan evidence/instruksi promotor yang lebih kuat.
