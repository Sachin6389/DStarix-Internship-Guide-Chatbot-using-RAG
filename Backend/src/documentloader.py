from pathlib import Path
from typing import List , Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader

def Load_All_Documents(data_dir:str)->List[Any]:
    # Use Project Root data folder
    data_path = Path(data_dir).resolve()
    documents=[]

    # Load PDf Files
    pdf_files = list(data_path.glob("**/*.pdf"))
    print(F"Found {len(pdf_files)}PDF files")
    for pdf_file in pdf_files:
        print(f"Loading PDF file : {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            docs = loader.load()
           
            documents.extend(docs)
        except Exception as e:
            print(f"Error to PDF loading {pdf_file}: {e}")
    

    # Load Text Files
    text_files = list (data_path.glob("**/*.txt"))
    print(F"Found {len(text_files)} text files")
    for text_file in text_files:
        print(f"Loading text file : {text_file}")
        try:
            loader = TextLoader(str(text_file))
            docs = loader.load()
            print(f"Loaded {len(docs)} documents from {text_file}")
            documents.extend(docs)
        except Exception as e:
            print(f"Error to text file loading {text_file}: {e}")
    

    # Load CSV Files
    csv_files= list (data_path.glob("**/*.csv"))
    print(f"Found {len(csv_files)}CSV files")
    for csv_file in csv_files:
        print(f"Loading CSV file : {csv_file}")
        try:
            Loader=CSVLoader(str(csv_file))
            docs=Loader.Load()
            print(f"Loaded {len(docs)} documents from {csv_file}")
            documents.extend(docs)
        except Exception as e:
            print(f"Error to CSV file loading {csv_file }:{e}")
    

    # Excel Files
    excel_files = list(data_path.glob("**/*.xlsx"))
    print(f"Found {len(excel_files)} Excel files")
    for excel_file in excel_files:
        print(f"Loading Excel file : {excel_file}")
        try:
            loader = UnstructuredExcelLoader(str(excel_file))
            docs = loader.load()
            print(f"Loaded {len(docs)} documents from {excel_file}")
            documents.extend(docs)
        except Exception as e:
            print(f"Error to Excel file loading {excel_file}: {e}")
    
    # Word files
    word_files = list(data_path.glob("**/*.docx"))
    print(f"Found {len(word_files )} Word files")
    for word_file in word_files:
        print(f"Loading Word file :{word_file}")
        try:
            Loader = Docx2txtLoader(str(word_file))
            docs = Loader.load()
            print(f"Loaded {len(docs)} documents from {word_file}")
            documents.extend(docs)
        except Exception as e:
            print(f"Error to Word file loading {word_file}: {e}")
    

    # JSON Files
    json_files = list(data_path.glob("**/*.json"))
    print(f"Found {len(json_files)} JSON files")
    for json_file in json_files:
        print(f"Loading JSON file : {json_file}")
        try:
            loader = JSONLoader(str(json_file))
            docs = loader.load()
            print(f"Loaded {len(docs)} documents from {json_file}")
            documents.extend(docs)
        except Exception as e:
            print(f"Error to JSON file loading {json_file}: {e}")

    return documents   
 

