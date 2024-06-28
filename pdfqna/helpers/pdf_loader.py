from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf(path: str):
    if path.endswith('.pdf'):
        loader = PyPDFLoader(path)
        pages = loader.load_and_split()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        documents = text_splitter.split_documents(pages)
        return documents
    else:
        raise "Invalid file provided"