# -*- coding: utf-8 -*-
import SocketServer
import json
from time import gmtime, strftime
import re

history = ''
logged_in = []



class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            # TODO: Add handling of received payload from client
            
            received_dict = json.loads(received_string)

            if self in logged_in:
                if received_dict["request"] == "logout":
                    logout(self)
                elif received_dict["request"] == "msg":
                    message = received_dict['content']
                    sendMessagetoClients(message)
                elif received_dict["request"] == "names":
                    sendNamestoThisClient(self)
                elif received_dict["request"] == "help":
                    sendHelpTexttoThisClient(self)
                else:
                    sendError(self)
            elif received_dict["request"] == "help":
                sendHelpTexttoThisClient(self)
            elif received_dict["request"] == "login":
                    user_name = received_dict['content']
                    login(self, user_name)
            else:
                sendError(self)


def usernameValid(user_name):

    if not re.match("^[A-Za-z0-9_-]*$", user_name):
        return False
        #print("Error! Only characters a-z, A-Z and 0-9 are allowed!")
    else:
        return True
        #print("Your username is now: " + username)

def login(client, user_name):
    if usernameValid(user_name):
        logged_in.append(client)
        logged_in.append(user_name)
        response(client, "info", history, "")
        response(client, "info", "--------------\n logged in as ".append(user_name), client)
    else:
        sendError(client)

def logout(client):
    # Remove the client from the logged_in list
    index = logged_in.index(client)
    del logged_in[index:index+2]
    
    # Send a logout-respone to the client
    response(client, "info", "Successfully logged out.", "")
    
    # Disconnect the client
    client.connection.close()

def sendMessagetoClients(message):
    index = logged_in.index(self)
    history.append(logged_in[index+1] + ": " + message + "\n")
    for x in xrange(0,len(logged_in), 2):
        response(logged_in[x], "message", message, logged_in(index+1))

def sendNamestoThisClient(client):
    pass

def sendHelpTexttoThisClient(client):
    help_content = "Help\n\n"
    + "This client console accepts commands: \n\n"
    + "login <username>: logs on the server with the given username.\n"
    + "logout: logs out of the server.\n"
    + "msg <message>: sends a message to the chatroom.\n"
    + "names: list the user in the chatroom.\n"
    + "help: lists this message.\n"
    
    response(client, 'info', help_content, '')

def sendError(client):
    response(client, 'error', 'This is embarrassing! Type help for command reference.\n Are you logged in?', '')

def response(client, responsetype, content, sender):
    # Get the timestamp for the time NOW
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    # Get a string from a dict as a json-object
    payload = json.dumps({"timestamp": timestamp, "sender": sender, "response": responsetype, "content": content})
    
    # --- START TESTPRINTING ---
    print payload
    # --- END TESTPRINTING ---

    # Check if we want to send to ALL connected clients, or just to one
    if responsetype == "message":
        for i in xrange(0, len(logged_in), 2):
            cur_client = logged_in[i]
            cur_client.connection.send(payload)
    else:
        client.connection.send(payload)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations is necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations is necessary
    """
    HOST, PORT = 'localhost', 9998
    print 'Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
