from PIL import Image
import random

class Steganographer:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
    
    def read_image(self, image_path):
        image = Image.open(image_path)
        return image

    def image_to_bits(self, image):
        pixel_data = list(image.getdata())
        bits = ''.join(format(pixel, '08b') for pixel in pixel_data)
        return bits

    def bits_to_image(self, bits, original_image):
        width, height = original_image.size
        modified_pixel_data = [int(bits[i:i+8], 2) for i in range(0, len(bits), 8)]
        modified_image = Image.new('L', (width, height))
        modified_image.putdata(modified_pixel_data)
        return modified_image

    def xor_with_random(self, pixel):
        xored_pixel = (
            pixel[0] ^ random.randint(0, 255),
            pixel[1] ^ random.randint(0, 255),
            pixel[2] ^ random.randint(0, 255)
        )
        return xored_pixel

    def process_image(self, image):
        pixel_data = list(image.getdata())
        processed_pixel_data = [self.xor_with_random(pixel) for pixel in pixel_data]
        processed_image = Image.new(image.mode, image.size)
        processed_image.putdata(processed_pixel_data)
        return processed_image
    
    def encode_decode_image(self, input_image_path, output_image_path):
        input_image = self.read_image(input_image_path)
        processed_image = self.process_image(input_image)
        processed_image.save(output_image_path)

# Driver Code
if __name__ == "__main__":
    input_image_path = str(input("Enter Input Image Path: "))
    output_image_path = str(input("Enter Output Image Path: "))
    seed = int(input("Enter Seed: "))

    steganographer = Steganographer(seed)
    steganographer.encode_decode_image(input_image_path, output_image_path)
