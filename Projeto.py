passageiros = []
usuarios = []
caronas = []

import os
import cadastros.carona
import cadastros.usuario
import cadastros.reserva
import cancelar_remover.cancelar_reserva
import cancelar_remover.remover_carona
import login.fazer_login
import login.abrir_usuarios
import mostrar.buscar_caronas
import mostrar.carona_cadastrada
import mostrar.detalhes_carona
import mostrar.listar_caronas
import mostrar.relatorio

login.abrir_usuarios.abrir_arquivo(usuarios)

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print()
    print('-'*50)
    print('FUNÇÕES'.center(50))
    print('-'*50)
    print()

    print("| 1 - Cadastro |\n"
          "| 2 - Login    |\n"
          "| 0 - Sair     |\n")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastros.usuario.cadastrar_usuario(usuarios)

    elif opcao == '2':
        usuario = login.fazer_login.logar(usuarios)
        
        if not usuario:
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
                
        while True:

            print()
            print('-'*50)
            print('FUNÇÕES'.center(50))
            print('-'*50)
            print()

            print("\n| 1 - Cadastrar caronas   |\n" \
                    "| 2 - Listar caronas      |\n" \
                    "| 3 - Buscar caronas      |\n" \
                    "| 4 - Reservar caronas    |\n" \
                    "| 5 - Cancelar reserva    |\n" \
                    "| 6 - Remover carona      |\n" \
                    "| 7 - Detalhes da carona  |\n" \
                    "| 8 - Caronas cadastradas |\n" \
                    "| 9 - Relatorio total     |\n" \
                    "| 10 - Logout             |\n" 
                )
            
            opcao2 = input("\nEscolha uma das opções: ")
        
            if opcao2 == '1':
                caronas = cadastros.carona.cadastrar_carona(usuario, caronas)
                
            elif opcao2 == '2':
                mostrar.listar_caronas.listar(caronas, usuario)
                                                            
            elif opcao2 == '3':
                mostrar.buscar_caronas.buscar(caronas)
                    
            elif opcao2 == '4':
                passageiros = cadastros.reserva.reservar(caronas, usuarios, usuario)

            elif opcao2 == '5': 
                cancelar_remover.cancelar_reserva.remover_reserva(caronas, passageiros)
            elif opcao2 == '6':
                cancelar_remover.remover_carona.remover_carona(caronas, usuario)
            
            elif opcao2 == '7':
                mostrar.detalhes_carona.detalhes(usuarios, caronas, passageiros)

            elif opcao2 == "8":
                mostrar.carona_cadastrada.cadastradas_usuario(caronas, passageiros, usuario)

            elif opcao2 == '9':
                mostrar.relatorio.totalizadores(caronas, passageiros, usuario)

            elif opcao2 == '10':
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            else:
                print("\nOpção inválida")
                input("Pressione Enter para continuar")
                os.system('cls' if os.name == 'nt' else 'clear')

    elif opcao == '0':
        print('-'*50)
        print('Programa encerrado !'.center(50))
        print('-'*50)
        exit()

    else:
        print("\nOpção inválida")
        input("Pressione Enter para continuar")
        os.system('cls' if os.name == 'nt' else 'clear')