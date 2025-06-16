def cadastradas_usuario(caronas, passageiros, usuario):
    for car in caronas:
        if car['motorista'] == usuario:

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
                else:
                    pass                    