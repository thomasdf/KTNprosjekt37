# -*- coding: utf-8 -*-
import SocketServer
import json
from time import gmtime, strftime

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

            if(self in logged_in):
                if((received_dict[0])['request'] == "login"):
                    user_name = (received_dict[0])['content']
                    login(self, user_name)
                elif((received_dict[0])['request'] == "logout"):
                    logout(self)
                elif((received_dict[0])['request'] == "msg"):
                    message = (received_dict[0])['content']
                    sendMessagetoClients(message)
                elif((received_dict[0])['request'] == "names"):
                    sendNamestoThisClient(self)
                elif((received_dict[0])['request'] == "help"):
                    sendHelpTexttoThisClient(self)
                else:
                    sendError(self)
            elif((received_dict[0])['request'] == "help"):
                sendHelpTexttoThisClient(self)
            else:
                sendError(self)



def login(client, user_name):

def logout(client):
    # Remove the client from the logged_in list
    index = logged_in.index(client)
    del logged_in[index:index+2]
    
    # Send a logout-respone to the client
    response(client, "info", "Successfully logged out.", "")
    
    # Disconnect the client
    client.connection.close()

def sendMessagetoClients(message):

def sendNamestoThisClient(client):

def sendHelpTexttoThisClient(client):

def sendError(client):

def response(client, responsetype, content, sender):
    # Get the timestamp for the time NOW
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    # Get a string from a dict as a json-object
    payload = json.dumps({"timestamp": timestamp, "sender": sender, "response": responsetype, "content": content})
    
    # --- START TESTPRINTING ---
    print payload
    # --- END TESTPRINTING ---

    # Check if we want to send to ALL connected clients, or just to one
    if (responsetype == "message"):
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
