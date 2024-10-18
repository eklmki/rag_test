import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Cohere
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddingsfrom
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts  import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder

#Define LLM and Embeddings Models

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-m3")

cohere_llm = Cohere(model="command",
                    temperature=0.1,
                    cohere_api_key =  "0vpKCMUtFx0tfaEipecHxKYpylcaNnm0JpYD6IAa")

doc_path = "source_data"
chroma_path = "contracts_chroma2"
pdf_folder_path = "source_data"
documents = []
for file in os.listdir(pdf_folder_path):
    if file.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder_path, file)
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())

# split the doc into smaller chunks i.e. chunk_size=500
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

db_chroma = Chroma.from_documents(chunks, embeddings, persist_directory=chroma_path)




# you can use a prompt template

queries = ["Mikä on ammattiliittojen rooli sopimisessa", "Kauan  saa isyyslomaa"]

queries_lang = ["English", "Finnish"]


# Return document most similar to the query
answers = []
for query in queries:
    docs = db_chroma.similarity_search(query)
    answers.append(docs[0].page_content)

# Print the top document match for each query
for idx, query in enumerate(queries):
    print(f"Query language: {queries_lang[idx]}")
    print(f"Query: {query}")
    print(f"Most similar existing question: {answers[idx]}")
    print("-" * 20, "\n")
