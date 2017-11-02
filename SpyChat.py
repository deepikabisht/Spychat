from spy_details import spy_name,spy_salutation,spy_age,spy_rating

print 'Let\'s get started'

STATUS_MESSAGES=["Busy","At work"]
response= raw_input("Do you  want to continue as "+spy_salutation+" "+spy_name+ " (Y/N)?")


def start_chat(spy_name,spy_age,spy_rating):
    show_menu=True
    current_status_message = None
    while show_menu==True:
        menu_choices= "What do you want to do ? \n 1. Add a status update\n 2. Closing Application"
        menu_choice= int(raw_input(menu_choices))
        if menu_choice==1:
           current_status_message= add_status(current_status_message)
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



if response.upper()=="Y":
    print "App has started"
    start_chat(spy_name,spy_age,spy_rating)
else:

    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy_name) > 0:
        print 'Welcome ' + spy_name + '. Glad to have you back with us.'
        spy_salutation = raw_input("Should I call you Mister or Miss?: ")
        spy_name = spy_salutation + " " + spy_name
        print "Alright " + spy_salutation + " " + spy_name + ". I'd like to know a little bit more about you before we proceed..."
    else :
        print  "A spy needs to have a valid name. Try again please."

    spy_age= 0
    spy_rating= 0.0
    spy_is_online = False
    spy_age= (int)(raw_input(" What is your age? "))

    if spy_age>12 and spy_age<50:
        spy_rating= (float)(raw_input(" what is your spy rating "))
        if spy_rating > 4.5:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'
        spy_is_online = True
        print "Authentication complete. Welcome " + spy_name + " age: " + (str)(spy_age) + " and rating of: " + (str)(
        spy_rating) + " Proud to have you onboard"

    else:
        print "Please enter a vlaid age"
    start_chat(spy_name, spy_age, spy_rating)



