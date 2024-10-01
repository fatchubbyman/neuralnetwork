#                                                          ideas/scrapped ideas
#we will attempt to make an neural network with limited amount of neurons with the fundamentals of python only
#maybe we can approximate mathematical functions
#randomizer for weights and an optimizer
#very limited layers
#learn numpy
#create epochs using loops
#this is how neural networks work
# use functions to use a neuron
# gauging weights can be done using randrange
# this is the weight bias equation:    y = wx + b
# initialization of weights is done randomly
# we could use while loops to get closer and closer to the right weights as it goes on for infinite amounts of time?
# our while loop stops when we hit a certain threshold of error
# print every epoch
# i know that the weight is supposed to change by looking at the errors but we'll think that through

import random as rd
import time


def neuron(start,stop):
    weight= rd.randrange(start,stop)
    error = (w*x - weight*x)
    if (error >= -0.1) and (error <= 0.1):
        print("The weight of this relationship b/w x and y is %f" % weight)
        return weight,error
    else:
        print("epoch no. %d,weight = %d error = %f" % (i,weight,error))
        time.sleep(0.1)
        wts.append(weight)
        errs.append(error)
        return error,weight
    
print("Welcome to Jatin's own local TensorFlow made in his basement, we will attempt to approximate a function based off the relationship b/w x and y of your entries \n and might as well predict y or x with an x or y of your choice")
for j in range(3):
    print(".")
    time.sleep(0.5)
y = int(input("Enter y: "))
x = int(input("Enter x: "))
w = y/x
w1 = rd.randrange(1,1000)
global wts
wts = []
global errs
errs = []
global weight
global error
global i
i = 0
j = 0
error = (w*x - w1*x)
if not (-0.1 <= error <= 0.1):
    start = 900
    stop = 1000
    while not (-0.1 <= error <= 0.1):
        i += 1
        neuron(start,stop)
        if 20 > i >= 10:                    #range of the randrange will change every 10 epochs
            start= 700
            stop = 800
        elif 30 > i >= 20:
            start= 600
            stop = 700
        elif 40 > i >= 30:
            start= 500
            stop = 600
        elif 50 > i >= 40:
            start = 400
            stop = 500
        elif 60 > i >= 50:
            start= 300
            stop = 400
        elif 70 > i >= 60:
            start= 200
            stop = 300
        elif 80 > i >= 70:
            start= 100
            stop = 200
        elif 90 > i >= 80:
            start= 1
            stop = 100
        elif i < 90:
            start = int(min(errs)) - 5
            stop = int(min(errs)) + 5
else:
    print("The weight of this relationship b/w x and y is %f" % w1)
    weight = w1
    
predict_y = int(input("Enter your x to predict the y according to the relationship we built"))
for j in range(2):
    print(".")
    time.sleep(0.5)
print(weight*predict_y)

    


