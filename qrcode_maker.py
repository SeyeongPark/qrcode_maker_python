import qrcode

img = qrcode.make("www.google.com")
img.save("google.jpg")

import cv2
d = cv2.QRCodeDetector()
retval, points, straight_qrcode = d.detectAndDecode(cv2.imread("google.jpg"))

print(retval)