from helpers import pdf_loader, model_loader
from helpers.vector_store import initialize_store

def main():
    documents = pdf_loader.load_pdf("Untitled.pdf")
    get_llm_response("Which language does she speasks", documents)


def get_llm_response(query, documents):
    vectordb = initialize_store(documents)
    chain = model_loader.create_chain()
    matching_documents = vectordb.similarity_search(query)
    answer = chain.run(input_documents = matching_documents, question = query)
    print(answer)
if __name__ == "__main__":
    main()   