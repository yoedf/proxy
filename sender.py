import requests


class Sender(object):
    def __init__(self, server_ip, server_port, page_name):
        self.server_ip = server_ip
        self.server_port = server_port
        self.page_name = page_name

    def send_message(self, message):
        print(message)
        response = requests.put(("%s:%s/%s" % self.server_ip, str(self.server_port), self.page_name), data=message)
        print(response)
