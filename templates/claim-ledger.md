# Daftar klaim dan bukti

Satu baris merepresentasikan **satu hubungan evidence → claim**, bukan satu claim secara keseluruhan. Satu CLM dapat memiliki banyak baris dan banyak sumber. Lihat [model provenance](../docs/provenance.md).

## Claim registry

| CLM ID | Klaim persis | Jenis | Status claim | Lokasi naskah | Supersedes/replaced by | Catatan |
|---|---|---|---|---|---|---|

Status claim: DRAFT / UNVERIFIED / SUPPORTED / MIXED / CONTRADICTED / RETRACTED.

Jenis: empiris, teoretis, konseptual, normatif, atau inferensi peneliti.

## Evidence relations

| CLM ID | SRC ID | STUDY ID | Relation | Directness | Access | Locator | Appraisal/kualitas & batas | Versi/status source | Tindakan |
|---|---|---|---|---|---|---|---|---|---|

Relation: SUPPORTS / CONTRADICTS / LIMITS / CONTEXTUALIZES.

Directness: DIRECT / INDIRECT / SECONDARY.

Access: FULL_TEXT / PARTIAL / ABSTRACT_ONLY / METADATA_ONLY / UNAVAILABLE.

Tindakan: pertahankan, kualifikasi, cari bukti, pisahkan claim, atau tarik.

## Claim-level synthesis

Untuk claim substantif, ringkas setelah evidence relations diperiksa:

| CLM ID | Supporting pattern | Counterevidence | Alternative explanation | Boundary conditions | Remaining unknown | Decision/DEC |
|---|---|---|---|---|---|---|

Jangan mengartikan jumlah sumber sebagai ukuran otomatis kekuatan bukti. Source yang nyata belum tentu mendukung claim; report yang berbeda juga dapat berasal dari STUDY yang sama.
