def remover_reserva(caronas, usuarios):
    email_motorista = input("\nDigite o email do motorista: ")
    data_carona = input("Digite a data da carona (DD/MM/AAAA): ")
    
    for car in caronas:
        for usu in usuarios:
            if car['data'] == data_carona and usu['email'] == email_motorista:
                for r in car['reservas']:
                    car['vagas'] += r['vagas_reservadas']
                    car['reservas'].remove(r)
                    print("Reserva cancelada com sucesso")
                    break
            else:
                print("Nenhuma reserva não encontrada")

