## Result

Ringkas hasil akhir untuk reviewer yang belum membaca percakapan. Jelaskan masalah yang diselesaikan dan perubahan yang benar-benar dibuat.

## Issue and scope

- Owner/repo:
- Issue utama:
- Parent/child atau dependency:
- Base / head:
- Scope final:
- Perubahan scope dari rencana:

Gunakan `Refs #nomor` untuk PR parsial. Gunakan `Closes #nomor` hanya pada PR final ketika seluruh closure conditions issue terpenuhi.

## Epistemic delta

Jelaskan perubahan pengetahuan/keputusan yang dihasilkan PR ini, bukan hanya perubahan teks.

| Item/ID | Sebelum | Sesudah | Dasar bukti | Confidence/status |
|---|---|---|---|---|

Contoh status: SUPPORTED / INFERRED / ASSUMED / UNKNOWN / RETRACTED / MIXED.

### Unknowns that remain

- 

### Assumptions that remain

- 

### Decisions made or superseded

| DEC ID | Keputusan | Evidence/claim IDs | Supersedes | Dampak |
|---|---|---|---|---|

## Outputs and acceptance evidence

| Success criterion issue | Berkas/permalink/commit | Bukti aktual | Status |
|---|---|---|---|

Status: PASS / FAIL / BLOCKED / NOT APPLICABLE.

## Evidence and provenance

Tautkan ID yang relevan.

- Sources/reports (SRC):
- Studies (STUDY):
- Claims (CLM):
- Decisions (DEC):
- Reviews/findings (REV):
- Protocol/deviation IDs:
- Evidence yang tidak dapat diakses/diverifikasi:

Jangan menyatakan “source supports claim” hanya karena sumber tercantum. Hubungan dukungan harus terlihat pada source note/claim ledger.

## Falsification and alternatives

Untuk perubahan klaim/teori/metode yang substantif:

- Bukti tandingan yang diperiksa:
- Penjelasan alternatif yang diperiksa:
- Boundary conditions:
- Apa yang masih dapat membatalkan keputusan ini:

Isi TIDAK BERLAKU dengan alasan untuk perubahan mekanis yang tidak menyentuh klaim akademik.

## Verification performed

| Check | Version/HEAD checked | Method | Result | Limitation |
|---|---|---|---|---|

Pisahkan:

- **mechanical verification** — link, schema, syntax, path, build/check otomatis;
- **epistemic verification** — kecocokan klaim–bukti, counterevidence, inference boundary;
- **academic judgement** — quality gate/review manusia atau agent sesuai scope.

Jangan mengubah PASS mekanis menjadi klaim bahwa riset valid secara akademik.

## Surgical-change check

- [ ] Setiap perubahan substantif dapat ditelusuri ke issue, bukti, DEC, REV, atau acceptance criterion.
- [ ] Tidak ada drive-by refactor/rewrite di luar scope.
- [ ] Perubahan ini hanya membersihkan orphan/inconsistency yang dibuat oleh perubahan sendiri, kecuali scope diperluas secara eksplisit.

## Data, ethics, and integrity

- [ ] Tidak ada data sensitif, credentials, consent bertanda tangan, atau raw participant data.
- [ ] Tidak ada sumber, hasil, kutipan, locator, review manusia, izin, atau aktivitas yang diklaim tanpa bukti.
- [ ] Status etik/izin tidak diasumsikan.
- [ ] Materi berlisensi tidak ditambahkan tanpa dasar izin.

## Review and corrective actions

Reviewer/peran (agent/mandiri/manusia), versi, temuan, respons, dan unresolved items:

| REV ID | Reviewer/peran | Finding | Action | Status |
|---|---|---|---|---|

Review agent bukan persetujuan promotor, reviewer jurnal, atau komite etik.

## Integration readiness

- [ ] Target owner/repo, base, dan head benar.
- [ ] Success criteria yang akan ditutup berstatus PASS.
- [ ] Verification sesuai perubahan selesai dan batasnya dicatat.
- [ ] Issue snapshot/checkpoint sesuai keadaan terbaru.
- [ ] Quality gate tidak dinaikkan hanya karena PR siap merge.
- [ ] Otorisasi merge dan branch protection telah diperiksa.

## Planned closure

- Issue yang ditutup:
- Issue/pekerjaan yang tetap terbuka:
- Gate yang terdampak/reopen:
- Cara memverifikasi hasil di `main` setelah merge:

Commit merge dan status MERGED dicatat setelah benar-benar terjadi; jangan menuliskan hasil masa depan sebagai fakta.
