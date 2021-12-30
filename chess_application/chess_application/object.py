import json
class request:
    def __init__(self,image_id="",name="",password="",action="",opponent="",piece_color="",turn="",request="",request_sender="",request_receiver=""):
        self.image_id=image_id
        self.name=name
        self.password=password
        self.action=action
        self.opponent=opponent
        self.piece_color=piece_color
        self.turn=turn
        self.request=request
        self.request_sender=request_sender
        self.request_receiver=request_receiver
    def to_json(self):
        return json.dumps(self.__dict__)
    def from_json(js_string):
        string=json.loads(js_string)
        return request(string["image_id"],string["name"],string["password"],string["action"],string["opponent"],string["piece_color"],string["turn"],string["request"],string["request_sender"],string["request_receiver"])

class response:
    def __init__(self,image_id="",name="",password="",action="",opponent="",piece_color="",turn="",request="",authenticate=False,output="",request_sender_list="",request_receiver_list=""):
        self.image_id=image_id
        self.name=name
        self.authenticate=authenticate
        self.password=password
        self.action=action
        self.opponent=opponent
        self.piece_color=piece_color
        self.turn=turn
        self.request=request
        self.output=output
        self.request_sender_list=request_sender_list
        self.request_receiver_list=request_receiver_list
    def to_json(self):
        return json.dumps(self.__dict__)
    def from_json(js_string):
        string=json.loads(js_string)
        return response(string["image_id"],string["name"],string["password"],string["action"],string["opponent"],string["piece_color"],string["turn"],string["request"],string["authenticate"],string["output"],string["request_sender_list"],string["request_receiver_list"])