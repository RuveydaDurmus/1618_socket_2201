import socket
import time
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

ip = "34.234.82.161"
port = 13571

s.connect((ip, port))
print("socket connected to %s" % (port))
connection_name = "ruveyda1".ljust(32)[:32]
topic_name = "ruveyda_topic".ljust(32)[:32]
byte_arrayb = bytearray(1024)

s.sendall(connection_name.encode('utf-8'))
s.sendall(topic_name.encode('utf-8'))
s.sendall(byte_arrayb)
while True:
    user_input = input("Enter text: ")
    byte_array = bytearray(user_input.encode('utf-8'))
    s.sendall(byte_array)

    time.sleep(5)

s.close()