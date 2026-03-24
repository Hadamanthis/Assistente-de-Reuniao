from file_reader import ler_transcricao
from llm_client import get_client, analisar_transcricao

# Perguntando onde está a transcrição e fazendo o resumo inicial
transcricao = ler_transcricao()
resultado = analisar_transcricao(transcricao)
print(resultado)