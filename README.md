# THE WORLD — Tuesday 24 November 2026 (v2)

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

The lead: Russia breaches Poland again — a Russian drone crosses NATO
airspace overnight on 24 November, the second incursion in four days,
as Warsaw demands permanent US troops and NATO sends its AWACS
early-warning jets. Around it, the day's other stories — 26 dead in the
Java candy-factory fire with a criminal probe opened, Jensen Huang back
at Nvidia with shares jumping 31%, Ukraine sinking the Russian corvette
Merkury off Libya, China probing Politburo member Chen Jining,
Lukashenko pitching a joint trip to Moscow with Zelensky, and the World
Chess Championship opening with a draw in Geneva — plus a ticker of
smaller items (Chapo Isidro to face trial in Mexico, about 175 migrants
unaccounted for off Senegal, Abrego Garcia leaving the US, Trump set to
unveil new tariffs, Bangladesh garment workers clashing with police,
Alcaraz winning his first ATP Finals title, and Eisenkot clinching a
first coalition deal in Israel). Every story on the page happened on,
or was first reported on, Tuesday 24 November 2026; the sources are
listed in [NOTES.md](NOTES.md).

## What changed from v1

- **The lead is now a story of 24 November itself.** v1 led with the
  NATO AWACS decision of 23 November; v2 leads with the overnight
  24 November drone incursion — the second breach in four days — and
  Poland's renewed push for permanent US troops the same day.
- **Fresher, verified line-up.** The Serang toll is corrected to 26
  (confirmed Tuesday, with a criminal probe opened); the chess
  championship's Game 1 draw in Geneva replaces the two-day-old
  Alcaraz final as the sport lead (Alcaraz moves to the ticker, dated
  by the event). COP31 and the Gaza strikes, both 22–23 November news,
  are dropped; genuinely 24 November stories take their place
  (Chen Jining probe, Lukashenko's Moscow pitch, the Senegal boat,
  Abrego Garcia, the tariffs probe).
- **Cleaner picture.** The lead illustration is drawn, not rendered,
  so no text can come out garbled: one AWACS silhouette, one
  simplified map with six large labels and a single dashed drone
  track. No tiny unreadable labels, no overlapping captions.
- **Stronger hierarchy.** One dominant headline, one deck, three
  large right-rail stories, two middle stories, one sport box, one
  ticker — every story readable at a glance.

## How the image was made

`build_image.py` draws the whole front page with Pillow (text and
shapes placed at explicit sizes and positions — nothing is left to an
image model to spell). Run it to regenerate the image:

```bash
python3 build_image.py
```

## How it runs

The finished image ships in this repository as `entry.png`. The entry
program is deliberately thin so its output can never drift:

```bash
python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` into the output directory — `$MAKEFUN_OUTPUT_DIR`,
or `/output` when that variable is unset — as `entry.png`, then checks
that the copy is complete by comparing the SHA-256 hash of the copy
with the source. Run it twice and the two outputs are byte-identical.

## Files

| File | What it is |
| --- | --- |
| `main.py` | Entry program: copies the bundled image to the output directory and verifies the copy. |
| `entry.png` | The finished front page, 1024 × 1024. |
| `build_image.py` | The script that draws `entry.png` (Pillow; run it to regenerate the image). |
| `NOTES.md` | Story-by-story notes: what each item on the page is, and where it was reported. |
| `LICENSE` | MIT. |

## Bounty

Built for the make.fun bounty
[news-image-20261124](https://make.fun/bounty/news-image-20261124) —
"Sum up 24 November's world news in one image", $100.

---
*Referral: https://make.fun/?ref=0txwmf1m*
