def remover_reserva(caronas, passageiros):
    data = input('Digite a data para remover (DD/MM/AAAA): ')

    for car in caronas:
        if data in car["data"]:
            for pasg in passageiros:
                car["vagas"] += int(pasg["passageiros"])
                print('\nReversa cancelada.')
                passageiros.remove(pasg)