from spy_details import spy,friends,Spy,ChatMessage
from steganography.steganography import Steganography
from datetime import datetime
import csv

print 'Let\'s get started'

STATUS_MESSAGES=["Busy","At work"]

response= raw_input("Do you  want to continue as "+spy.salutation+" "+spy.name+ " (Y/N)?")


def load_friends():
    with open('friend.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            spy = Spy(row[0], row[1], row[2], row[3])
            friends.append(spy)


def start_chat(spy):
    load_friends()
    show_menu=True
    current_status_message = None
    while show_menu==True:
        menu_choices= "What do you want to do ? \n 1. Add a status update\n 2. Add a friend\n 3. Select a friend\n 4. Send a message\n 5. Read a message\n6. Closing Application"
        menu_choice= int(raw_input(menu_choices))
        if menu_choice==1:
           current_status_message= add_status(current_status_message)
        elif menu_choice==2:
            number_of_friends=add_friend()
            print "You have %d friends" %(number_of_friends)
        elif menu_choice==3:
            select_friend()
        elif menu_choice==4:
            send_message()
        elif menu_choice==5:
            read_message()
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

    Spy.name = raw_input("Please add your friend's name: ")
    Spy.salutation = raw_input("Are they Mr. or Ms.?: ")

    Spy.name = Spy.salutation + " " + Spy.name

    Spy.age = int(raw_input("Age?"))

    Spy.rating = float(raw_input("Spy rating?"))
    if len(Spy.name) > 0 and Spy.age > 12 and Spy.rating >= spy.rating:
        friends.append(Spy)
        print 'Friend Added!'

        with open('friend.csv', 'wb') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([Spy.name,Spy.salutation,Spy.age,Spy.rating])

    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

def select_friend():
  item_number = 0

  for friend in friends:
    print '%d %s' % ((item_number + 1), friend.name)

    item_number = item_number + 1

  friend_choice = input("Choose from your friends")
  friend_choice_position=friend_choice-1
  f = friends[friend_choice_position]
  return  f



def send_message():
    friend_choice= select_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)
    ch=ChatMessage(text,True)
    (friend_choice.chats).append(ch)
    if text=="SAVE ME"or text=="SOS":
        print "I am in danger. Please help me out ASAP"
    print "Your secret message is ready"


def read_message():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    output_path= "C:\Users\user\Desktop\Test1\%s"%(output_path)
    secret_text = Steganography.decode(output_path)
    if secret_text=="SAVE ME"or secret_text=="SOS":
        print "Your friend is in danger. Please help your friend"
    c= ChatMessage(secret_text,False)
    (sender.chats).append(c)
    print "Your secret message has been saved"


if response.upper()=="Y":
    print "App has started"
    start_chat(spy)
else:

    Spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(Spy.name) > 0:
        print 'Welcome ' + Spy.name + '. Glad to have you back with us.'
        Spy.salutation = raw_input("Should I call you Mister or Miss?: ")
        Spy.name = Spy.salutation + " " + Spy.name
        print "Alright " + Spy.name + ". I'd like to know a little bit more about you before we proceed..."
    else :
        print  "A spy needs to have a valid name. Try again please."

    Spy.age= (int)(raw_input(" What is your age? "))

    if Spy.age>12 and Spy.age<50:
        Spy.rating= (float)(raw_input(" what is your spy rating "))
        if Spy.rating > 4.5:
            print 'Great ace!'
        elif Spy.rating > 3.5 and Spy.rating <= 4.5:
            print 'You are one of the good ones.'
        elif Spy.rating >= 2.5 and Spy.rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'

        print "Authentication complete. Welcome " + Spy.name + " age: " + (str)(Spy.age) + " and rating of: " + (str)(
            Spy.rating) + " Proud to have you onboard"

    else:
        print "Please enter a vlaid age"
    start_chat(Spy)



