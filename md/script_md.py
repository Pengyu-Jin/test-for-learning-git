import os
from pathlib import Path

SOURCE_DIR = "md"
OUTPUT_DIR = "docs"
CSS_LINK = "<link rel='stylesheet' href='.\style.css'>"
WRAPPED_DIV_START = '<div class="crossnote markdown-preview">'
WRAPPED_DIV_END = '</div>'

def process_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("<style>", f"{CSS_LINK}\n<style>")
    content = content.replace('<div class="crossnote markdown-preview  ">', f'<div class="crossnote markdown-preview  "\n{WRAPPED_DIV_START}>')
    content = content.replace('</div>', f'{WRAPPED_DIV_END}\n</div>')

    output_path = Path(OUTPUT_DIR) / "index.html"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.lower().endswith(".html"):
                process_html_file(os.path.join(root, file))

if __name__ == "__main__":
    main()