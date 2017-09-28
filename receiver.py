import socket


class Receiver:
    def __init__(self, address, port, on_message_arrived):
        self.address = address
        self.port = port
        self.on_message_arrived = on_message_arrived

    def start_listening(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.address, self.port))
        while True:
            header = s.recv(5)
            message_length = int(header[1:])
            print('message length:' + str(message_length))
            message = s.recv(message_length)
            while len(message) < message_length:
                message += s.recv(message_length - len(message))
            self.on_message_arrived(message)
            footer = s.recv(1)
