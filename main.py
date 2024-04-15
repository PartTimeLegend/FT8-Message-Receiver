from socket_factory import SocketFactory
from message_processor import MessageProcessor

def main():
    # Prompt the user for host and port
    host = input("Enter host (default: 127.0.0.1): ") or '127.0.0.1'
    port = input("Enter port (default: 2237): ") or 2237
    port = int(port)  # Convert port to integer

    socket_factory = SocketFactory()
    socket = socket_factory.create_socket(host, port)

    message_processor = MessageProcessor(socket)
    message_processor.process_messages()

if __name__ == "__main__":
    main()
