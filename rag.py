import json
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

def load_vectorstore():
    with open("data.json") as f:
        data = json.load(f)

    docs = []
    for section in data.values():
        for item in section.values():
        # Convert dict/list to string
            if isinstance(item, dict):
               content = ", ".join([str(v) for v in item.values()])
            elif isinstance(item, list):
               content = ", ".join(item)
            else:
               content = str(item)

        docs.append(Document(page_content=content))

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )
    return FAISS.from_documents(docs, embeddings)

def retrieve(query, vectorstore):
    docs = vectorstore.similarity_search(query)
    return "\n".join([d.page_content for d in docs])        