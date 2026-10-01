from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.dirname(os.path.abspath(__file__))
ICON_DIR = os.path.join(OUT, "icons")
os.makedirs(ICON_DIR, exist_ok=True)

LAVENDER = (155, 142, 196, 255)
LAVENDER_DARK = (99, 79, 145, 255)
WHITE = (255, 255, 255, 255)

def make_icon(size, maskable=False):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.08) if maskable else 0
    draw.rounded_rectangle(
        [pad, pad, size - pad, size - pad],
        radius=int(size * 0.22),
        fill=LAVENDER,
    )
    # simple heart-pulse style glyph using an emoji-like sparkle/heart shape
    cx, cy = size / 2, size / 2
    r = size * 0.16
    # heart made of two circles + triangle
    draw.ellipse([cx - r * 1.6, cy - r * 0.9, cx - r * 0.2, cy + r * 0.9], fill=WHITE)
    draw.ellipse([cx + r * 0.2, cy - r * 0.9, cx + r * 1.6, cy + r * 0.9], fill=WHITE)
    draw.polygon(
        [
            (cx - r * 1.5, cy + r * 0.3),
            (cx + r * 1.5, cy + r * 0.3),
            (cx, cy + r * 2.1),
        ],
        fill=WHITE,
    )
    return img

for size in [192, 512]:
    make_icon(size).save(os.path.join(ICON_DIR, f"icon-{size}.png"))
    make_icon(size, maskable=True).save(os.path.join(ICON_DIR, f"icon-{size}-maskable.png"))

# apple touch icon (180x180, no transparency, square)
apple = Image.new("RGBA", (180, 180), LAVENDER)
d = ImageDraw.Draw(apple)
cx, cy, r = 90, 90, 28
d.ellipse([cx - r * 1.6, cy - r * 0.9, cx - r * 0.2, cy + r * 0.9], fill=WHITE)
d.ellipse([cx + r * 0.2, cy - r * 0.9, cx + r * 1.6, cy + r * 0.9], fill=WHITE)
d.polygon([(cx - r * 1.5, cy + r * 0.3), (cx + r * 1.5, cy + r * 0.3), (cx, cy + r * 2.1)], fill=WHITE)
apple.convert("RGB").save(os.path.join(ICON_DIR, "apple-touch-icon.png"))

# favicon
make_icon(64).save(os.path.join(ICON_DIR, "favicon.png"))

print("Icons generated:", os.listdir(ICON_DIR))
