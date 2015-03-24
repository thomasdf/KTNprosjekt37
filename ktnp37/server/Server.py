# -*- coding: utf-8 -*-
import SocketServer
import json

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
                elif(received_dict["request"] == "logout"):
                    logout(self)
                elif(received_dict["request"] == "msg"):
                    message = (received_dict[0])['content']
                    sendMessagetoClients(message)
                elif(received_dict["request"] == "names"):
                    sendNamestoThisClient(self)
                elif(received_dict["request"] == "help"):
                    sendHelpTexttoThisClient(self)
                else:
                    sendError(self)
            elif(received_dict["request"] == "help"):
                sendHelpTexttoThisClient(self)
            elif(received_dict["request"] == "login"):
                    user_name = (received_dict[0])['content']
                    login(self, user_name)
            else:
                sendError(self)



def login(client, user_name):
    if(usernameValid(user_name)):
        logged_in.append(client)
        logged_in.append(user_name)
        response(client, "info", history, "")
        response(client, "info", "--------------\n logged in as ".append(user_name), client)
    else:
        sendError(client)

def logout(client):

def sendMessagetoClients(message):

def sendNamestoThisClient(client):

def sendHelpTexttoThisClient(client):

def sendError(client):

def response(responsetype, content, sender):

    


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
