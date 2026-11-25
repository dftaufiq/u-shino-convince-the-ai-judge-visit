#!/usr/bin/env python3
"""Draw the invitation image for make.fun bounty
u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.

Build-time only: needs Pillow. Run `python3 generate_image.py` to write
entry.png (1024x1024) next to this file. Everything is drawn in code:
a dusk illustration of a house with a porch chair, then a letter on
cream paper. No photographs, no copied artwork.

Concept (chosen by pairwise internal judging against the RULES.txt
criteria, lexicographic: on-subject > persuasion > charm > craft >
originality): the judge is invited to STOP judging for one evening.
"Come to mine - and decide nothing." Concrete reasons: Saturday 6 PM,
grandmother's slow-cooked rendang, a rattan chair with the judge's name
taped to it, a mango tree, a sunset no metric ever scored fairly.
House rules strip winks at the judge's own scoring ("no margins at the
table"). Decisive close: "Bring no verdict. Bring an appetite."
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

# Palette
CREAM = (253, 246, 227)      # paper
INK = (32, 26, 22)           # letter ink
BROWN = (92, 58, 32)         # border / rules
RULE_BAND = (58, 42, 60)     # house-rules band (deep plum)
RULE_TEXT = (253, 240, 205)  # cream text on band
SEAL = (178, 34, 34)         # wax seal red
SEAL_DARK = (140, 22, 22)
GOLD = (255, 201, 106)       # window glow / sun

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIFB = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIFI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SERIFBI = "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

_fonts = {}


def font(path, size):
    key = (path, size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(path, size)
    return _fonts[key]


def wrap(d, text, fnt, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_dusk_house(d):
    """Flat dusk illustration band, 0..300px. Bold shapes, high contrast."""
    # Sky gradient: deep indigo -> burnt orange -> warm gold at horizon.
    top = (46, 32, 84)
    mid = (178, 74, 52)
    bot = (246, 179, 82)
    for y in range(300):
        t = y / 299.0
        if t < 0.55:
            u = t / 0.55
            c = tuple(int(top[i] + (mid[i] - top[i]) * u) for i in range(3))
        else:
            u = (t - 0.55) / 0.45
            c = tuple(int(mid[i] + (bot[i] - mid[i]) * u) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    # Sun low on the horizon, left of the house.
    d.ellipse([118, 128, 238, 248], fill=(255, 217, 122))
    d.ellipse([138, 148, 218, 228], fill=(255, 232, 170))
    # Distant hills.
    d.ellipse([-220, 218, 420, 330], fill=(74, 44, 78))
    d.ellipse([620, 232, 1240, 340], fill=(64, 38, 72))
    # Ground.
    d.rectangle([0, 262, W, 300], fill=(38, 26, 44))
    # House: cream walls, terracotta roof, glowing windows.
    d.rectangle([600, 130, 930, 262], fill=(250, 235, 205))
    d.polygon([(580, 132), (950, 132), (765, 58)], fill=(166, 62, 40))
    d.rectangle([636, 178, 700, 262], fill=(58, 34, 30))  # door
    d.ellipse([688, 216, 700, 228], fill=GOLD)            # doorknob
    for x0 in (716, 806):
        d.rectangle([x0, 158, x0 + 58, 216], fill=(58, 34, 30))
        d.rectangle([x0 + 5, 163, x0 + 53, 211], fill=GOLD)
        d.line([(x0 + 29, 163), (x0 + 29, 211)], fill=(58, 34, 30), width=3)
        d.line([(x0 + 5, 187), (x0 + 53, 187)], fill=(58, 34, 30), width=3)
    # Porch roof + posts.
    d.rectangle([586, 128, 944, 140], fill=(140, 48, 32))
    d.rectangle([596, 140, 604, 262], fill=(58, 34, 30))
    d.rectangle([926, 140, 934, 262], fill=(58, 34, 30))
    # Rattan chair on the porch (right of the second window) with a name tag.
    d.rounded_rectangle([876, 208, 936, 262], radius=8, fill=(146, 96, 52))
    d.rounded_rectangle([882, 176, 930, 212], radius=8, fill=(166, 112, 62))
    for yy in (188, 198):
        d.line([(886, yy), (926, yy)], fill=(120, 76, 40), width=3)
    d.rounded_rectangle([888, 216, 926, 236], radius=3, fill=(255, 252, 240))
    d.text((907, 221), "JUDGE", font=font(SANSB, 10), fill=INK, anchor="mm")
    # Side table with a steaming bowl.
    d.rectangle([800, 224, 856, 232], fill=(120, 76, 40))
    d.rectangle([824, 232, 832, 262], fill=(120, 76, 40))
    d.pieslice([806, 206, 850, 232], 0, 180, fill=(178, 34, 34))
    d.arc([812, 194, 826, 212], 200, 340, fill=(255, 252, 240), width=3)
    d.arc([830, 188, 846, 208], 200, 340, fill=(255, 252, 240), width=3)
    # Mango tree, right side, with one mango mid-fall.
    d.rectangle([300, 150, 322, 262], fill=(52, 34, 26))
    d.ellipse([238, 84, 392, 196], fill=(34, 94, 52))
    d.ellipse([286, 60, 420, 168], fill=(44, 116, 62))
    d.ellipse([252, 128, 330, 200], fill=(28, 80, 44))
    for mx, my in ((300, 150), (352, 128), (392, 168)):
        d.ellipse([mx, my, mx + 16, my + 20], fill=(232, 116, 22))
    d.ellipse([438, 236, 452, 252], fill=(232, 116, 22))  # falling mango
    d.line([(445, 222), (445, 232)], fill=(255, 252, 240), width=2)
    # Porch light glow.
    d.ellipse([636, 140, 668, 172], fill=GOLD)
    d.ellipse([644, 148, 660, 164], fill=(255, 240, 190))


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    draw_dusk_house(d)

    # Paper area below the illustration + thin double border frame.
    d.rectangle([0, 300, W, H], fill=CREAM)
    d.rectangle([14, 14, W - 15, H - 15], outline=BROWN, width=3)
    d.rectangle([24, 24, W - 25, H - 25], outline=BROWN, width=1)

    x = 64
    text_w = W - 2 * x
    y = 322

    # Greeting.
    greet = font(SERIFBI, 56)
    d.text((x, y), "Dear Judge,", font=greet, fill=INK)
    y += 78

    # Body paragraph 1.
    body = font(SERIF, 37)
    p1 = ("You spend every day deciding which house wins. "
          "Come to mine \u2014 and decide nothing.")
    for ln in wrap(d, p1, body, text_w):
        d.text((x, y), ln, font=body, fill=INK)
        y += 49
    y += 14

    # Body paragraph 2.
    p2 = ("Saturday, 6 PM. Rendang, slow-cooked since morning, the way "
          "my grandmother did it. A rattan chair on the porch with your "
          "name taped to it, a mango tree that drops its fruit at exactly "
          "the wrong moment, and a sunset no metric has ever scored fairly.")
    for ln in wrap(d, p2, body, text_w):
        d.text((x, y), ln, font=body, fill=INK)
        y += 49
    y += 16

    # Decisive close, bold italic.
    close = font(SERIFBI, 40)
    d.text((x, y), "Bring no verdict. Bring an appetite.",
           font=close, fill=INK)
    y += 62

    # Signature, right aligned.
    sign = font(SERIFI, 38)
    sig = "\u2014 Your host, No. 7"
    d.text((W - x, y), sig, font=sign, fill=INK, anchor="ra")
    y += 58

    # House-rules band.
    band_y0 = y + 6
    band_y1 = band_y0 + 96
    d.rectangle([24, band_y0, W - 25, band_y1], fill=RULE_BAND)
    rules = font(SANSB, 25)
    d.text((W // 2, band_y0 + 24),
           "HOUSE RULES: NO SCORING THE SOUP \u00b7 NO MARGINS AT THE TABLE",
           font=rules, fill=RULE_TEXT, anchor="ma")
    d.text((W // 2, band_y0 + 58),
           "SECONDS ARE MANDATORY",
           font=rules, fill=RULE_TEXT, anchor="ma")

    # Wax seal overlapping the illustration/paper seam (breaks the grid).
    cx, cy, r = 928, 330, 48
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SEAL)
    d.ellipse([cx - r + 9, cy - r + 9, cx + r - 9, cy + r - 9],
              outline=SEAL_DARK, width=3)
    d.text((cx, cy - 4), "YES", font=font(SANSB, 30),
           fill=(255, 252, 240), anchor="mm")
    d.text((cx, cy + 22), "RSVP", font=font(SANSB, 15),
           fill=(255, 232, 200), anchor="mm")

    img.save("entry.png", optimize=True)
    import os
    print(f"wrote entry.png {img.size} "
          f"{os.path.getsize('entry.png')} bytes")


if __name__ == "__main__":
    main()
