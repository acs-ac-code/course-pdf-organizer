---
name: course-pdf-organizer
description: Automates the compression, synchronization, and splitting of course textbooks into individual lesson PDFs with standardized naming for alphabetical sorting.
---

# Course PDF Organizer

This skill provides a structured workflow for processing large course PDFs (textbooks) into a set of smaller, well-named PDF files for each lesson, unit introduction, and summary.

## Trigger Conditions
- User provides a course PDF and wants it split into lessons/sections.
- The PDF is too large for external tools (e.g., > 200MB).
- The printed page numbers in the PDF do not match the actual PDF page indices.

## Required Tools & Dependencies
- **Python Libraries:** `pypdf` (for splitting and text extraction), `pikepdf` (for high-efficiency compression).
- **Installation:** `uv pip install pypdf pikepdf`

## User Preferences
- **Autonomous Execution:** Execute all workflow steps autonomously without requesting confirmation between each stage.

## Workflow Steps

### 1. Size Management & Compression
- **Check Size:** Check if the file size exceeds **200 MB**.
- **Action:** If $> 200\text{ MB}$, use `pikepdf` to save a linearized version to reduce size.
- **Output:** Save the compressed version as `[original]_compressed.pdf` to preserve the original.

### 2. Page Offset Synchronization
- **Analyze:** Use `scripts/detect_offset.py` to extract text and identify the **Printed Page Number** vs. the **Actual PDF Index** (0-based).
- **Verification Scan:** Run a script to scan the entire document for markers like "Unitatea X", "Lecția X", "Recapitulare", and "Test" to map the actual structural boundaries. Do not rely solely on the TOC, as printed page numbers may be misleading or sections may start/end unexpectedly.
- **Calculation:** $\text{Offset} = \text{Actual Page Index} + 1 - \text{Printed Page Number}$.
- **Identification:** Identify the exact pages causing the offset (e.g., front cover, copyright page).
- **Clean:** Use `pypdf` to delete the first $N$ pages causing the offset.
- **Output:** Save as `[original]_final.pdf`. In this file, $\text{Actual Page} = \text{Printed Page}$.

### 3. Table of Contents (TOC) Extraction & Cleaning
- **Extract:** Read the TOC pages from the `_final.pdf`.
- **Clean Titles:** 
    - Remove bracketed information (e.g., `(Investighez...)`, `(Proiect...)`).
    - Remove "Metode complementare de evaluare" (complementary evaluation methods) sections.
- **Cross-Reference:** Compare TOC ranges against the markers found during the **Verification Scan**. Adjust ranges to ensure each lesson PDF starts and ends exactly where the content does.
- **Calculate Ranges:** Determine the start and end page for every section by looking at the start page of the subsequent section.
- **Grouping:** Group all initial orientation material (everything before Unit I) into a single "Introduction & Orientation" entry (e.g., Pages 1–8). Ensure no overlap with the Unit 1 Introduction page.

### 4. PDF Splitting & Standardized Naming
Create a dedicated folder named after the course. Split the `_final.pdf` into separate files using the following naming convention to ensure correct alphabetical sorting:

| Section Type | Naming Format | Example | Sort Position |
| :--- | :--- | :--- | :--- |
| **General Intro** | `U0_Intro_Title.pdf` | `U0_Intro_Orientation.pdf` | First |
| **Unit Intro** | `U#_Intro_Title.pdf` | `U1_Intro_Povesti.pdf` | Start of Unit |
| **Lessons** | `U#_L#_Title.pdf` | `U1_L1_Numere.pdf` | Sequential |
| **Unit Closings** | `U#_Title.pdf` | `U1_Mateoteca.pdf` | End of Unit |
| **Recap & Test** | `U#_Recapitulare.pdf` & `U#_Test.pdf` | `U1_Recapitulare.pdf` | End of Unit |

*Note: Extract 'Recapitulare' and 'Test evaluare' as separate files. If pagination is confusing or markers overlap (as seen in some manuals), combine them into a single `U#_Recapitulare_Evaluare.pdf`.*
*Note: Avoid using "Club_" or other prefixes for closing sections so that "M" (Mateoteca) naturally follows "L" (Lessons) alphabetically.*

## Verification Checklist
- [ ] Is the final file size $\le 200\text{ MB}$?
- [ ] Does Actual Page 1 = Printed Page 1 in the split files?
- [ ] Are all lessons extracted?
- [ ] Do the filenames sort correctly in the folder?
- [ ] Are the bracketed "evaluation methods" removed from titles?

## Pitfalls & Troubleshooting
- **TOC Inaccuracy:** The TOC often lists the page where a lesson *starts*, but doesn't specify where it *ends*. Relying only on the next lesson's start page can accidentally include transition content or overlapping pages. Use the Verification Scan to confirm boundaries.
- **Boundary Shifts:** Be alert for cases where Lesson X ends and Lesson X+1 starts on the same page or unexpectedly early. Always verify the start of the next lesson's text before finalizing the previous range.
- **Compression:** `pypdf`'s `compress_content_streams()` is often insufficient for very large files; always prefer `pikepdf` for significant size reduction.
- **Indexing:** Always remember that `pypdf` uses 0-based indexing (Page 1 is index 0).
- **Transition Pages:** Be careful with pages that serve as both the end of one section (e.g., General Intro) and the start of another (e.g., Unit 1). Assign them to a single logical section to avoid duplication.
