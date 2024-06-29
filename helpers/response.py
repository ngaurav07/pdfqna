from helpers import pdf_loader, model_loader
from helpers.vector_store import initialize_store
import streamlit as st


class ResponseHelper:
    def __init__(self):
        super()
        self.pdf_save_path:str  = ""
        self.chain = model_loader.create_chain()

    def load_pdf(self, pdf):
        '''
            Load the pdf if it is updated.
            Creates the documents and store the embeddings in the vector store.
        '''
        #only load the documents and vector data if the pdf is updated
        if not self.pdf_save_path.endswith(pdf.name):
            #delete the previous information(documents and embeddings) after pdf is updated
            if(self.pdf_save_path != ""):
                prev_ids = self.vectordb._collection.get()['ids']
                if(len(prev_ids) > 0):
                    self.vectordb._collection.delete(ids = prev_ids)
            self.pdf_save_path = pdf_loader.save_pdf(pdf)
            self.documents = pdf_loader.load_pdf(self.pdf_save_path)
            self.vectordb = initialize_store(self.documents)

    def run(self, query):
        matching_documents = self.vectordb.similarity_search(query)
        answer = self.chain.run(input_documents = matching_documents, question = query)
        return answer





