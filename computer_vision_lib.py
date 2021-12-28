# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:14:01 2021

@author: Alexander
"""

from PIL import Image
print("--> Image imported")
import numpy as np
print("--> array imported")
import matplotlib.pyplot as plt
print("--> pyplot imported")
import math
print("--> math imported")

class seam:
    def __init__(self):
        self.value = 0
        self.positions = []
        
    def addPosition(self, position):
        self.positions.append(position)
    
    def getLastPosition(self):
        return self.positions[len(self.positions)-1]
    
    def printSeam(self):
        for i in range(0, len(self.positions)-1):
            print("x: ", self.positions[i].x)
            print("y: ", self.positions[i].y)
            print("value: ", self.positions[i].value)
            print("----------------")
        
class position:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
    
    def printPosition(self):
        print("X:", self.x, " Y: ", self.y, " Value: ", self.value)

def arrayToImage(imageArray):
    image = Image.fromarray(imageArray, mode='RGB')
    image.show()

def printHistogramm(imagePath):
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    width = image.width
    height = image.height
    imageArray = np.asarray(image)
    
    histogramArray = []
    for i in range(height):
        for j in range(width):
           histogramArray.append(imageArray[i][j][0])
           #Plot original Histogramm
    plt.hist(histogramArray, bins=255)
    
def brightenImage(imagePath, value):    
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    width = image.width
    height = image.height
    imageArray = np.asarray(image).copy()
    histogramArray = []
    for i in range(height):
        for j in range(width):
           if(imageArray[i][j][0] + value > 255):
               imageArray[i][j][0] = 255
               imageArray[i][j][1] = 255
               imageArray[i][j][2] = 255
           else:
               imageArray[i][j][0] = imageArray[i][j][0] + value
               imageArray[i][j][1] = imageArray[i][j][1] + value
               imageArray[i][j][2] = imageArray[i][j][2] + value
               
           histogramArray.append(imageArray[i][j][0])
           #Plot original Histogramm
    plt.hist(histogramArray, bins=255)
    brightendImage = Image.fromarray(imageArray, mode='RGB')
    brightendImage.show()
    
def darkenImage(imagePath, value):    
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    width = image.width
    height = image.height
    imageArray = np.asarray(image).copy()
    histogramArray = []
    for i in range(height):
        for j in range(width):
           if(imageArray[i][j][0] - value < 0):
               imageArray[i][j][0] = 0
               imageArray[i][j][1] = 0
               imageArray[i][j][2] = 0
           else:
               imageArray[i][j][0] = imageArray[i][j][0] - value
               imageArray[i][j][1] = imageArray[i][j][1] - value
               imageArray[i][j][2] = imageArray[i][j][2] - value
               
           histogramArray.append(imageArray[i][j][0])
           #Plot original Histogramm
    plt.hist(histogramArray, bins=255)
    darkenedImage = Image.fromarray(imageArray, mode='RGB')
    darkenedImage.show()
    
def negativeImage(imagePath):    
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    width = image.width
    height = image.height
    imageArray = np.asarray(image).copy()
    histogramArray = []
    for i in range(height):
        for j in range(width):
               imageArray[i][j][0] = 255-imageArray[i][j][0] 
               imageArray[i][j][1] = 255-imageArray[i][j][1] 
               imageArray[i][j][2] = 255-imageArray[i][j][2]
               histogramArray.append(imageArray[i][j][0])
           #Plot original Histogramm
    plt.hist(histogramArray, bins=255)
    negativeImage = Image.fromarray(imageArray, mode='RGB')
    negativeImage.show()
    
def nonLinearLogTransformedImage(imagePath):    
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    width = image.width
    height = image.height
    imageArray = np.asarray(image).copy()
    histogramArray = []
    for i in range(height):
        for j in range(width):
               imageArray[i][j][0] = 255*(math.log2(1+imageArray[i][j][0])/math.log2(256))
               imageArray[i][j][1] = 255*(math.log2(1+imageArray[i][j][1])/math.log2(256))
               imageArray[i][j][2] = 255*(math.log2(1+imageArray[i][j][2])/math.log2(256))
               histogramArray.append(imageArray[i][j][0])
           #Plot original Histogramm
    plt.hist(histogramArray, bins=255)
    nonLinearLogTransformedImage = Image.fromarray(imageArray, mode='RGB')
    nonLinearLogTransformedImage.show()

def exponentiallyTransformedImage(imagePath, exponent):    
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    width = image.width
    height = image.height
    imageArray = np.asarray(image).copy()
    histogramArray = []
    for i in range(height):
        for j in range(width):
               imageArray[i][j][0] = 255*(imageArray[i][j][0]/255)**exponent
               imageArray[i][j][1] = 255*(imageArray[i][j][1]/255)**exponent
               imageArray[i][j][2] = 255*(imageArray[i][j][2]/255)**exponent
               histogramArray.append(imageArray[i][j][0])
    #Plot original Histogramm
    plt.hist(histogramArray, bins=255)
    exponentiallyTransformedImage = Image.fromarray(imageArray, mode='RGB')
    exponentiallyTransformedImage.show()

def meanFilter(imagePath):
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    height = image.height
    width = image.width
    imageArray = np.asarray(image).copy()
    #define mean kernel
    kernel = [[1,1,1],[1,1,1],[1,1,1]]
    
    #expand image array
    meanFilteredImageArray = imageArray.copy()
    for i in range(1, height-1): #rows
        for j in range(1, width-1): #columns
            #apply kernel
            values = []
            for k in range(-1, 2):
                for h in range(-1, 2):
                    values.append(imageArray[i+k][j+h])      
            value = 0
            counter = 0
            for ki in range(0, len(kernel)):
                for kj in range(0, len(kernel[0])):
                    value = value + values[counter][0] * kernel[ki][kj]
                    counter = counter + 1
            meanFilteredImageArray[i][j][0] = int(value/9) 
            meanFilteredImageArray[i][j][1] = int(value/9) 
            meanFilteredImageArray[i][j][2] = int(value/9) 
    
    return meanFilteredImageArray

def medianFilter(imagePath):
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    height = image.height
    width = image.width
    imageArray = np.asarray(image).copy()
    
    #expand image array
    medianFilteredImageArray = imageArray.copy()
    for i in range(1, height-1): #rows
        for j in range(1, width-1): #columns
            values = []
            for k in range(-1, 2):
                for h in range(-1, 2):
                    values.append(imageArray[i+k][j+h])      
            medianFilteredImageArray[i][j][0] = np.median(values)
            medianFilteredImageArray[i][j][1] = np.median(values)
            medianFilteredImageArray[i][j][2] = np.median(values)  

    return medianFilteredImageArray            
                    
def gaussFilter(imagePath):
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    height = image.height
    width = image.width
    imageArray = np.asarray(image).copy()
    #define gaussian kernel
    kernel = [[1,2,1],[2,4,2],[1,2,1]]

    #expand image array
    gaussFilteredImageArray = imageArray.copy()
    for i in range(1, height-1): #rows
        for j in range(1, width-1): #columns
            #apply kernel
            values = []
            for k in range(-1, 2):
                for h in range(-1, 2):
                    values.append(imageArray[i+k][j+h])      
            value = 0
            counter = 0
            for ki in range(0, len(kernel)):
                for kj in range(0, len(kernel[0])):
                    value = value + values[counter][0] * kernel[ki][kj]
                    counter = counter + 1
            gaussFilteredImageArray[i][j][0] = int(value/16) 
            gaussFilteredImageArray[i][j][1] = int(value/16) 
            gaussFilteredImageArray[i][j][2] = int(value/16) 

    return gaussFilteredImageArray

def prewittHorizontalFilter(imagePath):
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    height = image.height
    width = image.width
    imageArray = np.asarray(image).copy()
    
    prewittHorizontalFilteredImageArray = imageArray.copy()
    
    kernel = [[1,1,1],[0,0,0],[-1,-1,-1]]
    
    for i in range (1, height-1):
        for j in range (1, width-1):
            values = []
            for k in range(-1, 2):
                for h in range(-1, 2):
                    values.append(imageArray[i+k][j+h][0]) 
            value = 0
            counter = 0
            for ki in range(0, len(kernel)):
                for kj in range(0, len(kernel[0])):
                    value = value + values[counter] * kernel[ki][kj]
                    counter += 1
            prewittHorizontalFilteredImageArray[i][j][0] = abs(value)
            prewittHorizontalFilteredImageArray[i][j][1] = abs(value)
            prewittHorizontalFilteredImageArray[i][j][2] = abs(value) 
    
    return prewittHorizontalFilteredImageArray

def prewittVerticalFilter(imagePath):
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    height = image.height
    width = image.width
    imageArray = np.asarray(image).copy()
    
    prewittVerticalFilteredImageArray = imageArray.copy()
    
    kernel = [[-1,0,1],[-1,0,1],[-1,0,1]]
    
    for i in range (1, height-1):
        for j in range (1, width-1):
            values = []
            for k in range(-1, 2):
                for h in range(-1, 2):
                    values.append(imageArray[i+k][j+h][0]) 
            value = 0
            counter = 0
            for ki in range(0, len(kernel)):
                for kj in range(0, len(kernel[0])):
                    value = value + values[counter] * kernel[ki][kj]
                    counter += 1
            prewittVerticalFilteredImageArray[i][j][0] = abs(value)
            prewittVerticalFilteredImageArray[i][j][1] = abs(value)
            prewittVerticalFilteredImageArray[i][j][2] = abs(value) 
    
    return prewittVerticalFilteredImageArray
    
def sobelHorizontalFilter(imagePath):
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    height = image.height
    width = image.width
    imageArray = np.asarray(image).copy()
    
    sobelHorizontalFilteredImageArray = imageArray.copy()
    
    kernel = [[1,2,1],[0,0,0],[-1,-2,-1]]
    
    for i in range (1, height-1):
        for j in range (1, width-1):
            values = []
            for k in range(-1, 2):
                for h in range(-1, 2):
                    values.append(imageArray[i+k][j+h][0]) 
            value = 0
            counter = 0
            for ki in range(0, len(kernel)):
                for kj in range(0, len(kernel[0])):
                    value = value + values[counter] * kernel[ki][kj]
                    counter += 1
            sobelHorizontalFilteredImageArray[i][j][0] = abs(value)
            sobelHorizontalFilteredImageArray[i][j][1] = abs(value)
            sobelHorizontalFilteredImageArray[i][j][2] = abs(value) 

    return sobelHorizontalFilteredImageArray
        
def sobelVerticalFilter(imagePath):
    image = Image.open(imagePath)
    #Image Info
    print(image.size)
    print(image.info)
    height = image.height
    width = image.width
    imageArray = np.asarray(image).copy()
    
    sobelVerticalFilteredImageArray = imageArray.copy()
    
    kernel = [[-1,0,1],[-2,0,2],[-1,0,1]]
    
    for i in range (1, height-1):
        for j in range (1, width-1):
            values = []
            for k in range(-1, 2):
                for h in range(-1, 2):
                    values.append(imageArray[i+k][j+h][0]) 
            value = 0
            counter = 0
            for ki in range(0, len(kernel)):
                for kj in range(0, len(kernel[0])):
                    value = value + values[counter] * kernel[ki][kj]
                    counter += 1
            sobelVerticalFilteredImageArray[i][j][0] = abs(value)
            sobelVerticalFilteredImageArray[i][j][1] = abs(value)
            sobelVerticalFilteredImageArray[i][j][2] = abs(value) 

    return sobelVerticalFilteredImageArray

def fullPrewittFilter(imagePath):
    image = Image.open(imagePath)
    imageArray = np.asarray(image).copy()
    
    height = image.height
    width = image.width
    
    horizontalPrewittArray = prewittHorizontalFilter(imagePath)
    verticalPrewittArray = prewittVerticalFilter(imagePath)
    
    prewittFilteredImageArray = imageArray.copy()
    
    for i in range (1, height-1):
        for j in range (1, width-1):
            prewittFilteredImageArray[i][j][0] = horizontalPrewittArray[i][j][0] + verticalPrewittArray[i][j][0]
            prewittFilteredImageArray[i][j][1] = horizontalPrewittArray[i][j][1] + verticalPrewittArray[i][j][1]
            prewittFilteredImageArray[i][j][2] = horizontalPrewittArray[i][j][2] + verticalPrewittArray[i][j][2]

    return prewittFilteredImageArray
    
def fullSobelFilter(imagePath):
    image = Image.open(imagePath)
    imageArray = np.asarray(image).copy()
    
    height = image.height
    width = image.width
    
    horizontalSobelArray = sobelHorizontalFilter(imagePath)
    verticalSobelArray = sobelVerticalFilter(imagePath)
    
    sobelFilteredImageArray = imageArray.copy()
    
    for i in range (1, height-1):
        for j in range (1, width-1):
            sobelFilteredImageArray[i][j][0] = horizontalSobelArray[i][j][0] + verticalSobelArray[i][j][0]
            sobelFilteredImageArray[i][j][1] = horizontalSobelArray[i][j][1] + verticalSobelArray[i][j][1]
            sobelFilteredImageArray[i][j][2] = horizontalSobelArray[i][j][2] + verticalSobelArray[i][j][2]
    
    sobelFilteredImageArray = np.delete(sobelFilteredImageArray, 0, 0)
    sobelFilteredImageArray = np.delete(sobelFilteredImageArray, height-2, 0)
    sobelFilteredImageArray = np.delete(sobelFilteredImageArray, 0, 1)
    sobelFilteredImageArray = np.delete(sobelFilteredImageArray, width-2, 1)
    return sobelFilteredImageArray

def minimalSeam(energyMap):
    
    height = len(energyMap)
    width = len(energyMap[0])
    
    s = seam()
    initialMinimum = min(energyMap[0])
    initialMinimumY = energyMap[0].index(initialMinimum)
    
    initialPosition = position(0, initialMinimumY, initialMinimum)
    
    s.addPosition(initialPosition)
    
    for i in range (1, height):
        index = height-i
        values = []
        p = s.getLastPosition()
        #p.printPosition()
        if(p.y == 0):
           p1 = position(index, p.y, energyMap[index][p.y]) 
           p2 = position(index, p.y+1, energyMap[index][p.y+1]) 
           values.append(p1)
           values.append(p2)
        elif(p.y == width-1):
            p1 = position(index, p.y, energyMap[index][p.y]) 
            p2 = position(index, p.y-1, energyMap[index][p.y-1]) 
            values.append(p1)
            values.append(p2)
        else:
            p1 = position(index, p.y, energyMap[index][p.y]) 
            p2 = position(index, p.y-1, energyMap[index][p.y-1]) 
            p3 = position(index, p.y+1, energyMap[index][p.y+1]) 
            values.append(p1)
            values.append(p2)
            values.append(p3)
        
        minValue = values[0].value
        minY = values[0].y
        for i in range(1, len(values)-1):
            if(values[i].value < minValue):
                minValue = values[i].value
                minY = values[i].y
        pNew = position(index, minY, minValue)
        s.addPosition(pNew)
    s.printSeam()
    

def findVerticalSeams(imagePath):
    image = Image.open(imagePath)
    
    height = image.height-2
    width = image.width-2
    
    sobelFilteredImageArray = fullSobelFilter(imagePath)
    energyMap = []
    
    firstRow = []
    for i in range (0, width):
       firstRow.append(sobelFilteredImageArray[0][i][0])
    energyMap.append(firstRow)
    
    for i in range (1, height):
        row = []
        for j in range (0, width):
                if j == 0:
                    values = []
                    values.append(sobelFilteredImageArray[i-1][j][0])
                    values.append(sobelFilteredImageArray[i-1][j+1][0])
                elif j == width-1:
                    values = []
                    values.append(sobelFilteredImageArray[i-1][j][0])
                    values.append(sobelFilteredImageArray[i-1][j-1][0])
                else:
                    values = []
                    values.append(sobelFilteredImageArray[i-1][j][0])
                    values.append(sobelFilteredImageArray[i-1][j+1][0])
                    values.append(sobelFilteredImageArray[i-1][j-1][0])
                row.append(sobelFilteredImageArray[i][j][0] + min(values))
        energyMap.append(row)
    minimalSeam(energyMap)
    
    