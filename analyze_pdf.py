from pypdf import PdfReader
import os

path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\STIINTE_4.pdf"
reader = PdfReader(path)
total_pages = len(reader.pages)

def get_text(page_idx):
    try:
        return reader.pages[page_idx].extract_text()
    except Exception as e:
        return f"Error: {e}"

print("--- First 20 Pages Analysis ---")
for i in range(min(20, total_pages)):
    text = get_text(i)
    clean_text = text.strip()[:200].replace('\n', ' ')
    print(f"Index {i}: {clean_text}")

mid = total_pages // 2
mid_text = get_text(mid).strip()[:200].replace('\n', ' ')
print(f"\n--- Middle Page Analysis (Index {mid}) ---\nText: {mid_text}")
