import socket
from object import request,response
class network:
    def __init__(self,server_socket,client_socket):
        self.server_socket=server_socket
        self.client_socket=client_socket
    def receive(self):
        request_size=0
        to_recieve=100
        byte=b''
        while len(byte)<to_recieve:                       #here we receive the request string size
            by=self.client_socket.recv(to_recieve-len(byte))
            byte+=by
        request_size=int(byte.decode(encoding="utf-8").strip())
        print(request_size)
        recieved=0
        req_data=""
        req_js=""
        while recieved<request_size:
            if request_size-recieved<4096:
                to_recieve=request_size-recieved
            else:
                to_recieve=4096
            byte=b''
            while len(byte)<to_recieve:
                by=self.client_socket.recv(to_recieve-len(byte))
                #print(by)
                byte+=by
            req_data=byte.decode(encoding="utf-8")
            req_js+=req_data
            recieved+=to_recieve
        
        print(req_js)
        return request.from_json(req_js)
    def send(self,response_obj):
        js_string=response_obj.to_json()
        self.client_socket.sendall(bytes(str(len(js_string)).ljust(100),"utf-8"))
        self.client_socket.sendall(bytes(js_string,"utf-8"))
        