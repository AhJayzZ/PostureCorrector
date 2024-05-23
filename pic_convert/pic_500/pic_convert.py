import cv2
import os
import glob

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
    image = cv2.imread(file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (480, 640), interpolation=cv2.INTER_AREA)
    print(image.shape)
    cv2.imwrite('./'+name+'/'+name+ str(cnt) +'.jpg', image)
    os.remove(file)
    cnt = cnt+1

print('Done')
    
