import socket

class SocketFactory:
    @staticmethod
    def create_socket(host, port):
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
