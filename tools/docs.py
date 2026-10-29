import sys
sys.path.insert(0, r'~\AppData\Local\Temp\claude\C--Users-alany-Documents-lexifina\bf2c37ff-5368-4758-a217-51eee3902b94\scratchpad\fb5_helper')
import fb5docs as mkdocs
F = r'~\Documents\lexifina\scripts\iran-law'
mkdocs.write(F, 'iran', 'IR', 'Iran', 'English (the Guardian Council\'s translation of the Persian Constitution)',
 [('`constitution/`', 'Constitution of the Islamic Republic of Iran (1979, as revised 1989)', '1', 'Oldest version available, dated 28 July 1989, the day the referendum approved the revision (177 articles)')],
 [('[Guardian Council (English site)](https://www.shora-gc.ir/en/news/87/constitution-of-the-islamic-republic-of-iran-full-text)', 'Constitution, full English text', 'Official translation by the Guardian Council; the Persian text is authoritative. No licence stated.')],
 'The text is the English translation of the Constitution published by the Guardian Council (shora-gc.ir). The Persian text is the authoritative one. This first build holds one version of the Constitution; no statute is built yet.',
 """The legal text is the Constitution of the Islamic Republic of Iran (as revised in 1989), in the English translation
published by the Guardian Council of the Constitution on its English site
(https://www.shora-gc.ir/en/news/87/constitution-of-the-islamic-republic-of-iran-full-text), retrieved 29 October 2026.
The page states no licence; the Persian text is the authoritative one.""",
 ['**One version.** The Guardian Council publishes only the current text. The original 1979 text and the 1989 revision are not shown as separate versions; the single version is dated 28 July 1989 and credited to the publisher ("oldest version available").',
  '**English translation.** The Persian text is authoritative and is not built here.',
  '**Apparatus.** Chapter and section headings, footnote markers and footnotes, and the translator credits are left out. The Guardian Council\'s interpretations of articles are not included.',
  '**Statutes.** No Iranian statute is included yet: qavanin.ir and rc.majlis.ir answer automated requests with a challenge page and were not used.'],
 '`parse.py` reads the saved HTML page and writes `corpus.json`.')
mkdocs.jur(F, 'iran', 'IR', 'Iran', 'first build: Constitution (1979, as revised 1989), English translation by the Guardian Council (1 version, oldest available, 1989-07-28)', 1)
