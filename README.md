# Iran: law history in git

The law of Iran as a git history: one file per provision, one commit per law or decision on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to a provision; `tools/on.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ir/`.

> **First build.** The text is the English translation of the Constitution published by the Guardian Council (shora-gc.ir). The Persian text is the authoritative one. This first build holds one version of the Constitution; no statute is built yet.

Language: the text is in English (the Guardian Council's translation of the Persian Constitution); this README is in English.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the Islamic Republic of Iran (1979, as revised 1989) | 1 | Oldest version available, dated 28 July 1989, the day the referendum approved the revision (177 articles) |

## Questions as git commands

| Question | Command |
| --- | --- |
| The whole act on a date | `python tools/on.py 2024-01-01 constitution` |
| One provision on a date | `python tools/on.py 2024-01-01 constitution <unit>` (unit = file name without `.md`) |
| Which law wrote each line of a provision? | `git blame constitution/<unit>.md` |
| Every change to a provision, word by word | `git log -p --word-diff constitution/<unit>.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## What it does not show

- **One version.** The Guardian Council publishes only the current text. The original 1979 text and the 1989 revision are not shown as separate versions; the single version is dated 28 July 1989 and credited to the publisher ("oldest version available").
- **English translation.** The Persian text is authoritative and is not built here.
- **Apparatus.** Chapter and section headings, footnote markers and footnotes, and the translator credits are left out. The Guardian Council's interpretations of articles are not included.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina's code reads the saved HTML page and writes `corpus.json`. The shared builder turns `corpus.json` into the commits; `REPRODUCE.md` lists the sources, commands and decisions, and the result of the checks (every version read back from git on its in-force day and the day before, trailers parsed, no merge commits, dates never going backwards).

## Sources

| Source | What | Notes |
| --- | --- | --- |
| [Guardian Council (English site)](https://www.shora-gc.ir/en/news/87/constitution-of-the-islamic-republic-of-iran-full-text) | Constitution, full English text | Official translation by the Guardian Council; the Persian text is authoritative. No licence stated. |

See `LICENSE` for the attribution.
