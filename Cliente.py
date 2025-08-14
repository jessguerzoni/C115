import socket

HOST = '127.0.0.1'  # Mesmo IP do servidor
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

while True:
    dados = cliente.recv(1024).decode()
    if not dados:
        break

    if "Questão" in dados or "Você acertou" in dados:
        print(dados)
        break

    print(dados)
    resposta = input("Digite o número da alternativa correta: ")
    cliente.sendall(resposta.encode())

cliente.close()