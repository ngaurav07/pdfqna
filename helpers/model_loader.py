from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains.question_answering import load_qa_chain
import os

#Initialize the open source llama models
def _initialize_model(model: str = 'llama3'):
    try:
        # base_url = os.environ['OLLAMA_HOST_URL']
        base_url = "http://ollama:11434"
        print("base url is", base_url)
        model = ChatOllama(
            base_url=base_url,
            model=model)
        return model
    except:
        raise Exception("Unable to initialize chat model")


#initialize the embedding model to store in the vector database
def initialize_embedding(model: str = 'mxbai-embed-large'):
    try:
        # base_url = os.environ['OLLAMA_HOST_URL']
        base_url = "http://ollama:11434"
        print("embedding", base_url)
        embedding_model = OllamaEmbeddings(
            base_url=base_url,
            model=model)
        return embedding_model
    except:
        raise Exception("Unable to initialize the embedding model")


#question answer chain
def create_chain():
    llm = _initialize_model()
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain