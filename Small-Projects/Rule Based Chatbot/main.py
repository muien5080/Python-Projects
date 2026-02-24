# Rule Based chatbot

import datetime

print("Welcome, To the rule-based chatbot")
user = 'Mohammed Muien'
now = datetime.datetime.now().hour
def greet():
    if 5 <= now <= 11:
        print("Good Morning,",user)
    elif 12 <= now <= 18:
        print("Good Afternoon,",user)
    else:
        print("Good Evening,",user)
greet()

# Creating Bot Memory in form of dictionary
 
print("You Can Ask Me About Weather, Time, Date, and Calculator")

responses = {
    'time': datetime.datetime.now().time(),
    'date': datetime.datetime.now().date(),
    'weather': 'Sunny',
    'calculator': 'I Can Help You With Calculator',
    'name' : user,
    'hi' : 'Hello, How Can I Help You',
    'hello' : 'Hi, How Can I Help You',
    'happy' : 'I am Happy To Help You',
    'sad' : 'I am Sad To Help You',
    'angry' : 'I am Angry To Help You',
    'bye' : 'Bye, Have A Nice Day',
    'goodbye' : 'Bye, Have A Nice Day',
    'quit' : 'Bye, Have A Nice Day',
    'who are you' : 'I am a Rule Based Chatbot',
    'what is your name' : 'Kimi',
    'how are you' : 'I am Fine, Thank You'
}

def reply(ui):
    if True:
        for op in responses:
            if ui in op:
                return responses[op]
                break
    else:
        return "I Don't Understand, I am still learning"
    
while True:
    ui = input("You:")
    ui = ui.lower()
    if ui == 'exit':
        break
    print("Bot:",reply(ui))  