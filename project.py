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
mean firstcol = numpy.mean(data[:,0])

print("average of first column is:", mean firstcol)
