import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#location = '/Desktop/PersonalProjects/IMGtoDrawing/images'
imgName = 'rockInRio.jpg'

#Read the image
imgRead = cv.imread(imgName)

cv.imshow('Original image', imgRead)

#cConvert to gray
grayIMG = cv.cvtColor(imgRead, cv.COLOR_BGR2GRAY)
#invert the image
invertGray = 255 - grayIMG

#Blur the image
blurred = cv.GaussianBlur(invertGray, (21,21), 0)

#invert the blur
invertBlur = 255 - blurred

#Pencil img
pencilIMG = cv.divide(grayIMG, invertBlur, scale=256.0)


#clahe=cv.createCLAHE(clipLimit=40)
#imgClahe=clahe.apply(imgContrast)
th = 80
max_val = 255

# Basic threhold example
imgContrast = cv.equalizeHist(pencilIMG)
th, dst = cv.threshold(imgContrast, 26, 215, cv.THRESH_BINARY)
cv.imshow('Final image', dst)
cv.imshow('Original image', pencilIMG)
cv.imshow('contrasted:',imgContrast)

cv.waitKey(15000)

cv.destroyAllWindows()