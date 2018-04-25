
f = open("data/iris.csv")


#prints the name of the file
print(f)


#print the contents of the file
#reference:https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7

print(f.read())

#calculate the mean of each column

import numpy

#read data file into array
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])

secondcol = data[:,1]
meansecondcol = numpy.mean(data[:,1])

thirdcol = data[:,1]
meanthirdcol = numpy.mean(data[:,2])



#to print the mean of the first column
print("the average of first column is:", meanfirstcol)

print("the average of the second column is:", meansecondcol)

print("the average of the third column is:", meanthirdcol)
