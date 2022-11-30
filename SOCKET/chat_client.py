import socket
import sys
import time
import socketserver

host = "localhost" # "", "127.0.0.1
port = 7900

print(f"Ouverture de la socket sur le serveur {host} port {port}")
client_socket = socket.socket()
client_socket.connect((host, port))
print("Serveur est connecté")

message = ""
while message != 'bye':
    message = input("Message au serveur ->")
    client_socket.send(message.encode())
    print("Message envoyé")
    message = client_socket.recv(1024).decode()
    print(f"Message du serveur : {message}")




# Fermeture de la socket du client
client_socket.close()
print("Socket fermée")
        
      
# #python3 Documents/GitHub/R309/SOCKET/chat_client.py

