# ollama_rag_query.py
import requests

def query_ollama_rag_model(query):
    url = "http://localhost:11411/v1/query"  # Replace with your Ollama server URL if different
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",  # Use your API key if needed
    }
    payload = {
        "model": "qwen2.5:0.5b",  # Replace with the model you want to use
        "query": query,
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error in running Ollama: {response.text}")
