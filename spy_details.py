from datetime import datetime
import time

class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class ChatMessage:
    def __init__(self,message,sent_by_me):
        self.message=message
        t = datetime.now()
        t = time.mktime(t.timetuple())
        self.time=time.strftime("%I:%M %p",time.localtime(t))
        self.sent_by_me=sent_by_me

spy= Spy("Deepika","Ms.",21,5)
friend_one = Spy('Raja', 'Mr.', 27, 4.9)
friend_two = Spy('Mata Hari', 'Ms.', 21, 4.39)
friend_three = Spy('No', 'Dr.', 37, 4.95)

friends = [friend_one, friend_two, friend_three]
chat= ChatMessage("hello",True)
chats=[]