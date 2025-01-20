import random
import socket




HOST = "25.54.201.178" #COLOQUE O IP DO SERVIDOR AQUI!!!
PORT = 1025
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET é o protocolo de endereçamento de IP, SOCK_STREAM é o protocolo de transporte TCP!!!

def execute_catch():
    pokemon_name=input("Digite o nome do Pokemon que você quer tentar capturar:").title()
    if (pokemon_name=="End"):
        client.close()
        print("Conexão fechada.")
    else:
        pokeData=catch(pokemon_name)
        if (pokeData):
            for i,j in enumerate(pokeData):
                match(i):
                    case 0:
                        continue
                    case 1:
                        print(f"DexID: {j}")
                    case 2:
                        print(f"Species name: {j}")
                    case 3:
                        print(f"Primary Type: {j}")
                    case 4:
                        print(f"Secondary Type: {j}")
                    case 5:
                        print(f"Category: {j}")
                    case 6:
                        print(f"Height: {j} m")
                    case 7:
                        print(f"Weight: {j} kg")
                    case 8:
                        print(f"Description: {j}")
                    case 9:
                        print(f"Ability: {j}\n")
                    
def catch(pokemon_name): 
    from functions import register_dex
    chance=random.randint(1,3)
    if (chance): #MODIFICAR PARA ENTREGA
        print("Catched!")
        return register_dex(pokemon_name)
    else:
        print(f"Oh no! {pokemon_name} runned away!")

def client_function(pokemon):
    try:
        client.connect((HOST, PORT))
    except:
        print("Conexão com a Dex Nacional previamente estabelecida.")
        client.send(pokemon.encode()) #encode transforma a string em bytes, qualquer coisa só mudar. Formato enviado: Pikachu
        data = client.recv(1024) #1024 é o tamanho do buffer de recebimento.
        if ("(" in data.decode()):
            return(eval(data.decode()))
        return(False)
    
    else:
        print("Conectado a Dex Nacional.")
        client.send(pokemon.encode()) #encode transforma a string em bytes, qualquer coisa só mudar. Formato enviado: Pikachu
        data = client.recv(1024) #1024 é o tamanho do buffer de recebimento.
        if ("(" in data.decode()):
            return(eval(data.decode()))
        return(False)