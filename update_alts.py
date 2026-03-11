import re
from pathlib import Path

file_path = Path(r"c:\Users\user\Downloads\new_files\demo-luxecart.html")
text = file_path.read_text(encoding='utf-8')

pattern = re.compile(
    r'(<img\s+alt=""\s+src="[^"]*"(?:\s+[^>]+)*>)(\s*</div>\s*<div class="ci-info">\s*<div class="ci-name">(.*?)</div>)', re.DOTALL)


def repl(m):
    img_tag = m.group(1)
    product_name = m.group(3)
    new_img = img_tag.replace('alt=""', f'alt="{product_name}"')
    return new_img + m.group(2)


new_text = pattern.sub(repl, text)

if new_text != text:
    file_path.write_text(new_text, encoding='utf-8')
    print("Updated alt attributes based on product names.")
else:
    print("No changes made.")
