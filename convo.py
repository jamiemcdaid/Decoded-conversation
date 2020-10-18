#Stores information about the user - name, age, favourite colour, etc.
#Uses the information to calculate more facts about the user - calculate birth year from age, for example
#Responds to certain user inputs in different ways, such as agreeing that a specific colour is the best,
# but disliking others
#Tells the user everything it has learnt throughout the conversation
# Build out the program as much as you wish, creating a conversation with multiple paths and outputs.
#you may wish to research how to import and use the datetime module.

name = input("What is your name?")
age = input("How many years old are you?")
colour = input("What is your favourite colour?")

if colour =="Red" or "red":
    print("Red is my favourite too!")
else:
    print("I don't like that colour")

try:
     age=int(age)
     print("Age is a number")
except:
    age = input("How old are you, as a NUMBER of years")

if age > 30:
    print("Wow you're getting old!")
