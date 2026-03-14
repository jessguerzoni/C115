import socket

print("Cliente")

HOST = "localhost"
PORT = 50400

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Conectando...")
s.connect((HOST, PORT))

nome = input("Digite seu nome: ")

s.send(nome.encode())


p1 = s.recv(1024).decode()
print(p1)
r1 = input("Resposta: ")
s.send(r1.encode())


p2 = s.recv(1024).decode()
print(p2)
r2 = input("Resposta: ")
s.send(r2.encode())


p3 = s.recv(1024).decode()
print(p3)
r3 = input("Resposta: ")
s.send(r3.encode())


resultado = s.recv(1024).decode()

print("\nResultado:")
print(resultado)

s.close()
