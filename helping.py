import numpy as np
import cv2

def sliding_window(image, y_step, x_step, windowSize):
    for y in range(0, image.shape[0], y_step):
        for x in range(0, image.shape[1], x_step):
            yield (x, y, image[y: y + windowSize[1] ,
                            x: x + windowSize[0]])

def mean_squared_error(img1, img2):
    if(img1.shape != img2.shape):
        raise ValueError("images should be the same shape, but given {}, {}".\
                format(img1.shape, img2.shape))
    error = np.sum((img1.astype("float") - img2.astype("float"))**2)
    error = error / (img1.shape[0]*img1.shape[1]*img1.shape[2])
    return error
#return np.abs(error)
