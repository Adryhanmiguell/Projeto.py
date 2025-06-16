def remover_reserva(caronas):
    email_motorista = input("\nDigite o email do motorista: ")
    data_carona = input("Digite a data da carona (DD/MM/AAAA): ")
    email_passageiro = input("Digite o email do passageiro a ser removido: ")

    reserva_encontrada = False

    for car in caronas:
        if car['data'] == data_carona and car['email_motorista'] == email_motorista:
            print(car.keys())  

        if car['data'] == data_carona and car.get('email_motorista') == email_motorista:
            for passageiro in car['passageiros']:
                if passageiro['email'] == email_passageiro:
                    car['vagas'] += passageiro['quantidade']
                    car['passageiros'].remove(passageiro)
                    print("Reserva cancelada com sucesso.")
                    reserva_encontrada = True
                    break
            if not reserva_encontrada:
                print("Passageiro não encontrado nessa carona.")
            break

    if not reserva_encontrada:
        print("Nenhuma carona encontrada com os dados informados.")