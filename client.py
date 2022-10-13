import socket
from interface import HOST, PORTA

sock = socket.socket()
sock.connect((HOST, PORTA))

mensagem = input("mensagem: ")

while mensagem.lower().strip() != '':
    sock.send(mensagem.encode())
    mensagem_recebida = sock.recv(1024).decode()

    print("recebido: " + mensagem_recebida)

    # sobreescreve a mensagem, quando entrar no loop novamente
    # vai repetir os passos com a nova mensagem.
    mensagem = input("resposta: ")

sock.close()  