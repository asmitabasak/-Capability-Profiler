import chromadb
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Vector DB
client = chromadb.Client()
collection = client.create_collection("hiring_data")

def add_hiring_data(job_description: str):
    # Store data in vector space
    collection.add(
        documents=[job_description],
        ids=["job_001"]
    )

def query_agent(student_profile: str):
    # 1. Retrieve relevant context
    results = collection.query(query_texts=[student_profile], n_results=1)
    context = results['documents'][0][0]
    
    # 2. Call Gemini with context
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    prompt = f"Context: {context}\n\nStudent Profile: {student_profile}\n\nAnalyze fit:"
    return llm.invoke(prompt)
