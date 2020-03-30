#Flower Identification

import numpy, random, os
lr = 1 #learning rate
bias = 1 #value of bias
weights = [random.random(), random.random(), random.random(), random.random()] 
#list of 4 random weights (4 weights in total for 3 neurons and the bias)

def Perceptron(input1, input2, input3, output) :
   outputP = input1*weights[0]+input2*weights[1]+bias*weights[2]+bias*weights[3]
   if outputP > 0 : #activation function (here Heaviside)
      outputP = 1
   else :
      outputP = 0
   error = output - outputP
   weights[0] += error * input1 * lr
   weights[1] += error * input2 * lr
   weights[2] += error * input3 * lr
   weights[3] += error * bias * lr

#Training
#input 1 = colour: (0 = red, 1 = white, 2 = pink, 3 = yellow)
#input 2 = scent: (0 = unscented, 1 = scented)
#input 3 = relative size: (0-1, 0 = smallest, 1 = largest)
#answer = flower type: (0 = rose, 1 = sunflower)
for i in range(100) :
   Perceptron(0,1,0.3,0) #red rose
   Perceptron(1,1,0.5,0) #white rose
   Perceptron(2,1,0.2,0) #pink rose
   #more roses
   Perceptron(0,1,0.1,0) 
   Perceptron(0,1,0.5,0) 
   Perceptron(1,1,0.6,0) 
   Perceptron(0,0,0.3,0) 
   Perceptron(0,1,0.2,0) 
   Perceptron(2,1,0.2,0) 

   Perceptron(3,0,0.7,1) #sunflower
   Perceptron(3,1,0.9,1) #scented sunflower
   #more sunflowers
   Perceptron(3,0,0.7,1) 
   Perceptron(3,0,1.0,1) 
   Perceptron(3,0,0.5,1) 
   Perceptron(3,0,0.6,1) 
   Perceptron(3,0,0.7,1) 
   Perceptron(3,1,1.0,1)

inp = True

#Testing
while inp == True:
   print("\nEnter your flower qualities!")
   print("Colour: (0 = red, 1 = white, 2 = pink, 3 = yellow)")
   colour = int(input())
   print("Scent: (0 = unscented, 1 = scented)")
   scent = int(input())
   print("Relative size: (1-10, 1 = smallest, 10 = largest)")
   size = float(input())/10
   outputP = colour*weights[0] + scent*weights[1] + size*weights[2] + bias*weights[3]
   if outputP > 0 : #activation function
      result = "Sunflower"
   else :
      result = "Rose"
   print("Neural network says your flower is: ", result)

   print("\nContinue testing? 1 for yes, 0 for no.")
   ans = int(input())
   
   if ans == 0:
      inp = False
      print("Bye!")
   if ans == 1:
      inp = True
   

