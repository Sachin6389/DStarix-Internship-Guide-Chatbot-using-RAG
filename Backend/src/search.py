import os
from dotenv import load_dotenv
from src.vectoreStore import FaissVectorStore 
from langchain_groq import ChatGroq

load_dotenv()

class RAGSearch:
    def __init__(self, persist_dir:str="faiss_store", embedding_model:str="all-MiniLM-L6-v2" , llm_model:str = "llama-3.3-70b-versatile" ):
        self.vectorstore= FaissVectorStore(persist_dir , embedding_model)
        faiss_path = os.path.join(persist_dir, "faiss.index")
        meta_path = os.path.join(persist_dir, "metadata.pkl")
        if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):
            from src.documentloader import Load_All_Documents
            documents=Load_All_Documents("Documents")
            self.vectorstore.build_from_documents(documents=documents)
        else:
            self.vectorstore.load()

        
        self.llm = ChatGroq( groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name=llm_model,
            temperature=0.7)
        

    def search_and_summerize(self,query:str , top_k:int=3)->str:
        results=self.vectorstore.query(query,top_k=top_k)
        text=[r["metadata"].get("text","")for r in results if r["metadata"]]
        context="\n\n".join(text)
        if not context:
            return "No relevent document found"
        prompt=f""" 
                   You are a helpful AI assistant.
                   Use Only the following context to answer the user's question.
                   Context:
                   {context}
                    Question:
                    {query}
                    Answer:
                    """
        response=self.llm.invoke(prompt)
        return response.content
    


        
