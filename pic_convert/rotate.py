import cv2
import os
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
    img = Image.open('./'+file)
    img = img.transpose(Image.ROTATE_90)
    img.save('./'+name+'/'+name+ str(cnt) +'.jpg')
    os.remove(file)
    cnt = cnt+1

print('Done')