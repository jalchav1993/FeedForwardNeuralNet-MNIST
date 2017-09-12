#!/usr/bin/python
# Author Jesus Chavez
# Module used concrete implementation of the net
import sys
import os
sys.path.append("..")
from filehandler import *
from mathhandler import *
# Neural net concrete implementation
f = FileHandler("./MNIST");
model = NeuralNetMath();

correct = 0;
incorrect = 0;
for index in range(len(f.xtest)):
    #neural net algorithm
    h0 = model.relu(model.add(model.product(f.xtest[index], f.w0), f.b0));
    h1 = model.relu(model.add(model.product(h0, f.w1), f.b1));
    o = model.osigmund(model.add(model.product(h1, f.w2), f.b2));
    if max(o) == o[int(f.ytest[index])]:
        correct= correct+1;
    else:
         incorrect = incorrect + 1;
print correct;