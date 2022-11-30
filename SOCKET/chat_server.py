import socket
import sys
import time
import socketserver

import socket

host = "localhost" # "", "127.0.0.1
port = 7900

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)

print('En attente du client')
conn, address = server_socket.accept()
print(f'Client connecté {address}')

message = ""
while message != 'bye':
    message = input("Message au client ->")
    print("Message envoyé")
    conn.send(message.encode())
    message = conn.recv(1024).decode()
    print(f"Message du client -> {message}")
  
    


# Fermeture
conn.close()
print("Fermeture de la socket client")
server_socket.close()
print("Fermeture de la socket serveur")

#python3 Documents/GitHub/R309/SOCKET/chat_server.py
