import cv2 as cv

#location = '/Desktop/PersonalProjects/IMGtoDrawing/images'
print("Hello! Type the name of your file(remember, it must be in the same directory as the program!):")
imgName = input()

print(imgName)
#Read the image
imgRead = cv.imread(imgName)

#Convert to gray
grayIMG = cv.cvtColor(imgRead, cv.COLOR_BGR2GRAY)
#invert the image
invertGray = 255 - grayIMG

#Blur the image
blurred = cv.GaussianBlur(invertGray, (21,21), 0)

#invert the blur
invertBlur = 255 - blurred

#Pencil image
pencilIMG = cv.divide(grayIMG, invertBlur, scale=256.0)


# Basic threshold test
imgContrast = cv.equalizeHist(pencilIMG)
th, dst = cv.threshold(imgContrast, 26, 215, cv.THRESH_BINARY)

cv.imshow('Drawn image:', pencilIMG)
cv.waitKey(1000)

print("Do you think your picture is clear? If not, wanna make it clearer?(y/n)")
answer = input()
if answer == 'y':
    cv.imshow('contrasted:',imgContrast)
    cv.waitKey(1000)
    print("We've just increased the contrast of the picture."
    "It may contain many black dots, making the viewing difficult.\n"
    "If this is your case and you want us to try to fix it, press 'y'. If not, press 'n'.\n")
    answer2 = input()

    if answer2 == 'y':
        cv.imshow('Final image', dst)
        cv.waitKey(1000)
        print("End of the program! Whenever ou want to exit, just press 'q':")
        end = input()
        if end == 'q':
            cv.destroyAllWindows()
            exit()
    else:
        cv.destroyAllWindows()
        exit()
else:
    cv.destroyAllWindows()
    exit()

cv.waitKey(0)
cv.destroyAllWindows()