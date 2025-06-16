def detalhes(usuarios, caronas, passageiros):
    email = input('\nDigite o email do motorista: ')
    data = input("Digite a data da carona (DD/MM/AAAA): ")
    
    for usu in usuarios:
        for car in caronas:
            if email == usu['email'] and data == car['data']:

                print()
                print('*' * 30)
                print(f'ORIGEM: {car["origem"]}')
                print(f'DESTINO: {car["destino"]}')
                print(f'DATA: {car["data"]}')
                print(f'HORA: {car["horario"]}')
                print(f'VALOR: {car["valor"]}')
                print(f'VAGAS LIVRES: {car["vagas"]}')
                print('*' * 30)
                    
                for pasg in passageiros:
                    if pasg['passageiros'] > 0:
                        print(f'PASSAGEIROS: {pasg['passageiros']}')
                        print('*' * 30)
                    else:
                        ...