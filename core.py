def core(image_path, plot, color, seconds= .5):
    import cv2
    import numpy as np
    import time
    from helping import sliding_window, mean_squared_error

    image = cv2.imread(image_path)
    #due to cv2 not raise path error and return None
    #i will raise it manually
    try:
        image.shape
    except:
        raise ValueError("can't open the image in the given path please verify that you wrote python3 road_sign.py -i correct_image_path")
    stop = cv2.imread('stop.png')
    winH, winW = image.shape[:2]
    #cv2.imshow("stop sign", stop)
    winH = int(winH / 5)
    winW = int(winW/ 5)
    x, y = 0, 0
    #print(stop.shape)
    stop = cv2.resize(stop, (winW, winH))
    #print(stop.shape)

    (x, y, window) = next(iter(sliding_window(image, winH, winW, (winW, winH))))

    reserved_error = mean_squared_error(stop, window)
    if(color == 'red'):
        color = (0, 0, 255)
    elif(color == 'green'):
        color = (0, 255, 0)
    else:
        color = (255, 0, 0)


    for (x, y, window) in sliding_window(image, winH, winW, (winW, winH)):
       #here to prevent window from having size less thang winw
        #as mean_square_error will raise an error
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
        error = mean_squared_error(stop, window)
        if(reserved_error >= error):
            reserved_error = error
            x_cord, y_cord = x, y
            #print(x_cord, y_cord)
            #print(reserved_error)
     #the following line will plot rectangle 
            #the following line should be deleted
        if(plot == 'rect'):
            clone = image.copy()
            cv2.rectangle(clone, (x, y), (x+window.shape[0], y+window.shape[1]),
               color, 3)
     #the following line will plot the two images
        elif(plot == 'stop'):
            clone = image.copy()
            try:
                clone[x: x+window.shape[0], y:y+window.shape[1]] = stop
            except:
                continue
        elif(plot == None):
            continue
        else:
            raise ValueError("please write in plot 'rect' or 'stop' not %s" %plot)
        cv2.imshow("clone", clone)
        cv2.waitKey(1)
        time.sleep(seconds)

    cv2.rectangle(image, (x_cord, y_cord), (x_cord+winH, y_cord+winW), color, 3)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
