import socket

print("Cliente")

HOST = "localhost"
PORT = 50400

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Conectando...")
s.connect((HOST, PORT))

nome = input("Digite seu nome: ")

s.send(nome.encode())

# pergunta 1
p1 = s.recv(1024).decode()
print(p1)
r1 = input("Resposta: ")
s.send(r1.encode())

# pergunta 2
p2 = s.recv(1024).decode()
print(p2)
r2 = input("Resposta: ")
s.send(r2.encode())

# pergunta 3
p3 = s.recv(1024).decode()
print(p3)
r3 = input("Resposta: ")
s.send(r3.encode())

# resultado final
resultado = s.recv(1024).decode()

print("\nResultado:")
print(resultado)

s.close()
