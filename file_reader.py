import sys

def ler_transcricao():
    print('> Olá, me chamo Teresa, sua assistente de reuniões online. Vamos começar')
    caminho = input('> Por favor, digite o caminho até o arquivo contendo a transcrição da reunião.\n> ')

    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            transcricao = f.read()
    except FileNotFoundError:
        print('> O arquivo informado não existe')
        sys.exit(1)

    return transcricao