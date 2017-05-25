# -*- coding: utf-8 -*-
from six.moves import cPickle
from PIL import Image
import matplotlib as mlt
import numpy as np
import cv2
import os

# 这份文件主要是为了制作pkl数据
path = './ng-data/'
f = open('file.txt','r')
lines = f.readlines()
f.close()
screendata = np.empty((2000,128*128))
screendata_label=np.empty(2000)
for i in range(0,2000):
    p = lines[i].strip('\n')
    p = p.strip('\r')
    picpath = path + p
    img = Image.open(picpath)
    image = np.asarray(img)
    screendata[i]=np.ndarray.flatten(image)
    screendata_label[i]=1

screendata_label = screendata_label.astype(np.int)
write_file = open('screendata_ng_128.pkl','wb')
cPickle.dump(screendata,write_file,-1)
cPickle.dump(screendata_label,write_file,-1)
write_file.close()