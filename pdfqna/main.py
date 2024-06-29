from helpers.response import ResponseHelper
import streamlit as st


if 'response_helper_instance' not in st.session_state:
     st.session_state.response_helper_instance = ResponseHelper()

if __name__ == "__main__":
      st.set_page_config(page_title="Upload PDF and ask question.")
      st.header("Ask PDF 🔗")
      pdf = st.file_uploader("Upload PDF", type="pdf")
      if pdf is not None:
          st.session_state.response_helper_instance.load_pdf(pdf)
          user_question = st.text_input("Ask a question about your PDF:")
          output = st.session_state.response_helper_instance.run(user_question)
          st.write(output)

