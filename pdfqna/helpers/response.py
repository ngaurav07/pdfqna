from helpers import pdf_loader, model_loader
from helpers.vector_store import initialize_store
import streamlit as st


class ResponseHelper:
    def __init__(self):
        super()
        self.pdf_save_path:str  = ""
        self.chain = model_loader.create_chain()

    def load_pdf(self, pdf):
        #only load the documents and vector data if the pdf is updated
        if not self.pdf_save_path.endswith(pdf.name):
            print("pdf updated so i am called")
            self.pdf_save_path = pdf_loader.save_pdf(pdf)
            self.documents = pdf_loader.load_pdf(self.pdf_save_path)
            self.vectordb = initialize_store(self.documents)

    def get_llm_response(self, query):
        matching_documents = self.vectordb.similarity_search(query)
        answer = self.chain.run(input_documents = matching_documents, question = query)
        return answer

    def run(self, question):
        return self.get_llm_response(question)





