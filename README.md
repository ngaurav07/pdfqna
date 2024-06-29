# PDF Question and Answer
Upload the pdf and ask the information thats inside the PDF.
> **_NOTE:_**  The models used are from the Meta Llama which will run in your own machine. Everything is totally free.

## Installation
Docker based installation is simple. It contains Ollama(llama runner) with the streamlit based application that you can interact using the browser.
```console
foo@bar:~$ docker compose build app
foo@bar:~$ docker compose up
```
> **_NOTE:_** Open https://localhost:8501 in the browser

## Components
The components used in this repository are: 
1. Python
- Programming language used to perform the task.
2. Langchain
- Python library that provides abstraction and tools to interact with the Large language models
3. Chroma
- Vector based database that will store the documents and embedding that we provide from the PDF.
4. Streamlit
- UI to upload and chat with the large language model like llama3.
5. Ollama
- Tool that will help to run llm in the local machine.
6. Docker
- Tool that runs streamlit and ollama inside the docker container.
