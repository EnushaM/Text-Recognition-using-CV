import cv2,easyocr
import os
from os import listdir
from matplotlib import pyplot as plt
import numpy as np

def ocr(input):
    reader=easyocr.Reader(['en'],gpu=False)
    result=reader.readtext(input)
    img=cv2.imread(input)
    for detection in result:
        top_left=tuple([int(val)for val in detection[0][0]])
        bottom_right=tuple([int(val) for val in detection[0][2]])
        text=detection[1]
        font=cv2.FONT_HERSHEY_SIMPLEX
        img=cv2.rectangle(img,top_left,bottom_right,(255,0,0),5)
        img=cv2.putText(img,text,top_left,font,.5,(0,255,0),2,cv2.LINE_AA)
    plt.figure(figsize=(10,10))
    #plt.imshow(img)
    #plt.show()
    cv2.imwrite(os.path.join(dest,f[c]),img)


path ="C:/Users/91965/Downloads/License Images"
dest="C:/Users/91965/Downloads/License Outputs"
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))
c=0
for i in files:
    ocr(i)
    c+=1
