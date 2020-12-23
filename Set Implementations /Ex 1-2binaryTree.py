#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Exercise 1
#Implement set as Binary tree
class Node:
    def __init__ (self, value):
        self.leftchild = None
        self.rightchild = None
        self.value = value
               
    def children (self):
        children = []
        if (self.leftchild):
            children = self.leftchild
        if (self.rightchild):
            if not children:
                children = self.rightchild
            else:
                children[1] = self.rightchild
        return children 
    
class Tree:
    
    def __init__ (self):
        self.root = None
        self.sizeOfTree = 0
        
    def getRoot (self):
        return self.root.value

    def add (self, value):
        if self.root is None:
            self.root = Node(value)
            self.sizeOfTree += 1
        else:
            self.addNode(self.root, value)
            
    def addNode (self, cNode, value):
        if (value < cNode.value):
            if cNode.leftchild:
                self.addNode(cNode.leftchild, value)
            else:
                cNode.leftchild = Node (value)
                self.sizeOfTree += 1
                return True
            
        elif (value > cNode.value):
            if cNode.rightchild:
                self.addNode(cNode.rightchild, value)
            else:
                cNode.rightchild = Node (value)
                self.sizeOfTree += 1
                return True
        else: 
            return False
                
    def contains (self, value):
        if self.root is None:
            return False
        else:
            return self.rec_contains(self.root, value)
   
    def rec_contains(self, cNode, value):
        if (value < cNode.value):
            if (cNode.leftchild):
                return self.rec_contains(cNode.leftchild, value)
            else:
                return False
        elif (value > cNode.value):
            if cNode.rightchild:
                return self.rec_contains(cNode.rightchild, value)
            else:
                return False
        else: 
            return True
    
    def printTree(self):
        self.rec_printTree(self.root)
    
    def rec_printTree(self, cNode):
        if cNode is None:
            return
        else:
            print(cNode.value, end=' ')
            self.rec_printTree(cNode.leftchild)
            self.rec_printTree(cNode.rightchild)
            
class mySet:         
    def __init__(self):
        self.sizeOfset = 0
        self.dataset = Tree()
        
    def add(self, value):
        self.dataset.add(value)
        self.sizeOfset = self.dataset.sizeOfTree
        
    def contains (self,value):
        return self.dataset.contains(value)

    def size (self):
        return self.sizeOfset
    
    def printSet(self):
        self.dataset.printTree()
        
        


# In[30]:


S = mySet()
print(S.dataset)
S.add('Hello')
S.add('there')
S.add('how')
S.add('are')
S.add('you')
S.add('Apple')
S.add('Amgen')
S.add('Ares')
S.add('it')
S.add('I\'ll')
S.add('Ill')
S.printSet()


# In[31]:


from tokenize import generate_tokens
import re
import time

addtime = [[] for i in range(100)] # array of 10x7105
sizeovertime = [[] for i in range(100)]
searchtime = [[] for i in range(100)]

for repeat in range(100):

    S = mySet()
    file = open ('pride-and-prejudice.txt','r')
    line = file.readline()
    while (line!=''):
        #array = line.split()
        array = re.findall('[a-zA-Z0-9]+', line) # regular expression matching
        length = len(array)
        for i in range(length):
            start = time.time_ns()
            S.add(array[i]) #add word to set
            t1 = time.time_ns()
            addtime[repeat].append(t1 - start)
            sizeovertime[repeat].append(S.size())

        line = file.readline()
    
    file.close()
    #S.printSet()

    file1 = open ('words-shuffled.txt', 'r')
    line = file1.readline()

    Count = 0 

    notfoundset = mySet()
    while (line!=''):
        array = re.findall('[a-zA-Z0-9]+\'?[a-z]*', line)
        length = len(array)
        for i in range(length):
            start = time.time_ns()
            foundOutput = S.contains(array[i])
            t2 = time.time_ns()
            searchtime[repeat].append(t2 - start)
            if (foundOutput == False):
                Count+=1
                notfoundset.add(line)
        line = file1.readline()
    print(Count)



# In[32]:


notfoundset.printSet()


# In[33]:


import statistics
from matplotlib import pyplot as plt
#matplotlib inline

meanaddtimes = [0]*len(addtime[0])
stdaddtimes = [0]*len(addtime[0])

for w in range(len(addtime[0])):
    times = [addtime[i][w] for i in range(100)]
    meanaddtimes[w] = statistics.mean(times)
    stdaddtimes[w] = statistics.stdev(times)


# In[37]:


plt.plot(sizeovertime[0], meanaddtimes)
plt.ylim(bottom=0, top=2e4)
plt.xlabel('#of words already inserted')
plt.ylabel('time in ns to insert new word')
plt.figure()
plt.plot(sizeovertime[0], stdaddtimes)
plt.xlabel('#of words already inserted')
plt.ylabel('stdev of time in ns to insert new word')
plt.ylim(bottom=0, top=1e5)


# In[38]:


meansearchtimes = [0]*len(searchtime[0])
stdsearchtimes = [0]*len(searchtime[0])

for w in range(len(searchtime[0])):
    times = [searchtime[i][w] for i in range(100)]
    meansearchtimes[w] = statistics.mean(times)
    stdsearchtimes[w] = statistics.stdev(times)
globalmeansearchtime = statistics.mean(meansearchtimes)
bestmeansearchtime = min(meansearchtimes)
worstmeansearchtime = max(meansearchtimes)
print('average search time = ',globalmeansearchtime)
print('best search time = ', min(meansearchtimes), 'for index ', meansearchtimes.index(bestmeansearchtime))
print('worse search time =',worstmeansearchtime, 'for index ', meansearchtimes.index(worstmeansearchtime))


# In[41]:


plt.plot(meansearchtimes)
plt.ylim(bottom=0, top=2e4)
plt.xlabel('index of word')
plt.ylabel('time in ns to search a word')
plt.figure()
plt.plot(stdsearchtimes)
plt.xlabel('index of word')
plt.ylabel('stdev of time in ns to search a word')
plt.ylim(bottom=0, top=1e4)


# In[ ]:




