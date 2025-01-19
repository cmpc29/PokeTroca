import socket
import threading
from functions import take_from_db

HOST = "0.0.0.0" #permite solicitações de qualquer ip
PORT = 1025
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.settimeout(30)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

def handle_client(conexao, endereco):
    """Função que lida com a comunicação com cada cliente"""
    try:
        quitWords = ["end"]
        
        while True:
            # Recebe a mensagem do cliente
            nome_pokemon = conexao.recv(1024).decode()
            
            if not nome_pokemon:  # Verifica se o cliente desconectou abruptamente
                print("Treinador desconectado.")
                break

            if nome_pokemon.lower() in quitWords:  # Verifica se o cliente pediu para encerrar
                print("Comando de saída recebido. Fechando conexão.")
                break  # Sai do loop, encerrando a conexão com este cliente
            
            print(f"Treinador {endereco} capturou um {nome_pokemon} e deseja informações.")

            pokemon = take_from_db(nome_pokemon)
            if pokemon:
                conexao.send(str(pokemon).encode())  # Envia as informações sobre o Pokémon
            else:
                errorNoPokemon = "Isso não é o nome de nenhum Pokemon"
                conexao.send(errorNoPokemon.encode())  # Envia a mensagem de erro

    except Exception as e:
        print(f"Ocorreu um erro durante a comunicação com o cliente: {e}")
    finally:
        conexao.close()  # Fecha a conexão com o cliente

def execute():
    print(f"Pokedex Nacional carregada! Aguardando conexões de treinadores em {HOST}:{PORT} ")
    
    state=True
    while state:
        try:
            conexao , endereco = server.accept() #acho que não precisa estar dentro do while
            print(f"Conexão estabelecida com {endereco}")

            client_thread=threading.Thread(target=handle_client,args=(conexao,endereco))
            client_thread.start()
        except socket.timeout:
            print("Tempo de espera expirado, aguardando novas conexões...")
            break

