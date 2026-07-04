from pypdf import PdfReader

path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\istorie 4.pdf"
reader = PdfReader(path)

def find_page_number(text):
    # Common patterns for page numbers at the start or end of text
    import re
    # Look for a standalone number at the very start or end of the page
    lines = text.strip().split('\n')
    if not lines: return None
    
    first_line = lines[0].strip()
    last_line = lines[-1].strip()
    
    for line in [first_line, last_line]:
        match = re.search(r'^\d+$', line)
        if match:
            return int(match.group())
    return None

print("--- Page Number Detection ---")
for i in range(20):
    text = reader.pages[i].extract_text()
    pn = find_page_number(text)
    print(f"Index {i}: Printed Page {pn} | Text snippet: {text.strip()[:50]}...")

mid = len(reader.pages) // 2
text_mid = reader.pages[mid].extract_text()
pn_mid = find_page_number(text_mid)
print(f"\nIndex {mid}: Printed Page {pn_mid} | Text snippet: {text_mid.strip()[:50]}...")
