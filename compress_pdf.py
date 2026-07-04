import pikepdf
import os

input_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\Mate-4.pdf"
output_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\Mate-4_compressed.pdf"

try:
    with pikepdf.open(input_path) as pdf:
        pdf.save(output_path, linearize=True)
    
    final_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Compression complete.")
    print(f"Original size: 206 MB")
    print(f"Compressed size: {final_size:.2f} MB")
    print(f"Saved as: {output_path}")

except Exception as e:
    print(f"Error during compression: {e}")
