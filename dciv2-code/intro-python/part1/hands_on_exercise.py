"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi

print (pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50

i = random.randint(0, 100)
print (i)
if i <=50 :
    print ("i is less than 50 ya fawzy :)")
elif i>=50 :
    print ("i is grater than 50 ya fawzy :)")
else :
    print ("i is not in range 0 to 100")

# TODO: Write a conditional that prints the color of the picked fruit

picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

print (picked_fruit)

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
x1=12 
x2=96
y1=48
y2=17
def multi1(a,b):
    mul=a*b
    return (mul)
z=multi1(x1,x2)
x=multi1(y1,y2)
c=multi1(196523,87323)

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",z)

print("48 x 17 =",x)

print("196523 x 87323 =",c)
