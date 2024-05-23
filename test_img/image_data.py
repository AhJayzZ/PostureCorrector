import cv2
import sys
import numpy as np
import glob
from PIL import Image
from pathlib import Path

np.set_printoptions(threshold=sys.maxsize)



# image = cv2.imread(IMG_PATH)

for file in glob.glob("*.jpg"):
    IMG_PATH = './'+file
    file_name = Path(IMG_PATH).stem
    image = Image.open(IMG_PATH)
    data_array = np.array(image)
    np.savetxt('./'+file_name+'.txt', data_array, fmt = '%s', delimiter=',', newline=',\n')
print('done')
