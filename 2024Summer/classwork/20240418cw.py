# IMPORTS

from PIL import Image
import math

# FUNCTIONS

def openImg(directory: str) -> Image:
    return Image.open(directory)

def imgInfo(image: Image):
    print(f"\nFormat: {image.format}\nsize: {image.size}\nmode: {image.mode}\n")

def modifyImg(image: Image, mode: str) -> Image:
    mode = mode.upper()
    newImage = Image.new(image.mode, image.size)
    pixels = image.load()
    newPixels = newImage.load()
    if mode == "RED":
        for y in range(newImage.size[1]):
            for x in range(newImage.size[0]):
                newPixels[(x, y)] = (pixels[(x, y)][0], 0, 0)
                #print(f"\nx: {x}, y: {y}\nRGB: {pixels[(x, y)]}\n")
    elif mode == "GREEN":
        for y in range(newImage.size[1]):
            for x in range(newImage.size[0]):
                newPixels[(x, y)] = (0, pixels[(x, y)][1], 0)
                #print(f"\nx: {x}, y: {y}\nRGB: {pixels[(x, y)]}\n")
    elif mode == "BLUE":
        for y in range(newImage.size[1]):
            for x in range(newImage.size[0]):
                newPixels[(x, y)] = (0, 0, pixels[(x, y)][2])
                #print(f"\nx: {x}, y: {y}\nRGB: {pixels[(x, y)]}\n")
    elif mode == "MIRROR_H":
        for y in range(newImage.size[1]):
            for x in range(newImage.size[0]):
                newPixels[(x, y)] = pixels[(image.size[0] - x - 1, y)]
                #print(f"\nx: {x}, y: {y}\nRGB: {pixels[(x, y)]}\n")
    elif mode == "MIRROR_V": # Somehow doesn't work for landscape.png
        for y in range(newImage.size[1]):
            for x in range(newImage.size[0]):
                newPixels[(x, y)] = pixels[(x, image.size[0] - y - 1)]
                #print(f"\nx: {x}, y: {y}\nRGB: {pixels[(x, y)]}\n")
    elif mode == "MIRROR_HV": # Somehow doesn't work for landscape.png
        for y in range(newImage.size[1]):
            for x in range(newImage.size[0]):
                newPixels[(x, y)] = pixels[(image.size[0] - x - 1, image.size[0] - y - 1)]
                #print(f"\nx: {x}, y: {y}\nRGB: {pixels[(x, y)]}\n")
    elif mode == "GREY":
        for y in range(newImage.size[1]):
            for x in range(newImage.size[0]):
                avrg = int((pixels[(x, y)][0] + pixels[(x, y)][1] + pixels[(x, y)][2]) / 3)
                newPixels[(x, y)] = (avrg, avrg, avrg)
                #print(f"\nx: {x}, y: {y}\nRGB: {pixels[(x, y)]}\n")
    else:
        raise Exception("Invalid mode")
    return newImage

def addImg(firstImg: Image, secondImg: Image) -> Image: # Add the RGB value of the images together
    if firstImg.size[0] > secondImg.size[0]:
        newX = firstImg.size[0]
        smallX = [secondImg.size[0], 0]
    else:
        newX = secondImg.size[0]
        smallX = [firstImg.size[0], 1]
    if firstImg.size[1] > secondImg.size[1]:
        newY = firstImg.size[1]
        smallY = [secondImg.size[1], 0]
    else:
        newY = secondImg.size[1]
        smallY = [firstImg.size[1], 1]
    newImage = Image.new("RGB", (newX, newY))
    pixels = [firstImg.load(), secondImg.load()]
    newPixels = newImage.load()
    for y in range(newImage.size[1]):
            for x in range(newImage.size[0]):
                if x >= smallX[0]:
                    r = pixels[smallX[1]][(x, y)][0]
                    g = pixels[smallX[1]][(x, y)][1]
                    b = pixels[smallX[1]][(x, y)][2]
                elif y >= smallY[0]:
                    r = pixels[smallY[1]][(x, y)][0]
                    g = pixels[smallY[1]][(x, y)][1]
                    b = pixels[smallY[1]][(x, y)][2]
                else:
                    r = (pixels[0][(x, y)][0] + pixels[1][(x, y)][0]) % 255
                    g = (pixels[0][(x, y)][1] + pixels[1][(x, y)][1]) % 255
                    b = (pixels[0][(x, y)][2] + pixels[1][(x, y)][2]) % 255
                newPixels[(x, y)] = (r, g, b)
                #print(f"\nx: {x}, y: {y}\nRGB: {pixels[(x, y)]}\n")
    return newImage

def stkImg(firstImg: Image, secondImg: Image, offsetX: int, offsetY: int, mode: str = "STK", tolerance: int = 192) -> Image: # "Stack" images together
    mode = mode.upper()
    modeList = ["STK", "STKDIR", "STKRB", "STKGB", "STKBB"]
    # Check whether firstImg or secondImg is larger
    if firstImg.size[0] > secondImg.size[0] + offsetX:
        newX = firstImg.size[0]
        smallX = [secondImg.size[0] + offsetX, 0] # [size of the smaller image, which image is bigger]
    else:
        newX = secondImg.size[0] + offsetX
        smallX = [firstImg.size[0], 1]
    if firstImg.size[1] > secondImg.size[1] + offsetY:
        newY = firstImg.size[1]
        smallY = [secondImg.size[1] + offsetY, 0]
    else:
        newY = secondImg.size[1] + offsetY
        smallY = [firstImg.size[1], 1]
    # Create the new image based on the biggest x and y value of both iamges
    newImage = Image.new("RGB", (newX, newY))
    pixels = [firstImg.load(), secondImg.load()]
    newPixels = newImage.load()
    if mode == modeList[0]:
        # Iterate through every pixel of the new image and check if it needs to be "stacked"
        for y in range(newImage.size[1]):
                for x in range(newImage.size[0]):
                    if y >= smallY[0] and x >= smallX[0]:
                        r, g, b = 0, 0, 0
                    # Leave the pixel as it is when x is only available for 1 of the images
                    elif x >= smallX[0]:
                        r, g, b = pixels[smallX[1]][(x, y)][0], pixels[smallX[1]][(x, y)][1], pixels[smallX[1]][(x, y)][2]
                    # Leave the pixel as it is when y is only available for 1 of the images
                    elif y >= smallY[0]:
                        r, g, b = pixels[smallY[1]][(x, y)][0], pixels[smallY[1]][(x, y)][1], pixels[smallY[1]][(x, y)][2]
                    # "Stack" the pixel's colour when both x and y is in range of both images
                    elif not((x <= secondImg.size[0] + offsetX and y <= offsetY) or (x <= offsetX and y <= secondImg.size[1] + offsetY)):
                        r = int((pixels[0][(x, y)][0] + pixels[1][(x - offsetX, y - offsetY)][0]) / 2)
                        g = int((pixels[0][(x, y)][1] + pixels[1][(x - offsetX, y - offsetY)][1]) / 2)
                        b = int((pixels[0][(x, y)][2] + pixels[1][(x - offsetX, y - offsetY)][2]) / 2)
                    # Make sure that the offset parts show only image 0
                    else:
                        r, g, b = pixels[0][(x, y)][0], pixels[0][(x, y)][1], pixels[0][(x, y)][2]
                    try:
                        newPixels[(x, y)] = (r, g, b)
                    except IndexError:
                        pass
    elif mode in modeList:
        # Iterate through every pixel of the new image and check if it needs to be "stacked"
        for y in range(newImage.size[1]):
                for x in range(newImage.size[0]):
                    if y >= smallY[0] and x >= smallX[0]:
                        r, g, b = 0, 0, 0
                    # Leave the pixel as it is when x is only available for 1 of the images
                    elif x >= smallX[0]:
                        r, g, b = pixels[smallX[1]][(x, y)][0], pixels[smallX[1]][(x, y)][1], pixels[smallX[1]][(x, y)][2]
                    # Leave the pixel as it is when y is only available for 1 of the images
                    elif y >= smallY[0]:
                        r, g, b = pixels[smallY[1]][(x, y)][0], pixels[smallY[1]][(x, y)][1], pixels[smallY[1]][(x, y)][2]
                    # "Stack" the pixel's colour when both x and y is in range of both images
                    elif not((x <= secondImg.size[0] + offsetX and y <= offsetY) or (x <= offsetX and y <= secondImg.size[1] + offsetY)):
                        if mode == modeList[1]:
                            r, g, b = pixels[1][(x, y)][0], pixels[1][(x, y)][1], pixels[1][(x, y)][2]
                        elif mode == modeList[2]:
                            if pixels[1][(x, y)][0] >= tolerance:
                                r, g, b = pixels[0][(x, y)][0], pixels[0][(x, y)][1], pixels[0][(x, y)][2]
                            else:
                                r, g, b = pixels[1][(x, y)][0], pixels[1][(x, y)][1], pixels[1][(x, y)][2]
                        elif mode == modeList[3]:
                            if pixels[1][(x, y)][1] >= tolerance:
                                r, g, b = pixels[0][(x, y)][0], pixels[0][(x, y)][1], pixels[0][(x, y)][2]
                            else:
                                r, g, b = pixels[1][(x, y)][0], pixels[1][(x, y)][1], pixels[1][(x, y)][2]
                        elif mode == modeList[4]:
                            if pixels[1][(x, y)][2] >= tolerance:
                                r, g, b = pixels[0][(x, y)][0], pixels[0][(x, y)][1], pixels[0][(x, y)][2]
                            else:
                                r, g, b = pixels[1][(x, y)][0], pixels[1][(x, y)][1], pixels[1][(x, y)][2]
                    # Make sure that the offset parts show only image 0
                    else:
                        r, g, b = pixels[0][(x, y)][0], pixels[0][(x, y)][1], pixels[0][(x, y)][2]
                    try:
                        newPixels[(x, y)] = (r, g, b)
                    except IndexError:
                        pass
    return newImage

def addCircle(image: Image, r: int, g: int, b: int, circleRadius: int, centerX: int, centerY: int, mode: str = "EMPTY", colorTest: bool = False) -> Image:
    mode = mode.upper()
    modeList = ["EMPTY", "SMALLSOLID", "LARGESOLID"]
    newImage = Image.new(image.mode, image.size)
    pixels = image.load()
    newPixels = newImage.load()
    for y in range(newImage.size[1]):
            for x in range(newImage.size[0]):
                 newPixels[(x, y)] = (pixels[(x, y)][0], pixels[(x, y)][1], pixels[(x, y)][2])
    if mode == modeList[0]:
        angle = 0
        while angle < (2 * math.pi):
            x = circleRadius * math.cos(angle) + centerX
            y = circleRadius * math.sin(angle) + centerY
            if colorTest:
                newPixels[(x, y)] = (int(x) , int(y), int((x + y) % 255))
            else:
                newPixels[(x, y)] = (r, g, b)
            angle += 0.01
    elif mode == modeList[1]:
        for radius in reversed(range(circleRadius)):
            angle = 0
            while angle < (2 * math.pi):
                x = radius * math.cos(angle) + centerX
                y = radius * math.sin(angle) + centerY
                try:
                    if colorTest:
                        newPixels[(x, y)] = (int(x) , int(y), int((x + y) % 255))
                    else:
                        newPixels[(x, y)] = (r, g, b)
                except IndexError:
                    pass
                angle += 0.01
    elif mode == modeList[2]:
        pass # TBD
    else:
        raise Exception("Invalid mode")
    return newImage

# MAIN

if __name__ == "__main__":
    imgDir = [
        "2024Summer/classwork/landscape.png", 
        "2024Summer/classwork/preston.jpg", 
        "2024Summer/classwork/abds.jpg", 
        "2024Summer/classwork/doit.jpg"
    ]
    #imgInfo(openImg(imgDir[0]))
    #addCircle(openImg(imgDir[0]), 255, 255, 255, 128, 128, 128, "EMPTY").show()
    #stkImg(openImg(imgDir[0]), modifyImg(openImg(imgDir[1]), "GREY"), 20, 20, "STK").show()
    stkImg(openImg(imgDir[2]), addCircle(openImg(imgDir[3]), 0, 250, 0, 32, 320, 200, "SMALLSOLID"), 0, 0, "STKGB", 192).show()