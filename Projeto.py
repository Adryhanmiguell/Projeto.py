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
import mostrar.buscar_caronas
import mostrar.carona_cadastrada
import mostrar.detalhes_carona
import mostrar.listar_caronas
import mostrar.relatorio

if os.path.exists('usuarios.txt'):
    with open('usuarios_salvos.txt', 'r', encoding = 'utf-8') as arquivo:
        for i in arquivo:
            ler_linhas = i.strip().split(';')
            if len(ler_linhas) == 3:
                nome, email, senha = ler_linhas
                usuarios.append({
                    'nome': nome,
                    'email': email,
                    'senha': senha
                })
else:
    pass

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
        usuario_logado = login.fazer_login.logar(usuarios)
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
                caronas = cadastros.carona.cadastrar_carona(usuario_logado, caronas)
                
            elif opcao2 == '2':
                mostrar.listar_caronas.listar(caronas, usuario_logado)
                                                            
            elif opcao2 == '3':
                mostrar.buscar_caronas.buscar(caronas)
                    
            elif opcao2 == '4':
                passageiros = cadastros.reserva.reservar(caronas, usuarios, usuario_logado)

            elif opcao2 == '5': 
                cancelar_remover.cancelar_reserva.remover_reserva(caronas, usuarios)
                    
            elif opcao2 == '6':
                cancelar_remover.remover_carona.remover_carona(caronas, usuario_logado)
            
            elif opcao2 == '7':
                mostrar.detalhes_carona.detalhes(usuarios, caronas, passageiros)

            elif opcao2 == "8":
                mostrar.carona_cadastrada.cadastradas_usuario(caronas, passageiros, usuario_logado)

            elif opcao2 == '9':
                mostrar.relatorio.totalizadores(caronas, passageiros, usuario_logado)

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