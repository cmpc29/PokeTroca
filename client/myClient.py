import socket

HOST = "123.1.2.2" #COLOQUE O IP DO SERVIDOR AQUI!!!
PORT = 80
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET é o protocolo de endereçamento de IP, SOCK_STREAM é o protocolo de transporte TCP!!!

def myClient(pokemon):
    client.connect((HOST, PORT))

    client.send(pokemon.encode()) #encode transforma a string em bytes, qualquer coisa só mudar. Formato enviado: Pikachu
    data = client.recv(1024) #1024 é o tamanho do buffer de recebimento.
    client.close()

    return(data.decode())

    
