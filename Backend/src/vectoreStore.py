import os
import faiss
import numpy as np
import pickle
from typing import List, Any
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.embedding import EmbeddingPipeline

class FaissVectorStore:
    def __init__(self , persist_dir:str = "faiss_store", embedding_model:str="sentence-transformers/all-MiniLM-L6-v2", chunk_size:int=1000, chunk_overlap:int=200):
        self.persit_dir = persist_dir
        os.makedirs(self.persit_dir , exist_ok=True)
        self.index=None
        self.metadata=[]
        self.embedding_model=embedding_model
        self.model=HuggingFaceEmbeddings(model_name=embedding_model)
        self.chunk_size=chunk_size
        self.chunk_overlap = chunk_overlap
        

    def build_from_documents(self, documents:List[Any]):
        emb_pipe= EmbeddingPipeline(model_name=self.embedding_model,chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        chunks=emb_pipe.chunk_documents(documents)
        embeddings=emb_pipe.embed_chunks(chunks)
        metadatas=[{"text":chunk.page_content} for chunk in chunks]
        self.add_embeddings(np.array(embeddings).astype('float32'), metadatas)
        self.save()
        

    def add_embeddings(self , embeddings:np.ndarray,metadatas:List[Any]=None):
        dim = embeddings.shape[1]
        if self.index is None:
            self.index=faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        if metadatas:
            self.metadata.extend(metadatas)

        

    def save(self):
        faiss_path=os.path.join(self.persit_dir,"faiss.index")
        meta_path = os.path.join(self.persit_dir,"metadata.pkl")
        faiss.write_index(self.index,faiss_path)
        with open (meta_path ,"wb")as f:
            pickle.dump(self.metadata,f)
       

    def load(self):
        faiss_path=os.path.join(self.persit_dir,"faiss.index")
        meta_path = os.path.join(self.persit_dir,"metadata.pkl")
        self.index=faiss.read_index(faiss_path)
        with open(meta_path,"rb")as f:
            self.metadata=pickle.load(f)
        

    def search(self , query_embedding:np.ndarray, top_k:int=3):
        D,I = self.index.search(query_embedding ,top_k)
        results=[]
        for idx , dist in zip(I[0],D[0]):
            meta=self.metadata[idx] if idx < len(self.metadata) else None
            results.append({"index":idx , "distance":dist , "metadata":meta})
        return results

    def query(self,query_text:str,top_k:int=3):
        query_emb = np.array(self.model.embed_query(query_text),dtype=np.float32).reshape(1, -1)
        return self.search(query_emb,top_k=top_k)




        