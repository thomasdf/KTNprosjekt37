# -*- coding: utf-8 -*-
from threading import Thread
import json
from socket import *

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
        # TODO: Init the superconstructor
        Thread.__init__(self)

        # Flag to run thread as a deamon
        self.daemon = True

        # TODO: Finish initialization of MessageReceiver
        self.client = client
        self.connection = connection
        print "[+] New thread started for " + client.host + ":" + str(client.server_port)
        self.run()

    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while True:
            # Listen to the server
            self.connection.listen(5)

            # Get the payload from the json-object
            payload = json.loads(connection.recv(4096))
            
            # --- START TESTPRINTING ---
            print payload
            # --- END TESTPRINTING ---

            # Get all the info from the payload
            timestamp = payload["timestamp"]
            sender = payload["sender"]
            response = payload["response"]
            content = payload["content"]

            # Handle the different types of responses
            message = timestamp + ": "
            if (response == "error"):
                message.append("[ERROR] -\t" + content)
            elif (response == "info"):
                message.append("[INFO] -\t" + content)
            elif (response == "history"):
                message.append("[HIST] -\n" + content)
            elif (response == "message"):
                message.append("[MSG] -\t" + sender + " says: " + content)
            else:
                message.append("[BAD REQUEST]")

            # Send the message onward to the client
            self.client.receive_message(message)
