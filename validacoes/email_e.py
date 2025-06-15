def email_existente(email, usuarios):
    for usu in usuarios:
        while usu['email'] == email:
            print('\nEste email já existe')
            email = input('\nEmail: ')