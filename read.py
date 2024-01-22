import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "34.234.82.161"
port = 13571
s.connect((ip, port))

connection_name = "ruveyda2".ljust(32)[:32]
topic_name = "ruveyda_topic".ljust(32)[:32]
byte_array = bytearray(1024)

s.sendall(connection_name.encode('utf-8'))
s.sendall(topic_name.encode('utf-8'))
s.sendall(byte_array)

while True:
    data = s.recv(1024)
    print("Received:", data.decode('utf-8'))

s.close()
