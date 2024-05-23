import cv2
import sys
import numpy as np
from PIL import Image

np.set_printoptions(threshold=sys.maxsize)

IMG_PATH = "./sit0.jpg"

# image = cv2.imread(IMG_PATH)
image = Image.open(IMG_PATH)

data_array = np.array(image)
#print(data_array)
#print(data_array.shape)

# output_image = np.zeros((96,96),dtype=int)

# def down_scaling(input_image,input_height,input_width,output_image,output_width,output_height):
#     width_step  = 0;
#     height_step = 0;

#     width_i1  = 0;
#     height_i1 = 0;
#     width_i2  = 0;
#     height_i2 = 0;
#     pixel_buf = 0;

#     width_step  = int(input_width / output_width)
#     height_step = int(input_height / output_height)

#     for height_i1 in range(output_height) :
#         for width_i1 in range(output_width) :
#             pixel_buf = 0
#             for height_i2 in range(height_step) :
#                 for width_i2 in range(width_step) :
#                     pixel_buf = pixel_buf + input_image[height_i1 * height_step + height_i2][width_i1 * width_step + width_i2]
#             pixel_buf = pixel_buf / (width_step * height_step)
#             if(pixel_buf > 255) : pixel_buf = 255
#             output_image[height_i1][width_i1] = pixel_buf;
#     return output_image

# def imageToJPG(image) :
#     try : 
#         return cv2.imwrite('./test.jpg', image)
#     except Exception as e : 
#         print(e)
#         pass
    


# image = down_scaling(data_array, 640, 480, output_image, 96, 96)
# jpg = imageToJPG(image)
# print('done')