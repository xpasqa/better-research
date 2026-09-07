# Provenance model

Better Research menggunakan ID lokal untuk menjaga jalur **source → study → claim → decision → change/review** tetap dapat ditelusuri. Model ini adalah konvensi workspace, bukan standar bibliografi eksternal.

## Unit dan ID

| ID | Unit | Makna |
|---|---|---|
| `SRC-###` | Source/report | Satu report atau manifestasi yang benar-benar dapat dibaca: artikel, preprint, bab, dokumen, dataset documentation, dan sebagainya |
| `STUDY-###` | Study | Penelitian/analisis yang mendasari satu atau lebih report |
| `CLM-###` | Claim | Pernyataan yang dipakai atau diuji dalam proyek |
| `DEC-###` | Decision | Keputusan substantif proyek |
| `REV-###` | Review finding | Temuan audit/review yang memerlukan respons |
| `RQ-###` | Research question | Pertanyaan penelitian yang telah diberi identitas stabil |

Nomor dibuat ketika unit nyata masuk ke workspace. Jangan membuat ID hanya untuk mengisi contoh.

## Relasi minimum

```text
SRC ──reports/derives-from──> STUDY
SRC ──supports/contradicts/limits/contextualizes──> CLM
CLM ──informs/challenges──> DEC
REV ──challenges/requires-change──> CLM / DEC / artifact
DEC ──changes──> RQ / protocol / design / manuscript / gate
```

Setiap relasi substantif harus mempunyai locator atau alasan yang dapat diperiksa.

## Status claim

Gunakan salah satu status berikut pada claim ledger:

- `DRAFT` — kandidat klaim; belum cukup diperiksa.
- `UNVERIFIED` — sumber/dukungan yang diperlukan belum berhasil diverifikasi.
- `SUPPORTED` — dukungan yang relevan telah diperiksa dan batasnya tercatat.
- `MIXED` — terdapat dukungan dan bukti tandingan/heterogenitas yang material.
- `CONTRADICTED` — bukti yang diperiksa secara material bertentangan dengan klaim sebagaimana dirumuskan.
- `RETRACTED` — klaim proyek ditarik dan tidak boleh dipakai sebagai premis aktif.

Status bukan skor kebenaran universal. Status menyatakan keadaan bukti **dalam scope dan corpus yang benar-benar diperiksa**.

## Tipe hubungan evidence

Untuk setiap hubungan SRC/STUDY → CLM, catat:

- `SUPPORTS`
- `CONTRADICTS`
- `LIMITS`
- `CONTEXTUALIZES`

Jangan memakai banyaknya baris SUPPORTS sebagai pengganti appraisal kualitas, kompatibilitas desain, atau kekuatan inferensi.

## Directness dan access status

**Directness**

- `DIRECT` — bukti/hasil yang dirujuk secara langsung relevan dengan claim.
- `INDIRECT` — relevansi melalui konstruk, konteks, atau inferensi antara.
- `SECONDARY` — informasi diperoleh melalui sumber sekunder.

**Access**

- `FULL_TEXT`
- `PARTIAL`
- `ABSTRACT_ONLY`
- `METADATA_ONLY`
- `UNAVAILABLE`

Jangan meningkatkan directness hanya karena hasil sesuai harapan.

## Report versus study

Satu study dapat mempunyai beberapa report:

```text
STUDY-012
├── SRC-041 preprint
├── SRC-052 journal article
└── SRC-063 correction
```

Jangan menghitung ketiganya sebagai tiga penelitian independen. Jika dua report ternyata berasal dari study yang sama, pertahankan kedua SRC tetapi tautkan ke STUDY yang sama dan koreksi sintesis yang terpengaruh.

## Versi, correction, dan retraction

Setiap source note mencatat:

- versi yang dibaca;
- DOI/URL atau identifier yang diverifikasi;
- tanggal akses bila relevan;
- hubungan dengan preprint/published version/report lain;
- correction, expression of concern, atau retraction yang diketahui.

Versi baru tidak menghapus provenance versi lama. Catat report yang menggantikan atau memperbaiki report sebelumnya.

## Citation identity

`literature/references.bib` adalah basis metadata bibliografis kanonik. Konvensi citation key default:

```text
authorYYYYshorttitle
```

Gunakan huruf kecil ASCII tanpa spasi; tambahkan suffix `a`, `b`, dan seterusnya hanya jika collision tidak dapat diselesaikan dengan short title yang lebih jelas.

Contoh bentuk (bukan referensi nyata):

```text
santoso2025institutionaltrust
```

Aturan identitas:

1. DOI dinormalisasi tanpa `https://doi.org/` dan dibandingkan case-insensitively.
2. Citation key tidak menjadi bukti identitas; DOI, title, author, year, dan provenance tetap diperiksa.
3. Preprint dan artikel terbit dapat memiliki citation key/SRC berbeda tetapi STUDY sama.
4. Correction/retraction dicatat sebagai SRC tersendiri dan ditautkan.
5. Metadata tidak ditambahkan ke `references.bib` sebelum diverifikasi dari sumber yang benar-benar diakses.

## Decision provenance

Keputusan substantif mencatat minimal:

- masalah;
- alternatif;
- keputusan/status;
- SRC/STUDY/CLM/REV yang menjadi dasar;
- asumsi/unknown yang masih ada;
- artefak dan quality gate yang terdampak;
- DEC yang digantikan, bila ada.

Keputusan baru **supersedes**, bukan menghapus, keputusan lama.

## Review provenance

Review finding menggunakan `REV-###` dan memuat lokasi, evidence, dampak, tindakan, serta cara memeriksa penyelesaian. Menutup REV berarti masalah yang didefinisikan telah diperiksa ulang; bukan berarti seluruh naskah atau gate otomatis SIAP.

## Aturan penggunaan

- Jangan membuat relasi evidence tanpa membuka bukti yang sesuai dengan access status yang diklaim.
- Jangan mengubah `UNVERIFIED` menjadi `SUPPORTED` karena ringkasan AI atau metadata bibliografis.
- Jika claim berubah secara material, pertahankan CLM yang sama hanya bila identitas intelektualnya masih sama; jika tidak, buat CLM baru dan tandai hubungan supersedes/replaces.
- Perubahan provenance yang memengaruhi argumen, desain, atau inferensi harus dipantulkan pada decision log dan gate terkait.
