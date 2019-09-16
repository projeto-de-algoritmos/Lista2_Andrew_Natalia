import cv2 

cv2.namedWindow("Short Path",cv2.WINDOW_NORMAL)
img = cv2.imread('graph-game.png') # load initial image

while True:
    cv2.imshow("Short Path", img)

    # The function waitKey waits for a key event infinitely (when delay<=0)
    cv2.waitKey(1)
    img = cv2.imread('graph-game.png')
 


cv2.destroyAllWindows()