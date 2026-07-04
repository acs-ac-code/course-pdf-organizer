from pypdf import PdfReader, PdfWriter
import os

input_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\LLR4_final.pdf"
output_dir = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\LLR4_Split"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

reader = PdfReader(input_path)

def save_range(start_page, end_page, filename):
    writer = PdfWriter()
    for i in range(start_page - 1, end_page):
        if i < len(reader.pages):
            writer.add_page(reader.pages[i])
    
    with open(os.path.join(output_dir, filename), "wb") as f:
        writer.write(f)
    print(f"Saved: {filename} (Pages {start_page}-{end_page})")

# General Intro (Pages 1-11)
save_range(1, 11, "U0_Intro_Orientation.pdf")

# Unit 1: POVEȘTI DE TOAMNĂ
save_range(11, 11, "U1_Intro_Povesti_de_Toamna.pdf")
save_range(12, 14, "U1_L1_Ce_le_spun_cocorilor.pdf")
save_range(15, 17, "U1_L2_Sensul_cuvintelor.pdf")
save_range(18, 19, "U1_L3_In_biblioteca_scolii.pdf")
save_range(20, 21, "U1_L4_Comunicare.pdf")
save_range(22, 23, "U1_L5_Scrierea_creativa.pdf")
save_range(24, 25, "U1_Recapitulare_Initiala.pdf") #Approx based on TOC

# Unit 2: ÎMPREUNĂ CU CEILALȚI
save_range(23, 23, "U2_Intro_Impreuna_cu_Ceilalti.pdf")
save_range(24, 27, "U2_L1_Fii_tu_insuti.pdf")
save_range(28, 31, "U2_L2_O_calatorie_spre_tarile_calde.pdf")
save_range(32, 33, "U2_L3_Substantivul_Furtuna_frunzelor.pdf")
save_range(34, 36, "U2_L4_Satul_global.pdf")
save_range(37, 37, "U2_L5_Relatarea_unei_intamplari.pdf")
save_range(38, 40, "U2_L6_Cum_comunicam.pdf")
save_range(41, 41, "U2_Recapitulare.pdf")
save_range(42, 43, "U2_Test_evaluare.pdf")

# Unit 3: DORINȚE ÎMPLINITE
save_range(45, 45, "U3_Intro_Dorinte_Implinite.pdf")
save_range(46, 48, "U3_L1_Aventurile_lui_Tom_Sawyer.pdf")
save_range(49, 49, "U3_L2_Invitatia.pdf")
save_range(50, 50, "U3_L3_Adjectivul_Pozitia.pdf")
save_range(51, 51, "U3_L4_Adjectivul_Acordul.pdf")
save_range(52, 54, "U3_L5_Singur_pe_lume.pdf")
save_range(55, 55, "U3_L6_Descrierea_unui_personaj.pdf")
save_range(56, 57, "U3_L7_Bunul_meu_amic_Ilie.pdf")
save_range(58, 59, "U3_L8_Noi_vrem_sa_ne_unim_cu_tara.pdf")
save_range(60, 61, "U3_L9_Scrierea_corecta_a_adjectivelor.pdf")
save_range(62, 64, "U3_L10_Colind_de_Craciun.pdf")
save_range(65, 65, "U3_Recapitulare.pdf")
save_range(66, 67, "U3_Test_evaluare.pdf")

# Unit 4: JOCURILE COPILĂRIEI
save_range(69, 69, "U4_Intro_Jocurile_Copilariei.pdf")
save_range(70, 73, "U4_L1_Opreste_timpul_te_rog.pdf")
save_range(74, 75, "U4_L2_Pronumele_personal.pdf")
save_range(76, 77, "U4_L3_O_zi_alatura_de_un_copil.pdf")
save_range(78, 79, "U4_L4_Organizarea_informatiilor.pdf")
save_range(80, 81, "U4_L5_Pronumele_personal_de_politețe.pdf")
save_range(82, 82, "U4_Recapitulare.pdf")
save_range(83, 84, "U4_Test_evaluare.pdf")

# Unit 5: VISE ÎNSORITE
save_range(85, 85, "U5_Intro_Vise_Insorite.pdf")
save_range(86, 89, "U5_L1_Stigletele.pdf")
save_range(90, 90, "U5_L2_Verbul.pdf")
save_range(91, 91, "U5_L3_Persoana_si_numarul_verbului.pdf")
save_range(92, 94, "U5_L4_Papadia.pdf")
save_range(95, 95, "U5_L5_Cartea_postala.pdf")
save_range(96, 98, "U5_L6_Amintiri_din_copilarie.pdf")
save_range(99, 99, "U5_L7_Relatarea_banda_desenata.pdf")
save_range(100, 101, "U5_L8_Timpul_verbului.pdf")
save_range(102, 103, "U5_Recapitulare.pdf")
save_range(104, 105, "U5_Test_evaluare.pdf")

# Unit 6: ÎN RITM DE PRIMĂVARĂ
save_range(107, 107, "U6_Intro_In_Ritm_de_Primavara.pdf")
save_range(108, 109, "U6_L1_Prieteni_mici.pdf")
save_range(110, 112, "U6_L2_Draga_Nasturel.pdf")
save_range(113, 114, "U6_L3_Cuvântul_parte_de_propoziție.pdf")
save_range(115, 116, "U6_L4_Subiectul.pdf")
save_range(117, 119, "U6_L5_Predicatul.pdf")
save_range(120, 121, "U6_L6_Relatia_subiect_predicat.pdf")
save_range(122, 123, "U6_Recapitulare.pdf")
save_range(124, 125, "U6_Test_evaluare.pdf")

# Unit 7: CĂLĂTORIND PRIN LUME
save_range(125, 125, "U7_Intro_Calatorind_Prin_Lume.pdf")
save_range(126, 129, "U7_L1_Calatoriile_lui_Marco_Polo.pdf")
save_range(130, 133, "U7_L2_Calatoria_unui_bob_de_orez.pdf")
save_range(134, 135, "U7_L3_Invitatie_la_drumeție.pdf")
save_range(136, 138, "U7_L4_Organizarea_unei_drumeții.pdf")
save_range(139, 141, "U7_Recapitulare.pdf")
save_range(142, 143, "U7_Test_evaluare.pdf")

# Unit 8: PE ARIPILE IMAGINAȚIEI
save_range(143, 143, "U8_Intro_Aripile_Imaginatiei.pdf")
save_range(144, 145, "U8_L1_Cine_poate_sti.pdf")
save_range(146, 147, "U8_L2_Cai_verzi_si_intamplari_breze.pdf")
save_range(148, 151, "U8_L3_Copii_eram_noi_amândoi.pdf")
save_range(152, 154, "U8_L4_Caracatița.pdf")
save_range(155, 155, "U8_Recapitulare_Finala.pdf")
save_range(156, 158, "U8_Test_evaluare_finala.pdf")

# Appendix (159 to end)
save_range(159, len(reader.pages), "U8_Final_Appendix.pdf")
