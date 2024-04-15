# FT8 Message Receiver

This Python program listens for FT8 messages and displays their components in a grid format.

## Requirements

- Python 3.x
- WSJT-X or similar exposing traffic via UDP

## Usage

1. Clone the repository or download the files.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the files.
4. Run the `main.py` script:
   ```
   python main.py
   ```
5. When prompted, enter the host and port. Default values are provided if no input is entered.
6. The program will start listening for FT8 messages. When a message is received, it will be displayed in a grid format, showing its frequency, mode, callsign, and message text.
7. To exit the program, type "exit" and press Enter.

## Files

- `main.py`: The main script that prompts the user for host and port, creates a socket, and starts the message processing loop.
- `socket_factory.py`: Module containing the `SocketFactory` class, responsible for creating sockets.
- `message_processor.py`: Module containing the `MessageProcessor` class, responsible for processing received messages.


## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and distribute this code as needed.
