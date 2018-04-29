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
#import mathplotlib.pyplot as plt

#read data file into array
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])

secondcol = data[:,1]
meansecondcol = numpy.mean(data[:,1])

thirdcol = data[:,2]
meanthirdcol = numpy.mean(data[:,2])

fourthcol = data[:,3]
meanfourthcol = numpy.mean(data[:,3])


#to print the mean of the length and width of the sepals and petals of each sample collected by Ronald Fisher
print("the mean of sepal length in column 1 is:", meanfirstcol)

print("the mean of the Sepal width in column 2 is:", meansecondcol)

print("the mean of the Petal length in column 3 is:", meanthirdcol)

print("the mean of the Petal width in column 4 is:", meanfourthcol)


#to find the min of each column:
#reference: https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
#reference: https://plot.ly/numpy/min/

firstcol = data[:,0]
minfirstcol = numpy.min(firstcol)

secondcol = data[:,1]
minsecondcol = numpy.min(secondcol)

thirdcol = data[:,2]
minthirdcol = numpy.min(thirdcol)

fourthcol = data[:,3]
minfourthcol = numpy.min(fourthcol)

#to print the min of the length and width of the sepals and petals of each sample collected by Ronald Fisher
print("the min of sepal length in column 1 is:", minfirstcol)

print("the min of the Sepal width in column 2 is:", minsecondcol)

print("the min of the Petal length in column 3 is:", minthirdcol)

print("the min of the Petal width in column 4 is:", minfourthcol)



#To find the max of each column
#reference: https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
#reference: https://plot.ly/numpy/min/  (same concept as finding the min of each colum)

firstcol = data[:,0]
maxfirstcol = numpy.max(firstcol)

secondcol = data[:,1]
maxsecondcol = numpy.max(secondcol)

thirdcol = data[:,2]
maxthirdcol = numpy.max(thirdcol)

fourthcol = data[:,3]
maxfourthcol = numpy.max(fourthcol)

#to print the max of the length and width of the sepals and petals of each sample collected by Ronald Fisher
print("the max of sepal length in column 1 is:", maxfirstcol)

print("the max of the Sepal width in column 2 is:", maxsecondcol)

print("the max of the Petal length in column 3 is:", maxthirdcol)

print("the max of the Petal width in column 4 is:", maxfourthcol)


#to create a bar chart/histogram diagram of each column
#reference:Programming & Scripting, Matplotlib Pyplot, Ian McLaughlin (https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7)
#reference: https://matplotlib.org/users/pyplot_tutorial.html

import matplotlib.pyplot as pl
from matplotlib.ticker import NullFormatter
pl.figure(1)

pl.subplot(221)
pl.hist(firstcol)
pl.title('Sepal Length')  #create Title of graph
pl.ylabel('Samples Taken')  #to name the y axis
pl.xlabel('Measurements (cm)')  #to name the x axis


pl.subplot(222)
pl.hist(secondcol)
pl.title('Sepal Width')
pl.ylabel('Samples Taken')
pl.xlabel('Measurements (cm)')


pl.subplot(223)
pl.hist(thirdcol)
pl.title('Petal Lentgh')
pl.ylabel('Samples Taken')
pl.xlabel('Measurements (cm)')


pl.subplot(224)
pl.hist(fourthcol)
pl.title('Petal Width')
pl.ylabel('Samples Taken')
pl.xlabel('Measurements (cm)')


pl.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
pl.subplots_adjust(top=0.95, bottom=0.1, left=0.10, right=0.95, hspace=0.40,
                    wspace=0.35)

pl.show()
