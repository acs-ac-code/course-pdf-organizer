from pypdf import PdfReader

pdf_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\Mate-4_final.pdf"
reader = PdfReader(pdf_path)

# List of start pages from the TOC
pages_to_verify = [
    3, 4, 5, 6, 9, 10, 12, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 28, 29, 
    30, 31, 32, 33, 34, 36, 38, 40, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 
    54, 56, 57, 58, 60, 61, 62, 64, 66, 68, 70, 71, 72, 73, 74, 76, 78, 79, 80, 
    82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 95, 96, 98, 99, 100, 102, 104, 
    106, 107, 108, 109, 110, 112, 114, 115, 116, 117, 118, 119, 120, 122, 123, 
    124, 125, 126, 128, 129, 130, 131, 132, 134, 135, 136, 138, 140, 142, 143, 
    144, 145, 146, 148, 150, 151, 152, 153, 154, 156, 158, 160
]

print(f"{'Page':<6} | {'Actual Text Snippet'}")
print("-" * 50)

for p_num in pages_to_verify:
    if p_num <= len(reader.pages):
        # Index is p_num - 1
        text = reader.pages[p_num - 1].extract_text()
        # Get first 100 characters of the page to see the title
        snippet = text[:100].replace('\n', ' ') if text else "No text"
        print(f"{p_num:<6} | {snippet}")
    else:
        print(f"{p_num:<6} | Out of bounds")
