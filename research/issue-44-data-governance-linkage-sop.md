# Issue #44 — Data Governance dan Longitudinal Linkage SOP

## 1. Prinsip

Gunakan data minimum yang diperlukan. Pisahkan **identitas** dari **data penelitian**.

## 2. Tiga file utama

### File A — linkage key

Berisi hanya informasi yang diperlukan untuk mencocokkan siswa T1–T3, misalnya:

- participant ID;
- identifier sekolah yang dibutuhkan untuk pencocokan;
- nama/identifier siswa hanya bila benar-benar diperlukan secara operasional dan diizinkan etik.

File ini paling sensitif dan aksesnya paling terbatas.

### File B — research data

Berisi:

- participant ID;
- school/class IDs;
- responses;
- demografi yang disetujui;
- wave;
- waktu/quality fields.

Tidak berisi nama, nomor telepon, email, atau identifier langsung lain.

### File C — contact/recruitment log

Berisi status consent/assent, attendance atau scheduling yang diperlukan. Jangan mencampurkan jawaban kuesioner ke file ini.

## 3. Participant ID

Gunakan ID random/structured yang tidak mengandung tanggal lahir, NISN, nama, nomor kelas yang mudah ditebak, atau informasi personal lain.

Contoh format aman: `G-7F3K9Q` atau random UUID pendek yang dikelola sistem.

Jangan membuat ID seperti `SMP001-20091213-Ayu`.

## 4. Akses

- linkage key: hanya peneliti inti/data manager yang benar-benar membutuhkan;
- research data: hanya tim analisis yang disetujui;
- sekolah/guru: tidak mendapat data individual;
- file hasil untuk publik/presentasi: agregat/de-identified.

## 5. Penyimpanan

Gunakan storage institusional atau penyimpanan terenkripsi/restricted-access yang disetujui institusi.

Aturan minimum:

- jangan menyimpan linkage key bersama research data pada folder terbuka yang sama;
- jangan kirim raw data melalui grup chat;
- jangan memakai flash drive tanpa proteksi sebagai satu-satunya salinan;
- batasi sharing link;
- audit siapa yang memiliki akses.

## 6. Linkage antarwave

### Sebelum T1

- buat participant ID;
- simpan mapping pada linkage file;
- data survey hanya menggunakan participant ID.

### T2/T3

- sekolah/contact person membantu menemukan siswa melalui prosedur administratif yang disetujui, bukan dengan melihat respons;
- gunakan participant ID yang sama;
- siswa yang tidak lagi tersedia dicatat sebagai attrition, bukan digantikan dalam panel utama.

### Setelah linkage tidak dibutuhkan

Hapus/arsipkan linkage key sesuai retention period yang disetujui komite etik. Setelah key dihancurkan, data penelitian menjadi lebih sulit/ tidak mungkin dikaitkan kembali ke individu.

## 7. Download dan analisis

Buat versi analisis tanpa identifier langsung. Jika data berasal dari survey platform:

1. export ke lokasi aman;
2. cek variabel metadata otomatis yang mungkin mengandung email/IP/location;
3. hapus metadata yang tidak diperlukan;
4. simpan clean raw export sebagai read-only/archive;
5. lakukan cleaning di working copy/scripted pipeline.

## 8. Raw data

Raw data setelah fielding tidak diedit manual. Koreksi/cleaning dilakukan melalui script atau documented derived dataset.

Jika ada kesalahan linkage, perbaikannya harus dicatat.

## 9. Retention

Durasi retention final mengikuti kebijakan institusi/komite etik. Jangan mengarang jumlah tahun sebelum aturan institusi diketahui.

Yang harus dikunci dalam submission:

- berapa lama linkage key disimpan;
- berapa lama de-identified research data disimpan;
- siapa yang berwenang menghapus;
- apakah data dapat dibagikan untuk secondary research dan dalam bentuk apa.

## 10. Data sharing

Default konservatif:

- codebook/analysis code dapat dibagikan bila aman;
- individual-level adolescent data tidak otomatis dibuat open data;
- sharing dataset harus mengikuti consent, ethics approval, dan data agreement;
- jika dibagikan, gunakan de-identification dan kontrol akses sesuai risiko.

## 11. Incident response

Jika file sensitif salah kirim/terbuka:

- cabut akses secepat mungkin;
- simpan log kejadian;
- tentukan data apa yang terekspos;
- lapor melalui prosedur institusi;
- lakukan remediation;
- jangan menyembunyikan kejadian dalam research log.

## 12. Checklist pre-fielding

- [ ] storage location disetujui;
- [ ] role/access list dibuat;
- [ ] participant ID generator siap;
- [ ] linkage file terpisah;
- [ ] consent status tidak bercampur dengan response data;
- [ ] export/cleaning SOP diuji pada dummy data;
- [ ] retention schedule diisi sesuai aturan institusi;
- [ ] breach reporting contact diketahui.
