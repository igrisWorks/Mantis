# Mantis
A production ready RAG  in python


Minimal Retrieval-Augmented Generation (RAG) demo using a local Qdrant vector store.

Run:
1. uv run -m uvicorn main:app   
2. npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery        
3.uv run streamlit run ./frontend_page_streamlit.py

Key files: data_loader.py, vector_db.py, frontend_page_streamlit.py
