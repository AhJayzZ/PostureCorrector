import cv2
import glob
import os

POSTURE = {
    '1' : 'sit',
    '2' : 'lay',
    '3' : 'lean'
}

ROOT_DIR = os.path.dirname(__file__)

OUTPUT_IMAGE_WIDTH = 96
OUTPUT_IMAGE_HEIGTH = 96

PICTURE_COUNT = 0

def dir_check():
    if not os.path.exists('./sit') : os.makedirs('sit')
    if not os.path.exists('./lay') : os.makedirs('lay')
    if not os.path.exists('./lean') : os.makedirs('lean')

def get_base_dir(posture):
    if posture:
        return os.path.join(ROOT_DIR,posture)
    else : 
        print('Out of index') & exit()

def get_input_jpg_image():
    images = []
    for filename in glob.iglob(ROOT_DIR + '\*.jpg', recursive=True):
        images.append(filename)
    return images

def get_picture_count(dir):
    count = 0 
    for _ in glob.iglob(dir + '**/*.jpg', recursive=True):
        count = count + 1
    return count

def rgb_to_gray(image) :
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def reduce_resolution(image):
    return cv2.resize(image, (OUTPUT_IMAGE_HEIGTH,OUTPUT_IMAGE_WIDTH))

def save_image(image,save_path,posture,picture_count) : 
    file_extension = '.jpg'
    filename = posture + str(picture_count) + file_extension
    save_path = os.path.join(save_path,filename)
    cv2.imwrite(save_path,image)

if __name__ == '__main__' :
    dir_check()
    selection = input('1:sit    |   2:lay   |   3:lean :\n')
    posture = POSTURE.get(selection,None)
    base_dir = get_base_dir(posture)

    picture_count = get_picture_count(base_dir)
    for file_path in get_input_jpg_image() :
        image = cv2.imread(file_path)
        gray_image = rgb_to_gray(image)
        fixed_image = reduce_resolution(gray_image)
        save_image(fixed_image,base_dir,posture,picture_count)
        picture_count = picture_count + 1
        os.remove(file_path)
    print('Done')