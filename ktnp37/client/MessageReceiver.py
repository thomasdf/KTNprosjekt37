# -*- coding: utf-8 -*-
from threading import Thread

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and permits
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """
        # Init the superconstructor
        super(MessageReceiver, self).__init__()

        # Flag to run thread as a deamon
        self.daemon = True

        # TODO: Finish initialization of MessageReceiver
        self.client = client
        self.connection = connection
        print "[+] New thread started for " + client.host + ":" + str(client.server_port)

    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        # Listen to the server
        # self.connection.listen(4)

        while not self.client.dc:
            # Get the payload from the json-object
            payload = self.connection.recv(4096)

            # Send the message onward to the client
            self.client.receive_message(payload)
