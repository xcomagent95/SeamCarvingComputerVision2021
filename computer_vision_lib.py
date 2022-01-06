# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:14:01 2021

@author: Alexander Pilz
"""
#imports of functions and libraries
import warnings
warnings.filterwarnings('ignore')
from PIL import Image
print("--> PIL.Image imported")
import numpy as np
print("--> numpy imported")

#class definition of seam
#a seam has a value and a number of positions
class seam:
    #seam constructor
    def __init__(self):
        self.value = 0
        self.positions = []
        
    #positions can be added
    def addPosition(self, position):
        self.positions.append(position)
    
    #the last position get be retrieved
    def getLastPosition(self):
        return self.positions[len(self.positions)-1]
    
    #a seam can be printed to the console
    def printSeam(self):
        for i in range(0, len(self.positions)-1):
            print("x: ", self.positions[i].x)
            print("y: ", self.positions[i].y)
            print("value: ", self.positions[i].value)
            print("----------------")

#class definition of position
#a position has a pair of coordinates and a pixel value
class position:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
    
    #a position can be printed to the console
    def printPosition(self):
        print("X:", self.x, " Y: ", self.y, " Value: ", self.value)

#function converts an array containing pixel values into an image
def arrayToImage(imageArray):
    image = Image.fromarray(imageArray, mode='RGB')
    image.show()
    
#function converts an image to an array containing its pixel values    
def imageToArray(imagePath):
    image = Image.open(imagePath)
    imageArray = np.asarray(image).copy()
    
    return imageArray

#function converts an image to an rotated array containing its pixel values 
def imageToArray90(imagePath):
    image = Image.open(imagePath)
    imageArray = np.asarray(image).copy()
    imageArrayRotated = np.rot90(imageArray)
    
    return imageArrayRotated

#function sobel filters an array containing pixel values horizontally
def sobelHorizontalFilter(imageArray):

    height = len(imageArray) #store imahe height
    width = len(imageArray[0]) #store image width
    
    sobelHorizontalFilteredImageArray = imageArray.copy() #copy array with pixel values
    
    kernel = [[1,2,1],[0,0,0],[-1,-2,-1]] #initialize kernel
    
    for i in range (1, height-1): #iterate over height
        for j in range (1, width-1): #iterate over width
            values = [] #initialize values
            for k in range(-1, 2): #iterate over kernel-size
                for h in range(-1, 2): #iterate over kernel-size
                    value = (0.2126*imageArray[i+k][j+h][0] + 0.7152*imageArray[i+k][j+h][1] + 0.0722*imageArray[i+k][j+h][2]) #convert rgb value to greyscale value
                    values.append(value) #append value to values
            value = 0 #reset value
            counter = 0 #initialize counter
            for ki in range(0, len(kernel)): #iterate over kernel-height
                for kj in range(0, len(kernel[0])): #iterate over kernel-width
                    value = value + values[counter] * kernel[ki][kj] #add value to overall kernel-output
                    counter += 1 #increase counter
            sobelHorizontalFilteredImageArray[i][j][0] = abs(value) #write value to result array at position 0
            sobelHorizontalFilteredImageArray[i][j][1] = abs(value) #write value to result array at position 1
            sobelHorizontalFilteredImageArray[i][j][2] = abs(value) #write value to result array at position 2
            
    cornerValue = 0

    for i in range(1, height-1): #ietarte over vertical borders
        value1 = (0.2126*imageArray[i-1][1][0]+0.7152*imageArray[i-1][1][1]+0.0722*imageArray[i-1][1][2])
        -(0.2126*imageArray[i+1][1][0]+0.7152*imageArray[i+1][1][1]+0.0722*imageArray[i+1][1][2])
        +2*(0.2126*imageArray[i-1][0][0]+0.7152*imageArray[i-1][0][1]+0.0722*imageArray[i-1][0][2])
        -2*(0.2126*imageArray[i+1][0][0]+0.7152*imageArray[i+1][0][1]+0.0722*imageArray[i+1][0][2])
        
        cornerValue += value1
        
        sobelHorizontalFilteredImageArray[i][0][0] = abs(value1)
        sobelHorizontalFilteredImageArray[i][0][1] = abs(value1)
        sobelHorizontalFilteredImageArray[i][0][2] = abs(value1) 
        
        value2 = (0.2126*imageArray[i-1][width-2][0]+0.7152*imageArray[i-1][width-2][1]+0.0722*imageArray[i-1][width-2][2])
        -(0.2126*imageArray[i+1][width-2][1]+0.7152*imageArray[i+1][width-2][1]+0.0722*imageArray[i+1][width-2][2])
        +2*(0.2126*imageArray[i-1][width-1][0]+0.7152*imageArray[i-1][width-1][1]+0.0722*imageArray[i-1][width-1][2])
        -2*(0.2126*imageArray[i+1][width-1][0]+0.7152*imageArray[i+1][width-1][1]+0.0722*imageArray[i+1][width-1][2])
        
        cornerValue += value2
            
        sobelHorizontalFilteredImageArray[i][width-1][0] = abs(value2)
        sobelHorizontalFilteredImageArray[i][width-1][1] = abs(value2)
        sobelHorizontalFilteredImageArray[i][width-1][2] = abs(value2) 
        
    for i in range(1, width-1): #iterate over horizontal borders
        value1 = -(0.2126*imageArray[1][i-1][0]+0.7152*imageArray[1][i-1][1]+0.0722*imageArray[1][i-1][2])
        -2*(0.2126*imageArray[1][i][0]+0.7152*imageArray[1][i][1]+0.0722*imageArray[1][i][2])
        -(0.2126*imageArray[1][i+1][0]+0.7152*imageArray[1][i+1][1]+0.0722*imageArray[1][i+1][2])
        
        cornerValue += value1
        
        sobelHorizontalFilteredImageArray[0][i][0] = abs(value1)
        sobelHorizontalFilteredImageArray[0][i][1] = abs(value1)
        sobelHorizontalFilteredImageArray[0][i][2] = abs(value1)
        
        value2 = (0.2126*imageArray[height-2][i-1][0]+0.7152*imageArray[height-2][i-1][1]+0.0722*imageArray[height-2][i-1][2])
        +2*(0.2126*imageArray[height-2][i][0]+0.7152*imageArray[height-2][i][1]+0.0722*imageArray[height-2][i][2])
        +(0.2126*imageArray[height-2][i+1][0]+0.7152*imageArray[height-2][i+1][1]+0.0722*imageArray[height-2][i+1][2])
        
        cornerValue += value2
        
        sobelHorizontalFilteredImageArray[height-1][i][0] = abs(value2)
        sobelHorizontalFilteredImageArray[height-1][i][1] = abs(value2)
        sobelHorizontalFilteredImageArray[height-1][i][2] = abs(value2) 
        
    #set mean value for corners    
    for i in range(0, 3):    
        sobelHorizontalFilteredImageArray[0][0][i] = abs(cornerValue)/4
        sobelHorizontalFilteredImageArray[height-1][0][i] = abs(cornerValue)/4
        sobelHorizontalFilteredImageArray[0][width-1][i] = abs(cornerValue)/4
        sobelHorizontalFilteredImageArray[height-1][width-1][i] = abs(cornerValue)/4
        
    return sobelHorizontalFilteredImageArray #return the filtered result

#function sobel filters an array containing pixel values vertically
def sobelVerticalFilter(imageArray):
    
    height = len(imageArray) #store imahe height
    width = len(imageArray[0]) #store image width
    
    sobelVerticalFilteredImageArray = imageArray.copy() #copy array with pixel values
    
    kernel = [[-1,0,1],[-2,0,2],[-1,0,1]] #initialize kernel
    
    for i in range (1, height-1): #iterate over height
        for j in range (1, width-1): #iterate over width
            values = [] #initialize values
            for k in range(-1, 2): #iterate over kernel-size
                for h in range(-1, 2): #iterate over kernel-size
                    value = (0.2126*imageArray[i+k][j+h][0] + 0.7152*imageArray[i+k][j+h][1] + 0.0722*imageArray[i+k][j+h][2]) #convert rgb value to greyscale value
                    values.append(value) #append value to values
            value = 0 #reset value
            counter = 0 #initialize counter
            for ki in range(0, len(kernel)): #iterate over kernel-height
                for kj in range(0, len(kernel[0])): #iterate over kernel-width
                    value = value + values[counter] * kernel[ki][kj] #add value to overall kernel-output
                    counter += 1 #increase counter
            sobelVerticalFilteredImageArray[i][j][0] = abs(value) #write value to result array at position 0
            sobelVerticalFilteredImageArray[i][j][1] = abs(value) #write value to result array at position 1
            sobelVerticalFilteredImageArray[i][j][2] = abs(value) #write value to result array at position 2
            
    cornerValue = 0
        
    for i in range(1, height-1): #ietarte over vertical borders
        value1 = (0.2126*imageArray[i-1][1][0]+0.7152*imageArray[i-1][1][1]+0.0722*imageArray[i-1][1][2])
        +2*(0.2126*imageArray[i][1][0]+0.7152*imageArray[i][1][1]+0.0722*imageArray[i][1][2])
        +(0.2126*imageArray[i+1][1][0]+0.7152*imageArray[i+1][1][1]+0.0722*imageArray[i+1][1][2])
        
        cornerValue += value1
    
        sobelVerticalFilteredImageArray[i][0][0] = abs(value1)
        sobelVerticalFilteredImageArray[i][0][1] = abs(value1)
        sobelVerticalFilteredImageArray[i][0][2] = abs(value1) 
                 
        value2 = -(0.2126*imageArray[i-1][width-2][0]+0.7152*imageArray[i-1][width-2][1]+0.0722*imageArray[i-1][width-2][2])
        -2*(0.2126*imageArray[i][width-2][0]+0.7152*imageArray[i][width-2][1]+0.0722*imageArray[i][width-2][2])
        -(0.2126*imageArray[i+1][width-2][0]+0.7152*imageArray[i+1][width-2][1]+0.0722*imageArray[i+1][width-2][2])
        
        cornerValue += value2

        sobelVerticalFilteredImageArray[i][width-1][0] = abs(value2)
        sobelVerticalFilteredImageArray[i][width-1][1] = abs(value2)
        sobelVerticalFilteredImageArray[i][width-1][2] = abs(value2) 
        
    for i in range(1, width-1): #iterate over horizontal borders
        value1 = -2*(0.2126*imageArray[0][i-1][0]+0.7152*imageArray[0][i-1][1]+0.0722*imageArray[0][i-1][2])
        +2*(0.2126*imageArray[0][i+1][0]+0.7152*imageArray[0][i+1][1]+0.0722*imageArray[0][i+1][2])
        -(0.2126*imageArray[1][i-1][0]+0.7152*imageArray[1][i-1][1]+0.0722*imageArray[1][i-1][2])
        +(0.2126*imageArray[1][i+1][0]+0.7152*imageArray[1][i+1][1]+0.0722*imageArray[1][i+1][2])
        
        cornerValue += value1
        
        sobelVerticalFilteredImageArray[0][i][0] = abs(value1)
        sobelVerticalFilteredImageArray[0][i][1] = abs(value1)
        sobelVerticalFilteredImageArray[0][i][2] = abs(value1) 
        
        value2 = -2*(0.2126*imageArray[height-1][i-1][0]+0.7152*imageArray[height-1][i-1][1]+0.0722*imageArray[height-1][i-1][2])
        +2*(0.2126*imageArray[height-1][i+1][0]+0.7152*imageArray[height-1][i+1][1]+0.0722*imageArray[height-1][i+1][2])
        -(0.2126*imageArray[height-2][i-1][0]+0.7152*imageArray[height-2][i-1][1]+0.0722*imageArray[height-2][i-1][2])
        +(0.2126*imageArray[height-2][i+1][0]+0.7152*imageArray[height-2][i+1][1]+0.0722*imageArray[height-2][i+1][2])
        
        cornerValue += value2
            
        sobelVerticalFilteredImageArray[height-1][i][0] = abs(value2)
        sobelVerticalFilteredImageArray[height-1][i][1] = abs(value2)
        sobelVerticalFilteredImageArray[height-1][i][2] = abs(value2)
    
    #set mean value for corners    
    for i in range(0, 3):    
        sobelVerticalFilteredImageArray[0][0][i] = abs(cornerValue)/4
        sobelVerticalFilteredImageArray[height-1][0][i] = abs(cornerValue)/4
        sobelVerticalFilteredImageArray[0][width-1][i] = abs(cornerValue)/4
        sobelVerticalFilteredImageArray[height-1][width-1][i] = abs(cornerValue)/4

    return sobelVerticalFilteredImageArray #return the filtered result

#function sobel filters an array containing pixel values 
def fullSobelFilter(imageArray):
    
    height = len(imageArray) #store imahe height
    width = len(imageArray[0]) #store image width
    
    horizontalSobelArray = sobelHorizontalFilter(imageArray) #filter array horizontally
    verticalSobelArray = sobelVerticalFilter(imageArray) #filter array vertically
    
    sobelFilteredImageArray = imageArray.copy() #copy array with pixel values
    
    for i in range (1, height-1): #iterate over height
        for j in range (1, width-1): #iterate over width
            sobelFilteredImageArray[i][j][0] = horizontalSobelArray[i][j][0] + verticalSobelArray[i][j][0] #sum vertical and horizontal value
            sobelFilteredImageArray[i][j][1] = horizontalSobelArray[i][j][1] + verticalSobelArray[i][j][1] #sum vertical and horizontal value
            sobelFilteredImageArray[i][j][2] = horizontalSobelArray[i][j][2] + verticalSobelArray[i][j][2] #sum vertical and horizontal value
    
    return sobelFilteredImageArray #return the filtered result

#extracts a seam form an energy map
def minimalSeam(energyMap):
    
    height = len(energyMap) #store imahe height
    width = len(energyMap[0]) #store image width
    
    s = seam() #initialize seam
    initialMinimum = min(energyMap[height-1]) #find seam with minimal value -> minimal value in last row
    initialMinimumY = energyMap[height-1].index(initialMinimum) #get index of the minimal value
    
    initialPosition = position(height, initialMinimumY, initialMinimum) #construct first position of the minimal seam
    
    s.addPosition(initialPosition) #add first position to seam
    
    for i in range (1, height): #iterate over height
        index = height-i #get real index (since we are actually going upward)
        values = [] #initialize values
        p = s.getLastPosition() #get last (initial) position of the seam
        
        #dynamicly retrace seam through minimal neighboring pixels
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
        
        minValue = values[0].value #get minimal neighbor 
        minY = values[0].y #initialize min value
        for i in range(0, len(values)): #iterate over possible values
            if(values[i].value < minValue): 
                minValue = values[i].value #set new minimal value
                minY = values[i].y #set new y coordinate of new minimal value
        pNew = position(index, minY, minValue) #construct next position
        s.addPosition(pNew) #add new position to seam
    
    return s #return seam

def findMinimalSeam(imageArray, sobelFilteredImage):
    
    height = len(imageArray) #store imahe height
    width = len(imageArray[0]) #store image width
    
    sobelFilteredImageArray = sobelFilteredImage.copy() #copy image array
    energyMap = [] #initialize energy map
    
    firstRow = [] #initialize first row
    for i in range (0, width): #iterate ver width
       firstRow.append(sobelFilteredImageArray[0][i][0]) #append values of first row
    energyMap.append(firstRow) #appemnd first row to energy map
    
    for i in range (1, height-1): #iterate over height
        row = [] #initialize row
        for j in range (0, width): #iterate over width
                
                #dynamicly build energy map 
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
                row.append(sobelFilteredImageArray[i][j][0] + min(values)) #add value of minimal neighbor to current index 
        energyMap.append(row) #append row to energy map

    seam = minimalSeam(energyMap) #find minimal seam in energy map
    
    return seam #return minimal seam

#function removes a given vertical seam from a given array containing pixel values
def removeVerticalSeam(imageArray, seam):
    
    height = len(imageArray) #store imahe height
    width = len(imageArray[0]) #store image width

    newImageArray = imageArray.copy() #copy the array containign the pixel values
    newImageArray = np.delete(newImageArray, width-1, 1) #delte a collumn to correct for changes in dimension
    for i in range (0, height-1): #iterate over height
        row = imageArray[i] #retrieve row
        newRow = np.delete(row, seam.positions[i].y, 0) #delete corresponding seam position from array
        newImageArray[i] = newRow #add new row
    
    return newImageArray

#function removes a number of vertical seams from a given image
def removeVerticalSeams(imagePath, numberOfSeams):
    imageArray = imageToArray(imagePath) #convert image to an array containing its pixel values
    sobelFilteredImageArray = fullSobelFilter(imageArray) #apply sobel operator to array
    
    for i in range(0, numberOfSeams): #iterate over number of seams
        s = findMinimalSeam(imageArray, sobelFilteredImageArray) #find minimal seam
        imageArray = removeVerticalSeam(imageArray, s) #remove seam from image 
        sobelFilteredImageArray = removeVerticalSeam(sobelFilteredImageArray, s) #remove seam from energy map
        
    result = Image.fromarray(imageArray) #convert result to image
    result.save("images/vertical_removed.jpeg") #store resulting image

#function removes a number of horizontal seams from a given array containing pixel values  
def removeHorizontalSeams(imagePath, numberOfSeams):
    imageArray = imageToArray90(imagePath) #convert image to an array containing its pixel values a rotate it by 90 degrees
    sobelFilteredImageArray = fullSobelFilter(imageArray) #apply sobel operator to array
   
    for i in range(0, numberOfSeams): #iterate over number of seams
        s = findMinimalSeam(imageArray, sobelFilteredImageArray) #find minimal seam
        imageArray = removeVerticalSeam(imageArray, s) #remove seam from image 
        sobelFilteredImageArray = removeVerticalSeam(sobelFilteredImageArray, s) #remove seam from energy map 
        
    imageArrayRotated = np.rot90(imageArray, 3) #ratate array trhee times by 90 degrees
    result = Image.fromarray(imageArrayRotated) #convert result to image
    result.save("images/horizontal_removed.jpeg") #store resulting image
        

    
    