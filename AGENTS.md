# Instruksi Kerja Disertasi

Gunakan repository ini sebagai academic version-controlled workspace untuk disertasi Dodo Rohimat.

## Alur Wajib

1. Buat atau gunakan GitHub Issue untuk setiap revisi substantif.
2. Jangan bekerja langsung di `main` untuk perubahan naskah atau riset.
3. Buat branch dari Issue, misalnya `issue-1-rewrite-bab-1`.
4. Commit perubahan dengan pesan yang menjelaskan ruang lingkup akademik.
5. Buka Pull Request untuk review.
6. Jangan merge Pull Request tanpa instruksi eksplisit dari user.

## Struktur Workspace

- `manuscript/`: sumber naskah kanonik.
- `literature/references.bib`: database referensi akademik.
- `literature/matrix-literature-review.md`: matriks sintesis literatur.
- `literature/notes/`: catatan sumber per artikel/buku/laporan.
- `research/`: memo riset, audit evidence, construct boundary, dan problem statement.
- `reviews/revision-log.md`: catatan perubahan, review, dan keputusan.

## Standar Akademik

- Jangan mengarang referensi, DOI, data, statistik, kutipan, atau evidence.
- Bedakan theory, empirical evidence, interpretation, inference, speculation, dan normative claim.
- Jangan menyimpulkan causality dari association tanpa desain dan identifikasi yang memadai.
- Research gap harus berbasis puzzle substantif, bukan sekadar “few studies” atau “different context”.
- Novelty dan contribution harus proporsional terhadap evidence.
- Gunakan TODO eksplisit ketika evidence belum tersedia atau belum diverifikasi.

## Aturan File

- Jangan mengubah file sumber eksternal tanpa kebutuhan eksplisit.
- Perubahan naskah dilakukan di Markdown agar diff dapat diaudit.
- Citation key di naskah harus cocok dengan `literature/references.bib`.
- Jika citation belum diverifikasi, tulis sebagai TODO, bukan sebagai referensi final.
