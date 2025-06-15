passageiros = []

def reservar(caronas, usuarios, usuario):
    email_motorista = input("\nDigite o email do motorista: ")
    data_carona = input("Digite a data da carona (DD/MM/AAAA): ") 
    
    for car in caronas:
        for usu in usuarios:
            if car['data'] == data_carona and usu['email'] == email_motorista:
                if car['vagas'] > 0:
                    quant = int(input('\nDigite a quantidade de vagas para reservar: '))
                    if quant > car['vagas']:
                        print('Quantidade de vagas indisponível')
                    else:
                        car['vagas'] -= quant
                        passageiros.append({'motorista': usuario,
                                            'origem': car['origem'],
                                            'destino': car['destino'],
                                            'data': car['data'],
                                            'horario': car['horario'],
                                            'vagas': car['vagas'],
                                            "passageiros": quant,
                                            'valor': car['valor']
                                            })
                        print('Reserva realizada com sucesso')
                        return passageiros
                        
                else:
                    print('\nNão há vagas disponíveis')
                break
            else:
                print('\nNenhuma arona não encontrada')