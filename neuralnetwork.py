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
        return weight
    else:
        print("epoch no. %d, error = %f" % (i,error))
        time.sleep(1)
        return error
    
print("Welcome to Jatin's own local TensorFlow made in his basement, we will attempt to approximate a function based off the relationship b/w x and y of your entries and might as well predict y or x with an x or y of your choice")
for j in range(3):
    print(".")
    time.sleep(0.5)
y = int(input("Enter y: "))
x = int(input("Enter x: "))
w = y/x
w1 = rd.range(1000000,1)
global i
i = 0
error = (w*x - w1*x)
if not (-0.1 <= error <= 0.1):
    start = 10000
    stop = 900
    while not (-0.1 <= error <= 0.1):
        i += 1
        neuron(start,stop)
        if 20 > i >= 10:                    #range of the randrange will change every 10 epochs
            start= 800
            stop = 700
        elif 30 > i >= 20:
            start= 700
            stop = 600
        elif 40 > i >= 30:
            start= 600
            stop = 500
        elif 50 > i >= 40:
            start = 500
            stop = 400
        elif 60 > i >= 20:
            start= 400
            stop = 300
        elif 70 > i >= 30:
            start= 300
            stop = 200
        elif 80 > i >= 20:
            start= 200
            stop = 100
        elif 90 > i >= 30:
            start= 100
            stop = 1
        else:
            continue
else:
    print("The weight of this relationship b/w x and y is %f" % w1)
    


