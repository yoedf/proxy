import socket

import time


class Receiver:
    def __init__(self, address, port, timeout_in_second, time_between_retries, on_message_arrived):
        self.address = address
        self.port = port
        self.timeout = timeout_in_second
        self.on_message_arrived = on_message_arrived
        self.time_between_retries = time_between_retries
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(timeout_in_second)

    def connect(self):
        self.socket.connect((self.address, self.port))

    def disconnect(self):
        self.socket.close()

    def start_listening(self):
        self.connect()
        while True:
            header = self.receive_from_socket(5)
            message_length = int(header[1:])
            print('message length:' + str(message_length))
            message = self.receive_from_socket(message_length)
            while len(message) < message_length:
                message += self.receive_from_socket(message_length - len(message))
            self.on_message_arrived(message)
            footer = self.receive_from_socket(1)

    def receive_from_socket(self, buffer_size):
        try:
            data = self.socket.recv(buffer_size)
        except socket.timeout:
            print('Didnt get data for '+str(self.timeout)+' trying to reconnect')
            time.sleep(self.time_between_retries)
            self.disconnect()
            self.connect()
            self.receive_from_socket(buffer_size)
        return data
