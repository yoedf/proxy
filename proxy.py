import socket

from settings import RF_ENGINE_IP_ADDRESS, RF_ENGINE_IP_PORT


def full_message_arrived(message):
    print(message)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RF_ENGINE_IP_ADDRESS, RF_ENGINE_IP_PORT))
while True:
    header = s.recv(5)
    message_length = int(header[1:])
    print('message length:'+str(message_length))
    message = s.recv(message_length)
    while len(message) < message_length:
        message += s.recv(message_length-len(message))
    full_message_arrived(message)
    footer = s.recv(1)

