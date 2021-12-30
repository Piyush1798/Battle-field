import socket
from object import response
class network:
    def __init__(self):
        self.client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client_socket.connect(("localhost",1110))
    def send(self,request_obj):
        js=request_obj.to_json()
        self.client_socket.sendall(bytes(str(len("user_specification")).ljust(100),"utf-8"))#sended the json string  size
        self.client_socket.sendall(bytes(str("user_specification"),"utf-8"))   #sended the json string 
        self.client_socket.sendall(bytes(str(len(js)).ljust(100),"utf-8"))#sended the json string  size
        self.client_socket.sendall(bytes(str(js),"utf-8"))   #sended the json string 
        response_size=0
        to_recieve=100
        byte=b''
        while len(byte)<to_recieve:                       #here we receive the grid size
            by=self.client_socket.recv(to_recieve-len(byte))
            byte+=by
        response_size=int(byte.decode(encoding="utf-8").strip())

        recieved=0
        req_data=""
        req_js=""
        while recieved<response_size:
            if response_size-recieved<4029:
                to_recieve=response_size-recieved
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
        self.client_socket.close()
        return response.from_json(req_js)
        