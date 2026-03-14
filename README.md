# C115
Mini-Kahoot

Nome: Jéssica Guerzoni

Tecnolgias utilizadas: Python e Socket TCP
Rodado com VS Code
Executado com: Git Bash

Terminal Servidor:

python servidor.py
Jessica@DESKTOP-QP8MP39 MINGW64 ~/Desktop/Nova pasta
$ cd C115

Jessica@DESKTOP-QP8MP39 MINGW64 ~/Desktop/Nova pasta/C115 (main)
$ python servidor.py
Servidor
Esperando conexão...
Conectado: ('127.0.0.1', 58845)

Jessica@DESKTOP-QP8MP39 MINGW64 ~/Desktop/Nova pasta/C115 (main)
$ 

Terminal Cliente:

python client.py

Jessica@DESKTOP-QP8MP39 MINGW64 ~/Desktop/Nova pasta
$ cd C115

Jessica@DESKTOP-QP8MP39 MINGW64 ~/Desktop/Nova pasta/C115 (main)
$ python client.py
Cliente
Conectando...
Digite seu nome: Jess 
Q1. Em redes, qual protocolo é orientado à conexão?
A) UDP
B) TCP
C) ICMP
D) ARP
Resposta: B
Q2. Qual camada do modelo OSI faz roteamento?
A) Física
B) Enlace
C) Rede
D) Aplicação
Resposta: D
Q3. Qual porta padrão do HTTP?
A) 21
B) 25
C) 80
D) 443
Resposta: A

Resultado:
Usuario: Jess
Acertos: 1/3

Q1 (resposta: B | correta: B)
Q2 (resposta: D | correta: C)
Q3 (resposta: A | correta: C)


Etapas:

- Servidor é ligado e aguarda conexão
- Cliente conecta no servidor através da porta HOST
- Servidor pede o nome do jogador
- 3 perguntas dadas pelo enunciado são dadas pelo servidor e respondidas pelo cliente
- No final temos as respostas do cliente e as corretas, junto com a pontuação

  
  
