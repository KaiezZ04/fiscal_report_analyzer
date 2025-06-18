import fitz

def extract_report_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        doc.close()
        return full_text.strip()
    except Exception as e:
        print(f"❌ Fail to read pdf: {e}")
        return ""