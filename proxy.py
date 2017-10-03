from receiver import Receiver
from sender import Sender
from settings import RF_ENGINE_IP_ADDRESS, RF_ENGINE_IP_PORT, TIMEOUT_IN_SECOND, CONNECTION_RETRY_INTERVAL, \
    GENERIC_GATEWAY_IP_ADDRESS, GENERIC_GATEWAY_IP_PORT, GENERIC_GATEWAY_PAGE_NAME, GENERIC_GATEWAY_TIMEOUT


def full_message_arrived(message):
    print(message)


def start_proxy():
    sender = Sender(GENERIC_GATEWAY_IP_ADDRESS, GENERIC_GATEWAY_IP_PORT, GENERIC_GATEWAY_PAGE_NAME,
                    GENERIC_GATEWAY_TIMEOUT)
    receiver = Receiver(RF_ENGINE_IP_ADDRESS, RF_ENGINE_IP_PORT, TIMEOUT_IN_SECOND, CONNECTION_RETRY_INTERVAL,
                        sender.send_message)
    receiver.start_listening()


start_proxy()
