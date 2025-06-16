import os

def abrir_arquivo(usuarios):
    if os.path.exists('usuarios_salvos.txt'):
        with open('usuarios_salvos.txt', 'r', encoding = 'utf-8') as arquivo:
            for i in arquivo:
                ler_linhas = i.strip().split(';')
                if len(ler_linhas) == 3:
                    nome, email, senha = ler_linhas
                    usuarios.append({
                        'nome': nome,
                        'email': email,
                        'senha': senha
                    })
    else:
        pass