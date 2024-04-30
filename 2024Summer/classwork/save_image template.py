from PIL import Image

def save_otl_image(image: Image.Image, filename: str):
    pixels = image.load()
    width, height = image.size
    with open(filename, 'w') as file:
        pass
    print(f'Image saved to OTL format.\nSize: {width}x{height}\nFilename: {filename}')


def load_otl_image(filename: str) -> Image.Image:
    with open(filename, 'r') as file:
        meta_data_str = file.readline().strip().split(' ')
        width = int(meta_data_str[0])
        return_image = Image.new('RGB', (100,100))
        ## Complete the code
        
    return return_image

loaded_image = load_otl_image('image.otl')
loaded_image.save('temp.png')
