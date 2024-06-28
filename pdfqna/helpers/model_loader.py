from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains.question_answering import load_qa_chain

#Initialize the open source llama models
def _initialize_model(model: str = 'llama3'):
    model = ChatOllama(model=model)
    return model


#initialize the embedding model to store in the vector database
def initialize_embedding(model: str = 'mxbai-embed-large'):
    embedding_model = OllamaEmbeddings(model=model)
    return embedding_model

def create_chain():
    llm = _initialize_model()
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain