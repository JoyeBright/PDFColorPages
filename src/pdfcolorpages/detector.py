import fitz
import numpy as np

def is_color_image(pix):
    img=np.frombuffer(pix.samples,dtype=np.uint8)
    img=img.reshape(pix.height,pix.width,pix.n)
    if pix.n==1:
        return False
    rgb=img[...,:3]
    gray=(rgb[...,0]==rgb[...,1])&(rgb[...,1]==rgb[...,2])
    return not gray.all()

def count_color_pages(pdf_path):
    doc=fitz.open(pdf_path)
    total=len(doc)
    color=[]
    for i in range(total):
        pix=doc[i].get_pixmap(alpha=False)
        if is_color_image(pix):
            color.append(i+1)
    return total,color
