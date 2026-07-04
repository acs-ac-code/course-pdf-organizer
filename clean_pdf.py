from pypdf import PdfReader, PdfWriter
import os

input_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\Mate-4_compressed.pdf"
output_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\Mate-4_final.pdf"

try:
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Start from index 2 (Actual Page 3) to remove the first two pages (Cover and Copyright)
    for i in range(2, len(reader.pages)):
        writer.add_page(reader.pages[i])

    with open(output_path, "wb") as f:
        writer.write(f)
    
    print(f"Successfully removed first 2 pages.")
    print(f"New PDF saved as: {output_path}")
    print(f"Total pages in new PDF: {len(writer.pages)}")

except Exception as e:
    print(f"Error during PDF cleaning: {e}")
