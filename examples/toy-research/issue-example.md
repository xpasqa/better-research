# Synthetic Issue — qualify causal wording in CLM-SYN-001

> CONTOH SINTETIS; bukan GitHub Issue aktif dan bukan bukti penelitian nyata.

## Snapshot terkini

- Status kerja: READY FOR REVIEW
- Owner/repo: synthetic/example
- Branch / HEAD / PR: issue-12-qualify-role-clarity / synthetic
- Gate/tahap terkait: G3 dan G7
- Checkpoint terakhir: setelah verification
- Blocker: none
- Langkah berikutnya: review diff lalu merge

## Objective

Menentukan apakah wording kausal pada CLM-SYN-001 dapat dipertahankan. Jika tidak, turunkan klaim ke bentuk yang sesuai dengan evidence sintetis yang tersedia.

## Epistemic state

### KNOWN
- Naskah menggunakan kalimat “coordination routine meningkatkan role clarity”.
- SRC-SYN-001 melaporkan hubungan observasional sintetis.

### SUPPORTED
- SRC-SYN-001 hanya mendukung asosiasi dalam contoh ini.

### INFERRED
- Wording kausal melampaui desain observasional sintetis.

### ASSUMED
- Tidak ada eksperimen atau identifikasi kausal lain di corpus contoh.

### UNKNOWN
- Apakah mekanisme kausal benar dalam dunia nyata.

### DECISION NEEDED
- Retain causal wording atau qualify menjadi associational wording.

## Evidence required

| Evidence/ID | Mengapa diperlukan | Lokasi/sumber | Status |
|---|---|---|---|
| SRC-SYN-001 | Memeriksa desain dan temuan | source-note-SRC-SYN-001.md | FULL_TEXT synthetic |
| CLM-SYN-001 | Memeriksa hubungan evidence–claim | claim-ledger.md | VERIFIED synthetic |

## Scope

### Included
- CLM-SYN-001
- satu paragraf manuscript
- decision record terkait

### Out of scope
- menambah konstruk
- redesign studi
- menulis ulang seluruh bab

## Success criteria

- [x] Desain SRC-SYN-001 diperiksa.
- [x] Bukti tandingan terhadap wording kausal dicatat.
- [x] Keputusan claim dicatat.
- [x] Hanya paragraf terdampak yang direvisi.
- [x] Gate tidak dinaikkan otomatis.

## Verification plan

| Criterion | Method | Expected evidence | Status |
|---|---|---|---|
| Wording sesuai desain | Compare source note ↔ claim | causal claim removed | PASS |
| Scope surgical | Inspect changed artifact | one paragraph + ledger/decision | PASS |
| Gate separation | Inspect gate review | G3 remains PERLU REVISI | PASS |

## Falsification / alternatives

Wording kausal dapat dipertahankan hanya jika tersedia evidence tambahan yang benar-benar mengidentifikasi causal effect. Evidence tersebut tidak tersedia dalam contoh.

## Closure

Delivery dapat selesai setelah PR synthetic merged. Academic readiness tetap dinilai terpisah.
