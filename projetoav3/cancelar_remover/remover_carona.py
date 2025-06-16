def remover_carona(caronas, usuario):

    data_c = input('\nDigite a data da carona (DD/MM/AAAA): ')

    for car in caronas:
        if car['data'] == data_c and car['motorista'] == usuario:
            caronas.remove(car)
            print('Carona removida com sucesso')
            break
        else:
            print('Nenhuma carona encontrada')