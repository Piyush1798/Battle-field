import socket 
import json
import tkinter
class new_point(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.geometry("700x700")
        
        self.after(1000,self.client_sender)
    def client_sender(self):
        client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect(("localhost",1110))
        lst=[[123,345,645],[232,233,23]]
        strr=json.dumps(lst)
        client_socket.sendall(bytes(str(123).ljust(100),"utf-8"))
        client_socket.sendall(bytes(str(len(strr)).ljust(100),"utf-8"))
        client_socket.sendall(bytes(strr,"utf-8"))
        grid_size=0
        to_recieve=100
        byte=b''
        while len(byte)<to_recieve:                       #here we receive the grid size
            by=client_socket.recv(to_recieve-len(byte))
            byte+=by
        grid_size=int(byte.decode(encoding="utf-8").strip())
        #take file name




        #take file
        recieved=0
        req_data=""
        grid=""
        while recieved<grid_size:
            if grid_size-recieved<4029:
                to_recieve=grid_size-recieved
            else:
                to_recieve=4096
            byte=b''
            while len(byte)<to_recieve:
                by=client_socket.recv(to_recieve-len(byte))
                #print(by)
                byte+=by
            req_data=byte.decode(encoding="utf-8")
            grid+=req_data
            
            
            
            recieved+=to_recieve
        print(grid)
        self.after(1000,self.client_sender)
l=new_point()
l.mainloop()