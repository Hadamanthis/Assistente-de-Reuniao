import sys

def ler_transcricao():
    caminho = input('> Digite o caminho até o arquivo contendo a transcrição\n')

    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            transcricao = f.read()
    except FileNotFoundError:
        print('> O arquivo informado não existe')
        sys.exit(1)

    return transcricao