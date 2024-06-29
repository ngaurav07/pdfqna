from helpers import pdf_loader, model_loader
from helpers.response import ResponseHelper
from helpers.vector_store import initialize_store
import streamlit as st

def get_llm_response(query, vectordb):
    chain = model_loader.create_chain()
    matching_documents = vectordb.similarity_search(query)
    answer = chain.run(input_documents = matching_documents, question = query)
    st.write(answer)

if 'my_instance' not in st.session_state:
     st.session_state.my_instance = ResponseHelper()

if __name__ == "__main__":
      st.set_page_config(page_title="Upload PDF and ask question.")
      st.header("Ask PDF 🔗")
      pdf = st.file_uploader("Upload PDF", type="pdf")
      if pdf is not None:
          st.session_state.my_instance.load_pdf(pdf)
          user_question = st.text_input("Ask a question about your PDF:")
          output = st.session_state.my_instance.run(user_question)
          st.write(output)

