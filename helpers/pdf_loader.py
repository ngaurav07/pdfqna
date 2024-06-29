from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

pdf_location = "files"

def save_pdf(pdf_contents) -> str:
    if not os.path.exists(pdf_location):
        os.makedirs(pdf_location)
    pdf_save_path = os.path.join(pdf_location,pdf_contents.name)
    with open(pdf_save_path, mode='wb') as w:
        w.write(pdf_contents.getvalue())
    return pdf_save_path

def load_pdf(path: str):
    loader = PyPDFLoader(path)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_documents(pages)
    #remove file after use
    os.remove(path)
    return documents