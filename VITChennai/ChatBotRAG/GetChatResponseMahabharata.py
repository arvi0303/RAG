# Standard library imports
import os

# Third-party library imports
from dotenv import load_dotenv
from huggingface_hub import login
import chromadb
import torch

#For display
from IPython.display import display
import pandas as pd

# Project-specific imports (Llama Index, LangChain, etc.)
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.prompts.prompts import SimpleInputPrompt
from llama_index.embeddings.langchain import LangchainEmbedding
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

# Define system and query wrapper prompts
system_prompt = """
You are a Q&A assistant. Your goal is to answer questions as
accurately as possible based on the instructions and context provided.
"""
query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")

# Load environment variables from the .env file
load_dotenv()

# Authenticate
auth_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
login(token=auth_token)

# Load the model and tokenizer
llama_model_name = "meta-llama/Llama-2-7b-chat-hf"

print(torch.cuda.is_available())
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize the language model using Hugging Face's Llama-2-7b model
llm = HuggingFaceLLM(
    context_window=4096,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.0, "do_sample": False},
    system_prompt=system_prompt,
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name=llama_model_name,
    model_name=llama_model_name,
    device_map="cuda",
    model_kwargs={
        "torch_dtype": torch.float16, 
        "load_in_8bit": True
        }
    # model_kwargs={
    #     "torch_dtype": torch.float32,  # Use float32 since quantization typically requires GPU
    #     "load_in_8bit": False,  # Disable 8-bit quantization if on CPU
    # }    
)

# Set up the embedding model using sentence-transformers
embed_model = LangchainEmbedding(
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
)

# initialize the Persistent client, setting path to save data
db = chromadb.PersistentClient(path="./chroma_db")

# create collection
chroma_collection = db.get_or_create_collection("mahabharata_database")
chroma_vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

vector_index = VectorStoreIndex.from_vector_store(embed_model=embed_model,vector_store=chroma_vector_store)

# create a query engine and query
query_engine = vector_index.as_query_engine(llm=llm)

response = query_engine.query("what is jupiter?")
print(response)

response = query_engine.query("who killed bhishma?")
print(response)

response = query_engine.query("who is bhima?")
print(response)

response = query_engine.query("who is krishna?")
print(response)

response = query_engine.query("who is arjuna?")
print(response)

response = query_engine.query("who is pandu?")
print(response)

response = query_engine.query("who is rama?")
print(response)