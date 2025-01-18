import socket
from functions import take_from_db

def execute():

    HOST = "0.0.0.0" #permite solicitações de qualquer ip
    PORT = 80


    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Pokedex Nacional carregada! Aguardando conexões de treinadores em {HOST}:{PORT} ")


    state=True
    while state:
        conexao , endereco = server.accept() #acho que não precisa estar dentro do while
        print(f"Conexão estabelecida com {endereco}")
        
        nome_pokemon = conexao.recv(1024).decode() #recebe o nome do pokemon com a primeira letra maiuscula - tratado no client

        quitWords=["quit","exit","end","terminate"]
        if (nome_pokemon in quitWords):
            conexao.close()
            break

        print(f"Treinador capturou um {nome_pokemon} e deseja informações")


        pokemon=take_from_db(nome_pokemon)
        if (pokemon):
            conexao.send(pokemon.encode())
            
        else:
            errorNoPokemon="Isso não é o nome de nenhum Pokemon"
            conexao.send(errorNoPokemon.encode())
            
