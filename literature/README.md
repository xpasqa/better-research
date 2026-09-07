# Literatur dan bukti

[references.bib](references.bib) adalah basis metadata bibliografis terverifikasi. File dimulai kosong agar tidak ada referensi fiktif.

Gunakan [model provenance](../docs/provenance.md) untuk membedakan **report/source (SRC)**, **study (STUDY)**, **claim (CLM)**, **decision (DEC)**, dan **review finding (REV)**.

Buat saat diperlukan:

- `searches/`: log dan ekspor penelusuran yang boleh disimpan.
- `screening/`: keputusan seleksi serta hubungan record–report–study.
- `notes/`: satu catatan per SRC menggunakan source-note.
- `claim-ledger.md`: hubungan claim–evidence dari template.

PDF berlisensi disimpan lokal pada `literature/pdfs/` yang diabaikan Git atau di penyimpanan institusi. Jangan menganggap kepemilikan file memberi izin redistribusi.

## Identity dan deduplication

Satu publikasi/report menggunakan satu SRC. Beberapa report dapat berasal dari STUDY yang sama.

Contoh struktur:

```text
STUDY-012
├── SRC-041 preprint
├── SRC-052 journal article
└── SRC-063 correction
```

Jangan menghitung report tersebut sebagai tiga studi independen.

Saat deduplikasi, periksa setidaknya DOI/identifier, title, authors, year, versi, dan hubungan report–study. DOI dinormalisasi tanpa prefix `https://doi.org/` dan dibandingkan case-insensitively.

## Citation keys

Konvensi default:

```text
authorYYYYshorttitle
```

Gunakan huruf kecil ASCII tanpa spasi. Tambahkan suffix `a`, `b`, dan seterusnya hanya bila collision tetap terjadi setelah short title dibuat cukup jelas.

Citation key hanyalah identifier kerja; ia bukan bukti bahwa dua record identik atau berbeda.

## Version lifecycle

Preprint, published article, correction, expression of concern, dan retraction dapat menjadi SRC berbeda. Catat versi yang benar-benar dibaca dan tautkan hubungan antar-report pada source note.

Jika versi terbit menggantikan preprint, jangan menghapus provenance preprint. Periksa apakah claim, locator, atau appraisal perlu diperbarui.

## Verification rule

Metadata masuk ke `references.bib` hanya setelah diverifikasi dari sumber yang benar-benar diakses. Keberadaan DOI atau citation key tidak membuktikan bahwa isi source mendukung suatu claim.

Daftar pustaka yang dibaca manusia dihasilkan dari bibliografi setelah alat ekspor disiapkan. Jangan memelihara metadata yang sama secara manual di dua tempat.
