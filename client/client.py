import socket

HOST = "123.1.2.2" #COLOQUE O IP DO SERVIDOR AQUI!!!
PORT = 80


while True:
    cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET é o protocolo de endereçamento de IP, SOCK_STREAM é o protocolo de transporte TCP!!!
    cliente.connect((HOST, PORT))
    cliente.send("ola mundo".encode()) #encode transforma a string em bytes, qualquer coisa só mudar
    data = cliente.recv(1024) #1024 é o tamanho do buffer de recebimento.
    print(data.decode())
    cliente.close() #fecha a conexão :D
    break