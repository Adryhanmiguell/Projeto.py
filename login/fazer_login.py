def logar(usuarios):
    email = input("\nDigite seu email: ")
    senha = input("Digite sua senha: ")

    for usu in usuarios:
        if email == usu["email"] and senha == usu["senha"]:
            usuario = usu['nome']
            return usuario