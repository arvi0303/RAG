# Standard library imports
import os

# Third-party library imports
from dotenv import load_dotenv
#from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
import torch

# Project-specific imports (Llama Index, LangChain, etc.)
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.prompts.prompts import SimpleInputPrompt
from llama_index.embeddings.langchain import LangchainEmbedding
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

# Load environment variables from the .env file
load_dotenv()

# Load documents from the specified directory
documents = SimpleDirectoryReader(r".\EarthDocs").load_data()

# Set up the embedding model using sentence-transformers
embed_model = LangchainEmbedding(
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
)

# Create a VectorStoreIndex from the documents
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,
    chunk_size=1024, 
    show_progress=True
)

# Authenticate
auth_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
login(token=auth_token)

# Load the model and tokenizer
llama_model_name = "meta-llama/Llama-2-7b-chat-hf"

# Define system and query wrapper prompts
system_prompt = """
You are a Q&A assistant. Your goal is to answer questions as
accurately as possible based on the instructions and context provided.
"""
query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")

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

query_engine = index.as_query_engine(llm=llm)

# Query the index
response = query_engine.query("what is the age of earth?")
print(response)

response = query_engine.query("what is earth's atmosphere?")
print(response)

response = query_engine.query("what is atmosphere?")
print(response)

response = query_engine.query("what is jupiter?")
print(response)