from langchain_cohere import CohereEmbeddings


from langchain_community.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_community.document_loaders import PyPDFLoader
import streamlit as st
from langchain_cohere.chat_models import ChatCohere


openai_api_key = os.getenv('OPENAI_API_KEY')
doc_path = "source_data"
chroma_path = "src/contracts_cohere2"
pdf_folder_path = "source_data"
documents = []
for file in os.listdir(pdf_folder_path):
    if file.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder_path, file)
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())

# split the doc into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

embeddings = CohereEmbeddings(cohere_api_key="0vpKCMUtFx0tfaEipecHxKYpylcaNnm0JpYD6IAa",

                                     model="embed-multilingual-v3.0", user_agent="langchain")
db = Chroma(embedding_function=embeddings)
