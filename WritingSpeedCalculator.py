from datetime import *

before = datetime.now()

text = "I like to drive fast"
print("Please type: {}".format(text))

if text == input(": "):
    after = datetime.now()
    
    speed = after - before
    seconds = speed.total_seconds()
    letter_per_second = round(len(text) / seconds, 1)
    
    print("You won!")
    print("Your score is: {} seconds.".format(seconds))
    print("{} letters per second.".format(letter_per_second))
else:
    print("You failed.")