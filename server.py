import socket
from interface import HOST, PORTA

# Inicia o socket
sock = socket.socket() # sem parâmetros = default TCP e STREAM
sock.bind((HOST, PORTA))

# Configura quantos clientes podem ouvir ao mesmo tempo
# e recebe as instancias de conexao e endereço
sock.listen(2)
(conexao, (host_cliente, porta_cliente)) = sock.accept()

print("Host do cliente: " + str(host_cliente))
print("Porta do cliente (escolhida pelo SO): " + str(porta_cliente))

# loop de recebimento dos dados
while True:
    # recebe pacotes de 1024 bytes da conexao
    bytes = conexao.recv(1024).decode()

    # Encerra o loop quando recebe uma mensagem em branco
    if not bytes:
        break

    print("recebido: " + str(bytes))

    # envia uma resposta, necessário usar encode para converter
    # de String para bytes para enviar em rede.
    resposta = input("resposta: ")
    conexao.send(resposta.encode())


conexao.close()  # encerra a conexao e libera a porta