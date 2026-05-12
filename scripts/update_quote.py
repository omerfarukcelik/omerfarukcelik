import random
import json
import textwrap
from pathlib import Path

QUOTES_PATH = Path("quotes.txt")
THEMES_PATH = Path("data/themes.json")
SVG_PATH = Path("assets/quote.svg")

THEME_NAME = "tokyonight"

quotes = [line.strip() for line in QUOTES_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]

selected = random.choice(quotes)

if " — " in selected:
    quote, author = selected.split(" — ", 1)
else:
    quote, author = selected, "Unknown"

themes = json.loads(THEMES_PATH.read_text(encoding="utf-8"))
theme = themes[THEME_NAME]

wrapped_quote = textwrap.wrap(quote, width=48)

svg_lines = []
start_y = 85

for i, line in enumerate(wrapped_quote):
    svg_lines.append(
        f'<tspan x="70" y="{start_y + i * 45}">{line}</tspan>'
    )

author_y = start_y + len(wrapped_quote) * 55 + 25

svg = f'''<svg width="1000" height="300" viewBox="0 0 1000 300" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="1000" height="300" rx="18" fill="#{theme["background"]}"/>
  <text x="55" y="82" fill="#{theme["symbol"]}" font-size="40" font-family="Arial, Luminari" font-style="italic" font-weight="700">"</text>

  <text fill="#{theme["quote"]}" font-size="34" font-family="JetBrains Mono, Luminari" font-style="italic" font-weight="600">
    {"".join(svg_lines)}
  </text>

  <text x="800" y="{author_y}" text-anchor="end" fill="#{theme["author"]}" font-size="28" font-family="Space Grotesk, Luminari" font-weight="600">
    — {author}
  </text>
</svg>
'''

SVG_PATH.write_text(svg, encoding="utf-8")

print(f"Updated quote.svg with: {quote} — {author}")