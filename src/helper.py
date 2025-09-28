from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List 

# Extract Data From the Pdf File 
def load_pdf_file(data): 
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load() 
    return documents 

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    Filters a list of Document objects to retain only essential information.

    Args:
        docs (List[Document]): A list of Document objects, each containing
                               page content and metadata.

    Returns:
        List[Document]: A new list of Document objects, where each object
                        contains only:
                        - page_content (original content)
                        - metadata with only the 'source' key
    """
    minimal_docs: List[Document] = []  

    for doc in docs:
        
        src = doc.metadata.get("source")

        minimal_docs.append(
            Document(
                page_content=doc.page_content,  
                metadata={"source": src}      
            )
        )


    return minimal_docs

# Split the document into smaller chunks 
def text_split(minimal_docs): 
    text_splitter = RecursiveCharacterTextSplitter( 
                            chunk_size=500, 
                            chunk_overlap=20,
                            )
    texts_chunk = text_splitter.split_documents(minimal_docs) 
    return texts_chunk

def dowload_embeddings(): 
    """Dowload and return the HuggingFace embeddings model""" 
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings( 
                        model_name=model_name,
                       )
    return embeddings     

def download_hugging_face_embeddings(): 
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings