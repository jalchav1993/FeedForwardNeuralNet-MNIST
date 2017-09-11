# handles files
#!/usr/bin/python
import sys
import re

class FileHandler:
    xtest = [];
    ytest = [];
    w0 = [];
    w1 = [];
    w2 = [];
    b0 = [];
    b1 = [];
    b2 = [];
    def __init__(self):
        self.xtest = self.matrixToList("/Users/aex/Desktop/lab1/xtest.txt");
        self.ytest = self.vectortolist("/Users/aex/Desktop/lab1/ytest.txt");
        self.w0 = self.csvtolist("/Users/aex/Desktop/lab1/W0.txt");
        self.w1 = self.csvtolist("/Users/aex/Desktop/lab1/W1.txt");
        self.w2 = self.csvtolist("/Users/aex/Desktop/lab1/W2.txt");
        self.b0 = self.vectortolist("/Users/aex/Desktop/lab1/b0.txt");
        self.b1 = self.vectortolist("/Users/aex/Desktop/lab1/b1.txt");
        self.b2 = self.vectortolist("/Users/aex/Desktop/lab1/b2.txt");
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