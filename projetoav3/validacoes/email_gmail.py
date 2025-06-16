def validar_email(email):
    if '@gmail.com' not in email:
        while True:
            print('\nErro, mail invalido')
            email = input("Digite seu email novamente: ")
            if '@gmail.com' in email:
                break