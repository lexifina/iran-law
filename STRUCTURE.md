# Structure of iran-law

Folder names are in Persian, the language people search Iranian law in. Years are Solar Hijri (the calendar the
sources use) and all numbers use Western digits. Every folder holds at most 1,000 entries.

| Folder | What | One file is |
| --- | --- | --- |
| `قانون-اساسی/` | The Constitution of the Islamic Republic of Iran in Persian, the authoritative text: 1358 (1979) and the 1368 (1989) revision | one principle (`اصل-001.md`), the preamble (`مقدمه.md`) |
| `constitution/` | Its English translation published by the Guardian Council (a translation, not an official text) | one article (`art-001.md`) |
| `قوانین/<سال>/<عنوان>/` | Laws and codes, by the Solar Hijri year of enactment and short title (`قوانین/1311/قانون-تجارت/`); a code over 1,000 articles is split by its own parts (`قوانین/1307/قانون-مدنی/جلد-1/`) | one article (`ماده-001.md`) |
| `آرای-قضایی/<مرجع>/<سال>/<ماه>/` | Court judgments from the Judiciary's national judgments system (ara.jri.ac.ir), by court and the Solar Hijri year and month of the final judgment | one case's published judgments (`<شماره-دادنامه>.md`) |
| `data/`, `tools/` | Tables, charts and the tools to read the history | |

Courts (`<مرجع>`): `دیوان-عالی-کشور` (Supreme Court), `دیوان-عدالت-اداری` (Administrative Justice Court),
`دادگاه-تجدیدنظر-استان` (provincial appeal courts), `دادگاه-بدوی` (first instance), and the general boards'
unifying rulings under `هیئت-عمومی-...`.

## Versions and dates

- One commit per version of a law and one per published case, in the order they took effect.
- The author date is 12:00 Tehran time on the day the version took effect; for a judgment, the day of the final
  judgment (تاریخ دادنامه قطعی), converted from the Solar Hijri date. Before 1970 the date is 1970-01-01 and the real
  day starts the commit subject.
- Every commit carries `Kind:` (law, judgment, publisher, layout, documentation), `In-force:` (the day) and
  `In-force-basis:` (the clause or field the day comes from), and `Source:`.
- A record whose in-force day cannot be read from the source (for example a law the source gives only an approval
  day for, with no publication day) is held, not committed.
- The author is the law or court that made the record; the committer is Lexifina.

## Privacy

The judgments system publishes judgments with the parties reduced to initials. Cases about family matters, minors
and sexual offences are not published here.

## Sources

- Laws and the Persian Constitution: the Islamic Parliament Research Center's laws system (rc.majlis.ir), texts as
  enacted from the Majlis volumes. Its pages say "حق کپی رایت متعلق به مرکز پژوهش های مجلس شورای اسلامی است".
- Judgments: سامانه ملی آرای قضایی, Judiciary Research Institute (ara.jri.ac.ir). Its pages say "کلیه حقوق برای
  پژوهشگاه قوه قضاییه محفوظ است".
- English Constitution: Guardian Council of the Constitution (shora-gc.ir).

Lexifina's arrangement, commit messages, tables and tools are dedicated to the public domain under CC0 1.0.
