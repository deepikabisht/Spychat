print 'Let\'s get started'
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
spy_is_online = True
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
else:
    print "Please enter a vlaid age"


if spy_is_online == True:
     print "Authentication complete. Welcome " + spy_name + " age: " + (str)(spy_age) + " and rating of: " + (str)(spy_rating) + " Proud to have you onboard"

