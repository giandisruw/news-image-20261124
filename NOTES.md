# Notes — THE WORLD, Tuesday 24 November 2026 (v2)

What is on the front page, story by story, and where each item was
reported. Every item below happened on, or was first reported on,
Tuesday 24 November 2026, unless a date is given. Nothing on the page
invents a casualty figure or a quote.

## Lead story

**Russia breaches Poland again.** A Russian drone briefly entered
Polish airspace overnight into Tuesday 24 November during Russian
strikes on Ukraine — the second incursion in four days, after three
Russian Kh-101 cruise missiles crossed into Poland on Friday
20 November. Poland announced on Tuesday that it had renewed its push
for a permanent US military presence, and NATO jets scrambled. NATO
had authorised the forward deployment of an AWACS early-warning
aircraft to Poland on Monday 23 November, after the North Atlantic
Council met in Brussels; the front page's main illustration — an AWACS
E-3A Sentry over a simplified map of Poland and its neighbours, with
the dashed drone track — and its headline carry this story.
Reported 24 November 2026 (Reuters, 23 November; Fox News, 24
November; NATO spokesperson Allison Hart; Polish Defence Ministry).

## The day's other stories

- **26 dead in the Java candy-factory fire.** Indonesian authorities
  confirmed on Tuesday 24 November that 26 workers were killed in
  the fire at the PT Fonusa Agung Mulia confectionery plant in
  Cikande, Serang regency, Banten, which broke out on Saturday
  21 November; police said on Tuesday they had opened a criminal
  negligence investigation. The number of people still missing differs
  by source (28 unaccounted for, police say; 8 per the Associated
  Press), so the page gives no missing figure. Reported 24 November
  2026 (Associated Press; Xinhua; Banten police).
- **Huang's back — Nvidia soars 31%.** Nvidia's board reinstated
  Jensen Huang as chief executive on Monday 23 November, less than
  two weeks after he resigned; shares closed up 31.48% that day, their
  best day since 2003, adding about $950 billion in market value,
  while the Nasdaq jumped 6.5%. The page says "shares jump 31%" and
  dates the reinstatement to the board's Monday announcement.
  Reported 23–24 November 2026 (CNN; Reuters; Investopedia).
- **Ukraine sinks Russian warship off Libya.** Ukraine says its sea
  drones sank the Russian Navy corvette Merkury at Benghazi, Libya,
  and hit the cargo vessel MV Angara; a Ka-27 helicopter aboard the
  corvette was destroyed. The attack took place on Sunday 22 November
  and was claimed by President Zelensky on Monday 23 November; the
  page attributes the sinking to Kyiv ("Kyiv says…"). Reported
  23 November 2026 (Reuters; CNN; Wall Street Journal).
- **China probes top leader.** Shanghai party chief Chen Jining, a
  member of China's elite Politburo, is under investigation, state
  news agency Xinhua said on Tuesday. Reported 24 November 2026
  (Reuters; Xinhua).
- **Lukashenko's pitch.** Belarusian President Alexander Lukashenko
  proposed in an interview published on Tuesday that he and Ukrainian
  President Volodymyr Zelensky fly together to Moscow for Kremlin
  talks to end the war. Reported 24 November 2026 (Reuters; Le Point).
- **Chess crown opens with a draw.** India's D Gukesh and
  Uzbekistan's Javokhir Sindarov drew Game 1 of the World Chess
  Championship in Geneva on Tuesday 24 November; the match score
  stands 0.5–0.5. Reported 24 November 2026 (World Chess; FIDE
  via ChessBase).

## Ticker

The strip along the bottom of the page carries the day's smaller
items, all reported on Tuesday 24 November 2026: alleged drug lord
Fausto Isidro Meza Flores, known as "Chapo Isidro", to be tried in
Mexico despite a US extradition request (Reuters); around 175 migrants
unaccounted for after contact was lost with a boat that left Dakar,
Senegal (Reuters); Salvadoran migrant Kilmar Abrego Garcia to leave
the US voluntarily, US media report (Reuters; CBS News); the Trump
administration set to unveil new tariffs after a probe of excess
factory capacity (Reuters); Bangladesh garment workers clashing with
police in pay protests (Reuters); Carlos Alcaraz winning his first ATP
Finals title, beating Alexander Zverev 6–2, 7–6(7) in Turin on Sunday
22 November (ATP Tour; Reuters); and Israel's Gadi Eisenkot clinching
a first coalition agreement in his bid to form a government (Reuters).

## What v2 deliberately left out

- **The Houthi strike on Riyadh's PIF Tower.** It happened on
  Thursday 19 November, not 24 November (Reuters, 19 November), so
  it is not on the page as the day's news.
- **COP31 ending without a deal.** The summit collapsed on Sunday
  22 November (UN News; Reuters), and the fallout stories ran on
  Monday 23 November.
- **The Gaza strikes.** The airstrikes that killed three people,
  including an UNRWA worker, took place on Monday 23 November
  (Reuters).
- **The "Chapo Isidro" capture itself.** The capture happened on
  Friday 20 November; only the decision to try him in Mexico is
  24 November news, and that is what the ticker carries.

## How the page was made

The front page was drawn as a single 1024 × 1024 image by
`build_image.py` (Pillow: every headline, label and caption placed at
an explicit size and position, so no text can come out garbled) and
ships in this repository as `entry.png`. The entry program `main.py`
copies that bundled image to the output directory unchanged, so the
judged output is exactly the image in the repository — byte for byte,
every run.
