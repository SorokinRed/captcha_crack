import time
import cv2
import numpy as np
from PIL import Image
import argparse
import pytesseract
import os

def detect_symbols(img_path):
        low_red = (0,50,0)
        high_red = (255, 255, 255)

        img = cv2.imread(img_path, 1)
        black = np.zeros_like(img)
        black = np.rot90(black)

        only_symbols = cv2.inRange(img, low_red, high_red)
        rot = np.rot90(only_symbols.copy())
        detected_symbols = []

        index = 0
        for row in rot:
                if 255 in row:
                        black[index] = [255, 255, 255]
                index += 1

        black = np.rot90(black)
        black = np.rot90(black)
        black = np.rot90(black)

        index = 0
        x1 = 0
        x2 = 0
        for p in black[1]:
                if 255 not in black[1][index-1] and 255 in p:
                        x1 = index
                if 255 in p and 255 not in black[1][index+1]:
                        x2 = index
                index += 1
                if x1 != 0 and x2 != 0:
                        filename = "{}.png".format(time.time())
                        cv2.imwrite('symbols/' + filename, only_symbols[0:49, x1-1:x2+2])
                        #os.remove(filename)
                        x1 = 0
                        x2 = 0

#cv2.imshow('sum', only_symbols)
#cv2.imshow('black', black)

if __name__ == '__main__':
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
        args = vars(ap.parse_args())
        detect_symbols(args["image"])
