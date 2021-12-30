import json
from object import response
class chess_info:
    def __init__(self,game_id,opponent,user):
        self.game_id=game_id
        self.player1=opponent
        self.piece_color=dict()
        self.piece_color[opponent]="white"
        self.piece_color[user]="black"
        self.player2=user
        self.turn=opponent
        self.both_are_playing=True
class initialization:
    def __init__(self):
        with open("user_data.json") as el:
            df=el.read()
        self.members=json.loads(df)
        self.playing_users=set()
        self.logged_in_users=set()
        self.request_sender=dict()
        self.request_receiver=dict()
        self.create_match=dict()
        self.id_gen=1000
    def authenticate(self,user,password):
        if self.members.get(user)!=None:
            if self.members[user]==password:
                self.logged_in_users.add(user)
                print(self.logged_in_users)
                return True
        return False
    def update_turn(self,user,match):
        if self.create_match.get(user)==None:
            return
        obj=self.create_match[user]
        if obj.turn==user:
            obj.turn=match
    def is_player_in_match(self,user):
        if self.create_match.get(user)==None:
            return None
        return self.create_match[user]
    def update_request_sender(self,user,match):
        if user==match:
            return 
        if self.request_sender.get(user)==None:
            self.request_sender[user]=set()
        self.request_sender[user].add(match)
    def update_match(self,user,match):
        self.id_gen+=1
        
        
        obj=chess_info(str(self.id_gen),match,user)
        self.create_match[user]=obj
        self.create_match[match]=obj
        return self.id_gen
    def update_request_receiver(self,user,match):
        if user==match:
            return 
        if self.request_receiver.get(user)==None:
            self.request_receiver[user]=set()
        self.request_receiver[user].add(match)
    def delete_from_list(self,user,match):
        self.request_receiver[user].remove(match)
        self.request_sender[match].remove(user)
    def get_invited(self):
        return self.request_receiver,self.request_sender
    def get_available_user(self):
        if len(self.playing_users)>=1:
            s1=self.logged_in_users-self.playing_users
        else:
            s1=self.logged_in_users
        print(s1)
        return list(s1)
    def remove(self,user):
        
        
        if self.request_receiver.get(user)==None and  self.request_sender.get(user)==None:
            return 
        if self.request_receiver.get(user)!=None:
            del self.request_receiver[user]
        if self.request_sender.get(user)!=None:
            del self.request_sender[user]
        for i in self.request_receiver:
            if user in self.request_receiver[i]:
                self.request_receiver[i].remove(user)
        for i in self.request_sender:
            if user in self.request_sender[i]:
                self.request_sender[i].remove(user)
        self.playing_users.add(user)
    def remove_from_playing(self,user):
        #first check wether the user is present in playing or not
        if len(self.playing_users)>=1 and (user in self.playing_users):
            self.playing_users.remove(user)
    def log_out(self,user):
        print("ssd")
        if self.create_match.get(user)!=None:
            obj=self.create_match[user]
            pl1=obj.player1
            pl2=obj.player2
            del self.create_match[pl1]
            del self.create_match[pl2]
            self.remove_from_playing(pl1)
            self.remove_from_playing(pl2)
        
        if len(self.logged_in_users)>=1:
            self.logged_in_users.remove(user) #remove from logged in users
        self.remove_from_playing(user)
        if self.request_receiver.get(user)==None and  self.request_sender.get(user)==None:
            return 
        if self.request_receiver.get(user)!=None:
            del self.request_receiver[user]
        if self.request_sender.get(user)!=None:
            del self.request_sender[user]
        for i in self.request_receiver:
            if user in self.request_receiver[i]:
                self.request_receiver[i].remove(user)
        for i in self.request_sender:
            if user in self.request_sender[i]:
                self.request_sender[i].remove(user)
            
