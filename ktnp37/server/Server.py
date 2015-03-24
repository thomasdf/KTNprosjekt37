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
        self.broken = False

        # Loop that listens for messages from the client
        while not self.broken:
            try:
                received_string = self.connection.recv(4096)
            except:
                pass
            # TODO: Add handling of received payload from client
            # Deserialize
            received_dict = 0
            try:
                received_dict = json.loads(received_string)
                if "request" not in received_dict or "content" not in received_dict:
                    raise ValueError
            except:
                self.sendError()
                continue

            if self in logged_in:
                if received_dict["request"] == "logout":
                    self.logout()
                elif received_dict["request"] == "msg":
                    message = received_dict['content']
                    self.sendMessagetoClients(message)
                elif received_dict["request"] == "names":
                    self.sendNamestoThisClient()
                elif received_dict["request"] == "help":
                    self.sendHelpTexttoThisClient()
                else:
                    self.sendError()
            elif received_dict["request"] == "help":
                self.sendHelpTexttoThisClient()
            elif received_dict["request"] == "login":
                    user_name = received_dict['content']
                    self.login(user_name)
            else:
                self.sendError()


    def usernameValid(self, user_name):

        if not re.match("^[A-Za-z0-9_-]*$", user_name):
            return False
            #print("Error! Only characters a-z, A-Z and 0-9 are allowed!")
        else:
            return True
            #print("Your username is now: " + username)

    def login(self, user_name):
        global logged_in

        if self.usernameValid(user_name):
            logged_in.append(self)
            logged_in.append(user_name)
            self.response("info", history + "\n--------------\n logged in as " + user_name, "")
        else:
            self.sendError()

    def logout(self):
        # Defince global
        global logged_in

        # Remove the client from the logged_in list
        index = logged_in.index(self)
        del logged_in[index:index+2]
        
        # Send a logout-respone to the client
        self.response("info", "Successfully logged out.", "")

    def sendMessagetoClients(self, message):
        global history
        index = logged_in.index(self)
        history += logged_in[index+1] + ": " + message + "\n"
        for x in xrange(0, len(logged_in), 2):
            logged_in[x].response("message", message, logged_in[index+1])

    def sendNamestoThisClient(self):
        pass

    def sendHelpTexttoThisClient(self):
        help_content = "Help\n\n" + "This client console accepts commands: \n\n" + "login <username>: logs on the server with the given username.\n" + "logout: logs out of the server.\n" + "msg <message>: sends a message to the chatroom.\n" + "names: list the user in the chatroom.\n" + "help: lists this message.\n"

        self.response('info', help_content, '')

    def sendError(self):
        self.response('error', 'This is embarrassing! Type help for command reference.\n Are you logged in?', '')

    def response(self, responsetype, content, sender):
        try:
            # Get the timestamp for the time NOW
            timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

            # Get a string from a dict as a json-object
            payload = json.dumps({"timestamp": timestamp, "sender": sender, "response": responsetype, "content": content})

            # Check if we want to send to ALL connected clients, or just to one
            self.connection.send(payload)
        except:
            self.broken = True

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
