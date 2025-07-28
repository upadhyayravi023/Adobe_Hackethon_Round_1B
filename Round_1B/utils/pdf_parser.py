import fitz  # PyMuPDF

def extract_text_from_pdfs(pdf_paths):
    parsed_docs = {}
    for path in pdf_paths:
        doc_text = []
        pdf = fitz.open(path)
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text = page.get_text("blocks")
            doc_text.append({"page": page_num + 1, "blocks": text})
        parsed_docs[path] = doc_text
    return parsed_docs
