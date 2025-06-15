def totalizadores(caronas, passageiros, usuario):
    encontrou = False
    total_geral = 0.0

    for car in caronas:
        for pasg in passageiros:
            if car["motorista"] == usuario:
                encontrou = True
                valor = float(car["valor"])
                quantidade_passageiros = pasg["passageiros"]
                total = valor * quantidade_passageiros
                total_geral += total

                print()
                print("*" * 50)
                print('Relatorio Totalizado'.center(50))
                print("*" * 50)

                print(f'ORIGEM: {car["origem"]}')
                print(f'DESTINO: {car["destino"]}')
                print(f'DATA: {car["data"]}')
                print(f'HORARIO: {car["horario"]}')
                print(f'VALOR: {valor} R$')
                print(f'PASSAGEIRO(S): {quantidade_passageiros}')
                print(f'VAGAS LIVRES: {car["vagas"]}')
                print(f'VALOR TOTAL: {total}')
                print("*" * 50)

    if encontrou:
        print("-" * 50)
        print(f"TOTAL: {total_geral}")
        print("-" * 50)

        salvar_relatorio = input('\nSalvar relatorio total ? (S/N) ')

        if salvar_relatorio == 's':
            with open('totalizador.txt', 'a', encoding = 'utf-8') as arquivo_total:
                salvar_arquivo = (f'{car["origem"]};{car["destino"]};{car["data"]};{car["horario"]};{car["vagas"]};{quantidade_passageiros};{valor};{total}\n')
                arquivo_total.write(salvar_arquivo)
        else:
            pass
    else:
        print("\nNenhuma carona encontrada")