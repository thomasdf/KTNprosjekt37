# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver
import sys

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Create the Message Receiver for the socket
        self.host = host
        self.server_port = server_port
        self.receiver = MessageReceiver(self, self.connection)

        # TODO: Finish init process with necessary code
        # self.connection.bind((self.host, self.server_port))
        # self.connection.settimeout(4)

        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))

        # Start the MSG Receiver
        self.receiver.start()

        message = ""
        while True:
            message = raw_input()
            message = message.strip()
            splitted = message.split()
            if (len(splitted) == 0):
                continue
            elif len(splitted) == 1:
                self.send_payload(splitted[0], None)
            elif len(splitted) == 2:
                self.send_payload(splitted[0], splitted[1])
            else:
                first_space = message.index(" ")
                self.send_payload(message[:first_space], message[first_space+1:])
        self.disconnect()

    def disconnect(self):
        # TODO: Handle disconnection
        self.connection.close()

    def receive_message(self, message):
        # TODO: Handle incoming message
        messages = message.split('}')
        for message in messages:
            if message == '':
                continue
            message += '}'
            message_json = json.loads(message)
            print ((message_json['timestamp'] + ' - ' + message_json['sender'] + ' says: ') if (message_json["response"] == "message") else "") + message_json['content']

    def send_payload(self, request, content):
        # TODO: Handle sending of a payload
        try:
            data = json.dumps({'request': request, 'content': content})
            self.connection.send(data)
        except Exception as e:
            print e
            print "[BAD COMMAND]"

if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.
    No alterations is necessary
    """
    # client = Client('localhost', 9998)

    # Take host and port from arguments if possible
    HOST = 'localhost'
    PORT = 9998
    if len(sys.argv) > 1:
        HOST = sys.argv[1]
        if len(sys.argv) > 2:
            PORT = int(sys.argv[2])
    client = Client(HOST, PORT)
