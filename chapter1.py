import cv2 as cv
# print("okk")
img = cv.imread("C:\\Users\\imran.hossain\\Pictures\\Camera Roll\\fahad.jpg")
cv.imshow("Image",img)
cv.waitKey(0)

# vdo = cv.VideoCapture("C:\\Users\\imran.hossain\\Pictures\\New folder\\video.mp4")

# while True:
#     success, img = vdo.read()
#     cv.imshow("video", img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
