"""the first python game"""
skip=3
import random
answer=random.randint(1,10)

while skip>0:
    temp=input("猜一猜数字")
    guess=int(temp)

    if guess==answer:
        print("You are right!")
        print("See you next time")
        break
    elif guess<answer:
        print("You are wrong")
        print("small")
    elif guess>answer:
           print("You are wrong")
           print("big")
    else:
        print("Please enter the right NUMBER")
    skip=skip-1
       
        

if guess!=answer:
        print(answer)
        print("Goodbye")
   
