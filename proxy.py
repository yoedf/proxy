import socket

from receiver import Receiver
from settings import RF_ENGINE_IP_ADDRESS, RF_ENGINE_IP_PORT


def full_message_arrived(message):
    print(message)


def start_proxy():
    receiver = Receiver(RF_ENGINE_IP_ADDRESS, RF_ENGINE_IP_PORT, full_message_arrived)
    receiver.start_listening()


start_proxy()
