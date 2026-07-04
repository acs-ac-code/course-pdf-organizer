from pypdf import PdfReader, PdfWriter
import os

input_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\STIINTE_4_final.pdf"
output_dir = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\STIINTE_4_Split"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

reader = PdfReader(input_path)

def save_range(start_page, end_page, filename):
    # start_page and end_page are 1-indexed
    writer = PdfWriter()
    # pypdf is 0-indexed
    for i in range(start_page - 1, end_page):
        if i < len(reader.pages):
            writer.add_page(reader.pages[i])
    
    with open(os.path.join(output_dir, filename), "wb") as f:
        writer.write(f)
    print(f"Saved: {filename} (Pages {start_page}-{end_page})")

# General Intro
save_range(1, 7, "U0_Intro_Orientation.pdf")

# Unit 1
save_range(7, 7, "U1_Intro_Parinti_si_Urmasi.pdf")
save_range(8, 9, "U1_L1_Cicluri_de_viata_la_plante.pdf")
save_range(10, 11, "U1_L2_Cicluri_de_viata_la_insecte.pdf")
save_range(12, 13, "U1_L3_Cicluri_de_viata_la_pesti_si_amfibieni.pdf")
save_range(14, 15, "U1_L4_Cicluri_de_viata_la_reptile_si_pasari.pdf")
save_range(16, 17, "U1_L5_Cicluri_de_viata_la_mamifere.pdf")
save_range(18, 19, "U1_L6_Ciclul_de_viata_la_om.pdf")
save_range(20, 25, "U1_Recapitulare.pdf")

# Unit 2
save_range(26, 29, "U2_L1_Padurea.pdf")
save_range(30, 33, "U2_L2_Pajistea.pdf")
save_range(34, 37, "U2_L3_Raul.pdf")
save_range(38, 41, "U2_L4_Desertul.pdf")
save_range(42, 45, "U2_L5_Mari_si_oceane.pdf")
save_range(46, 51, "U2_Recapitulare.pdf")

# Unit 3
save_range(52, 55, "U3_L1_Lanturi_trofice.pdf")
save_range(56, 59, "U3_L2_Dieta_echilibrata_Miscare.pdf")
save_range(60, 65, "U3_Recapitulare.pdf")

# Unit 4
save_range(66, 69, "U4_L1_Pamantul_in_Sistemul_Solar.pdf")
save_range(70, 73, "U4_L2_Fosilele.pdf")
save_range(74, 75, "U4_L3_Omul_si_mediul_de_viata.pdf")
save_range(76, 81, "U4_Recapitulare.pdf")

# Unit 5
save_range(82, 83, "U5_L1_Plutirea_corpurilor_in_apa.pdf")
save_range(84, 85, "U5_L2_Amestecuri.pdf")
save_range(86, 89, "U5_L3_Dizolvarea.pdf")
save_range(90, 91, "U5_L4_Apa_proprietati_si_utilizari.pdf")
save_range(92, 95, "U5_L5_Transformari_ale_materiei.pdf")
save_range(96, 101, "U5_Recapitulare.pdf")

# Unit 6
save_range(102, 105, "U6_L1_Transfer_de_caldura.pdf")
save_range(106, 109, "U6_L2_Circuitul_electric.pdf")
save_range(110, 113, "U6_L3_Lumina.pdf")
save_range(114, 117, "U6_Recapitulare.pdf")

# Final
save_range(118, len(reader.pages), "U6_Recapitulare_Finala.pdf")
