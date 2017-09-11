#!/usr/bin/python
import sys
import os
import math
sys.path.append("..")
from filehandler import *

class NeuralNetMath:
    def product(self, x,w):
        listref = [];
        i = 0;
        j = 0;
        while j < len(w[0]):
            innerdigit = 0;
            index = 0;
            i = 0;
            for pixel in x:
                innerdigit = float(pixel)*float(w[i][j]) + innerdigit;
                i = i + 1;
            listref.append(innerdigit);
            j = j + 1;
        return listref;
        
    def add(self, xW, b):
        listref = [];
        for child in range(len(xW)):
            
            listref.append(xW[child]+float(b[child]));
        return listref;
        
    def relu(self, y):
        for i in range(len(y)):
            if y[i] <= 0:
                y[i] = 0.0;
        return y; 
        
    def osigmund(self, sigma):
        for i in range(len(sigma)):
            sigma[i] = 1 / ( 1 + math.exp((-1)*sigma[i]));
        return sigma; 
    
#
f = FileHandler();
model = NeuralNetMath();

correct = 0;
incorrect = 0;
for index in range(len(f.xtest)):
    print correct;
    h0 = model.relu(model.add(model.product(f.xtest[index], f.w0), f.b0));
    h1 = model.relu(model.add(model.product(h0, f.w1), f.b1));
    o = model.osigmund(model.add(model.product(h1, f.w2), f.b2));
    if max(o) == o[int(f.ytest[index])]:
        correct= correct+1;
    else:
         incorrect = incorrect + 1;
print correct;
print incorrect;
    
