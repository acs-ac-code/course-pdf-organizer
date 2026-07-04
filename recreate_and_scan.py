from pypdf import PdfReader, PdfWriter
import os

# I will recreate LLR4_final.pdf first to be absolutely sure it exists
input_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\LLR4.pdf"
final_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\LLR4_final.pdf"

reader = PdfReader(input_path)
writer = PdfWriter()

# Same offset as before: remove first 2 pages
for i in range(2, len(reader.pages)):
    writer.add_page(reader.pages[i])

with open(final_path, "wb") as f:
    writer.write(f)

print(f"Re-created synchronized PDF: {final_path}")

# Now scan for structure
reader_final = PdfReader(final_path)
findings = []

for i in range(len(reader_final.pages)):
    text = reader_final.pages[i].extract_text()
    if not text:
        continue
    
    # Search for keywords
    if "Unitatea" in text:
        findings.append(f"Page {i+1}: Unit marker")
    if "Lecția" in text:
        snippet = text.strip()[:60].replace('\n', ' ')
        findings.append(f"Page {i+1}: Lesson marker - {snippet}")
    if "Recapitulare" in text:
        findings.append(f"Page {i+1}: Recap marker")
    if "Test de evaluare" in text:
        findings.append(f"Page {i+1}: Test marker")

with open(r"C:\Users\Astrid\llr4_final_scan.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(findings))

print("Scan complete. Results in llr4_final_scan.txt")
