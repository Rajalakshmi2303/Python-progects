print("chatbot(type 'bye' to exit)")
while true:
    user=input("you; ").lower( )
    if(user=='hi'or user=='hello'):
        print("bot: hello! how can I help you")
    elif(user=='how are you'):
        print("bot: I am fine! what about you?")
    elif(user=='what is your name'):
        print("bot:I am your simple chatbot")
    elif(user=='bye'):
        print("bot:bye! have a nice day")
    else:
        print("bot: sorry I don't understand")