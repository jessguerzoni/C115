import socket

# Questões (pergunta, opções, resposta correta)
questoes = [
    ("Qual é a capital da Itália?",
     ["Roma", "Paris", "Lisboa", "Londres"],
     "Roma"),
    ("Qual é o maior planeta do Sistema Solar?",
     ["Terra", "Júpiter", "Marte", "Saturno"],
     "Júpiter")
]

HOST = '127.0.0.1'  # Localhost
PORT = 5000         # Porta

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen(1)

print(f"Servidor aguardando conexões em {HOST}:{PORT}...")
conn, addr = servidor.accept()
print(f"Conexão estabelecida com {addr}")

# Envia perguntas e recebe respostas
resultados = []
acertos = 0
for pergunta, opcoes, correta in questoes:
    mensagem = pergunta + "\n"
    for i, opcao in enumerate(opcoes, start=1):
        mensagem += f"{i}) {opcao}\n"
    conn.sendall(mensagem.encode())

    resposta = conn.recv(1024).decode().strip()
    if resposta.isdigit():
        resposta_int = int(resposta) - 1
        if 0 <= resposta_int < len(opcoes) and opcoes[resposta_int] == correta:
            acertos += 1
            resultados.append("Correto")
        else:
            resultados.append("Errado")
    else:
        resultados.append("Errado")

# Envia resultado final
resposta_final = f"Você acertou {acertos} de {len(questoes)} questões.\n"
for i, status in enumerate(resultados, start=1):
    resposta_final += f"Questão {i}: {status}\n"

conn.sendall(resposta_final.encode())

conn.close()
servidor.close()