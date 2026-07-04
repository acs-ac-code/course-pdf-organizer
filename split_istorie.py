from pypdf import PdfReader, PdfWriter
import os

input_path = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\istorie_4_final.pdf"
output_dir = r"C:\Users\Astrid\OneDrive\Documente\kitty\manuale kitty\istorie_4_Split"

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

# Unit 1: PRIMII PAȘI ÎN ISTORIE
# L1: 12-13
# L2: 14-17
# Recap: 18-19
# Test: 20-21
save_range(11, 11, "U1_Intro_Primii_pasi_in_Istorie.pdf") # Unit 1 entry page
save_range(12, 13, "U1_L1_Primii_pasi_in_Istorie.pdf")
save_range(14, 17, "U1_L2_Cum_se_masoara_timpul_istoric.pdf")
save_range(18, 19, "U1_Recapitulare.pdf")
save_range(20, 21, "U1_Test_evaluare.pdf")

# Unit 2: DE LA ISTORIA PERSONALĂ LA ISTORIA NAȚIONALĂ
# L1: 22-25
# L2: 26-27
# L3: 28-29
# Recap: 30-31
# Test: 32-33
save_range(21, 21, "U2_Intro_De_la_istoria_personala.pdf") # Buffer
save_range(22, 25, "U2_L1_Istoria_personala_si_a_familiei.pdf")
save_range(26, 27, "U2_L2_Istoria_comunitatii_locale_si_nationale.pdf")
save_range(28, 29, "U2_L3_Comunitati_locale_minoritare.pdf")
save_range(30, 31, "U2_Recapitulare.pdf")
save_range(32, 33, "U2_Test_evaluare.pdf")

# Unit 3: CIVILIZAȚII ALE ANTICHITĂȚII
# L1: 34-41
# L2: 42-47
# L3: 48-51
# L4: 52-53
# L5: 54-55
# L6: 56-57
# L7: 58-59
# Recap: 60-61
# Test: 62-63
save_range(33, 33, "U3_Intro_Civilizatii_Antichității.pdf")
save_range(34, 41, "U3_L1_Grecia_antica.pdf")
save_range(42, 47, "U3_L2_Roma_antica.pdf")
save_range(48, 51, "U3_L3_Geto_dacii.pdf")
save_range(52, 53, "U3_L4_Razboaiele_daco_romane.pdf")
save_range(54, 55, "U3_L5_Popoare_de_ieri_si_azi_I.pdf")
save_range(56, 57, "U3_L6_Popoare_de_ieri_si_azi_II.pdf")
save_range(58, 59, "U3_L7_Popoare_de_ieri_si_azi_III.pdf")
save_range(60, 61, "U3_Recapitulare.pdf")
save_range(62, 63, "U3_Test_evaluare.pdf")

# Unit 4: EUROPA ȘI ȚĂRILE ROMÂNE ÎN EPOCA MEDIEVALĂ
# L1: 66-69
# L2: 70-73
# L3: 74-77
# L4: 76-77 (overlap in TOC) - let's use 74-75, 76-77 etc based on TOC
# L3: 74-75
# L4: 76-77
# L5: 78-79
# L6: 80-81
# L7: 82-83
# L8: 84-87
# Recap: 88-89
# Test: 90-91
save_range(64, 65, "U4_Intro_Europa_si_Tari_Romane.pdf")
save_range(66, 69, "U4_L1_Formarea_statelor_medievale.pdf")
save_range(70, 73, "U4_L2_Transilvania_spatiu_multietnic.pdf")
save_range(74, 75, "U4_L3_Tara_Romaneasca_Mircea_cel_Batrun.pdf")
save_range(76, 77, "U4_L4_Tara_Romaneasca_Vlad_Tepes.pdf")
save_range(78, 79, "U4_L5_Moldova_Stefan_cel_Mare.pdf")
save_range(80, 81, "U4_L6_Domnia_lui_Mihai_Viteazul.pdf")
save_range(82, 83, "U4_L7_Sustinatori_ai_culturii.pdf")
save_range(84, 87, "U4_L8_Calatori_si_calatorii.pdf")
save_range(88, 89, "U4_Recapitulare.pdf")
save_range(90, 91, "U4_Test_evaluare.pdf")

# Unit 5: EUROPA ȘI ROMÂNII ÎN EPOCA MODERNĂ
# L1: 94-95
# L2: 96-97
# L3: 98-99
# L4: 100-101
# L5: 102-103
# L6: 104-105
# Recap: 106-107
# Test: 108-109
save_range(92, 93, "U5_Intro_Europa_si_Romanii.pdf")
save_range(94, 95, "U5_L1_Unirea_Principatelor_Romane.pdf")
save_range(96, 97, "U5_L2_Cucerirea_independentei.pdf")
save_range(98, 99, "U5_L3_Participarea_la_Primul_Razboi_Mondial.pdf")
save_range(100, 101, "U5_L4_Formarea_statului_national.pdf")
save_range(102, 103, "U5_L5_Exploratori_al_secolului_XX.pdf")
save_range(104, 105, "U5_L6_Europa_si_România_la_cumpana.pdf")
save_range(106, 107, "U5_Recapitulare_finala.pdf")
save_range(108, 109, "U5_Test_evaluare_finala.pdf")

# Final Pages (110 to end)
save_range(110, len(reader.pages), "U5_Final_Appendix.pdf")
