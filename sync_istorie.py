from pypdf import PdfReader, PdfWriter

input_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\istorie 4.pdf"
output_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\istorie_4_final.pdf"

reader = PdfReader(input_path)
writer = PdfWriter()

# Printed Page 3 is Index 4. 
# Printed Page 1 must be Index 2.
# Offset: Index 2 is Printed Page 1.
# We remove Index 0 and 1.
for i in range(2, len(reader.pages)):
    writer.add_page(reader.pages[i])

with open(output_path, "wb") as f:
    writer.write(f)

print(f"Created synchronized PDF: {output_path}")

# Now extract TOC pages for analysis
reader_final = PdfReader(output_path)
toc_pages = []
# TOC usually starts early. Let's take first 10 pages of final.
for i in range(min(10, len(reader_final.pages))):
    toc_pages.append(reader_final.pages[i].extract_text())

with open(r"C:\Users\Astrid\toc_istorie.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(toc_pages):
        f.write(f"--- Page {i+1} ---\n{text}\n\n")

print("Extracted TOC to toc_istorie.txt")
