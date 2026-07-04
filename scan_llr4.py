from pypdf import PdfReader
import re

path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\LLR4_final.pdf"
reader = PdfReader(path)

findings = []

for i in range(len(reader.pages)):
    text = reader.pages[i].extract_text()
    if not text:
        continue
    
    # Look for "Unitatea X"
    unit_match = re.search(r'Unitatea\s+(\d+)', text, re.IGNORECASE)
    if unit_match:
        findings.append(f"Page {i+1}: Unit {unit_match.group(1)}")
    
    # Look for "Lecția X"
    lesson_match = re.search(r'Lecția\s+(\d+)', text, re.IGNORECASE)
    if lesson_match:
        lesson_num = lesson_match.group(1)
        snippet = text.strip()[:100]
        snippet_clean = snippet.replace('\n', ' ')
        findings.append(f"Page {i+1}: Lesson {lesson_num} - {snippet_clean}")

    # Look for "Recapitulare" or "Test"
    if "Recapitulare" in text:
        findings.append(f"Page {i+1}: Recapitulare found")
    if "Test de evaluare" in text:
        findings.append(f"Page {i+1}: Test found")

with open(r"C:\Users\Astrid\llr4_structure_scan.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(findings))

print("Scan complete. Results in llr4_structure_scan.txt")
