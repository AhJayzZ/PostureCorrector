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

for file in glob.glob("*.jpg"):
    np.set_printoptions(threshold=sys.maxsize)
    IMG_PATH = './'+file

    image = Image.open(IMG_PATH)
    data_array = np.array(image)
    #print('before conversion')
    #print(data_array)
    output_image = np.zeros((96,96),dtype=int)
    for height in range(96):
        for width in range(96):
            output_image[height][width] = data_array[height][width]  - 128;
    #print('after conversion')
    #print(output_image)
    cv2.imwrite('./' + name+'/' + name + str(cnt) + '.jpg', output_image)
    os.remove(file)
    cnt = cnt+1
    
print('done')