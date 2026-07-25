from typing import List, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np



class EmbeddingPipeline:
    def __init__(self,model_name:str="all-MiniLM-L6-v2" , chunk_size : int =1000 , chunk_overlap:int = 200):
        self.chunk_size=chunk_size
        self.model= SentenceTransformer(model_name)
        self.chunk_overlap = chunk_overlap
        


    def chunk_documents(self , document:List[Any])->List[Any]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap ,
            length_function=len,
            separators=["\n\n","\n"," ", ""]

        )
        chunks=splitter.split_documents(document)
        return chunks

    def embed_chunks(self , chunks:List[Any])->np.ndarray:
        text = [chunk.page_content for chunk in chunks]
        embeddings= self.model.encode(text )
        return embeddings

