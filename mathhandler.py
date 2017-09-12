#!/usr/bin/python
# Author Jesus Chavez
# model (model of the neural net) for processing MNIST dataset
import sys
import os
import math
import profile
sys.path.append("..")
from filehandler import *

class NeuralNetMath:
    # @param x reference to a vector of size j
    # @param w reference to a matrix of size i * j
    # @return list reference of x * w
    def product(self, x,w):
        listref = [];
        i = 0;
        j = 0;
        while j < len(w[0]):
            innerdigit = 0;
            index = 0;
            i = 0;
            for pixel in x:
                # row times column
                innerdigit = float(pixel)*float(w[i][j]) + innerdigit;
                i = i + 1;
            listref.append(innerdigit);
            j = j + 1;
        return listref;
        
    # @param x reference to a vector of size j
    # @param w reference to a vector of size j
    # @return list reference of x + w
    def add(self, xW, b):
        listref = [];
        for child in range(len(xW)):
            
            listref.append(xW[child]+float(b[child]));
        return listref;
        
    # @param y reference to a vector of size j
    # @return list reference of y that has been rectified
    def relu(self, y):
        for i in range(len(y)):
            if y[i] <= 0:
                y[i] = 0.0;
        return y; 
        
    # @param sigma reference to a vector of size j
    # @return list reference of y that has been corrected
    def osigmund(self, sigma):
        for i in range(len(sigma)):
            sigma[i] = 1 / ( 1 + math.exp((-1)*sigma[i]));
        return sigma; 
    

    
