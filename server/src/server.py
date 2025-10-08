import threading
import socket
from .connection import Connection
from .router import Router
from .response import Response
from .utils import not_found

class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024)
        self.socket.bind(("localhost", 2002))
        self.socket.listen(100)
        self.router = Router()
     

    def handle_request(self, connection):
        request = connection.parse_request()
        routing_output = self.router.match_route(request)
        body, status_code, headers = routing_output(request)
        response = Response(headers=headers, body=body, status_code=status_code)
        if request.is_old_protocol() is True:
            print("identified as old protocol")
            response.protocol = "HTTP/1.0"
            if request.close_connection_1_0() is True:
                print("client is asking to close connection")
                connection.respond(response.serialize(), request)
                return
            print("client is asking to reuse connection")
            response.headers["Connection"] = "keep-alive"
            connection.respond(response.serialize(), request)
        else:
            if request.close_connection() == True:
                response.headers["Connection"] = "close"
                connection.respond(response.serialize(), request)
                return
            response.headers["Connection"] = "keep-alive"
            connection.respond(response.serialize(), request)
            self.handle_request(connection)


    def start(self):
        try:
            while True:
                # a new connection is created!
                conn_socket, address = self.socket.accept()
                connection = Connection(conn_socket)
                t = threading.Thread(target=self.handle_request, args=(connection,))
                t.daemon = True
                t.start()

        except:
            self.socket.close()
