# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:40:50 2022

@author: Alexander
"""

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

#####might be disfunctional
def addVerticalSeams(imagePath, numberOfSeams):
    imageArray = imageToArray(imagePath)
    sobelFilteredImageArray = fullSobelFilter(imageArray) 
    
    for i in range(0, numberOfSeams):
        random.seed(i)
        s = findRandomSeam(imageArray, sobelFilteredImageArray)
        imageArray = addVerticalSeam(imageArray, s)  
        
    result = Image.fromarray(imageArray)
    result.save("vertical_added.jpeg")

def addHorizontalSeams(imagePath, numberOfSeams):
    imageArray = imageToArray90(imagePath)
    sobelFilteredImageArray = fullSobelFilter(imageArray) 
    
    for i in range(0, numberOfSeams):
        random.seed(i)
        s = findRandomSeam(imageArray, sobelFilteredImageArray)
        imageArray = addVerticalSeam(imageArray, s)  
        
    imageArrayRotated = np.rot90(imageArray, 3)
    result = Image.fromarray(imageArrayRotated)
    result.save("horizontal_added.jpeg")          

def addVerticalSeam(imageArray, seam):
    
    height = len(imageArray)
    width = len(imageArray[0])
    
    newImageArray = imageArray.copy()
    newImageArray.resize((height, width+1, 3))
    for i in range (0, height-1):
        row = imageArray[i]
        pos = seam.positions[i].y+1
        newRow = np.insert(row, pos, imageArray[i][seam.positions[i].y], 0)
        newImageArray[i] = newRow
    
    
    return newImageArray

def findRandomSeam(imageArray, sobelFilteredImage):
    
    height = len(sobelFilteredImage)
    width = len(sobelFilteredImage[0])
    
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

    seam = randomSeam(energyMap)
    
    return seam