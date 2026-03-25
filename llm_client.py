import os
from dotenv import load_dotenv
from openai import OpenAI

# Instância responsável por se comunicar com a LLM
_client = None

def get_client():
    # Carrega as variáveis do .env
    load_dotenv()

    # Cria a conexão com o provedor
    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )

    return client

def chamar_llm(mensagens):
    global _client

    # Instanciando client caso necessário
    if _client is None:
        _client = get_client()

    # Requisição
    response = _client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=mensagens
    )

    return response.choices[0].message.content