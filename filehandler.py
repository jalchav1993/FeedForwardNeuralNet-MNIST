# handles files
#!/usr/bin/python
# Author Jesus Chavez
# Control for reading MNIST dataset
import sys
import re
import profile
class FileHandler:
    xtest = [];
    ytest = [];
    w0 = [];
    w1 = [];
    w2 = [];
    b0 = [];
    b1 = [];
    b2 = [];
    # @param mnistref reference string to the url of the data set
    # w0..w2 weight
    # b0..b2 bias
    # xtest img set
    # ytest expected results
    def __init__(self, mnistref):
        mnistref = mnistref +"/";
        self.xtest = self.matrixToList(mnistref+ "xtest.txt");
        self.ytest = self.vectortolist(mnistref+ "ytest.txt");
        self.w0 = self.csvtolist(mnistref+"W0.txt");
        self.w1 = self.csvtolist(mnistref+"W1.txt");
        self.w2 = self.csvtolist(mnistref+"W2.txt");
        self.b0 = self.vectortolist(mnistref+"b0.txt");
        self.b1 = self.vectortolist(mnistref+"b1.txt");
        self.b2 = self.vectortolist(mnistref+"b2.txt");
        
    # reads file url of matrix builds list form
    # @param fileurl is the url of the text file containing the values
    # @return list for of matrix
    def matrixToList(self, fileurl):
        print "reading file" + fileurl;
        listref = [];
        file = open(fileurl, 'r'); 
        lines = file.readlines();
        print "compressing";
        for line in lines:
            innerlist = re.findall(r'[0-9][0-9,.]+', line)[0].split(',');
            for i in range(len(innerlist)):
                innerlist[i] = float(innerlist[i]) / 255;
            listref.append(innerlist);
        return listref;
    # reads file url of matrix builds list form
    # @param fileurl is the url of the text file containing the csv values
    # @return list for of matrix
    def csvtolist(self, fileurl):
        print "reading file"+ fileurl;
        listref = [];
        file = open(fileurl, 'r'); 
        lines = file.readlines();
        print "compressing";
        for line in lines:
            innerline = line.split('\n');
            innerlist = innerline[0].split(',');
            listref.append(innerlist);
        return listref;
     # reads file url of vector builds list form
     # @param fileurl is the url of the text file containing the vector values
     # @return list for of vector   
    def vectortolist(self, fileurl):
        print " reading file"+ fileurl;
        listref = [];
        file = open(fileurl, 'r'); 
        lines = file.readlines();
        print "compressing";
        for line in lines:
            line = line.split("\n");
            listref.append(line[0]);
        return listref;
