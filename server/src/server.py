import threading
import socket
from .connection import Connection
from .router import Router


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
        # pyright eror is because of the case when match_route return not_found function which takes no arguments
        response = routing_output(request).encode()
        connection.respond(response)

    def start(self):
        try:
            while True:
                conn_socket, address = self.socket.accept()
                connection = Connection(conn_socket)
                t = threading.Thread(target=self.handle_request, args=(connection,))
                t.daemon = True
                t.start()

        except:
            self.socket.close()
