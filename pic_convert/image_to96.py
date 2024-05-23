import cv2
import os
import sys
import numpy as np
import glob
from PIL import Image

selection = input('1:sit    |   2:lay   |   3:lean :\n')
if selection == '1':
    name = 'sit'
elif selection == '2':
    name = 'lay'
elif selection == '3':
    name = 'lean'
else:
    name = 'sit'

cnt = 0

for file in glob.glob('./'+name+'/*.jpg'):
    cnt = cnt+1


def down_scaling(input_image,input_height,input_width,output_image,output_width,output_height):
    width_step  = 0;
    height_step = 0;

    width_i1  = 0;
    height_i1 = 0;
    width_i2  = 0;
    height_i2 = 0;
    pixel_buf = 0;

    width_step  = int(input_width / output_width)
    height_step = int(input_height / output_height)

    for height_i1 in range(output_height) :
        for width_i1 in range(output_width) :
            pixel_buf = 0
            for height_i2 in range(height_step) :
                for width_i2 in range(width_step) :
                    pixel_buf = pixel_buf + input_image[height_i1 * height_step + height_i2][width_i1 * width_step + width_i2]
            pixel_buf = pixel_buf / (width_step * height_step)
            if(pixel_buf > 255) : pixel_buf = 255
            output_image[height_i1][width_i1] = pixel_buf;
    return output_image

def imageToJPG(name, image) :
    try : 
        return cv2.imwrite('./test.jpg', image)
    except Exception as e : 
        print(e)
        pass


for file in glob.glob("*.jpg"):
    np.set_printoptions(threshold=sys.maxsize)
    IMG_PATH = './'+file

    image = Image.open(IMG_PATH)
    data_array = np.array(image)
    output_image = np.zeros((96,96),dtype=int)

    image = down_scaling(data_array, 480, 640, output_image, 96, 96)
    cv2.imwrite('./' + name+'/' + name + str(cnt) + '.jpg', image)
    os.remove(file)
    cnt = cnt+1
    
print('done')