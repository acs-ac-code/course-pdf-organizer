from pypdf import PdfReader

pdf_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\Mate-4_final.pdf"
reader = PdfReader(pdf_path)

# Based on previous inspection, Cuprins is on pages 4 and 5 of the final PDF
toc_pages = [3, 4] # 0-indexed indices for pages 4 and 5

print("--- TABLE OF CONTENTS ---")
for idx in toc_pages:
    if idx < len(reader.pages):
        page = reader.pages[idx]
        text = page.extract_text()
        print(text)
        print("\n--- Page Break ---\n")
