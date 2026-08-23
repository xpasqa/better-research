# AGENT.md: Workflow GitHub-Only untuk Publion Dissertation Workspace

Dokumen ini mengatur cara agent bekerja di folder/repository disertasi Publion ketika workflow utama menggunakan GitHub version control, Markdown manuscript, Issues, Branches, Pull Requests, dan Review Comments.

Gunakan dokumen ini setelah user melakukan init pada folder disertasi atau saat agent diminta membantu membuat struktur awal repository.

## 0. Tujuan Workflow

Workflow ini dibuat agar penulisan disertasi dapat berjalan seperti project terkontrol:

- Naskah utama disimpan sebagai file Markdown di `manuscript/`.
- Setiap pekerjaan riset, revisi, atau penambahan data dimulai dari GitHub Issue.
- Setiap perubahan dikerjakan di branch terpisah.
- Setiap perubahan masuk ke `main` melalui Pull Request.
- Promotor/reviewer dapat memberi highlight/comment pada baris tertentu.
- Revisi promotor dapat ditindaklanjuti pada versi berikutnya.
- Semua perubahan punya riwayat: Issue, Branch, Commit, Pull Request, Review Comment, dan Merge.

Alur inti:

```text
Issue -> Branch -> Edit Markdown/Data/Literature -> Commit -> Pull Request -> Review -> Revise -> Merge -> History
```

Untuk revisi promotor:

```text
Masukan Promotor -> Issue/PR Comment -> Perbaikan di Branch -> Commit -> PR Review -> Merge -> Revision Log
```

## 1. Prinsip Utama

Agent harus memperlakukan repository ini sebagai workspace akademik, bukan sekadar code repository.

Selalu jaga:

- Kejelasan sumber.
- Jejak revisi.
- Keterhubungan antara issue, branch, commit, PR, dan file naskah.
- Naskah Markdown tetap rapi, mudah dibaca, dan siap diekspor.
- Perubahan besar tidak langsung masuk ke `main` tanpa review.
- Setiap klaim akademik penting punya referensi atau TODO sumber.
- Data mentah tidak rusak dan tidak ditimpa.

Agent tidak boleh:

- Mengubah banyak bagian naskah tanpa issue yang jelas.
- Menghapus komentar/review promotor tanpa alasan.
- Mengarang referensi akademik.
- Menambahkan citation palsu.
- Mengubah struktur folder utama tanpa persetujuan.
- Menimpa file final tanpa branch dan PR.
- Mengubah data mentah secara langsung.
- Merge PR sendiri tanpa instruksi eksplisit dari user.

## 2. Mode Kerja Agent

Agent dapat bekerja dalam tiga mode.

### 2.1 Bootstrap Mode

Dipakai saat folder disertasi baru dibuat atau belum punya struktur.

Tugas agent:

1. Cek apakah folder sudah menjadi Git repository.
2. Jika belum, bantu init Git repository.
3. Buat struktur folder default.
4. Buat file Markdown awal.
5. Buat `.gitignore`.
6. Buat `README.md`.
7. Buat template Issue dan Pull Request.
8. Buat commit awal.
9. Beri instruksi singkat untuk push ke GitHub.

### 2.2 Writing Mode

Dipakai saat agent diminta membantu menulis atau merevisi naskah.

Tugas agent:

1. Identifikasi issue atau buat draft issue.
2. Buat branch kerja.
3. Edit file yang relevan saja.
4. Catat sumber dan asumsi.
5. Commit perubahan.
6. Siapkan PR.

### 2.3 Review Mode

Dipakai saat agent diminta menindaklanjuti masukan promotor/reviewer.

Tugas agent:

1. Baca review comment, issue comment, atau catatan di `reviews/revision-log.md`.
2. Petakan komentar ke file dan section yang relevan.
3. Buat perubahan di branch.
4. Balas atau catat tindakan revisi.
5. Pastikan before/after dapat dilihat di PR diff.

## 3. Struktur Folder Default

Gunakan struktur berikut sebagai default:

```text
publion-disertasi/
├── manuscript/
│   ├── 00-abstrak.md
│   ├── 01-latar-belakang.md
│   ├── 02-tinjauan-pustaka.md
│   ├── 03-metodologi-penelitian.md
│   ├── 04-hasil-penelitian.md
│   ├── 05-pembahasan.md
│   ├── 06-kesimpulan.md
│   └── _combined.md
│
├── literature/
│   ├── references.bib
│   ├── matrix-literature-review.md
│   ├── notes/
│   └── pdfs/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── instruments/
│
├── analysis/
│   ├── coding/
│   ├── tables/
│   └── figures/
│
├── reviews/
│   ├── promotor-01/
│   ├── promotor-02/
│   └── revision-log.md
│
├── exports/
│   ├── docx/
│   └── pdf/
│
├── docs/
│   ├── style-guide.md
│   ├── citation-guide.md
│   └── workflow.md
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── revisi-bab.md
│   │   ├── literature-review.md
│   │   └── review-promotor.md
│   └── pull_request_template.md
│
├── .gitignore
├── AGENT.md
└── README.md
```

Catatan:

- `manuscript/_combined.md` adalah file hasil gabungan jika dibutuhkan untuk export. Jangan jadikan sumber utama.
- File sumber utama tetap file per bab di `manuscript/`.
- Folder `literature/pdfs/` boleh berisi PDF jika ukuran masih masuk akal untuk Git. Jika PDF terlalu besar, gunakan Git LFS atau simpan di storage eksternal dan catat linknya.

## 4. Bootstrap Checklist

Saat user berkata "init folder disertasi", agent harus membuat minimal:

```text
manuscript/00-abstrak.md
manuscript/01-latar-belakang.md
manuscript/02-tinjauan-pustaka.md
manuscript/03-metodologi-penelitian.md
literature/references.bib
literature/matrix-literature-review.md
reviews/revision-log.md
docs/style-guide.md
docs/citation-guide.md
docs/workflow.md
.github/ISSUE_TEMPLATE/revisi-bab.md
.github/ISSUE_TEMPLATE/literature-review.md
.github/ISSUE_TEMPLATE/review-promotor.md
.github/pull_request_template.md
.gitignore
README.md
AGENT.md
```

Initial commit message:

```text
init: scaffold dissertation workspace
```

Jika GitHub remote belum ada, agent boleh menyiapkan instruksi:

```text
git remote add origin <github-repo-url>
git branch -M main
git push -u origin main
```

Jangan membuat remote URL palsu. Minta user memberikan URL repo jika belum tersedia.

## 5. File Manuscript Canonical

File canonical manuscript berada di folder `manuscript/`.

Minimal:

```text
manuscript/01-latar-belakang.md
manuscript/02-tinjauan-pustaka.md
manuscript/03-metodologi-penelitian.md
```

File tambahan:

```text
manuscript/00-abstrak.md
manuscript/04-hasil-penelitian.md
manuscript/05-pembahasan.md
manuscript/06-kesimpulan.md
```

Aturan:

- Setiap bab memakai heading Markdown yang konsisten.
- Jangan mengganti nama file manuscript tanpa persetujuan.
- Jangan menyimpan naskah final di folder lain.
- Perubahan substantif harus lewat branch dan PR.
- Perubahan kecil seperti typo tetap sebaiknya dicatat dalam commit.
- Jika section belum selesai, tandai dengan TODO yang jelas.

Contoh struktur heading:

```markdown
# Bab 1. Latar Belakang

## 1.1 Konteks Penelitian

## 1.2 Masalah Penelitian

## 1.3 Rumusan Masalah

## 1.4 Tujuan Penelitian

## 1.5 Kontribusi Penelitian
```

TODO akademik:

```markdown
<!-- TODO: tambahkan sumber untuk klaim ini -->
<!-- TODO: cek ulang konsep dengan arahan promotor -->
<!-- TODO: sinkronkan dengan Bab 2 -->
```

## 6. Style Penulisan Markdown

Gunakan Markdown yang bersih:

- Satu heading `#` untuk judul bab.
- `##` untuk subbab.
- `###` untuk sub-subbab.
- Paragraf pendek dan jelas.
- Jangan memakai styling visual berlebihan.
- Jangan memakai heading hanya untuk menebalkan teks.
- Citation sementara boleh menggunakan citation key seperti `[@author2024]`.
- Catatan internal gunakan HTML comment agar tidak tampil di export.

Contoh citation:

```markdown
Kajian terdahulu menunjukkan bahwa moderasi beragama berkaitan dengan praktik kewargaan dan relasi sosial-politik [@author2024].
```

Jika citation belum pasti:

```markdown
Kajian terdahulu menunjukkan adanya hubungan antara religiositas dan perilaku elektoral. <!-- TODO: cari sumber empiris -->
```

## 7. Literature Review

Semua bahan literature review disimpan di `literature/`.

Gunakan:

```text
literature/references.bib
```

untuk daftar referensi utama.

Gunakan:

```text
literature/matrix-literature-review.md
```

untuk matriks literature review.

Gunakan:

```text
literature/notes/
```

untuk catatan per sumber.

Contoh nama file note:

```text
literature/notes/2026-nama-penulis-topik-singkat.md
```

Template literature note:

```markdown
# Author Year - Judul Singkat

## Metadata

- Author:
- Year:
- Title:
- Source:
- DOI/URL:
- Citation key:

## Ringkasan

## Argumen Utama

## Metode

## Temuan

## Relevansi untuk Disertasi

## Kutipan Penting

## Catatan Kritis
```

Template matrix literature review:

```markdown
# Matrix Literature Review

| Citation Key | Author/Year | Topik | Teori/Konsep | Metode | Temuan | Relevansi | Gap |
|---|---|---|---|---|---|---|---|
| author2024 | Author (2024) | ... | ... | ... | ... | ... | ... |
```

Agent harus memastikan setiap referensi yang dimasukkan ke naskah punya sumber yang bisa dilacak.

## 8. Data dan Analisis

Data disimpan di `data/`.

Aturan:

- `data/raw/` berisi data mentah.
- `data/processed/` berisi data yang sudah dibersihkan.
- `data/instruments/` berisi instrumen penelitian.
- Jangan mengubah data mentah tanpa membuat salinan baru.
- Setiap transformasi data harus dijelaskan di `analysis/` atau commit/PR.
- File sensitif atau data pribadi jangan dimasukkan ke GitHub publik.

Output analisis disimpan di:

```text
analysis/
```

Contoh:

```text
analysis/tables/
analysis/figures/
analysis/coding/
```

Jika data sensitif diperlukan, simpan hanya metadata atau instruksi akses, bukan data mentahnya.

## 9. GitHub Issue Workflow

Setiap pekerjaan dimulai dari Issue.

Issue digunakan untuk:

- Revisi bab.
- Penambahan literature review.
- Perbaikan argumen.
- Penambahan data.
- Analisis.
- Permintaan promotor.
- Export DOCX/PDF.

Template Issue umum:

```markdown
## Tujuan

## File yang terdampak

- `manuscript/...`
- `literature/...`

## Instruksi

## Referensi/Sumber

## Output yang diharapkan

## Checklist

- [ ] Draft perubahan dibuat
- [ ] Referensi dicek
- [ ] Naskah diperbarui
- [ ] PR dibuat
- [ ] Review promotor ditindaklanjuti
```

Label GitHub yang disarankan:

```text
type:writing
type:literature
type:data
type:analysis
type:review
type:export
type:admin
chapter:bab-1
chapter:bab-2
chapter:bab-3
chapter:bab-4
chapter:bab-5
chapter:bab-6
status:backlog
status:in-progress
status:review
status:blocked
priority:high
priority:medium
priority:low
source-needed
promotor-feedback
```

Milestone yang disarankan:

```text
Proposal Draft
Bab 1 Complete
Bab 2 Complete
Bab 3 Complete
Seminar Proposal
Data Collection
Analysis Draft
Full Dissertation Draft
Final Revision
```

## 10. Branch Naming

Setiap issue dikerjakan di branch sendiri.

Format:

```text
issue-<nomor>-<deskripsi-singkat>
```

Contoh:

```text
issue-12-literature-review-moderasi-beragama
issue-18-revisi-latar-belakang-promotor
issue-24-tambah-metodologi-pls-sem
```

Jika belum ada nomor issue:

```text
draft-<deskripsi-singkat>
```

Namun setelah issue dibuat, branch sebaiknya disesuaikan ke format issue.

Jangan bekerja langsung di `main` kecuali untuk perubahan administratif kecil dan sudah disetujui.

## 11. Commit Message

Commit harus singkat dan jelas.

Format:

```text
<type>: <ringkasan>
```

Type yang disarankan:

```text
init
draft
revise
cite
review
data
analysis
export
docs
chore
```

Contoh:

```text
draft: add religious moderation literature review
revise: strengthen background argument
cite: add references for electoral behavior section
review: address promotor comments on chapter 2
data: add interview instrument draft
analysis: add coding table for preliminary themes
export: update docx output
```

Setiap commit substantif sebaiknya terkait dengan issue.

## 12. Pull Request Workflow

Setelah perubahan siap, buat Pull Request.

PR harus menjelaskan:

- Issue yang ditutup atau ditindaklanjuti.
- File yang berubah.
- Ringkasan perubahan.
- Referensi yang ditambahkan.
- Bagian yang perlu dicek promotor/reviewer.
- Apakah ada pertanyaan terbuka.

Template PR:

```markdown
## Ringkasan

## Issue Terkait

Closes #

## File yang Berubah

- `manuscript/...`
- `literature/...`

## Perubahan Utama

## Referensi Baru

## Catatan untuk Promotor/Reviewer

## Checklist

- [ ] Naskah sudah dicek ulang
- [ ] Referensi tidak palsu
- [ ] Citation key konsisten
- [ ] Tidak ada file besar yang tidak perlu
- [ ] Data sensitif tidak ikut ter-commit
- [ ] Siap direview
```

## 13. Promotor/Reviewer Highlight Workflow

Promotor/reviewer memberi masukan melalui PR review comment atau Issue comment.

Workflow:

1. Promotor membuka PR.
2. Promotor memberi komentar pada baris tertentu di file Markdown.
3. Komentar dianggap sebagai highlight/review note.
4. Author memperbaiki naskah di branch yang sama.
5. Author membalas komentar dengan ringkasan perbaikan.
6. Promotor dapat resolve comment jika revisi sudah sesuai.
7. Setelah semua komentar penting selesai, PR boleh di-merge.

Jika komentar promotor berasal dari luar GitHub, catat di:

```text
reviews/revision-log.md
```

Format revision log:

```markdown
## YYYY-MM-DD - Review Promotor

### Sumber Review

- Promotor:
- Media: GitHub / meeting / WhatsApp / dokumen / lainnya
- Terkait issue:
- Terkait PR:

### Catatan Revisi

| Bagian | Masukan | Tindakan | Status | Commit/PR |
|---|---|---|---|---|
| Bab 1 | ... | ... | Open/In Progress/Done | ... |
```

Status revisi:

```text
Open
In Progress
Done
Need Follow Up
Rejected with Reason
```

Jika masukan promotor tidak diterapkan, agent harus mencatat alasan akademik atau keputusan user.

## 14. Merge Rules

PR boleh di-merge jika:

- Issue jelas.
- Perubahan sesuai scope.
- Tidak ada referensi palsu.
- Review comment penting sudah dijawab.
- File manuscript tetap rapi.
- Tidak ada konflik.
- Riwayat perubahan terbaca.
- User atau reviewer sudah menyetujui.

Setelah merge:

- Issue ditutup jika pekerjaan selesai.
- Jika masih ada follow-up, buat issue baru.
- Update `reviews/revision-log.md` jika revisi terkait promotor.
- Pastikan branch lama boleh dihapus setelah merge.

## 15. Historical Changes

Riwayat perubahan dilihat dari:

- Git commit history.
- Pull Request diff.
- Review comments.
- Issue discussion.
- `reviews/revision-log.md`.

Agent harus menjaga agar setiap revisi penting bisa ditelusuri:

```text
Issue -> Branch -> Commit -> Pull Request -> Review Comment -> Merge
```

Untuk revisi promotor:

```text
Masukan Promotor -> Issue/PR Comment -> Perubahan Markdown -> Commit -> PR Review -> Merge
```

Saat diminta menjelaskan histori perubahan, agent harus menyebut:

- File yang berubah.
- Commit atau PR terkait.
- Ringkasan before/after.
- Masukan promotor yang ditindaklanjuti.
- Follow-up yang masih terbuka.

## 16. Export

Output export disimpan di:

```text
exports/docx/
exports/pdf/
```

Aturan:

- File export bukan canonical source.
- Canonical source tetap file Markdown di `manuscript/`.
- Export harus mencatat versi/commit sumber.
- Jangan edit manual file export lalu menganggapnya sebagai source.

Contoh nama export:

```text
exports/docx/disertasi-2026-08-23-commitabc123.docx
exports/pdf/disertasi-2026-08-23-commitabc123.pdf
```

Jika menggunakan Pandoc:

```text
pandoc manuscript/01-latar-belakang.md manuscript/02-tinjauan-pustaka.md manuscript/03-metodologi-penelitian.md --bibliography=literature/references.bib -o exports/docx/disertasi.docx
```

Sesuaikan command export dengan template dan citation style yang akhirnya dipilih.

## 17. Aturan untuk AI Agent

AI agent boleh membantu:

- Membuat draft section.
- Merangkum literatur.
- Membuat literature matrix.
- Mengusulkan perbaikan argumen.
- Menyusun PR description.
- Membantu menindaklanjuti review promotor.
- Membuat checklist issue.
- Membantu menyiapkan export.

AI agent tidak boleh:

- Mengarang referensi.
- Mengklaim sudah membaca PDF jika tidak ada akses.
- Mengubah naskah besar tanpa issue.
- Merge PR sendiri tanpa instruksi.
- Menghapus kritik promotor.
- Mengubah data mentah.
- Mengabaikan TODO sumber.

Jika AI menambahkan klaim akademik dan sumber belum jelas, agent harus menandai:

```markdown
<!-- TODO: perlu sumber untuk klaim ini -->
```

Jika AI memakai sumber, agent harus mencatat citation key atau metadata sumber.

## 18. `.gitignore` yang Disarankan

Gunakan `.gitignore` ini sebagai awal:

```gitignore
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.temp
~$*

# Local notes/private files
.env
.env.*
private/
secrets/

# Export build artifacts
exports/tmp/
*.log

# Large/local-only raw files if needed
data/raw/private/
```

Jangan ignore folder penting seperti `manuscript/`, `literature/`, `reviews/`, atau `docs/`.

## 19. README Awal yang Disarankan

`README.md` minimal harus menjelaskan:

```markdown
# Publion Dissertation Workspace

Repository ini menyimpan naskah disertasi, literature review, data penelitian, analisis, review promotor, dan export dokumen.

## Struktur

- `manuscript/`: naskah utama dalam Markdown
- `literature/`: referensi, literature matrix, dan catatan sumber
- `data/`: data mentah, data olahan, dan instrumen
- `analysis/`: tabel, coding, figure, dan catatan analisis
- `reviews/`: catatan review dan revision log
- `exports/`: hasil export DOCX/PDF
- `docs/`: panduan workflow, citation, dan style

## Workflow

Issue -> Branch -> Commit -> Pull Request -> Review -> Merge

Lihat `AGENT.md` untuk aturan kerja lengkap.
```

## 20. Definition of Done

Satu issue dianggap selesai jika:

- File yang diminta sudah diperbarui.
- Referensi yang dipakai tercatat.
- PR sudah dibuat.
- Review comment sudah ditindaklanjuti.
- PR sudah di-merge.
- Issue ditutup atau follow-up issue dibuat.
- Riwayat perubahan dapat dilacak.

Untuk revisi promotor, issue dianggap selesai jika:

- Komentar promotor sudah dipetakan ke section/file.
- Revisi sudah dibuat atau alasan tidak diterapkan sudah dicatat.
- Promotor/user dapat melihat before/after di PR.
- `reviews/revision-log.md` diperbarui jika feedback berasal dari luar GitHub.

## 21. Prioritas Kerja Agent

Saat menerima tugas, agent harus:

1. Cek status repo dan branch aktif.
2. Cari issue terkait.
3. Jika belum ada issue, buat atau sarankan isi issue.
4. Buat branch sesuai nomor issue.
5. Edit file yang relevan saja.
6. Catat referensi dan asumsi.
7. Commit perubahan dengan pesan jelas.
8. Buat PR.
9. Minta review jika diperlukan.
10. Tindak lanjuti komentar.
11. Merge hanya jika sudah disetujui.

## 22. Quick Start untuk Agent

Jika folder kosong dan user meminta init:

```text
1. Buat struktur folder default.
2. Buat file manuscript awal.
3. Buat literature/references.bib kosong.
4. Buat literature/matrix-literature-review.md.
5. Buat reviews/revision-log.md.
6. Buat docs/style-guide.md, docs/citation-guide.md, docs/workflow.md.
7. Buat .github issue templates dan PR template.
8. Buat .gitignore.
9. Buat README.md.
10. Init Git repository jika belum ada.
11. Commit dengan pesan: init: scaffold dissertation workspace.
```

Jika repo sudah ada:

```text
1. Jangan hapus struktur lama.
2. Tambahkan hanya file/folder yang belum ada.
3. Jangan overwrite manuscript yang sudah ada.
4. Cek Git status sebelum dan sesudah perubahan.
5. Jelaskan perubahan yang dilakukan.
```

## 23. Mandatory APA 7 + 07. References Workflow

Bagian ini bersifat **mandatory** dan mengikat seluruh pekerjaan literature, citation, writing, review, dan export di repository ini.

### 23.1 Citation Standard

Standar resmi adalah **APA Style 7th Edition**.

Aturan minimum:

- in-text citation menggunakan author–year;
- untuk tiga penulis atau lebih, gunakan `et al.` sejak sitasi pertama sesuai APA 7;
- corporate/institutional author harus konsisten;
- same-author/same-year harus menggunakan suffix `a`, `b`, `c`, dan seterusnya secara konsisten antara body dan daftar pustaka;
- judul artikel menggunakan sentence case;
- nama jurnal dan volume mengikuti format APA 7;
- DOI ditulis sebagai URL `https://doi.org/...`;
- URL digunakan untuk sumber resmi/regulasi jika DOI tidak tersedia;
- hanging indent diterapkan pada export DOCX/PDF final;
- jangan menambah metadata bibliografis yang belum diverifikasi.

### 23.2 Dua File Referensi yang Wajib Sinkron

Setiap sumber/literature yang digunakan harus masuk ke **dua file pada PR yang sama**:

```text
literature/references.bib
manuscript/07-references.md
```

Fungsinya berbeda:

- `literature/references.bib` = **canonical metadata/reference database** yang machine-readable dan menjadi basis rekonsiliasi metadata.
- `manuscript/07-references.md` = **07. References / Draft Daftar Pustaka**, human-readable, berformat APA 7, dan disiapkan sebagai bagian manuscript.

`manuscript/07-references.md` adalah **Draft Daftar Pustaka aktif**. Ia tidak menggantikan `references.bib`; keduanya harus sinkron.

Jika ada mismatch, jangan menebak. Verifikasi metadata dan gunakan `literature/references.bib` sebagai basis rekonsiliasi, lalu perbarui `07-references.md`.

### 23.3 Mandatory Literature Insertion Sequence

Setiap kali agent memasukkan literature baru ke argumentasi, manuscript, literature review, research memo, atau hypothesis justification, lakukan urutan berikut:

```text
Search -> Fetch/Open Source -> Verify Metadata -> Assess Evidence Quality -> Add/Update references.bib -> Add/Update 07-references.md in APA 7 -> Update literature matrix if relevant -> Cite in manuscript -> Commit -> PR
```

Tidak boleh ada keadaan berikut:

- sumber muncul di body manuscript tetapi tidak ada di `references.bib`;
- sumber muncul di body manuscript tetapi tidak ada di `07-references.md`;
- entry di `07-references.md` dibuat dari metadata tebakan;
- DOI/URL dibuat atau diperkirakan tanpa verifikasi;
- sumber institutional diperlakukan sebagai peer-reviewed causal evidence;
- citation year di body berbeda dari reference entry tanpa alasan bibliografis yang terdokumentasi.

Jika metadata belum lengkap/meragukan:

```markdown
<!-- TODO APA7-METADATA: verifikasi publisher/DOI/year/volume/issue/pages sebelum finalisasi -->
```

### 23.4 Literature Matrix Rule

Jika sumber baru relevan untuk literature synthesis, theory, hypothesis, research gap, rival explanation, measurement, atau method justification, selain dua file referensi wajib di atas, sumber tersebut juga harus dimasukkan atau dipetakan ke:

```text
literature/matrix-literature-review.md
```

Matrix harus membedakan minimal:

- theoretical claim;
- empirical evidence;
- design/method;
- level of analysis;
- key finding;
- limitation;
- relevance;
- rival explanation/boundary condition bila ada.

### 23.5 PR Checklist untuk Perubahan Literature

Setiap PR yang menambah atau mengganti literature harus memeriksa:

- [ ] sumber nyata dan traceable;
- [ ] metadata author/year/title/source diverifikasi;
- [ ] DOI/URL diverifikasi jika tersedia;
- [ ] `literature/references.bib` diperbarui;
- [ ] `manuscript/07-references.md` diperbarui dalam APA 7;
- [ ] same-author/same-year suffix konsisten dengan in-text citation;
- [ ] literature matrix diperbarui jika sumber relevan untuk synthesis;
- [ ] evidence quality dan level of analysis tidak disalahartikan;
- [ ] tidak ada fake citation, citation dumping, atau unsupported causal claim.

Jika salah satu file wajib belum diperbarui, PR literature **belum memenuhi Definition of Done**.

### 23.6 07. References sebagai Draft Daftar Pustaka

File canonical draft:

```text
manuscript/07-references.md
```

Heading utamanya harus menyatakan bahwa file tersebut adalah **07. References — Draft Daftar Pustaka**.

Aturan:

- urut alfabetis menurut APA 7;
- hanya memasukkan sumber yang benar-benar digunakan/ditetapkan sebagai working references;
- metadata yang belum dapat diverifikasi diberi TODO, bukan difabrikasi;
- source type harus dapat dibedakan antara peer-reviewed article, report, regulation, dan institutional webpage;
- setiap literature baru wajib ditambahkan pada saat yang sama dengan perubahan manuscript/literature yang menggunakannya;
- saat literature dihapus dari model/manuscript, evaluasi apakah reference entry masih digunakan sebelum menghapusnya dari Draft Daftar Pustaka.

### 23.7 Export Rule

Pada export final, APA 7 harus diterapkan konsisten dan daftar pustaka memakai hanging indent.

Jika tool export merender bibliography secara otomatis dari `literature/references.bib`, jangan menghasilkan daftar pustaka ganda dengan merender `manuscript/07-references.md` sekaligus. Dalam kondisi tersebut, `07-references.md` tetap berfungsi sebagai Draft Daftar Pustaka untuk audit/sinkronisasi, sedangkan output final dapat dirender dari `references.bib` selama hasilnya identik secara substantif dan mengikuti APA 7.

### 23.8 Definition of Done Tambahan untuk Literature/Citation Work

Pekerjaan yang menyentuh literature/citation belum selesai sampai:

- sumber telah diverifikasi;
- `references.bib` sinkron;
- `07-references.md` sinkron;
- APA 7 diterapkan;
- body citation sinkron dengan reference entry;
- matrix diperbarui jika relevan;
- uncertainty bibliografis yang tersisa ditandai eksplisit.
