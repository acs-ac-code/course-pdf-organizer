from pypdf import PdfReader, PdfWriter
import os

input_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\STIINTE_4.pdf"
output_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\STIINTE_4_final.pdf"

reader = PdfReader(input_path)
writer = PdfWriter()

# Remove first 2 pages (Index 0 and 1)
# Printed Page 1 is at Index 2
for i in range(2, len(reader.pages)):
    writer.add_page(reader.pages[i])

with open(output_path, "wb") as f:
    writer.write(f)

print(f"Created synchronized PDF: {output_path}")

# Now extract TOC pages. 
# In the original, "Cuprins" (TOC) was Index 5 (Printed Page 4).
# In the final, it should be Index 3.
reader_final = PdfReader(output_path)
toc_pages = []
for i in range(3, 7): # Read a few pages starting from the TOC
    toc_pages.append(reader_final.pages[i].extract_text())

with open(r"C:\Users\Astrid\toc_extract.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(toc_pages):
        f.write(f"--- Page {i+4} ---\n{text}\n\n")

print("Extracted TOC to toc_extract.txt")
