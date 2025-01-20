from myClient import *
from functions import check_dex,check_all_dex



while True:
    option=input("Selecione uma opção:\n0:Pegar um Pokemon.\n1:Olhar a Dex de um Pokemon.\n2:Olhar a Dex completa.\nEnd:Finalizar a execução\n").title()
    match(option):
        case "0":
            print()
            execute_catch()
        case "1":
            print()
            pokemon_name=input("Digite o nome de um Pokemon:")
            check_dex(pokemon_name)
        case "2":
            print()
            check_all_dex()
            print()
        case "End":
            print()
            print("Finalizando a execução.")
            break