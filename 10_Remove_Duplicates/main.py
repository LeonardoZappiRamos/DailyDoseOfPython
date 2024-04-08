import os
import cv2
import numpy as np


FILES_PATH = os.path.join(os.path.dirname(__file__), "files")


def compare_image(image_1, image_2):
    i1 = cv2.imread(image_1)
    i2 = cv2.imread(image_2)
    i1 = cv2.cvtColor(i1, cv2.COLOR_BGR2GRAY)
    i2 = cv2.cvtColor(i2, cv2.COLOR_BGR2GRAY)
    
    h, v = i1.shape
    diff = cv2.subtract(i1, i2)
    err = np.sum(diff**2)
    mse = err/(float(h*v))
    return mse, diff


def compare_file(file_1, file_2):
    try:
        txt_1 = open(file_1, 'r').read()
        txt_2 = open(file_2, 'r').read()
        return (txt_1 == txt_2)
    except Exception:
        return False

if __name__ == "__main__":
    files = os.listdir(FILES_PATH)
    imgs = [file for file in files if file.split('.')[-1] == 'png']
    texts = [file for file in files if file.split('.')[-1] == 'txt']
    
    # Delete Image Samples Duplicates
    for img in imgs:
        for comp in imgs:
            if img.split('.')[0] != comp.split('.')[0]:
                try:
                    mse, err = compare_image(os.path.join(FILES_PATH,img), os.path.join(FILES_PATH,comp))
                    if mse == 0.0:
                        os.remove(os.path.join(FILES_PATH,comp))
                except Exception as e:
                    pass
    # Delete Text Samples Duplicates
    for txt in texts:
        for comp in texts:
            if txt.split('.')[0] != comp.split('.')[0]:
                flq = compare_file(os.path.join(FILES_PATH,txt), os.path.join(FILES_PATH,comp))
                if flq is True:
                        os.remove(os.path.join(FILES_PATH,comp))