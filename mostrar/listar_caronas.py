def listar(caronas, usuario):
    if len(caronas) == 0: 
        print("\nNão ha caronas disponiveis")
    else:
        for car in caronas:
            if car ['vagas']  > 0:
                print()
                print('*' * 30)
                print(f"MOTORISTA: {usuario}")
                print(f"ORIGEM: {car['origem']}")
                print(f"DESTINO: {car['destino']}")
                print(f"DATA: {car['data']}")
                print(f"HORARIO: {car['horario']}")
                print(f"VALOR: {car['valor']}")
                print(f"VAGAS: {car['vagas']}")
                print('*' * 30)