from .utils import Status_Codes

class Response:
    def __init__(self, status_code, headers, body):
        self.protocol = "HTTP/1.1"
        self.status_code = status_code
        self.reason_phrase = Status_Codes[status_code]
        self.headers = headers
        self.body = body
    

    def serialize(self):
        request_line = " ".join([self.protocol, f"{self.status_code}", self.reason_phrase])
        if "Content-Length" not in self.headers:
            self.headers["Content-Length"] = len(self.body.encode())
        headers = "".join([f"{key}: {value}\r\n" for key,value in self.headers.items()])
        response = "\r\n".join([request_line, headers, self.body]) 
        return response.encode()
