import socket
import sqlite3
from functions import take_from_db


connect = sqlite3.connect("pokedb.db")
cursor = connect.cursor()


HOST = "0.0.0.0" #permite solicitações de qualquer ip
PORT = 80


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Pokedex carregada, Aguardando conexoes de treinadores em {HOST}:{PORT} ")


state=True
while state:
    conexao , endereco = server.accept()
    print(f"Conexão estabelecida com {endereco}")

    nome_pokemon = conexao.recv(1024).decode() #recebe o nome do pokemon com a primeira letra maiuscula - tratado no client
    print(f"Treinador capturou um {nome_pokemon} e deseja informações")

    quitWords=["quit","exit","end","terminate"]
    if (conexao.recv(1024).decode().strip().lower() in quitWords):
        conexao.close()
        break

    pokemon=take_from_db(nome_pokemon)
    if (pokemon):
        pokemon_infos=list(pokemon)
        conexao.send(pokemon_infos.encode())
    else:
        errorNoPokemon="Isso não é o nome de nenhum Pokemon"
        conexao.send(errorNoPokemon.encode())

    
    
#eu ainda nao vou usar as funç~eos do banco de dados, vou usar estatico ´pra ver se funciona, depois a gente muda