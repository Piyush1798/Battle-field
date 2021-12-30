from object import response ,request
from client_network import network
from tkinter import END
import tkinter
from move_validator import move_validator
from time import time
import socket
from object import response,request
import json
import tkinter.messagebox
class chess_board(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.valid_path=[]
        self.check_mate=[]
        self.img_id=list()
        self.image_list=list()
        self.block=list()
        self.list_in_user=list()
        self.ui_turn_id=None
        self.parent=()
        self.heading_address=None
        self.buttom_address=None
        self.geometry("1210x750")
        self.fr=None
        self.build_title()
        self.turn_list_head=list()
        self.turn_list_bottom=list()
        self.can=tkinter.Canvas(self,width=600,height=600,bg="blue")
        self.can.grid(row=1,column=0)
        self.user=None
        self.password=None
        self.list_of_online_users=list()
        self.list_of_requested_users=list()
        self.matrix=self.load_data()
        self.dic=self.load_dict()
        self.verify_user()
        self.initialize_game()
        self.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.button=list()
        self.get_available_after=None
    def build_title(self):
        self.heading=tkinter.Canvas(self,width=600,height=50,bg="light steel blue")
        self.heading_address=self.heading.create_text(300,20,fill="black",font="Times 20 bold",text="WELCOME TO BATTLE FIELD!!")
        self.heading.grid(row=0,column=0)
    def build_bottom(self):
        self.bottom=tkinter.Canvas(self,width=600,height=50,bg="light steel blue")
        self.bottom_address=self.bottom.create_text(300,20,fill="black",font="Times 20 bold",text="WELCOME TO BATTLE FIELD!!")
        self.bottom.grid(row=2,column=0)
    def create_table(self,output,request_sender_list,request_receiver_list):

        # take the data 
     
        if len(request_sender_list)>=1:
            output=set(output)-set(request_sender_list)
            output=list(output)
        if len(request_receiver_list)>=1:
            output=set(output)-set(request_receiver_list)
            output=list(output)

        count=1
        lst=list()
        lst_sen=list()
        lst_rec=list()
        for i in output:
            if self.user==i:
                continue
            lst.append((count,i))
            count+=1
        for j in request_receiver_list:
            lst_rec.append((count,j))
            count+=1
        for j in request_sender_list:
            lst_sen.append((count,j))
            count+=1

        # find total number of rows and 
        # columns in list 
        self.heading_for_frame=tkinter.Canvas(self,width=600,height=50,bg="light steel blue",bd=0)
        self.heading_for_frame.create_text(300,20,fill="black",font="Times 20 bold",text="LIST OF ONLINE USERS!!")
        self.heading_for_frame.grid(row=0,column=1)
        self.fr=tkinter.Frame(self,width=600,height=600,bg="alice blue")
        self.fr.grid(row=1,column=1,sticky='Nw')

        total_columns=total_rows=0
        if len(lst)>=1:
            total_rows = len(lst) 
            total_columns = len(lst[0]) 
            
        print(lst,lst_rec,lst_sen)
        
		# code for creating table of available online user
        
        self.button=list()
        row_number=0
        for i in range(0,total_rows):
            padx_=0
            pady_=0
            for j in range(0,total_columns):
                self.e =tkinter.Entry(self.fr, width=25,fg='black',font=('Arial',12,'bold'),bg="gray87",bd=0) 
                self.e.grid(row=row_number, column=j,padx=padx_,pady=pady_,sticky='W') 
                self.e.insert(END, lst[i][j])
                self.list_in_user.append(self.e)
            padx_=10
            pady_=10
            self.btn=tkinter.Button(self.fr,text="invite",fg="black",bd=2,font=('Arial',12,'bold'),activebackground="mint cream",bg="cyan")
            self.btn.configure(command=lambda bu=lst[i][1]:self.send_invite(bu))
            self.btn.grid(row=row_number,column=4,padx=padx_,pady=pady_)
            self.list_in_user.append(self.btn)
            row_number+=1
        total_columns=total_rows=0

        if len(lst_rec)>=1:
            total_rows = len(lst_rec) 
            total_columns = len(lst_rec[0]) 
            
		# code for creating table available request receiver
        
        for i in range(0,total_rows):
            padx_=0
            pady_=0
            for j in range(0,total_columns):
                
                self.e =tkinter.Entry(self.fr, width=25,fg='black',font=('Arial',12,'bold'),bg="gray87",bd=0) 
                self.e.grid(row=row_number, column=j,padx=padx_,pady=pady_,sticky='W') 
                self.e.insert(END, lst_rec[i][j])
                self.list_in_user.append(self.e)
            padx_=10
            pady_=10
            self.btn=tkinter.Button(self.fr,text="accept",fg="black",bd=2,font=('Arial',12,'bold'),activebackground="mint cream",bg="lawn green")
            self.btn.configure(command=lambda bu=lst_rec[i][1]:self.accept_user(bu))
            self.btn.grid(row=row_number,column=4,padx=padx_,pady=pady_)
            self.list_in_user.append(self.btn)
            #button for declining the user
            padx_=1
            pady_=1
            self.btn=tkinter.Button(self.fr,text="decline",fg="black",bd=2,font=('Arial',12,'bold'),activebackground="mint cream",bg="tomato")
            self.btn.configure(command=lambda bu=lst_rec[i][1]:self.decline_user(bu))
            self.btn.grid(row=row_number,column=5,padx=padx_,pady=pady_)
            self.list_in_user.append(self.btn)
            row_number+=1
        total_columns=total_rows=0

        if len(lst_sen)>=1:
            total_rows = len(lst_sen) 
            total_columns = len(lst_sen[0]) 
            
		# code for creating table availble request sender
        
        for i in range(0,total_rows):
            pady_=0
            padx_=0
            for j in range(0,total_columns):
                
                self.e =tkinter.Entry(self.fr, width=25,fg='black',font=('Arial',12,'bold'),bg="gray87",bd=0) 
                self.e.grid(row=row_number, column=j,padx=padx_,pady=pady_,sticky='W')
                self.e.insert(END, lst_sen[i][j])
                self.list_in_user.append(self.e)
            padx_=10
            pady_=10
            self.btn=tkinter.Button(self.fr,text="invited",fg="black",bd=2,font=('Arial',12,'bold'),activebackground="mint cream",bg="mint cream")
            
            self.btn.grid(row=row_number,column=4,padx=padx_,pady=pady_)
            self.list_in_user.append(self.btn)
            row_number+=1
            

    def accept_user(self,user):
        rs=request(name=self.user, password=self.password,action="accept_user",request_sender=self.user,request_receiver=user)
        nt=network()
        response_obj=nt.send(rs)
    def decline_user(self,user):
        rs=request(name=self.user, password=self.password,action="decline_user",request_sender=self.user,request_receiver=user)
        nt=network()
        response_obj=nt.send(rs)
    def send_invite(self,player):
        rs=request(name=self.user, password=self.password,action="invitation",request_sender=self.user,request_receiver=player)
        nt=network()
        response_obj=nt.send(rs)
    def delete_table(self):
        if self.fr!=None:
            for i in self.list_in_user:
                i.destroy()
            self.fr.destroy()

    def on_closing(self):
        rs=request(name=self.user, password=self.password,action="logout")
        nt=network()
        print("Sds")
        response_obj=nt.send(rs)
        self.destroy()
    def on_closing2(self):
        rs=request(name=self.user, password=self.password,action="logout")
        nt=network()
        print("Sds")
        response_obj=nt.send(rs)
    def get_available_user(self):
        rs=request(name=self.user, password=self.password,action="get_available")
        nt=network()
        response_obj=nt.send(rs)
        if response_obj.image_id!="":
            print(response_obj.image_id)
            self.after_cancel(self.get_available_after)
            self.delete_table()
            self.game_id=response_obj.image_id
            self.opponent=response_obj.opponent
            self.turn=response_obj.turn
            self.color_piece=response_obj.piece_color[self.user]
            self.write_request_sender()
            self.add_event()
            self.create_ui_for()
            self.after(1000,self.client_sender)
        else:    
            self.delete_table()
            self.list_of_online_users=response_obj.output
            self.create_table(self.list_of_online_users,response_obj.request_sender_list,response_obj.request_receiver_list)
            self.get_available_after=self.after(1500,self.get_available_user)
    def verify_user(self):
        name=input("input user name")
        password=input("input user pass")
        rs=request(name=name, password=password,action="authentication")
        nt=network()
        response_obj=nt.send(rs)
        if response_obj.authenticate==False:
            raise Exception("please enter valid user name password")
        self.title(name)
        self.user=name
        self.password=password
        self.get_available_user()
        self.after(1500,self.get_available_user)
    
    def re_enter_in_lobby(self):
        self.valid_path=[]
        self.check_mate=[]
        self.img_id=list()
        self.image_list=list()
        self.block=list()
        self.list_in_user=list()
        self.ui_turn_id=None
        self.parent=()
        self.heading_address=None
        self.buttom_address=None
        self.geometry("1210x750")
        self.fr=None
        self.build_title()
        self.turn_list_head=list()
        self.turn_list_bottom=list()
        self.can=tkinter.Canvas(self,width=600,height=600,bg="blue")
        self.can.grid(row=1,column=0)

        self.list_of_online_users=list()
        self.list_of_requested_users=list()
        self.matrix=self.load_data()
        self.dic=self.load_dict()
       
        
        rs=request(name=self.user, password=self.password,action="authentication")
        nt=network()
        response_obj=nt.send(rs)
        if response_obj.authenticate==False:
            raise Exception("please enter valid user name password")
        self.initialize_game()
        self.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.button=list()
        self.get_available_after=None
        self.get_available_user()
        self.after(1500,self.get_available_user)
    def find_validation(self,event):
        print(event.x,event.y)
        x=int(event.x/75)
        y=int(event.y/75)
        
        
        if x<8 and y<8 and x>=0 and y>=0: #this will be not null if and only if user has its turn 
            if self.turn==self.user :
                return (y,x)
            
            
        return (None,None)
    def create_ui_for(self):
        #here first we change the heading
        print(self.color_piece)
        self.heading_for_frame.delete('all')
        self.geometry(f"{600}x{750}")
        self.build_bottom()
        if self.color_piece=="white":
            self.heading.create_rectangle(0,0,20,20,fill="white")
            self.heading.delete(self.heading_address)
            self.heading.create_text(40,10,fill="black",font=('Arial',12,'bold'),text=self.user)
            self.bottom.create_rectangle(0,0,20,20,fill="black")
            self.bottom.delete(self.bottom_address)
            self.bottom.create_text(40,10,fill="black",font=('Arial',12,'bold'),text=self.opponent)
            
        else:
            self.heading.create_rectangle(0,0,20,20,fill="white")
            self.heading.delete(self.heading_address)
            self.heading.create_text(40,10,fill="black",font=('Arial',12,'bold'),text=self.opponent)
            
            self.bottom.create_rectangle(0,0,20,20,fill="black")
            self.bottom.delete(self.bottom_address)
            self.bottom.create_text(40,10,fill="black",font=('Arial',12,'bold'),text=self.user)
            
        
    def update_ui_turn(self):
        for i in self.turn_list_head:
            self.heading.delete(i)
        for i in self.turn_list_bottom:
            self.bottom.delete(i)
        if self.turn==self.user:
            stri="its your turn "+self.user
            if self.color_piece=="white":
                self.turn_list_head.append(self.heading.create_text(300,20,fill="black",font=('Arial',12,'bold'),text=stri))
            else:
                self.turn_list_bottom.append(self.bottom.create_text(300,20,fill="black",font=('Arial',12,'bold'),text=stri))
        else:
            stri="its your opponent's turn "+self.opponent
            if self.color_piece=="white":
                self.turn_list_head.append(self.heading.create_text(300,20,fill="black",font=('Arial',12,'bold'),text=stri))
            else:
                self.turn_list_bottom.append(self.bottom.create_text(300,20,fill="black",font=('Arial',12,'bold'),text=stri))
          
    def show_match_summary(self,winner):
       
        if winner==self.user:
            
            response=tkinter.messagebox.askokcancel("Ask Question","congratulations!! you win the game do you want to return to lobby")
            if response==True:
                self.on_closing2()
                #return to the lobby
                self.re_enter_in_lobby()
            else:
                self.on_closing()
                #delete the window
            #appear a message box show that opponenent left the room
            #reinitialize on game or destroy the window
            return
        else:
            response=tkinter.messagebox.askokcancel("Ask Question","sorry!! you lost the game do you want to return to lobby")
            if response==True:
                self.on_closing2()
                #return to the lobby
                self.re_enter_in_lobby()
            else:
                self.on_closing()
                #delete the window
            #appear a message box show that opponenent left the room
            #reinitialize on game or destroy the window
            return
    def check_winner(self):
        white_king_present=False
        black_king_present=False
        for i in range(0,8):
            for j in range(0,8):
                if self.matrix[i][j]=="kw":
                    white_king_present=True
                if self.matrix[i][j]=="kb":
                    black_king_present=True
        if white_king_present==True and black_king_present==True:
            return None
        if white_king_present==False:
            if self.color_piece=="white":
                return self.opponent
            else:
                return self.user
        if black_king_present==False:
            if self.color_piece=="black":
                return self.opponent
            else:
                return self.user
        return None
    def client_sender(self):
        rs=request(name=self.user, password=self.password,action="opponent_reader",opponent=self.opponent,image_id=self.game_id,piece_color=self.color_piece,turn=self.turn)
        nt=network()
        response_obj=nt.send(rs)
        if response_obj.image_id=="":
            
            response=tkinter.messagebox.askokcancel("Ask Question","opponent has left the game do you wish to go to the lobby")
            if response==True:
                #return to the lobby
                self.on_closing2()
                self.re_enter_in_lobby()
            else:
                self.on_closing2()
                self.destroy()
                #delete the window
            #appear a message box show that opponenent left the room
            #reinitialize on game or destroy the window
            return
        
        self.turn=response_obj.turn
        self.update_ui_turn()
        client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect(("localhost",1110))
        lst=self.matrix
        strr=json.dumps(lst)
        client_socket.sendall(bytes(str(len("chess_specification")).ljust(100),"utf-8"))#sended the pre_specification size
        client_socket.sendall(bytes(str("chess_specification"),"utf-8"))   #sended the pre specification
        client_socket.sendall(bytes(str(self.game_id).ljust(100),"utf-8"))#sended the game id
        client_socket.sendall(bytes(str(len("read")).ljust(100),"utf-8"))#sended the request_size
        client_socket.sendall(bytes(str("read"),"utf-8"))#sended the request
       
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
        
        grid=json.loads(grid)
        self.matrix=grid
        self.initialize_game()
        client_socket.close()
        winner=self.check_winner()
        if winner!=None:
            self.show_match_summary(winner)
            return
        self.after(1000,self.client_sender)
        


    def write_request_sender(self):
        #before sending the write request check if game exist or not
        rs=request(name=self.user, password=self.password,action="opponent_writer",opponent=self.opponent,image_id=self.game_id,piece_color=self.color_piece,turn=self.turn)
        nt=network()
        
        
        response_obj=nt.send(rs)
        if response_obj.image_id=="":
            #game id not found at server so not doing any write request
            return
        client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect(("localhost",1110))
        lst=self.matrix
        strr=json.dumps(lst)
        
        client_socket.sendall(bytes(str(len("chess_specification")).ljust(100),"utf-8"))#sended the pre_specification size
        client_socket.sendall(bytes(str("chess_specification"),"utf-8"))   #sended the pre specification

        client_socket.sendall(bytes(str(self.game_id).ljust(100),"utf-8"))#sended the game id
        client_socket.sendall(bytes(str(len("write")).ljust(100),"utf-8"))#sended the request_size
        client_socket.sendall(bytes(str("write"),"utf-8"))   #sended the request
        client_socket.sendall(bytes(str(len(strr)).ljust(100),"utf-8"))
        client_socket.sendall(bytes(strr,"utf-8"))
        client_socket.close()

    def next_move(self,event):
        x,y=self.find_validation(event)
        
        if x!=None and y!=None:
            
            if True:
                flag=0
                if len(self.valid_path) >0 or len(self.check_mate)>0:
                    
                    for i in self.valid_path:
                        if x==i[0] and y==i[1]:
                            flag=1
                            print(self.matrix[x][y])
                            print(self.valid_path,self.check_mate)
                            par_x=self.parent[0]
                            par_y=self.parent[1]
                            #self.can.delete(self.img_id[par_x][par_y]) #delete the old 
                            #self.img_id[x][y]=self.can.create_image(y*75,x*75,anchor="nw",image=self.dic[self.matrix[par_x][par_y]])#draw the new
                            
                            self.matrix[x][y]=self.matrix[par_x][par_y]
                            self.matrix[par_x][par_y]=None
                            self.img_id[par_x][par_y]=None
                            self.write_request_sender() 
                            #code for movement

                    for i in self.check_mate:
                        if x==i[0] and y==i[1]:
                            flag=1
                            par_x=self.parent[0]
                            par_y=self.parent[1]
                            
                            self.matrix[x][y]=None
                            self.can.delete(self.img_id[x][y])
                            self.can.delete(self.img_id[par_x][par_y])
                            self.img_id[x][y]=self.can.create_image(y*75,x*75,anchor="nw",image=self.dic[self.matrix[par_x][par_y]])
                            
                            self.matrix[x][y]=self.matrix[par_x][par_y]
                            self.matrix[par_x][par_y]=None
                            self.img_id[par_x][par_y]=None
                            self.write_request_sender() 
                            #code for repacement
                    
                    self.check_mate=[]
                    self.valid_path=[]
                    self.parent=()

                
                    
                if flag==0 and self.matrix[x][y]!=None:
                    if self.matrix[x][y][len(self.matrix[x][y])-1]!=self.color_piece[0]:
                        return
                    obj=move_validator
                    
                    self.valid_path=obj.validate(self.matrix,x,y)[0]
                    self.check_mate=obj.validate(self.matrix,x,y)[1]
                    self.parent=(x,y)
                    print(self.matrix[x][y])
                    print(self.valid_path,self.check_mate)

    def add_event(self):
        self.can.bind('<Button-1>',self.next_move)

    def initialize_game(self):
        
        for i in self.image_list:
            self.can.delete(i)
        for i in self.block:
            self.can.delete(i)
        self.can.delete('all')
        x=0
        x_cor=0
        for i in range(8):
            y_cor=0
            if i%2==1:
                    x+=1
            id_l=list()
            for j in range(8):
                
                if x%2==0:
                    ll=self.can.create_rectangle(y_cor+75*j,75*i,y_cor+75*j+75,75*i+75,fill="white")
                    self.block.append(ll)
                else:
                    ll=self.can.create_rectangle(y_cor+75*j,75*i,y_cor+75*j+75,75*i+75,fill="black")
                    self.block.append(ll)
                x+=1
                
                if self.matrix[i][j]!=None:
                    id_1=self.can.create_image(75*j,75*i,anchor="nw",image=self.dic[self.matrix[i][j]])
                    self.image_list.append(id_1)
                    id_l.append(id_1)
                else:
                    id_l.append(None)
                self.img_id.append(id_l)
            if i%2==1:
                    x-=1
        
        

    def load_dict(self):
        s=dict()
        s["bw"]=tkinter.PhotoImage(file="bw.png")
        s["bb"]=tkinter.PhotoImage(file="bb.png")
        s["kb"]=tkinter.PhotoImage(file="kb.png")
        s["kw"]=tkinter.PhotoImage(file="kw.png")
        s["ktw"]=tkinter.PhotoImage(file="ktw.png")
        s["ktb"]=tkinter.PhotoImage(file="ktb.png")
        s["pb"]=tkinter.PhotoImage(file="pb.png")
        s["pw"]=tkinter.PhotoImage(file="pw.png")
        s["qw"]=tkinter.PhotoImage(file="qw.png")
        s["qb"]=tkinter.PhotoImage(file="qb.png")
        s["rw"]=tkinter.PhotoImage(file="rw.png")
        s["rb"]=tkinter.PhotoImage(file="rb.png")
        return s
    def load_data(self):
        x=list()
        for i in range(8):
            y=list()
            for z in range(8):
                y.append(None)
            x.append(y)
        x[0][0]="rw"
        x[0][1]="ktw"
        x[0][2]="bw"
        x[0][3]="kw"
        x[0][4]="qw"
        x[0][5]="bw"
        x[0][6]="ktw"
        x[0][7]="rw"
        x[1][0]="pw"
        x[1][1]="pw"
        x[1][2]="pw"
        x[1][3]="pw"
        x[1][4]="pw"
        x[1][5]="pw"
        x[1][6]="pw"
        x[1][7]="pw"
        
        x[7][0]="rb"
        x[7][1]="ktb"
        x[7][2]="bb"
        x[7][3]="kb"
        x[7][4]="qb"
        x[7][5]="bb"
        x[7][6]="ktb"
        x[7][7]="rb"
        x[6][0]="pb"
        x[6][1]="pb"
        x[6][2]="pb"
        x[6][3]="pb"
        x[6][4]="pb"
        x[6][5]="pb"
        x[6][6]="pb"
        x[6][7]="pb"
        return x
    

cb=chess_board()
cb.protocol("WM_DELETE_WINDOW",cb.on_closing)
cb.mainloop()
