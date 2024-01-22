import socket
import time
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

ip = "34.234.82.161"
port = 13571

s.connect((ip, port))
print("socket connected to %s" % (port))
connection_name = "ruveyda1".encode('utf-8')
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
    user_input = input("Enter text: ")
    #user_input = user_input.strip(b'\x00')
    byte_array = bytearray(user_input.encode('utf-8'))
    s.sendall("Ruveyda: ".encode('utf-8') + byte_array)

    time.sleep(5)

