# THE WORLD — Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/giandisruw/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/giandisruw/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![make.fun bounty](https://img.shields.io/badge/make.fun-news--image--20261124-blue)](https://make.fun/bounty/news-image-20261124)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![python](https://img.shields.io/badge/python-3.13-blue)](main.py)

One day of world news, summed up in a single front page.

## The image

`entry.png` is a one-page newspaper — **THE WORLD, Tuesday 24 November
2026** — laid out like a broadsheet: a masthead, one lead story with a
large illustration, and the rest of the day's news in columns around it.

The lead: the war spilling over — NATO sending its AWACS early-warning
jets to Poland after three Russian cruise missiles landed on Polish
soil, with Kyiv warning that Moscow is preparing new strikes. Around
it, the day's other stories — 24 dead in the Serang candy-factory
fire with about 30 still missing, COP31 ending without a deal, Gaza
strikes killing three including a UN aid worker, Mexico capturing top
drug lord "Chapo Isidro", Jensen Huang returning to Nvidia with shares
jumping more than 31%, Alcaraz winning his first ATP Finals title,
and the World Chess Championship opening in Geneva — plus a ticker of
smaller items (Trump pausing the Iowa explosives disposal, US sanctions
on Iran's shadow banks, the Murmansk governor detained, North Korea
mulling shutting the Swiss office, the O'Hare ground stop, and the
India–New Zealand Test drawn). Every story on the page happened on,
or was reported on, 23–24 November 2026; the sources are listed in
[NOTES.md](NOTES.md).

## How it runs

The finished image ships in this repository as `entry.png`. The entry
program is deliberately thin so its output can never drift:

```bash
python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` into the output directory — `$MAKEFUN_OUTPUT_DIR`,
or `/output` when that variable is unset — as `entry.png`, then checks
that the copy is complete by comparing its size with the source. Run it
twice and the two outputs are byte-identical.

## Files

| File | What it is |
| --- | --- |
| `main.py` | Entry program: copies the bundled image to the output directory and verifies the copy. |
| `entry.png` | The finished front page, 1024 × 1024. |
| `NOTES.md` | Story-by-story notes: what each item on the page is, and where it was reported. |
| `LICENSE` | MIT. |

## Bounty

Built for the make.fun bounty
[news-image-20261124](https://make.fun/bounty/news-image-20261124) —
"Sum up 24 November's world news in one image", $100.

---
*Referral: `0txwmf1m` — make.fun*
