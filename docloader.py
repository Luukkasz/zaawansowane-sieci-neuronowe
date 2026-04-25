import fitz
import os

def load_pdf(file_path):
    """Wczytuje tekst z pliku PDF przy użyciu biblioteki fitz (PyMuPDF)."""
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def load_documents_from_folder(folder_path):
    """Wczytuje teksty ze wszystkich plików PDF w folderze."""
    documents = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            documents[filename] = load_pdf(file_path)
    return documents
