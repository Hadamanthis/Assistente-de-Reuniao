import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis do .env
load_dotenv()

# Cria a conexão com o provedor
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


transcricao = """
[10:00] João (Gerente de Produto): Bom dia a todos. Vamos começar a reunião de planejamento do Q2.
[10:02] Maria (Dev): Antes de começar, preciso mencionar que o sistema de pagamentos está com lentidão desde ontem.
[10:03] João: Entendido. Maria, você pode investigar isso até amanhã?
[10:04] Maria: Sim, consigo verificar até o final do dia hoje.
[10:05] João: Ótimo. Sobre o Q2, decidimos priorizar três funcionalidades: checkout rápido, programa de fidelidade e relatórios gerenciais.
[10:08] Carlos (Design): O layout do checkout já está pronto. Posso compartilhar com a equipe hoje.
[10:09] João: Perfeito. Carlos, envia pro time até as 18h.
[10:10] Maria: Para o programa de fidelidade, ainda precisamos definir as regras de pontuação. Quem decide isso?
[10:11] João: Boa pergunta. Vou alinhar com o diretor comercial essa semana e trago uma resposta na próxima reunião.
[10:13] Carlos: O prazo para lançamento do checkout rápido ainda é 30 de abril?
[10:14] João: Sim, mantemos o prazo. Alguma outra questão?
[10:15] Maria: Precisamos contratar mais um desenvolvedor para o Q2. Ainda não temos orçamento aprovado.
[10:16] João: Vou verificar com o RH. Por enquanto encerramos aqui.
"""

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

print(response.choices[0].message.content)


'''
## Resumo
A reunião de planejamento do Q2 discutiu os principais objetivos e funcionalidades a serem priorizadas, incluindo checkout rápido, programa de fidelidade e relatórios gerenciais. Além disso, foram abordados problemas técnicos, como a lentidão do sistema de pagamentos, e questões de recursos humanos, como a necessidade de contratar mais um desenvolvedor.

## Decisões Tomadas
- Priorizar três funcionalidades para o Q2: checkout rápido, programa de fidelidade e relatórios gerenciais.
- Maria investigará a lentidão do sistema de pagamentos até o final do dia.
- Carlos enviará o layout do checkout para a equipe até as 18h.
- Manter o prazo de lançamento do checkout rápido para 30 de abril.

## Tarefa
- Maria: Investigar a lentidão do sistema de pagamentos (prazo: final do dia).
- Carlos: Enviar o layout do checkout para a equipe (prazo: até as 18h).
- João: Alinhar com o diretor comercial sobre as regras de pontuação do programa de fidelidade (prazo: esta semana).
- João: Verificar com o RH sobre a contratação de mais um desenvolvedor (sem prazo definido).

## Pontos em Aberto
- Definição das regras de pontuação do programa de fidelidade.
- Aprovação do orçamento para contratação de mais um desenvolvedor.
'''