import cv2
import numpy as np


def mouse_position(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        print("left click")
        print(x,y)

def inverte(image):
    image_inverse = (255-image)
    return image_inverse
def flip_transform(image):
    image_copy=image.copy()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image_copy[i][j]=image[image.shape[0]-i-1][image.shape[1]-j-1]
    return image_copy


def conv(image,kernel):

    kernel=flip_transform(kernel)
    image_h=image.shape[0]
    image_w=image.shape[1]

    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]

    image_conv=np.zeros(image.shape)

    h=kernel_h//2
    w=kernel_w // 2

    print(h,image_h-h)
    print(w, image_w - w)
    for i in range(h,image_h-h):
        for j in range(w,image_w-w):
              sum=0
              for m in range(kernel_h):
                  for n in range(kernel_w):
                      sum=sum+kernel[m][n]*image[i-h+m][j-w+n]

              image_conv[i][j]=sum



    return image_conv


img1 = cv2.imread("4.jpg")
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY )#construct gray image
img3=inverte(img2)#inverte img2
_,thresh1=cv2.threshold(img3,190,255,cv2.THRESH_BINARY)#first threshold in order to pass only white pxs

cv2.namedWindow('thresh2')
cv2.setMouseCallback("thresh2",mouse_position)

kernel=thresh1[310:334,80:117]#defining kernel
kernel=kernel/np.sum(kernel[:])#normalizing filter

filterd_img = cv2.filter2D(thresh1,-1,kernel)#apply filter on thresh image
_,thresh2=cv2.threshold(filterd_img,190,255,cv2.THRESH_BINARY)
#cv2.equalizeHist(filterd_img)

while(True):

    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)
    cv2.imshow('thresh1',thresh1)#imshow() method is used to display an image in a window

    cv2.imshow('filtered_img',filterd_img)

    cv2.imshow('thresh2', thresh2)
    k=cv2.waitKey(1)&0xFF

    if k==27:
       break

cv2.destroyAllWindows()



