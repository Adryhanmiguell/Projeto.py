def verificar_senha(senha):
    if len(senha) < 4:
        while True:
            print("Sua senha contém menos de 4 caracteres, digite novamente")
            senha = input("Digite sua senha novamente: ")
            if len(senha) >= 4:
                break