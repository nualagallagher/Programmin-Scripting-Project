#To create code to determine the mean, max and min of the length
# and width of the sepals and petals of each sample of Iris flowers
#that was taken. 
# The 3 sample species of Iris are Virginica, Setosa & Verisolor
#Column 1 contains measurements of the Sepal lentgh
#Column 2 contains measurements of the Sepal width
#Column 3 contains measurements of the Petal length
#Column 4 contains measurements of the Petal width
#Please note all data collected of the 3 species mentioned above are included in each column.


#how to open the file & import it from when it was stored
f = open("data/iris.csv")


#prints the name of the file
print(f)


#print the contents of the file
#reference:https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7

print(f.read())
print("Please see the data contents of Fisher's Iris Data Set above  ")

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

fourthcol = data[:,1]
meanfourthcol = numpy.mean(data[:,3])


#to print the mean of the length and width of the sepals and petals of each sample collected by Ronald Fisher
print("the average of sepal length in column 1 is:", meanfirstcol)

print("the average of the Sepal width in column 2 is:", meansecondcol)

print("the average of the Petal length in column 3 is:", meanthirdcol)


print("the average of the Petal width in column 4 is:", meanfourthcol)


#to create a bar chart/histogram diagram of each column

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()


pl.hist(secondcol)
pl.show()

pl.hist(thirdcol)
pl.show()

pl.hist(fourthcol)
pl.show()






