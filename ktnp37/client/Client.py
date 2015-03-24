# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver

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
        self.host = host
        self.server_port = server_port

        # TODO: Finish init process with necessary code
        # self.connection.bind((self.host, self.server_port))
        # self.connection.settimeout(4)

        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))

        # Accepting the connection and creating a clientSocket
        (clientSocket, (ip, addr)) = self.connection.accept()

        # Create the Message Receiver for the socket
        message_receiver = MessageReceiver(self, clientSocket)

        message = ""
        while message != "logout":
            message = raw_input(": ")
            message = message.strip()
            message = message.split()
            if len(message)==1:
                self.send_payload(message[0], None)
            elif len(message)==2:
                self.send_payload(message[0],message[1])
        self.disconnect()

    def disconnect(self):
        # TODO: Handle disconnection
        send_payload('logout',None)
        # find client 

    def receive_message(self, message):
        # TODO: Handle incoming message
        print message    

    def send_payload(self, request, content):
        # TODO: Handle sending of a payload
        data = json.dumps({'request': request, 'content': content})
        self.connection.send(data)

if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.
    No alterations is necessary
    """
    client = Client('localhost', 9998)
