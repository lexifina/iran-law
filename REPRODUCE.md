# How this repository was made (Iran)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Guardian Council: Constitution of the Islamic Republic of Iran (full text), English | <https://www.shora-gc.ir/en/news/87/constitution-of-the-islamic-republic-of-iran-full-text> | 2026-10-29 | no licence stated; official English translation published by the Guardian Council |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Islamic Republic of Iran (1979, as revised 1989) | 1 | 1989-07-28 to 1989-07-28 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Asia/Tehran) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution art. 177: the decisions of the Constitutional Revision Shura, once confirmed by the Leader, take effect when approved by a referendum; the 1989 revision was approved by referendum on 28 July 1989. https://www.shora-gc.ir/en/news/87/constitution-of-the-islamic-republic-of-iran-full-text

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `b4075aaa197cd2517d111ad9b4f6468923263a0e01546d721f64ad69bb313075` (115030 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `6229396f41c9d7f1d6f405becfbe4097b35b82da`, `check.py` `5e112e6a33b7e93d00112e55f01fbb4fb3fdd8da`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- English is the translation published by the Guardian Council on its English site; the Persian text is authoritative and is not built here.
- One version, the oldest available (first_law null), credited to the Guardian Council. The page states no date for the text; it has 177 articles, the 1989 revised Constitution, so it is dated 1989-07-28, the day the referendum approved the revision. The original 1979 text (in force 3 December 1979) is not built.
- The Guardian Council's interpretations (estefsariyeh) of articles are separate acts and are not built.
- Unit files: the preamble and one per article (art-NNN, 1-177); chapter headings, footnote markers and footnotes, and the translator credits are left out; list items keep their numbers.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
