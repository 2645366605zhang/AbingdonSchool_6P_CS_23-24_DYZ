# IMPORTS

from PIL import Image

# FUNCTIONS

def saveOtlImage(image: Image, filename: str):
    pixels, width, height = image.load(), image.size[0], image.size[1]
    with open(filename, 'w') as file:
        file.write(f"{width} {height}\n")
        for y in range(height):
            for x in range(width):
                file.write(f"{pixels[(x, y)][0]} {pixels[(x, y)][1]} {pixels[(x, y)][2]}\n")
    print(f'Image saved to OTL format.\nSize: {width}×{height}\nFilename: {filename}')


def loadOtlImage(filename: str) -> Image:
    with open(filename, 'r') as file: metaDataList, pixelData = file.readline().strip().split(' '), file.readlines()[1:]
    width, height = int(metaDataList[0]), int(metaDataList[1])
    for index in range(len(pixelData)): pixelData[index] = tuple(map(int, pixelData[index].strip().split(' ')))
    newImage = Image.new('RGB', (width, height))
    newImage.putdata(pixelData)
    return newImage

# MAIN

if __name__ == "__main__":
    #loaded_image = loadOtlImage('image.otl')
    #loaded_image.save('temp.png')
    saveOtlImage(loadOtlImage('image.otl'), "rkrl.otl")
    loadOtlImage("rkrl.otl").show()
