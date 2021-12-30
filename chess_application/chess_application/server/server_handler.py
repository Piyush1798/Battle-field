import socket 
import json
import threading
from object import response,request
from server_start import initialization
from server_network import network
class server:
    def __init__(self):
        with  open("server_config.cfg") as js:
            data=json.loads(js.read())
        self.host=data["host"]
        self.port=data["port"]
        self.img_id=dict()
        self.db=initialization()
        self.active()
    def thread_for_db(self,server_socket,client_socket):
        sr=network(server_socket,client_socket)
        request_obj=sr.receive()
        
        if request_obj.action=="authentication":
            
            ans=self.db.authenticate(request_obj.name,request_obj.password)
            resp=response(request_obj.image_id,request_obj.name,request_obj.action,request_obj.opponent,request_obj.piece_color,request_obj.turn,request_obj.request,authenticate=ans)
            #print(resp.authenticate)
            sr.send(resp)
        elif request_obj.action=="logout":
            if self.img_id.get(request_obj.image_id)!=None:
                del self.img_id[request_obj.image_id]
            self.db.log_out(request_obj.name)
            resp=response(request_obj.image_id,request_obj.name,request_obj.action,request_obj.opponent,request_obj.piece_color,request_obj.turn,request_obj.request)
            #print(resp.authenticate)
            sr.send(resp)
        elif request_obj.action=="get_available":
            if self.db.is_player_in_match(request_obj.name)!=None:
                obj=self.db.is_player_in_match(request_obj.name)
                if obj.player1==request_obj.name:
                    op=obj.player2
                else:
                    op=obj.player1
                resp=response(image_id=obj.game_id,name=request_obj.name,action=request_obj.action,opponent=op,piece_color=obj.piece_color,turn=obj.turn,request=request_obj.request,authenticate=self.db.authenticate(request_obj.name,request_obj.password))
                sr.send(resp)
            else:  
                ans=self.db.get_available_user()
                
                li=self.db.get_invited()
                list_r=li[0]
                list_s=li[1]
                if list_r.get(request_obj.name)==None:
                    list_r=list()
                else:
                    list_r=list(list_r[request_obj.name])
                if list_s.get(request_obj.name)==None:
                    list_s=list()
                else:
                    list_s=list(list_s[request_obj.name])
                resp=response(request_obj.image_id,request_obj.name,request_obj.action,request_obj.opponent,request_obj.piece_color,request_obj.turn,request_obj.request,authenticate=self.db.authenticate(request_obj.name,request_obj.password),request_sender_list=list_s,request_receiver_list=list_r,output=ans)
                sr.send(resp)
        elif request_obj.action=="invitation":
            self.db.update_request_receiver(request_obj.request_receiver,request_obj.request_sender)
            self.db.update_request_sender(request_obj.request_sender,request_obj.request_receiver)
            
            
            resp=response(request_obj.image_id,request_obj.name,request_obj.action,request_obj.opponent,request_obj.piece_color,request_obj.turn,request_obj.request,authenticate=self.db.authenticate(request_obj.name,request_obj.password))
            sr.send(resp)
        elif request_obj.action=="decline_user":
            self.db.delete_from_list(request_obj.request_sender,request_obj.request_receiver)
            resp=response(request_obj.image_id,request_obj.name,request_obj.action,request_obj.opponent,request_obj.piece_color,request_obj.turn,request_obj.request,authenticate=self.db.authenticate(request_obj.name,request_obj.password))
            sr.send(resp)
        elif request_obj.action=="accept_user":
            self.db.remove(request_obj.request_receiver)
            self.db.remove(request_obj.request_sender)
            id=self.db.update_match(request_obj.request_sender,request_obj.request_receiver)
            resp=response(request_obj.image_id,request_obj.name,request_obj.action,request_obj.opponent,request_obj.piece_color,request_obj.turn,request_obj.request,authenticate=self.db.authenticate(request_obj.name,request_obj.password))
            sr.send(resp)
        elif request_obj.action=="opponent_reader":
            obj=self.db.is_player_in_match(request_obj.name)
            print(obj)
            if obj==None:
                request_obj.image_id=""
                resp=response(request_obj.image_id, request_obj.name,request_obj.action,request_obj.opponent,request_obj.piece_color,request_obj.turn,request_obj.request,authenticate=self.db.authenticate(request_obj.name,request_obj.password))
                sr.send(resp)
            else:
                resp=response(image_id=obj.game_id,name=request_obj.name,action=request_obj.action,opponent=request_obj.opponent,piece_color=obj.piece_color,turn=obj.turn,request=request_obj.request,authenticate=self.db.authenticate(request_obj.name,request_obj.password))
                sr.send(resp)
        elif request_obj.action=="opponent_writer":
            obj=self.db.is_player_in_match(request_obj.name)
            print(obj)
            if obj==None:
                request_obj.image_id=""
                resp=response(request_obj.image_id,request_obj.name,request_obj.action,request_obj.opponent,request_obj.piece_color,request_obj.turn,request_obj.request,authenticate=self.db.authenticate(request_obj.name,request_obj.password))
                sr.send(resp)
            else:
                self.db.update_turn(request_obj.name,request_obj.opponent)
                obj=self.db.is_player_in_match(request_obj.name)
                resp=response(image_id=obj.game_id,name=request_obj.name,action=request_obj.action,opponent=request_obj.opponent,piece_color=obj.piece_color,turn=obj.turn,request=request_obj.request,authenticate=self.db.authenticate(request_obj.name,request_obj.password))
                sr.send(resp)
    def make_thread(self,server_socket,client_socket):
        #if request is user_specification
        to_recieve=100
        byte=b''
        while len(byte)<to_recieve:
            by=client_socket.recv(to_recieve-len(byte))   #size of request string 
            byte+=by
        req_size=int(byte.decode(encoding="utf-8").strip())
        


        recieved=0
        req_data=""
        request_type=""
        while recieved<req_size:
            if req_size-recieved<4029:
                to_recieve=req_size-recieved
            else:
                to_recieve=4096                        #here we receive request
            byte=b''
            while len(byte)<to_recieve:
                by=client_socket.recv(to_recieve-len(byte))
                #print(by)
                byte+=by
            req_data=byte.decode(encoding="utf-8")
            request_type+=req_data
            recieved+=to_recieve
        print(req_data)
        if req_data=="user_specification":
            t=threading.Thread(target=self.thread_for_db(server_socket,client_socket))
            

        else:
            to_recieve=100
            byte=b''
            while len(byte)<to_recieve:
                by=client_socket.recv(to_recieve-len(byte))   #here we recevie the image id
                byte+=by
            image_id=int(byte.decode(encoding="utf-8").strip())
            


            to_recieve=100
            byte=b''
            while len(byte)<to_recieve:
                by=client_socket.recv(to_recieve-len(byte))   #request type size
                byte+=by
            request_type_size=int(byte.decode(encoding="utf-8").strip())

            
            recieved=0
            req_data=""
            request_type=""
            while recieved<request_type_size:
                if request_type_size-recieved<4029:
                    to_recieve=request_type_size-recieved
                else:
                    to_recieve=4096                        #request type(read/write)
                byte=b''
                while len(byte)<to_recieve:
                    by=client_socket.recv(to_recieve-len(byte))
                    #print(by)
                    byte+=by
                req_data=byte.decode(encoding="utf-8")
                request_type+=req_data
                recieved+=to_recieve
            print(request_type)
            if  request_type=="read":
                js_string=json.dumps(self.img_id[image_id])
                client_socket.sendall(bytes(str(len(js_string)).ljust(100),"utf-8"))
                client_socket.sendall(bytes(js_string,"utf-8"))

            elif request_type=="write":
                grid_size=0
                to_recieve=100
                byte=b''
                while len(byte)<to_recieve:                       #here we receive the grid size
                    by=client_socket.recv(to_recieve-len(byte))
                    byte+=by
                grid_size=int(byte.decode(encoding="utf-8").strip())
                print(grid_size)
                recieved=0
                req_data=""
                grid=""
                while recieved<grid_size:
                    if grid_size-recieved<4029:
                        to_recieve=grid_size-recieved
                    else:                                            #here we reciev the grid
                        to_recieve=4096
                    byte=b''
                    while len(byte)<to_recieve:
                        by=client_socket.recv(to_recieve-len(byte))
                        #print(by)
                        byte+=by
                    req_data=byte.decode(encoding="utf-8")
                    grid+=req_data
                    recieved+=to_recieve
                
                
                grid=json.loads(grid)
                
                self.img_id[image_id]=grid
                    
                
            
      
        

        
    def active(self):
        server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        server_socket.bind((self.host,self.port))
        server_socket.listen()
        print(f"server is in listening mode at 1100")



        #take file name size
        while True:
            client_socket,client_socket_name=server_socket.accept()
            t=threading.Thread(target=self.make_thread(server_socket,client_socket))
        client_socket.close()
        server_socket.close()
server()