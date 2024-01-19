import matplotlib.pyplot as plt
import easyocr as modelhindi2
import cv2


from pylab import rcParams
from IPython.display import Image


def ocrfunc(file_name):
    rcParams['figure.figsize'] = 8, 16
    reader = modelhindi2.Reader(['hi'])
    Image(file_name)
    output = reader.readtext(file_name)
    lis=[]
    str=""
    for item in output:
        lis.append(item)
        str+=(item[1])
        str+=' '
    lis.append(str)
    return lis