import fitz  # PyMuPDF

def extract_pdf_content(pdf_path):
    """Extract text and basic info from PDF"""
    doc = fitz.open(pdf_path)
    print(f"\n{'='*60}")
    print(f"FILE: {pdf_path}")
    print(f"{'='*60}")
    print(f"Total Pages: {len(doc)}")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        print(f"\n--- Page {page_num + 1} ---")
        print(text[:1000])  # First 1000 chars
        if len(text) > 1000:
            print(f"\n... (truncated, total length: {len(text)} chars)")
    
    doc.close()

# Examine all three PDFs
print("EXAMINING SAMPLE FILES")
print("="*60)

extract_pdf_content("Sample Report.pdf")
extract_pdf_content("Thermal Images.pdf")
extract_pdf_content("Main DDR.pdf")
