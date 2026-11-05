from PIL import Image
import os

OUT = os.path.dirname(os.path.abspath(__file__))
ICON_DIR = os.path.join(OUT, "icons")
os.makedirs(ICON_DIR, exist_ok=True)

LOGO_PATH = r"C:\Users\shire\.copilot\attachments\8e082be7-1b9f-4ace-8b7d-47469c5ed613-Main_logo_standalone.png"
BRAND_BG = (37, 26, 51, 255)  # deep purple, matches lavender-800 family

logo = Image.open(LOGO_PATH).convert("RGBA")

def make_standard(size):
    """Transparent background, logo fills most of the square (used for favicon/app icon)."""
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    resized = logo.resize((size, size), Image.LANCZOS)
    canvas.paste(resized, (0, 0), resized)
    return canvas

def make_maskable(size):
    """Solid background + logo scaled down so it survives OS icon masking/cropping."""
    canvas = Image.new("RGBA", (size, size), BRAND_BG)
    safe = int(size * 0.72)  # keep within the ~80% safe zone recommended for maskable icons
    resized = logo.resize((safe, safe), Image.LANCZOS)
    offset = ((size - safe) // 2, (size - safe) // 2)
    canvas.paste(resized, offset, resized)
    return canvas

for size in [192, 512]:
    make_standard(size).save(os.path.join(ICON_DIR, f"icon-{size}.png"))
    make_maskable(size).save(os.path.join(ICON_DIR, f"icon-{size}-maskable.png"))

# Apple touch icon: no alpha support, so flatten onto the brand background, 180x180
apple_canvas = Image.new("RGBA", (180, 180), BRAND_BG)
apple_safe = int(180 * 0.8)
apple_logo = logo.resize((apple_safe, apple_safe), Image.LANCZOS)
apple_offset = ((180 - apple_safe) // 2, (180 - apple_safe) // 2)
apple_canvas.paste(apple_logo, apple_offset, apple_logo)
apple_canvas.convert("RGB").save(os.path.join(ICON_DIR, "apple-touch-icon.png"))

# Favicon (transparent, small)
make_standard(64).save(os.path.join(ICON_DIR, "favicon.png"))

# In-app header logo (small, transparent, moderate resolution for crispness on retina)
make_standard(128).save(os.path.join(ICON_DIR, "logo.png"))

print("Icons regenerated from brand logo:", sorted(os.listdir(ICON_DIR)))
