import requests


class Sender(object):
    def __init__(self, server_ip, server_port, page_name, timeout):
        self.server_ip = server_ip
        self.server_port = server_port
        self.page_name = page_name
        self.timeout = timeout

    def send_message(self, message):
        print(message)
        try:
            response = requests.put("%s:%s/%s" % (self.server_ip, str(self.server_port), self.page_name), data=message,
                                    timeout=self.timeout)
        except Exception:
            pass
