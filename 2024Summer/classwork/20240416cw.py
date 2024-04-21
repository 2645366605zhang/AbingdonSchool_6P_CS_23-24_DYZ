# IMPORTS

from PIL import Image

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

def stkImg(firstImg: Image, secondImg: Image) -> Image: # "Stack" images together
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
                    r = int((pixels[0][(x, y)][0] + pixels[1][(x, y)][0]) / 2)
                    g = int((pixels[0][(x, y)][1] + pixels[1][(x, y)][1]) / 2)
                    b = int((pixels[0][(x, y)][2] + pixels[1][(x, y)][2]) / 2)
                newPixels[(x, y)] = (r, g, b)
                #print(f"\nx: {x}, y: {y}\nRGB: {pixels[(x, y)]}\n")
    return newImage

# MAIN

if __name__ == "__main__":
    imgDir = "2024Summer/classwork/landscape.png"
    imgDir0 = "2024Summer/classwork/preston.jpg"
    #modifyImg(openImg(imgDir), "RED").show()
    #modifyImg(openImg(imgDir), "GREEN").show()
    #modifyImg(openImg(imgDir), "BLUE").show()
    #modifyImg(openImg(imgDir), "GREY").show()
    #modifyImg(openImg(imgDir), "MIRROR_HV").show()
    #modifyImg(addImg(openImg(imgDir), openImg(imgDir0)), "RED").show()
    #addImg(openImg(imgDir0), modifyImg(openImg(imgDir0), "MIRROR_H")).show()
    #stkImg(openImg(imgDir0), modifyImg(openImg(imgDir), "MIRROR_H")).show()
    #addImg(openImg(imgDir0), modifyImg(openImg(imgDir0), "MIRROR_H")).show()
    #addImg(openImg(imgDir0), addImg(openImg(imgDir0), addImg(openImg(imgDir0), addImg(openImg(imgDir0), addImg(openImg(imgDir0), addImg(openImg(imgDir0), addImg(openImg(imgDir0), openImg(imgDir0)))))))).show()