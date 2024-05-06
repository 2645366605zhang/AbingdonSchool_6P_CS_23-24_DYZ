import binascii

PNG_SIGNATURE = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

class Chunk:
    def __init__(self, type, length, data, crc):
        self.type = type
        self.length = length
        self.data = data
        self.crc = crc

    def __repr__(self):
        return f'type: {self.type}, length: {self.length}, data: {self.data[0:10]}...'

class Header(Chunk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, ** kwargs)
        self.width = int.from_bytes(self.data[0:4], byteorder='big')
        self.height = int.from_bytes(self.data[4:8], byteorder='big')
        self.bit_depth = int.from_bytes(self.data[8:9], byteorder='big')
        self.colour_type = int.from_bytes(self.data[9:10], byteorder='big')
        self.compression_method = int.from_bytes(self.data[10:11], byteorder='big')
        self.filter = int.from_bytes(self.data[11:12], byteorder='big')
        self.interlace_method = int.from_bytes(self.data[12:13], byteorder='big')

    def display_info(self):
        print(f'size: {self.width}x{self.height}, bit depth: {self.bit_depth}, colour type: {self.colour_type}')


def readPngChunks(filename):
    with open(filename, 'rb') as pngFile:
        # read signature bytes
        signature = pngFile.read(8)
        # Check that signature is valid
        if signature != PNG_SIGNATURE:
            raise Exception("Invalid PNG signature")

        # loop reading one chunk at a time
        while True:
            # Read the chunk length 4 byte integer, big-endian - use int.from_bytes()
            length = int.from_bytes(pngFile.read(4), byteorder = "big")
            # Read the chunk type 4 byte ascii - decode('utf8')
            chunkType = pngFile.read(4).decode("utf8")
            # Read the chunk data. The length is the number you read earlier
            chunkData = pngFile.read(length)
            # Read the crc checksum. 4 byte integer
            crc = int.from_bytes(pngFile.read(4), byteorder = "big")
            # Check crc
            crcCheck = binascii.crc32(chunkType.encode('utf8') + chunkData)
            if crcCheck != crc:
                raise Exception("Invalid chunk")

            chunk = Chunk(chunkType, length, chunkData, crc)
            # Display the chunk that you've just read
            print(chunk)

            # If it's a header chunk do more stuff with it. If it's the end of the file, break the loop
            if chunk.type == 'IHDR':
                header = Header(chunkType, length, chunkData, crc)
                header.display_info()
            elif chunk.type == 'IEND':
                break

if __name__ == "__main__":
    #readPngChunks('Color-PNG-Image-Transparent-Background.png')
    readPngChunks('landscape.png')
