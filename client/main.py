from myClient import *
from functions import check_dex,check_all_dex



while True:
    option=input("Selecione uma opção:\n0:Pegar um Pokemon.\n1:Olhar a Dex de um Pokemon.\n2:Olhar a Dex completa.\nEnd:Finalizar a execução\n").title()
    match(option):
        case "0":
            execute_catch()
        case "1":
            pokemon_name=input("Digite o nome de um Pokemon.\n")
            check_dex(pokemon_name)
        case "2":
            check_all_dex()
        case "End":
            print("Finalizando a execução.")
            break