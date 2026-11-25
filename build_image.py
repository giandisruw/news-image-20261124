#!/usr/bin/env python3
"""Draw the v2 front page for news-image-20261124 and save entry.png.

Everything is drawn with Pillow primitives and real fonts, so no text can
come out garbled: every headline, label and caption is placed by this
script at an explicit size and position. The finished image is a
1024 x 1024 newspaper front page, "THE WORLD", Tuesday 24 November 2026.

Run:  python3 build_image.py
Writes: entry.png  (next to this script)
"""

import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 36
RIGHT = W - MARGIN

PAPER = (248, 244, 233)      # newsprint off-white
PANEL = (236, 227, 200)      # lead panel background
LAND = (236, 227, 200)       # map land
LAND_POLAND = (217, 203, 160)
SEA = (195, 206, 208)
INK = (20, 20, 20)
GREY = (90, 86, 74)
RED = (163, 18, 18)
DARK = (32, 36, 42)          # AWACS silhouette

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_IT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, text, fnt):
    return draw.textlength(text, font=fnt)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if text_w(draw, trial, fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def centered(draw, cx, y, text, fnt, fill=INK):
    draw.text((cx, y), text, font=fnt, fill=fill, anchor="ma")


def left(draw, x, y, text, fnt, fill=INK):
    draw.text((x, y), text, font=fnt, fill=fill, anchor="la")


def fit_size(draw, text, path, start, max_w):
    """Largest font size (<= start) at which text fits max_w."""
    size = start
    while size > 10 and text_w(draw, text, font(path, size)) > max_w:
        size -= 2
    return size


def draw_awacs(draw, x0, y0, scale=0.85):
    """Side-view AWACS silhouette (facing right), drawn from polygons."""
    def pt(x, y):
        return (x0 + x * scale, y0 + y * scale)

    def poly(points, fill):
        draw.polygon([pt(x, y) for x, y in points], fill=fill)

    # tail fin
    poly([(18, 44), (52, 44), (44, 10), (26, 10)], DARK)
    # tailplane
    poly([(12, 68), (58, 68), (38, 94), (18, 94)], DARK)
    # fuselage: long hexagon, pointed nose right, tail left
    poly([(8, 52), (20, 42), (300, 42), (340, 48), (360, 57),
          (340, 66), (300, 72), (20, 72), (8, 62)], DARK)
    # radar dome on its pylon
    draw.rectangle([pt(150, 30)[0], pt(150, 30)[1],
                    pt(162, 44)[0], pt(162, 44)[1]], fill=DARK)
    draw.ellipse([pt(108, 12)[0], pt(108, 12)[1],
                  pt(212, 34)[0], pt(212, 34)[1]], fill=DARK)
    # main wing, swept back toward the tail, below the fuselage
    poly([(150, 70), (235, 70), (190, 108), (135, 108)], (44, 49, 58))
    # engines under the wing
    draw.ellipse([pt(150, 96)[0], pt(150, 96)[1],
                  pt(178, 106)[0], pt(178, 106)[1]], fill=DARK)
    draw.ellipse([pt(190, 92)[0], pt(190, 92)[1],
                  pt(218, 102)[0], pt(218, 102)[1]], fill=DARK)
    # cockpit windows
    poly([(318, 48), (338, 48), (330, 56), (318, 56)], PAPER)


def dashed_line(draw, points, fill, width=3, dash=9, gap=6):
    """Polyline drawn as dashes."""
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        dx, dy = x2 - x1, y2 - y1
        length = (dx * dx + dy * dy) ** 0.5
        if length == 0:
            continue
        ux, uy = dx / length, dy / length
        dist = 0.0
        while dist < length:
            seg = min(dash, length - dist)
            ax, ay = x1 + ux * dist, y1 + uy * dist
            bx, by = x1 + ux * (dist + seg), y1 + uy * (dist + seg)
            draw.line([(ax, ay), (bx, by)], fill=fill, width=width)
            dist += dash + gap


def star(draw, cx, cy, r, fill):
    """Eight-point asterisk star."""
    for angle in range(0, 180, 45):
        import math
        rad = math.radians(angle)
        dx, dy = math.cos(rad) * r, math.sin(rad) * r
        draw.line([(cx - dx, cy - dy), (cx + dx, cy + dy)],
                  fill=fill, width=4)
    draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=fill)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- outer frame -------------------------------------------------
    d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=3)

    # ---- masthead ----------------------------------------------------
    mast_size = fit_size(d, "THE WORLD", SERIF, 150, RIGHT - MARGIN)
    centered(d, W // 2, 14, "THE WORLD", font(SERIF, mast_size))

    # ---- dateline ----------------------------------------------------
    d.line([(MARGIN, 184), (RIGHT, 184)], fill=INK, width=1)
    date_font = font(SANS, 20)
    date_text = "TUESDAY 24 NOVEMBER 2026  —  ONE DAY, ONE PAGE"
    centered(d, W // 2, 192, date_text, date_font)
    d.line([(MARGIN, 222), (RIGHT, 222)], fill=INK, width=4)
    d.line([(MARGIN, 230), (RIGHT, 230)], fill=INK, width=1)

    # ---- lead headline ----------------------------------------------
    head_size = fit_size(d, "RUSSIA BREACHES", SERIF, 96, RIGHT - MARGIN)
    head_font = font(SERIF, head_size)
    centered(d, W // 2, 238, "RUSSIA BREACHES", head_font)
    centered(d, W // 2, 330, "POLAND AGAIN", head_font)

    # ---- deck (two centred lines) ------------------------------------
    deck_font = font(SERIF_IT, 25)
    centered(d, W // 2, 428,
             "A Russian drone crosses NATO airspace overnight — the second",
             deck_font)
    centered(d, W // 2, 460,
             "incursion in four days — as Warsaw demands US troops",
             deck_font)

    # ---- lead row ----------------------------------------------------
    # Left: map panel (x 36..706), right: three-story rail (x 722..988).
    panel_top, panel_bottom = 500, 764
    d.rectangle([MARGIN, panel_top, 706, panel_bottom],
                fill=PANEL, outline=INK, width=3)

    # sky band with the AWACS silhouette
    draw_awacs(d, 64, 502, scale=0.85)
    sans20 = font(SANS, 20)
    left(d, 400, 524, "NATO AWACS — E-3A SENTRY", sans20)
    left(d, 400, 552, "NATO's eyes in the sky", font(SERIF_IT, 18))

    # sea strip
    d.rectangle([MARGIN + 3, 596, 703, 622], fill=SEA)
    left(d, 60, 600, "BALTIC SEA", font(SANS, 15), fill=GREY)

    # land
    d.rectangle([MARGIN + 3, 622, 703, panel_bottom - 3], fill=LAND)
    # Poland, slightly darker, with a heavy outline
    poland = [(180, 654), (300, 636), (400, 646), (430, 674),
              (410, 719), (350, 744), (260, 746), (200, 722), (172, 686)]
    d.polygon(poland, fill=LAND_POLAND, outline=(42, 42, 42), width=3)
    # schematic neighbour borders
    border = (138, 130, 112)
    d.line([(445, 626), (460, 694), (445, 761)], fill=border, width=2)
    d.line([(605, 626), (625, 699), (610, 761)], fill=border, width=2)
    d.line([(445, 694), (605, 699)], fill=border, width=2)
    d.line([(120, 622), (140, 761)], fill=border, width=2)
    # country labels — few, and large
    centered(d, 310, 662, "POLAND", font(SERIF, 27))
    left(d, 70, 700, "GERMANY", font(SANS, 15), fill=GREY)
    left(d, 500, 648, "BELARUS", font(SANS, 14), fill=GREY)
    left(d, 520, 726, "UKRAINE", font(SANS, 16), fill=GREY)
    left(d, 636, 646, "RUSSIA", font(SANS, 15), fill=GREY)

    # drone track: dashed red arc from the east into Poland
    track = [(688, 724), (600, 696), (500, 676), (420, 679),
             (330, 695), (272, 716)]
    dashed_line(d, track, RED, width=3)
    d.ellipse([684, 720, 692, 728], fill=RED)
    star(d, 272, 716, 13, RED)
    left(d, 356, 706, "DRONE INCURSION", font(SANS, 15), fill=RED)
    left(d, 356, 726, "OVERNIGHT 24 NOV", font(SANS, 13), fill=RED)

    # caption under the panel
    cap_font = font(SERIF_IT, 20)
    left(d, MARGIN, 774,
         "NATO's AWACS radar jets head for Poland after a Russian drone", cap_font)
    left(d, MARGIN, 800,
         "crossed allied airspace overnight.", cap_font)

    # ---- right rail: three stories -----------------------------------
    rail_x = 722
    rail_w = RIGHT - rail_x
    head_f = font(SERIF, 23)
    body_f = font(SERIF_REG, 16)
    stories = [
        ("26 DEAD IN JAVA",
         "FACTORY FIRE",
         "Toll confirmed on Tuesday as police open a criminal probe."),
        ("HUANG'S BACK —",
         "NVIDIA SOARS 31%",
         "Board reinstates its founder as CEO; shares jump 31%."),
        ("UKRAINE SINKS",
         "RUSSIAN WARSHIP",
         "Kyiv says sea drones sank the corvette Merkury at Benghazi."),
    ]
    y = 500
    for i, (h1, h2, body) in enumerate(stories):
        left(d, rail_x, y, h1, head_f)
        left(d, rail_x, y + 26, h2, head_f)
        for j, line in enumerate(wrap(d, body, body_f, rail_w)):
            left(d, rail_x, y + 58 + j * 19, line, body_f)
        y += 108
        if i < 2:
            d.line([(rail_x, y - 8), (RIGHT, y - 8)], fill=INK, width=1)

    # ---- middle row: China | Lukashenko | Sport ----------------------
    mid_top = 836
    d.line([(360, mid_top + 4), (360, 944)], fill=INK, width=1)
    d.line([(676, mid_top + 4), (676, 944)], fill=INK, width=1)

    mid_head = font(SERIF, 23)
    mid_body = font(SERIF_REG, 17)
    left(d, MARGIN, mid_top, "CHINA PROBES TOP LEADER", mid_head)
    china = ("Shanghai party chief Chen Jining, a Politburo member, "
             "is under investigation, Xinhua says.")
    for j, line in enumerate(wrap(d, china, mid_body, 308)):
        left(d, MARGIN, mid_top + 32 + j * 21, line, mid_body)

    left(d, 376, mid_top, "LUKASHENKO'S PITCH", font(SERIF, 22))
    luka = ("Belarus leader proposes flying to Kremlin talks together "
            "with Ukraine's Zelensky.")
    for j, line in enumerate(wrap(d, luka, mid_body, 284)):
        left(d, 376, mid_top + 32 + j * 21, line, mid_body)

    # sport box
    d.rectangle([692, mid_top, RIGHT, 944], outline=INK, width=2)
    d.rectangle([692, mid_top, RIGHT, mid_top + 28], fill=INK)
    centered(d, (692 + RIGHT) // 2, mid_top + 2, "SPORT",
             font(SANS, 20), fill=PAPER)
    sport_head = font(SERIF, 21)
    centered(d, (692 + RIGHT) // 2, mid_top + 34, "CHESS CROWN OPENS", sport_head)
    centered(d, (692 + RIGHT) // 2, mid_top + 58, "WITH A DRAW", sport_head)
    centered(d, (692 + RIGHT) // 2, mid_top + 88,
             "Gukesh v Sindarov, Game 1 drawn.", font(SERIF_REG, 16))

    # ---- ticker ------------------------------------------------------
    d.rectangle([MARGIN, 954, RIGHT, 1010], fill=INK)
    tick_font = font(SANS_REG, 15)
    items = [
        "Chapo Isidro to face trial in Mexico",
        "About 175 migrants unaccounted for off Senegal",
        "Abrego Garcia to leave the US voluntarily",
        "Trump set to unveil new tariffs",
        "Bangladesh garment workers clash with police",
        "Alcaraz wins his first ATP Finals title in Turin",
        "Eisenkot clinches first coalition deal in Israel",
    ]
    tick_text = "ALSO:  " + "   •   ".join(items)
    tick_lines = wrap(d, tick_text, tick_font, RIGHT - MARGIN - 24)
    for j, line in enumerate(tick_lines[:3]):
        centered(d, W // 2, 957 + j * 19, line, tick_font, fill=PAPER)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    data = open(out, "rb").read()
    print(f"wrote {out}")
    print(f"size: {len(data)} bytes (limit 1048576)")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    print(f"dimensions: {img.size}")


if __name__ == "__main__":
    main()
