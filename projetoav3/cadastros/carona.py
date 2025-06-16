def cadastrar_carona(usuario, caronas):
    email_motorista = input("Digite o email do motorista: ")
    local_de_origem = input("\nDigite o local de origem: ")
    destino_da_carona = input("Digite o local destino: ")
    data_da_carona = input("Digite a data (DD/MM/AAAA): ")

    if len(data_da_carona) == 16 and data_da_carona[2] == '/' and data_da_carona[5] == '/' and data_da_carona[10] == ' ' and data_da_carona[13] == ':':
        dia = int(data_da_carona[0:2])
        mes = int(data_da_carona[3:5])
        ano = int(data_da_carona[6:10])
        hora = int(data_da_carona[11:13])
        minuto = int(data_da_carona[14:16])

        if 1 <= dia <= 31 and 1 <= mes <= 12 and 0 <= hora <= 23 and 0 <= minuto <= 59:
            print("Formato e valores OK")
        else:
            print("Valores inválidos")

    horario_da_carona = input("Digite o horário (HH:MM): ")

    if horario_da_carona[2] != ":":
        while True:
            print("Hora invalida")
            horario_da_carona = input('Digite o horário novamente: ')
            if horario_da_carona[2] == ':':
                break

    vagas_por_carona = int(input("Digite o número de vagas: "))
    valor_da_carona = input("Digite o valor da carona: ")
    
    carona = {
        'motorista': usuario, 
        'origem': local_de_origem,
        'destino': destino_da_carona,
        'data': data_da_carona,
        'horario': horario_da_carona,
        'vagas': vagas_por_carona,
        'valor': valor_da_carona
    }
    
    caronas.append(carona)
    print("\nCarona cadastrada com sucesso!")
    return caronas