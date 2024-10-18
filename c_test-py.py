
from langchain_community.vectorstores import Chroma

# To split the documents into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
# To use MyScale as a vector database
# To use Hugging Face for embeddings
from langchain_huggingface import HuggingFaceEmbeddings
# To load a wikipedia page
from langchain_community.document_loaders.wikipedia import WikipediaLoader
import anthropic
client = anthropic.Anthropic()
loader = WikipediaLoader(query="Fifa")

# Load the documents


docs = loader.load()
chroma_path = "fifa_chroma2"

character_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
docs = character_splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
chunks = text_splitter.split_documents(documents)

db_chroma = Chroma.from_documents(chunks, embeddings, persist_directory=chroma_path)

query = "Who won fifa Fifa 2022?"
docs = db_chroma.similarity_search(query, 3)
print(docs)


stre = "".join(doc.page_content for doc in docs)
model = 'claude-3-opus-20240229'

response = client.messages.create(
        system =  "You are a helpful research assistant. You will be shown data from a vast knowledge base. You have to answer the query from the provided context.",
        messages=[
                    {"role": "user", "content":  "Context: " + stre + "\\\\n\\\\n Query: " + query},
                ],
        model= model,
        temperature=0,
        max_tokens=160
    )
response.content[0].text