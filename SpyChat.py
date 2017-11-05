from spy_details import spy
from steganography.steganography import Steganography
from datetime import datetime

print 'Let\'s get started'

STATUS_MESSAGES=["Busy","At work"]
friends=[]
response= raw_input("Do you  want to continue as "+spy['salutation']+" "+spy['name']+ " (Y/N)?")


def start_chat(spy):
    show_menu=True
    current_status_message = None
    while show_menu==True:
        menu_choices= "What do you want to do ? \n 1. Add a status update\n 2. Add a friend\n3. Closing Application"
        menu_choice= int(raw_input(menu_choices))
        if menu_choice==1:
           current_status_message= add_status(current_status_message)
        elif menu_choice==2:
            number_of_friends=add_friend()
            print "You have % friends" %(number_of_friends)
        elif menu_choice==3:
            n=select_friend()
            print n
        else:
            show_menu=False
    print "Thank you for using spychat"

def add_status(current_status_message):
    if current_status_message != None:
        print "Your Current status message is " + current_status_message + "\n"
    else:
        print "You  don't have any current status message"
    default= raw_input("Do you want to select from older status?(y/n)")
    if default.upper()== "N":
        new_status_message= raw_input("What status message you want to set?")
        if len(new_status_message)>0:
            updated_status_message=new_status_message
            STATUS_MESSAGES.append(updated_status_message)
    elif default.upper()== "Y":
        item_position=1
        for message in STATUS_MESSAGES:
            print str(item_position)+" "+message
            item_position=item_position+1
        message_selection= int(raw_input("\nChoose from the above staus messages"))
        if len(STATUS_MESSAGES)>= message_selection:
            updated_status_message=STATUS_MESSAGES[message_selection-1]
    return updated_status_message

def add_friend():
    new_friend={
        'name':'',
        'salutation':'',
        'age':0,
        'rating':0.0,
        'chats':[]

    }
    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = int(raw_input("Age?"))

    new_friend['rating'] = float(raw_input("Spy rating?"))
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print friends
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

def select_friend():
  item_number = 0

  for friend in friends:
    print '%d %s' % ((item_number + 1), friend['name'])

    item_number = item_number + 1

  friend_choice = input("Choose from your friends")
  friend_choice_position=friend_choice-1
  return friend_choice_position

def send_message():
    friend_choice= select_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)
    new_chat={
        "message":text,
        "time":datetime.now(),
        "sent_by_me":True
    }
    friends[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready"


def read_message():
    sender = select_friend()
    output_path = input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }
    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved"


if response.upper()=="Y":
    print "App has started"
    start_chat(spy)
else:

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy['name']) > 0:
        print 'Welcome ' + spy['name'] + '. Glad to have you back with us.'
        spy['salutation'] = raw_input("Should I call you Mister or Miss?: ")
        spy['name'] = spy['salutation'] + " " + spy['name']
        print "Alright " + spy['salutation'] + " " + spy['name'] + ". I'd like to know a little bit more about you before we proceed..."
    else :
        print  "A spy needs to have a valid name. Try again please."

    spy['age']= 0
    spy['rating']= 0.0
    spy['is_online'] = False
    spy['age']= (int)(raw_input(" What is your age? "))

    if spy['age']>12 and spy['age']<50:
        spy['rating']= (float)(raw_input(" what is your spy rating "))
        if spy['rating'] > 4.5:
            print 'Great ace!'
        elif spy['rating'] > 3.5 and spy['rating'] <= 4.5:
            print 'You are one of the good ones.'
        elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'
        spy['is_online'] = True
        print "Authentication complete. Welcome " + spy['name'] + " age: " + (str)(spy['age']) + " and rating of: " + (str)(
            spy['rating']) + " Proud to have you onboard"

    else:
        print "Please enter a vlaid age"
    start_chat(spy)



