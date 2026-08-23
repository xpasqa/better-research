# Issue #40 — Template Data Dictionary Pilot

Gunakan satu baris per variabel/item.

| Field | Isi |
|---|---|
| variable_name | nama pendek dan konsisten |
| construct | DPM / PTS / SEC / BPNS / Engagement / Demographic |
| subscale | nama dimensi |
| item_code | kode item, bukan teks penuh bila hak cipta membatasi |
| source | sumber instrumen |
| version | original / translated / revised |
| response_scale | contoh: 1–4, 1–5, yes/no |
| missing_code | kode missing |
| reverse_scored | yes/no |
| wave | pilot / T1 / T2 / T3 |
| notes | perubahan wording, masalah administrasi, dsb. |

Untuk data responden, simpan juga variabel operasional minimum:

- `participant_id` — pseudonymous ID;
- `school_id`;
- `class_id`;
- `grade`;
- `start_time` / `end_time` atau duration;
- `completion_status`;
- `session_notes` bila ada gangguan administrasi.

Jangan simpan nama lengkap siswa di file analisis.
