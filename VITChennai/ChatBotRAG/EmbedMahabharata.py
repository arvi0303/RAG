# Third-party library imports
import chromadb

# Project-specific imports (Llama Index, LangChain, etc.)
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.langchain import LangchainEmbedding
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

# Load documents from the specified directory
documents = SimpleDirectoryReader(r".\MDocs").load_data()

# Set up the embedding model using sentence-transformers
embed_model = LangchainEmbedding(
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
)

# initialize the Persistent client, setting path to save data
db = chromadb.PersistentClient(path="./chroma_db")

# create collection
chroma_collection = db.get_or_create_collection("mahabharata_database")

# assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# create and store your index
vector_index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,
    chunk_size=1024,
    storage_context=storage_context, 
    show_progress=True)