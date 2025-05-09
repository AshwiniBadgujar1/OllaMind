import streamlit as st
import requests

# Function to query the Ollama model
def query_ollama_model(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "qwen:0.5b",  # You can change this to "qwen2.5:0.5b" if needed
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["response"]
    except requests.exceptions.RequestException as e:
        return f"❌ Error in getting the response: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="OllaMind", layout="centered")
st.title("OllaMind")

user_input = st.text_area("🧠 Enter your question:", height=150)

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("🧠 Thinking..."):
            answer = query_ollama_model(user_input)
            st.markdown("### ✅ Answer:")
            st.write(answer)
