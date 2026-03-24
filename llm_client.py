import os
from dotenv import load_dotenv
from openai import OpenAI

def get_client():
    # Carrega as variáveis do .env
    load_dotenv()

    # Cria a conexão com o provedor
    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )

    return client

def analisar_transcricao(transcricao):
    client = get_client()

    # Requisição
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system",
             "content": """
             Você é a Teresa, uma assistente executiva experiente, direta e organizada.
             Você é especializada em análise de reuniões profissionais.

             Quando receber uma transcrição de reunião, extraia e organize as informações no seguinte formato:

             ## Resumo
             Um parágrafo conciso sobre o que foi discutido

             ## Decisões Tomadas
             Lista das decisões que foram definidas durante a reunião.

             ## Tarefa
             Lista de tarefas identificadas, com responsável e prazo quando mencionados.

             # Pontos em Aberto
             Questões que foram levantadas mas não foram resolvidas.

             Seja objetivo e fiel ao conteúdo da transcrição. Não invente informações que não foram mencionadas.
             """},
            {
                "role": "user",
                "content": f"Por favor, analise a seguinte transcrição de reunião:\n\n{transcricao}"
            }
        ]
    )

    return response.choices[0].message.content