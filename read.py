import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "34.234.82.161"
port = 13571
s.connect((ip, port))

connection_name = "ruveyda2".encode('utf-8')
if len(connection_name) < 32:
    padding_size = 32 - len(connection_name)
    padding = b'\x00' * padding_size
    connection_name += padding
topic_name = "test_topic".encode('utf-8')
if len(topic_name) < 32:
    padding_size = 32 - len(topic_name)
    padding = b'\x00' * padding_size
    topic_name += padding
a = 1024
size = struct.pack('!I', a)

s.sendall(connection_name)
s.sendall(topic_name)
s.sendall(size)

while True:
    data = s.recv(1024)
    data = data.strip(b'\x00')
    print(data.decode('utf-8'))

