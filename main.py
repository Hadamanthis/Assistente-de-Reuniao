from file_reader import ler_transcricao
from llm_client import chamar_llm

# Perguntando onde está a transcrição
transcricao = ler_transcricao()

mensagens = [
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

# Fazendo o resumo inicial
resultado = chamar_llm(mensagens)
mensagens.append({"role": "assistant", "content": resultado}) # Atualizando o histórico de mensagens

print(resultado)

while True:
    user_input = input('\n> O que quer saber sobre a reunião?\n> ')

    if user_input == 'Sair()':
        break

    mensagens.append({"role": "user", "content": user_input})
    resposta = chamar_llm(mensagens)
    mensagens.append({"role": "assistant", "content": resposta})
    print(resposta)

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