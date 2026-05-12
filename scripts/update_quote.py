import random
from pathlib import Path

readme_path = Path("README.md")
quotes_path = Path("quotes.txt")

start_marker = "<!--QUOTE_START-->"
end_marker = "<!--QUOTE_END-->"

readme = readme_path.read_text(encoding="utf-8")
quotes = [
    quote.strip()
    for quote in quotes_path.read_text(encoding="utf-8").splitlines()
    if quote.strip()
]

selected_quote = random.choice(quotes)

new_section = f"{start_marker}\n> {selected_quote}\n{end_marker}"

start_index = readme.index(start_marker)
end_index = readme.index(end_marker) + len(end_marker)

updated_readme = readme[:start_index] + new_section + readme[end_index:]

readme_path.write_text(updated_readme, encoding="utf-8")
