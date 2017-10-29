print 'Let\'s get started'
spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
if len(spy_name) > 0:
    print 'Welcome ' + spy_name + '. Glad to have you back with us.'
    spy_salutation = raw_input("Should I call you Mister or Miss?: ")
    spy_name = spy_salutation + " " + spy_name
    print "Alright " + spy_salutation + " " + spy_name + ". I'd like to know a little bit more about you before we proceed..."
else :
    print  "A spy needs to have a valid name. Try again please."