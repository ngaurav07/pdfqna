from langchain.vectorstores import Chroma
from helpers.model_loader import initialize_embedding

def initialize_store(chunked_documents):
    vectordb = Chroma.from_documents(
        documents=chunked_documents,
        embedding= initialize_embedding()
    )
    vectordb.persist()
    return vectordb
