# Reference Export Workflow

Folder ini digunakan untuk **generated reference exports**, bukan sebagai canonical source.

## Canonical Sources

- `literature/references.bib` — canonical machine-readable metadata database.
- `manuscript/07-references.md` — Draft Daftar Pustaka human-readable dalam APA Style 7th Edition.

## Zotero / Reference-Manager Compatibility

`literature/references.bib` dapat diimpor langsung ke Zotero sebagai BibTeX. Untuk interoperabilitas dengan reference manager atau citation engine lain, export release dapat menyediakan:

- `*.bib` — BibTeX; cocok untuk Zotero, LaTeX, Pandoc, Better BibTeX workflows.
- `*.ris` — RIS; format pertukaran bibliografi lintas reference manager.
- `*.csl.json` — CSL JSON; berguna untuk Pandoc/Citeproc dan citation-processing workflow.

Jika dibutuhkan, format lain boleh dibuat sebagai **generated derivative**, tetapi tidak boleh menjadi sumber metadata utama.

## Mandatory Rule

Jangan mengedit file export secara manual lalu menggunakannya untuk mengubah metadata canonical. Semua perbaikan harus dilakukan terlebih dahulu pada `literature/references.bib`, diverifikasi, disinkronkan ke `manuscript/07-references.md`, kemudian export dibuat ulang.

Alur:

```text
Verified source
  -> literature/references.bib
  -> manuscript/07-references.md (APA 7)
  -> generated exports (.bib / .ris / .csl.json)
  -> Zotero / citation manager / Pandoc
```

## Versioning

Untuk checkpoint penting (proposal submission, seminar proposal, final dissertation), gunakan nama file versioned, misalnya:

```text
exports/references/disertasi-dodo-proposal-2026-08-23.bib
exports/references/disertasi-dodo-proposal-2026-08-23.ris
exports/references/disertasi-dodo-proposal-2026-08-23.csl.json
```

Generated exports harus dapat direproduksi dari canonical bibliography dan sebaiknya mencatat commit sumber pada release note atau PR.