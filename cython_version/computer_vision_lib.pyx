# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:14:01 2021

@author: Alexander Pilz
"""
import warnings
warnings.filterwarnings('ignore')
from PIL import Image
print("--> PIL.Image imported")
import numpy as np
print("--> numpy imported")
import random
print("--> random imported")
import time
print("--> time imported")

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
    
def imageToArray(imagePath):
    image = Image.open(imagePath)
    imageArray = np.asarray(image).copy()
    
    return imageArray

def imageToArray90(imagePath):
    image = Image.open(imagePath)
    imageArray = np.asarray(image).copy()
    imageArrayRotated = np.rot90(imageArray)
    
    return imageArrayRotated

def sobelHorizontalFilter(imageArray):
    #Image Info
    height = len(imageArray)
    width = len(imageArray[0])
    imageArray = imageArray
    
    sobelHorizontalFilteredImageArray = imageArray.copy()
    
    kernel = [[1,2,1],[0,0,0],[-1,-2,-1]]
    
    for i in range (1, height-1):
        for j in range (1, width-1):
            values = []
            for k in range(-1, 2):
                for h in range(-1, 2):
                    value = (0.2126*imageArray[i+k][j+h][0] + 0.7152*imageArray[i+k][j+h][1] + 0.0722*imageArray[i+k][j+h][2])
                    values.append(value) 
            value = 0
            counter = 0
            for ki in range(0, len(kernel)):
                for kj in range(0, len(kernel[0])):
                    value = value + values[counter] * kernel[ki][kj]
                    counter += 1
            sobelHorizontalFilteredImageArray[i][j][0] = abs(value)
            sobelHorizontalFilteredImageArray[i][j][1] = abs(value)
            sobelHorizontalFilteredImageArray[i][j][2] = abs(value) 

    for i in range(1, height-1):
        value1 = imageArray[i-1][2][0]+(2*imageArray[i-1][0][0])+imageArray[i-1][1][0]-imageArray[i+1][2][0]-(2*imageArray[i+1][0][0])-imageArray[i+1][1][0]
        value2 = imageArray[i-1][width-3][0]+(2*imageArray[i-1][width-1][0])+imageArray[i-1][width-2][0]-imageArray[i+1][width-3][0]-(2*imageArray[i+1][width-1][0])-imageArray[i+1][width-2][0]
    
        sobelHorizontalFilteredImageArray[i][0][0] = abs(value1)
        sobelHorizontalFilteredImageArray[i][0][1] = abs(value1)
        sobelHorizontalFilteredImageArray[i][0][2] = abs(value1) 
            
        sobelHorizontalFilteredImageArray[i][width-1][0] = abs(value2)
        sobelHorizontalFilteredImageArray[i][width-1][1] = abs(value2)
        sobelHorizontalFilteredImageArray[i][width-1][2] = abs(value2) 
        
    for i in range(1, width-1):
        value1 = imageArray[0][i-1][0]+(2*imageArray[0][i][0])+imageArray[0][i+1][0]-imageArray[1][i-1][0]-(2*imageArray[1][i][0])-imageArray[1][i+1][0]
        value2 = imageArray[height-1][i-1][0]+(2*imageArray[height-1][i][0])+imageArray[height-1][i+1][0]-imageArray[height-2][i-1][0]-(2*imageArray[height-2][i][0])-imageArray[height-2][i+1][0]
        
        sobelHorizontalFilteredImageArray[0][i][0] = abs(value1)
        sobelHorizontalFilteredImageArray[0][i][1] = abs(value1)
        sobelHorizontalFilteredImageArray[0][i][2] = abs(value1) 
            
        sobelHorizontalFilteredImageArray[height-1][i][0] = abs(value2)
        sobelHorizontalFilteredImageArray[height-1][i][1] = abs(value2)
        sobelHorizontalFilteredImageArray[height-1][i][2] = abs(value2) 
        
    return sobelHorizontalFilteredImageArray
        
def sobelVerticalFilter(imageArray):
    #Image Info
    height = len(imageArray)
    width = len(imageArray[0])
    imageArray = imageArray
    
    sobelVerticalFilteredImageArray = imageArray.copy()
    
    kernel = [[-1,0,1],[-2,0,2],[-1,0,1]]
    
    for i in range (1, height-1):
        for j in range (1, width-1):
            values = []
            for k in range(-1, 2):
                for h in range(-1, 2):
                    value = (0.2126*imageArray[i+k][j+h][0] + 0.7152*imageArray[i+k][j+h][1] + 0.0722*imageArray[i+k][j+h][2])
                    values.append(value) 
            value = 0
            counter = 0
            for ki in range(0, len(kernel)):
                for kj in range(0, len(kernel[0])):
                    value = value + values[counter] * kernel[ki][kj]
                    counter += 1
            sobelVerticalFilteredImageArray[i][j][0] = abs(value)
            sobelVerticalFilteredImageArray[i][j][1] = abs(value)
            sobelVerticalFilteredImageArray[i][j][2] = abs(value) 
            
    for i in range(1, height-1):
        value1 = -imageArray[i-1][0][0]+imageArray[i-1][2][0]-(2*imageArray[i][0][0])+(2*imageArray[i][2][0])-imageArray[i+1][0][0]+imageArray[i+1][2][0]
        value2 = -imageArray[i-1][width-1][0]+imageArray[i-1][width-3][0]-(2*imageArray[i][width-1][0])+(2*imageArray[i][width-3][0])-imageArray[i+1][width-1][0]+imageArray[i+1][width-3][0]
    
        sobelVerticalFilteredImageArray[i][0][0] = abs(value1)
        sobelVerticalFilteredImageArray[i][0][1] = abs(value1)
        sobelVerticalFilteredImageArray[i][0][2] = abs(value1) 
            
        sobelVerticalFilteredImageArray[i][width-1][0] = abs(value2)
        sobelVerticalFilteredImageArray[i][width-1][1] = abs(value2)
        sobelVerticalFilteredImageArray[i][width-1][2] = abs(value2) 
        
    for i in range(1, width-1):
        value1 = -imageArray[0][i-1][0]+imageArray[1][i+1][0]-(2*imageArray[1][i-1][0])+(2*imageArray[1][i+1][0])-imageArray[2][i-1][0]+imageArray[2][i+1][0]
        value2 = -imageArray[height-1][i-1][0]+imageArray[height-1][i+1][0]-(2*imageArray[height-2][i-1][0])+(2*imageArray[height-2][i+1][0])-imageArray[height-3][i-1][0]+imageArray[height-3][i+1][0]
        
        sobelVerticalFilteredImageArray[0][i][0] = abs(value1)
        sobelVerticalFilteredImageArray[0][i][1] = abs(value1)
        sobelVerticalFilteredImageArray[0][i][2] = abs(value1) 
            
        sobelVerticalFilteredImageArray[height-1][i][0] = abs(value2)
        sobelVerticalFilteredImageArray[height-1][i][1] = abs(value2)
        sobelVerticalFilteredImageArray[height-1][i][2] = abs(value2) 

    return sobelVerticalFilteredImageArray

def fullSobelFilter(imageArray):
    
    height = len(imageArray)
    width = len(imageArray[0])
    
    horizontalSobelArray = sobelHorizontalFilter(imageArray)
    verticalSobelArray = sobelVerticalFilter(imageArray)
    
    sobelFilteredImageArray = imageArray.copy()
    
    for i in range (1, height-1):
        for j in range (1, width-1):
            sobelFilteredImageArray[i][j][0] = horizontalSobelArray[i][j][0] + verticalSobelArray[i][j][0]
            sobelFilteredImageArray[i][j][1] = horizontalSobelArray[i][j][1] + verticalSobelArray[i][j][1]
            sobelFilteredImageArray[i][j][2] = horizontalSobelArray[i][j][2] + verticalSobelArray[i][j][2]
    
    return sobelFilteredImageArray

def minimalSeam(energyMap):
    
    height = len(energyMap)
    width = len(energyMap[0])
    
    s = seam()
    initialMinimum = min(energyMap[height-1])
    initialMinimumY = energyMap[height-1].index(initialMinimum)
    
    initialPosition = position(height, initialMinimumY, initialMinimum)
    
    s.addPosition(initialPosition)
    
    for i in range (1, height):
        index = height-i
        values = []
        p = s.getLastPosition()
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
        for i in range(0, len(values)):
            if(values[i].value < minValue):
                minValue = values[i].value
                minY = values[i].y
        pNew = position(index, minY, minValue)
        s.addPosition(pNew)
    
    return s

def randomSeam(energyMap):
    
    height = len(energyMap)
    width = len(energyMap[0])
    
    s = seam()
    initialMinimum = energyMap[height-1][random.randint(0, width-1)]
    initialMinimumY = energyMap[height-1].index(initialMinimum)
    
    initialPosition = position(height, initialMinimumY, initialMinimum)
    
    s.addPosition(initialPosition)
    
    for i in range (1, height):
        index = height-i
        values = []
        p = s.getLastPosition()
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
        for i in range(0, len(values)):
            if(values[i].value < minValue):
                minValue = values[i].value
                minY = values[i].y
        pNew = position(index, minY, minValue)
        s.addPosition(pNew)
    
    return s

def findMinimalSeam(imageArray, sobelFilteredImage):
    
    height = len(imageArray)
    width = len(imageArray[0])
    
    sobelFilteredImageArray = sobelFilteredImage.copy()
    energyMap = []
    
    firstRow = []
    for i in range (0, width):
       firstRow.append(sobelFilteredImageArray[0][i][0])
    energyMap.append(firstRow)
    
    for i in range (1, height-1):
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

    seam = minimalSeam(energyMap)
    
    return seam

def removeVerticalSeam(imageArray, seam):
    
    height = len(imageArray)
    width = len(imageArray[0])

    newImageArray = imageArray.copy()
    newImageArray = np.delete(newImageArray, width-1, 1)
    for i in range (0, height-1):
        row = imageArray[i]
        newRow = np.delete(row, seam.positions[i].y, 0)
        newImageArray[i] = newRow
    
    return newImageArray
    
def removeVerticalSeams(imagePath, numberOfSeams):
    imageArray = imageToArray(imagePath)
    sobelFilteredImageArray = fullSobelFilter(imageArray)
    
    for i in range(0, numberOfSeams):
        s = findMinimalSeam(imageArray, sobelFilteredImageArray)
        imageArray = removeVerticalSeam(imageArray, s)  
        sobelFilteredImageArray = removeVerticalSeam(sobelFilteredImageArray, s)  
        
    result = Image.fromarray(imageArray)
    result.save("vertical_removed.jpeg")

def removeHorizontalSeams(imagePath, numberOfSeams):
    imageArray = imageToArray90(imagePath)
    sobelFilteredImageArray = fullSobelFilter(imageArray)
   
    for i in range(0, numberOfSeams):
        s = findMinimalSeam(imageArray, sobelFilteredImageArray)
        imageArray = removeVerticalSeam(imageArray, s)  
        sobelFilteredImageArray = removeVerticalSeam(sobelFilteredImageArray, s)  
        
    imageArrayRotated = np.rot90(imageArray, 3)
    result = Image.fromarray(imageArrayRotated)
    result.save("horizontal_removed.jpeg")
        

    
    