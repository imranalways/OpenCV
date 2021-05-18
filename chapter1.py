import cv2 as cv
# print("okk")
img = cv.imread("C:\\Users\\imran.hossain\\Pictures\\Camera Roll\\fahad.jpg")

imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Image",img)
cv.imshow(" Gray Image",imgGray)
cv.waitKey(0)

# vdo = cv.VideoCapture("C:\\Users\\imran.hossain\\Pictures\\New folder\\video.mp4")

# while True:
#     success, img = vdo.read()
#     cv.imshow("video", img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
