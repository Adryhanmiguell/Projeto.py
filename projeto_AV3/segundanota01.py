import os

usuarios = []
caronas = []

os.system('cls' if os.name == 'nt' else 'clear')
print('\n\n')
print('-'*50)
print('PAINEL DE CONTROLE'.center(50))
print('-'*50)
print()

while True:
    while True:
        print("1 - Cadastrar usuário\n"
            "2 - Login\n"
            "0 - Sair\n")
        opcao = input("\nEscolha uma opção: ")
        if opcao == '1':
            nome = input("\nDigite seu nome: ")

            email = input("Digite seu email: ")
            if '@gmail.com' not in email:
                while True:
                    print('\nErro, email invalido')
                    email = input("Digite seu email novamente: ")
                    if '@gmail.com' in email:
                        break

            senha = input("Digite sua senha: ")
            if len(senha) < 4:
                while True:
                    print("Senha com menos de 4 caracteres, digite novamente")
                    senha = input("Digite sua senha novamente: ")
                    if len(senha) >= 4:
                        break
        
            verificador_de_email = False
            for usuario in usuarios:
                if usuario["email"] == email:
                    print('Este email já existe!')
                    verificador_de_email = True
                    break
            
            if verificador_de_email:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
                
            usuario = {
                'nome': nome,
                'email': email,
                'senha': senha
            }

            usuarios.append(usuario)
            print("\nUsuário cadastrado com sucesso!")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif opcao == '2':
            verificacao = False
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            print()
            
            usuario_logado = None
            for usuario in usuarios:
                if email == usuario["email"] and senha == usuario["senha"]:
                    print(f"Nome: {usuario['nome']}")
                    print("-" * 50)
                    verificacao = True
                    usuario_logado = usuario
                    break
                

            if not verificacao:
                print('Erro, Email ou Senha inválidos')
                continue
                    
            while True:
                print("\n1 - Cadastrar caronas\n" \
                    "2 - Listar caronas\n" \
                    "3 - Buscar caronas\n" \
                    "4 - Reservar Caronas\n" \
                    "5 - Cancelar Reserva\n" \
                    "6 - Remover Carona\n" \
                    "7 - Mostrar Detalhes de Carona\n" \
                    "8 - Mostrar Carona cadastradas\n" \
                    "9 - Logout\n" 
                    )
                
                opcao2 = input("\nEscolha uma das opções: ")
            
                if opcao2 == '1':
                    local_de_origem = input("\nDigite o local de origem: ")
                    destino_da_carona = input("Digite o destino: ")
                    data_da_carona = input("Digite a data (DD/MM/AAAA): ")
                    
                    horario_da_carona = input("Digite o horário (HH:MM): ")
                    if horario_da_carona[2] != ":":
                        while True:
                            print("Hora invalida")
                            horario_da_carona = input('Digite a hora novamente: ')
                            if horario_da_carona[2] == ':':
                                break

                    vagas_por_carona = int(input("Digite o número de vagas: "))
                    valor_da_carona = input("Digite o valor da carona: ")
                    
                    carona = {
                        'motorista': usuario_logado['email'],
                        'origem': local_de_origem,
                        'destino': destino_da_carona,
                        'data': data_da_carona,
                        'horario': horario_da_carona,
                        'vagas': vagas_por_carona,
                        'valor': valor_da_carona,
                        'reservas': []
                    }
                    
                    caronas.append(carona)
                    print("\nCarona cadastrada com sucesso!")
                    
                elif opcao2 == '2':
                    print("\nLista de Caronas Disponíveis:")
                    for i, carona in enumerate(caronas, 1): #mudar o enumerate
                        print(f"\nCarona {i}:")
                        for chave, valor in carona.items():
                            if chave != 'reservas':
                                print(f"{chave}: {valor}")
                                
                elif opcao2 == '3':
                    origem = input("\nDigite a origem desejada: ")
                    destino = input("Digite o destino desejado: ")
                    encontrou = False
                    
                    for carona in caronas:
                        if origem.lower() in carona['origem'].lower() and destino.lower() in carona['destino'].lower():
                            print("\nCarona encontrada:")
                            for chave, valor in carona.items():
                                if chave != 'reservas':
                                    print(f"{chave}: {valor}")
                            encontrou = True
                            
                    if not encontrou:
                        print("\nNenhuma carona encontrada para esta rota.")
                        
                elif opcao2 == '4':
                    email_motorista = input("Digite o email do motorista: ")
                    data_carona = input("Digite a data da carona (DD/MM/AAAA): ") 
                    
                    for carona in caronas:
                        if carona['data'] == data_carona and carona['motorista'] == email_motorista:
                            if carona['vagas'] > 0:
                                quantidade = int(input('Quantidade de vagas para reservar: '))
                                if quantidade > carona['vagas']:
                                    print('Quantidade de vagas indisponível!')
                                else:
                                    carona['vagas'] -= quantidade
                                    carona['reservas'].append({
                                        'passageiro': usuario_logado['email'],
                                        'vagas_reservadas': quantidade
                                    })
                                    print('Reserva realizada com sucesso!')
                            else:
                                print('Não há vagas disponíveis nesta carona.')
                            break
                    else:
                        print('Carona não encontrada.')

                elif opcao2 == '5': 
                    email_motorista = input("Digite o email do motorista: ")
                    data_carona = input("Digite a data da carona (DD/MM/AAAA): ")
                    
                    for carona in caronas:
                        if carona['motorista'] == email_motorista and carona['data'] == data_carona:
                            for reserva in carona['reservas']:
                                if reserva['passageiro'] == usuario_logado['email']:
                                    carona['vagas'] += reserva['vagas_reservadas']
                                    carona['reservas'].remove(reserva)
                                    print("Reserva cancelada com sucesso!")
                                    break
                            else:
                                print("Você não tem reservas nesta carona.")
                            break
                    else:
                        print("Carona não encontrada.")
                        
                elif opcao2 == '6':
                    if usuario_logado['email'] in [carona['motorista'] for carona in caronas]:
                        data_carona = input("Digite a data da carona a ser removida (DD/MM/AAAA): ")
                        
                        for carona in caronas[:]:
                            if carona['motorista'] == usuario_logado['email'] and carona['data'] == data_carona:
                                caronas.remove(carona)
                                print('Carona removida com sucesso!')
                                break
                        else:
                            print('Nenhuma carona encontrada com estes dados.')
                    else:
                        print('Apenas motoristas podem remover caronas.')
                
                elif opcao2 == '7':
                    emaildomotorista3 = input('\nDigite o email do motorista: ')
                    datadacarona3 = input("Digite a data da carona (DD/MM/AAAA): ")
                    
                    for usu in usuarios:
                        for car in caronas:
                            if emaildomotorista3 in usu['email'] and datadacarona3 in car['data']:
                                for c, v in car.items():
                                    print(f"{c}: {v}")
                                break

                elif opcao2 == "8":
                    print("\nCaronas cadastradas por você:")
                    encontrou = False
                    for carona in caronas:
                        if carona['motorista'] == usuario_logado['email']:
                            print("\nDetalhes da Carona:")
                            for chave, valor in carona.items():
                                if chave != 'reservas':
                                    print(f"{chave}: {valor}")
                            encontrou = True

                elif opcao2 == '9':
                    print('\n\n')
                    print('-'*50)
                    print("VOCE SAIU DO SISTEMA, VOLTE SEMPRE! ")
                    print('-'*50)
                    print()
                    break
                    
                else:
                    print("Opção válida!")
                    input("\nPressione Enter para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')

        elif opcao == '0':
            print('\n\n')
            print('-'*50)
            print('ENCERRANDO SISTEMA, VOLTE SEMPRE!'.center(50))
            print('-'*50)
            print()

            exit()
        else:

            print("\nOpção inválida!")
            input("\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')