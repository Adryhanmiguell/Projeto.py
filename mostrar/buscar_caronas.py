def buscar(caronas):
    origem = input("\nDigite a origem desejada: ")
    destino = input("Digite o destino desejado: ")
    encontrou = False
    
    for car in caronas:
        if origem in car['origem'] and destino in car['destino']:

            print()
            print('*' * 30)
            print(f"MOTORISTA: {car['motorista']}")
            print(f"ORIGEM: {car['origem']}")
            print(f"DESTINO: {car['destino']}")
            print(f"HORA: {car['horario']}")
            print(f"DATA: {car['data']}")
            print(f"VALOR: {car['valor']}")
            print(f"VAGAS: {car['vagas']}")
            print('*' * 30)
            
            encontrou = True
            
    if not encontrou:
        print("\nNenhuma carona encontrada")


