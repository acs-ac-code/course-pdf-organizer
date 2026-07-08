# Course PDF Organizer - AI Agent Overview

This repository contains a specialized skill and a set of reference scripts designed for AI Agents to automate the processing of large course textbooks into smaller, well-organized PDFs. This is particularly useful for preparing materials for AI tools with file size limits (e.g., Notebook LM).

## 🎯 Purpose
The primary goal is to take a large, single-file course PDF and split it into logically named individual files (Lessons, Unit Intros, and Recaps) while ensuring that the page numbers in the resulting files match the printed page numbers in the book.

## 🛠️ Core Capabilities
- **Size Management:** Checks if a PDF exceeds **200 MB** and uses `pikepdf` to compress it. This ensures compatibility with most AI upload limits.
- **Page Synchronization:** Detects the offset between the actual PDF page index (0-based) and the printed page number. 
    - *Example:* If the front cover and title page are not numbered, Printed Page 1 is actually PDF Page 3. The skill removes these leading pages to create a `_final.pdf` where **Actual Page = Printed Page**.
- **Structural Mapping:** Extracts the Table of Contents (TOC) and cross-references it with a "Verification Scan" of the actual document text.
- **Intelligent Splitting:** Uses the refined mapping to extract precise page ranges into a folder with a standardized naming convention for perfect alphabetical sorting.

## 📋 Standardized Naming Convention
To ensure the files stay in order in any file explorer, the following format is used:
- **General Intro:** `U0_Intro_Orientation.pdf`
- **Unit Intro:** `U#_Intro_Title.pdf`
- **Lessons:** `U#_L#_Title.pdf` (e.g., `U1_L1_LessonName.pdf`)
- **Unit Closings/Summaries:** `U#_Title.pdf` (e.g., `U1_Mateoteca.pdf`)
- **Review & Tests:** `U#_Recapitulare.pdf` and `U#_Test.pdf` (Combined into `U#_Recapitulare_Evaluare.pdf` if pagination is confusing).

## ⚠️ Lessons Learned & Pitfalls (For AI Agents)
When implementing this workflow, be aware of the following:
1. **TOC Inaccuracy:** Never rely solely on the TOC. It often lists where a lesson *starts* but not where it *ends*. Always scan the text for the "Lecția X" marker of the *next* lesson to determine the boundary of the current one.
2. **Boundary Shifts:** Content may shift. A lesson might end and the next begin on the same page. A manual text scan of the boundaries is essential.
3. **Transition Pages:** Some pages serve as both the end of one section and the start of another. Assign them to one logical section to avoid duplication.
4. **Compression:** Standard `pypdf` compression is often insufficient for very large files; `pikepdf` is the preferred tool for significant size reduction.

## 📂 Repository Structure
- `course-pdf-organizer.md`: The formal skill definition for Hermes Agent.
- `scripts/`: A collection of reference Python scripts used during development (analysis, synchronization, and splitting).
