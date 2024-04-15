class MessageProcessor:
    def __init__(self, socket):
        self.socket = socket

    def process_messages(self):
        bufsize = 1024
        print("Waiting for FT8 messages...")

        while True:
            data, addr = self.socket.recvfrom(bufsize)
            message = data.decode('utf-8')
            if message.strip().lower() == "exit":
                print("Exiting...")
                break
            if self.is_valid_ft8_message(message):
                self.handle_ft8_message(message)

    def is_valid_ft8_message(self, message):
        return message.startswith("<") and message.endswith(">")

    def handle_ft8_message(self, message):
        parts = message.split(",")
        frequency = parts[2]
        mode = parts[1]
        callsign = parts[3]
        message_text = parts[4]

        # Display components in a grid format
        print(f"Received FT8 message:")
        print("+----------------------+")
        print(f"| Frequency: {frequency} MHz |")
        print(f"| Mode: {mode}         |")
        print(f"| Callsign: {callsign}    |")
        print(f"| Message: {message_text} |")
        print("+----------------------+")
