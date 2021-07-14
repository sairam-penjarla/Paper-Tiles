import requests
import cv2
import numpy as np
import imutils

while True:
    success,img = cap.read()
    

    # uncommen the following code if you use an IP cam
    '''url = "http://192.168.0.106:8080/shot.jpg"
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)'''



    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 170, 255)
    ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    (contours, _) = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    colors = [(163, 88, 88), (163, 125, 88), (160, 163, 88), (115, 163, 88), (88, 163, 138), (88, 144, 163), (88, 100, 163), (118, 88, 163), (163, 88, 88), (163, 125, 88), (160, 163, 88), (115, 163, 88), (88, 163, 138), (88, 144, 163), (88, 100, 163), (118, 88, 163)]
    i = 0
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) <50:
            moment = cv2.moments(cnt)
            cv2.drawContours(img, [cnt], -1, colors[(i % len(colors))-1], thickness=-100)
            cv2.imshow('polygons_detected', img)
            i += 1
    cv2.imshow('polygons_detected', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
