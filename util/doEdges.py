#!/usr/bin/python

import logging
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image


def doPixel():

  backgroundColor = (0,)*3
  pixelSize = int(sys.argv[2])
  basewidth = 300

  image = Image.open(sys.argv[1])
  outputname = sys.argv[3]
  basedir = "/home/thw/git/colorsearch"
  outputdest = "public/uploads"
  ext = "png"

  image = image.resize((image.size[0]/pixelSize, image.size[1]/pixelSize), Image.NEAREST)
  image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)
  pixel = image.load()
  logging.debug("running pixel ..")

  for i in range(0,image.size[0],pixelSize):
    for j in range(0,image.size[1],pixelSize):
      for r in range(pixelSize):
        pixel[i+r,j] = backgroundColor
        pixel[i,j+r] = backgroundColor

  logging.debug("done pixel ..")
  wpercent = (basewidth / float(image.size[0]))
  hsize = int((float(image.size[1]) * float(wpercent)))
  newimg = image.resize((basewidth, hsize), Image.ANTIALIAS)
  logging.debug("done pres ..")
  logging.debug("presaved .. " + outputname)
  try:
    newimg.save(outputname)
  except:
    logging.error(outputname + " failed")
  print("file saved")
  sys.stdout.flush()

def main():
  myhome="/home/thw"
  logging.basicConfig(filename=myhome+'/logs/thw.log',level=logging.DEBUG)
  logging.debug('into main..')
  doPixel()
  print("file saved")
  sys.stdout.flush()
  logging.debug('done flush main..')

if __name__ == '__main__':
  main()

import cv2
    2 import numpy as np
    3 from matplotlib import pyplot as plt
    4 
    5 img = cv2.imread('messi5.jpg',0)
    6 edges = cv2.Canny(img,100,200)
    7 
    8 plt.subplot(121),plt.imshow(img,cmap = 'gray')
    9 plt.title('Original Image'), plt.xticks([]), plt.yticks([])
   10 plt.subplot(122),plt.imshow(edges,cmap = 'gray')
   11 plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
   12 
   13 plt.show()
