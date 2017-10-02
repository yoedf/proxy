import socket

import time


class Receiver:
    def __init__(self, address, port, timeout_in_second, time_between_retries, on_message_arrived):
        self.address = address
        self.port = port
        self.timeout = timeout_in_second
        self.on_message_arrived = on_message_arrived
        self.time_between_retries = time_between_retries
        self.socket = None

    def connect(self):
        try:
            self.socket = socket.create_connection((self.address, self.port), self.time_between_retries)
        except Exception as e:
            print(e)
            print("Failed to connect to server. waiting %s seconds and trying again" % self.time_between_retries)
            time.sleep(self.time_between_retries)
            self.connect()

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
            return self.socket.recv(buffer_size)
        except socket.timeout:
            pass
        print("Didnt get data for %s seconds trying to reconnect" % str(self.timeout))
        time.sleep(self.time_between_retries)
        self.disconnect()
        self.connect()
        return self.receive_from_socket(buffer_size)
