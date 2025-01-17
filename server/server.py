import socket

pokedex = {
    "pikachu": "Pikachu é um Pokémon do tipo elétrico, que evolui para Raichu. Pikachu é o Pokémon mais famoso da franquia, sendo o mascote oficial da mesma, chato",
    "marcelo": "não pe um pokemon, mas é um cara aí :/",
}



HOST = "0.0.0.0" #isso deixa receber solicitçõesd e qualuqer ip
PORT = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server((HOST, PORT))
server.listen(1)

print(f"Pokedex carregada, Aguardando conexoes de treinadores em {HOST}:{PORT} ")

while True:
    conexao , endereco = server.accept()
    print(f"Conexão estabelecida com {endereco}")

    nome_pokemon = conexao.recv(1024).decode().strip.lower() #recebe o nome do pokemon com tratamento minusculo
    print(f"Treinador deseja informações de {nome_pokemon}")

    resposta = pokedex.get(nome_pokemon, f"Não tenho informações sobre {nome_pokemon}")

    conexao.send(str(resposta).encode())
    conexao.close()
    
#eu ainda nao vou usar as funç~eos do banco de dados, vou usar estatico ´pra ver se funciona, depois a gente muda