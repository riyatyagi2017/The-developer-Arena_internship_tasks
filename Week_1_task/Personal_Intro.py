# writing my first program
print("Hello World")

# Project --> Personal Introduction Program
def Personal_introduction():
    ## user input asking for the name
    name = input("What is your name?")
    
    ## user input asking for the age
    age = int(input("How old are you?"))
    
    ## user input asking for hobby
    hobby = input("What is your favourite hobby?")
    
    # Printing the welcome message
    print(f"🎉Welcome {name} 🎉")
    print(f"You are {age} years old and love {hobby}.")

Personal_introduction()
