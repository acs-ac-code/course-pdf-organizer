from pypdf import PdfReader, PdfWriter
import os

input_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\LLR4_final.pdf"
output_dir = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\LLR4_Split"

reader = PdfReader(input_path)

def save_range(start_page, end_page, filename):
    writer = PdfWriter()
    for i in range(start_page - 1, end_page):
        if i < len(reader.pages):
            writer.add_page(reader.pages[i])
    with open(os.path.join(output_dir, filename), "wb") as f:
        writer.write(f)
    print(f"Saved: {filename} (Pages {start_page}-{end_page})")

# Requested Corrections
corrections = [
    (18, 18, "U1_L4_Comunicare.pdf"),
    (19, 19, "U1_L5_Scrierea_creativa.pdf"),
    (20, 22, "U1_Recapitulare_Evaluare.pdf"),
    (41, 44, "U2_Recapitulare_Evaluare.pdf"),
    (65, 68, "U3_Recapitulare_Evaluare.pdf"),
    (78, 78, "U4_L4_Organizarea_informatiilor.pdf"),
    (79, 79, "U4_L5_Pronumele_personal_de_politețe.pdf"),
    (80, 84, "U4_Recapitulare_Evaluare.pdf"),
    (102, 106, "U5_Recapitulare_Evaluare.pdf"),
    (113, 113, "U6_L3_Cuvântul_parte_de_propoziție.pdf"),
    (114, 115, "U6_L4_Subiectul.pdf"),
    (116, 117, "U6_L5_Predicatul.pdf"),
    (118, 119, "U6_L6_Relatia_subiect_predicat.pdf"),
    (120, 124, "U6_Recapitulare_Evaluare.pdf"),
    (136, 136, "U7_L4_Organizarea_unei_drumeții.pdf"),
    (137, 142, "U7_Recapitulare_Evaluare.pdf"),
    (152, 155, "U8_L4_Caracatița.pdf"),
    (156, 158, "U8_Recapitulare_Evaluare.pdf"),
    (160, 160, "Raspunsuri_teste_evaluare.pdf"),
]

for start, end, name in corrections:
    save_range(start, end, name)
