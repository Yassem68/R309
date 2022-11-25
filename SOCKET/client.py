import socket
import sys
import time
import socketserver

client_socket = socket.socket()
client_socket.connect(('localhost', 6000))
client_socket.send('Hello World'.encode())
data = client_socket.recv(1024).decode()
print(data)

client_socket.close()