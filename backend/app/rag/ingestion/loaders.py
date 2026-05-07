from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split():
    loader = TextLoader(
        r"C:\Users\felip\Desktop\Python2026\Projetos IA\Agent\docs\text.txt",
        encoding="utf-8"
    )

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=150,
        separators=["\n\n","\n", ".", " "]
    )

    return splitter.split_documents(docs)