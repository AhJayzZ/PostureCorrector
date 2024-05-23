import numpy as np
from PIL import Image 

pic_name   = 'output.log'
data_input = np.genfromtxt(pic_name, delimiter=',')
data_input = np.uint8(data_input)

print(data_input)
print(data_input.shape)

img = Image.fromarray(data_input, 'L')
img.save(pic_name + '.png')
img.show()