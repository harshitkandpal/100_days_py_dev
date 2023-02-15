# Python Random module is an in-built module of Python which is used to generate random numbers.
import random

print("Enter 0 for snake, 1 for water, 2 for gun.\n")

# taking an integer as an input
a=int( input())

# if else ladder
if (a==0):
    z=str("snake")
elif(a==1):
    z = str("water")
else:
    z = str("gun")

# generating random integer
r=random.randint(0,2)

# decision making
if (r==0):
    b=str("snake")
elif(r==1):
    b = str("water")
else:
    b = str("gun")
if (a==r):
    print("You chose ",z )
    print("computer chose ",b)
    print("tie")
elif(a==0 and r==1):
    print("You chose ",z )
    print("computer chose ",b)
    print("You Win")
elif(a==0 and r==2):
    print("You chose ",z )
    print("computer chose ",b)
    print("You Lose")
elif(a==1 and r==0):
    print("You chose ",z )
    print("computer chose ",b)
    print("You Lose")
elif(a==1 and r==2):
    print("You chose ",z )
    print("computer chose ",b)
    print("You Win")
elif(a==2 and r==0):
    print("You chose ",z )
    print("computer chose ",b)
    print("You Win")
elif(a==2 and r==1):
    print("You chose ",z )
    print("computer chose ",b)
    print("You lose ")
input()