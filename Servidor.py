import socket

print("Servidor")

HOST = "localhost"
PORT = 50400

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)

print("Esperando conexão...")

conn, addr = s.accept()

print("Conectado:", addr)


nome = conn.recv(1024).decode()

p1 = "Q1. Em redes, qual protocolo é orientado à conexão?\nA) UDP\nB) TCP\nC) ICMP\nD) ARP"
p2 = "Q2. Qual camada do modelo OSI faz roteamento?\nA) Física\nB) Enlace\nC) Rede\nD) Aplicação"
p3 = "Q3. Qual porta padrão do HTTP?\nA) 21\nB) 25\nC) 80\nD) 443"

conn.send(p1.encode())
r1 = conn.recv(1024).decode()

conn.send(p2.encode())
r2 = conn.recv(1024).decode()

# envia pergunta 3
conn.send(p3.encode())
r3 = conn.recv(1024).decode()

# respostas corretas
c1 = "B"
c2 = "C"
c3 = "C"

acertos = 0

if r1.upper() == c1:
    acertos += 1

if r2.upper() == c2:
    acertos += 1

if r3.upper() == c3:
    acertos += 1

resultado = "Usuario: " + nome + "\n"
resultado += "Acertos: " + str(acertos) + "/3\n\n"
resultado += "Q1 (resposta: " + r1 + " | correta: " + c1 + ")\n"
resultado += "Q2 (resposta: " + r2 + " | correta: " + c2 + ")\n"
resultado += "Q3 (resposta: " + r3 + " | correta: " + c3 + ")\n"

conn.send(resultado.encode())

conn.close()
s.close()
