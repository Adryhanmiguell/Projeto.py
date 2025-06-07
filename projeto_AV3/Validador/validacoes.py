while True:
    def validar_email(email):
        if '@gmail.com' not in email:
                while True:
                    print('\nErro, email invalido')
                    email = input("Digite seu email novamente: ")
                    if '@gmail.com' in email:
                        break

    def verificador_senha(senha):
        senha = input("Digite sua senha: ")
        if len(senha) < 4:
                while True:
                    print("Senha com menos de 4 caracteres, digite novamente")
                    senha = input("Digite sua senha novamente: ")
                    if len(senha) >= 4:
                        break

    def verificar_emailexistente(usuarios, email):
        verificar_emailexistente = False
        for usuario in usuarios:
            if usuario["email"] == email:
                print('Este email já existe!')
            verificador_de_email = True
            break

        if verificar_emailexistente:
            continue
