import socket
import sys
import time
import socketserver

server_socket = socket.socket()
server_socket.bind(('localhost', 6000))
server_socket.listen(5)
print("Serveur en écoute")
conn, addr = server_socket.accept()

data = conn.recv(1024).decode()
conn.send(b'CA VA OU QUOI ?')
print(data)
print ("Le serveur se ferme")
conn.close()
