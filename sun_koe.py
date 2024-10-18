import sys

from langchain_cohere import CohereEmbeddings
import os

from requests_toolbelt import user_agent

os.environ["API_KEY"] =  "0vpKCMUtFx0tfaEipecHxKYpylcaNnm0JpYD6IAa"



from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_community.document_loaders import PyPDFLoader
import streamlit as st
from langchain_cohere.chat_models import ChatCohere


os.environ["OPENAI_API_KEY"] = "sk-proj-8FqpllUlcdCvSxqgkV1Z0pIuJM-0i" \
                               "-SPUnPSPfP1LCEOY2fAbfwFYxOJ4JPb9uokAQmQj82lPtT3BlbkFJeCGgoxvPlSXu_nd2EGBJSG" \
                               "-FiQ5MHd3XDt2cbmtlkpj5_z_aCRVMl8-dkB4i4QF4I379II2HwA"
openai_api_key = os.getenv('OPENAI_API_KEY')
doc_path = "source_data"
chroma_path = "src/contracts_chroma"
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


embeddings = CohereEmbeddings(
        model="multilingual-22-12"
    )
vectorstore = FAISS.from_documents(chunks, embeddings)

input_text = "kauan on vuosilomaa?"
# this is an example of a user question (query)
#def generate_response(input_text):
#from langchain_cohere import ChatCohere
# retrieve context - top 5 most relevant (closests) chunks to the query vector
# (by default Langchain is using cosine distance metric)
docs_chroma = db_chroma.similarity_search_with_score(input_text, k=5)

# generate an answer based on given user query and retrieved context information
#context_text = "\n\n".join([doc.page_content for doc, _score in docs_chroma])

# you can use a prompt template
print(docs_chroma)
sys.exit()
prompt_template = """Text: {context}
    Question: {question}
    you are a chatbot designed to assist the users.
    Answer only the questions based on the text provided. If the text doesn't contain the answer,
    reply that the answer is not available. Answer in Finnish, if the questiopn is in Finnish, in English, if the question i9s in English.
    keep the answers precise to the question"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = { "prompt" : PROMPT }
# call LLM model to generate the answer based on the given context and query
model= ChatCohere(cohere_api_key="0vpKCMUtFx0tfaEipecHxKYpylcaNnm0JpYD6IAa",

                 model="embed-multilingual-v3.0", user_agent="langchain")
# load retrieved context and user query in the prompt template
#prompt_template = model.invoke.from_template(PROMPT_TEMPLATE)
#prompt = prompt_template.format(context=context_text, question=input_text)
print(docs_chroma)

#st.info(model.invoke(prompt).content)

"""
# Streamlit UI
# ===============
st.set_page_config(page_title="Contract query/TE-sopimus haku", page_icon=":robot:")
st.header("Contract query/TE-sopimus haku")

form_input = st.text_input(
    "Enter query in the language you want the answer in/ kysy kysymystä kielellä. jolla haluat vastauksen")
submit = st.button("Query/Haku")

if submit:
    st.write(generate_response(form_input))
"""
