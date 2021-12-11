import cv2
import os

scale = 0.3


path = "Resource/zomato/RawBill"
myBills = os.listdir(path)


imgCrop = []
minArea = 500000

def getcontours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print (area)
        if area>minArea:
            cv2.drawContours(imgContour,cnt,-1,(255,255,0),3)
            peri = cv2.arcLength(cnt, True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            #print(len(approx))
            x, y, w1, h1 = cv2.boundingRect(approx)
            #print(x,y,w1,h1)
            imgCrop.append(imgContour[y:y+h1,x:x+w1])

for m,bills in enumerate(myBills):
    print(bills)
    img = cv2.imread(path+"/"+bills)
    imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imggray,(7,7),1)
    imgcanny = cv2.Canny(imgblur,7,7)
    imgContour = img.copy()
    getcontours(imgcanny)

for n,roi in enumerate(imgCrop):
    imgCropR = cv2.resize(roi, (0, 0), None, scale, scale)
    #cv2.imshow(str(n),imgCropR)
    cv2.imwrite("Resource/zomato/CroppedBills/" +str(n)+".png",roi)


# imgR = cv2.resize(imgContour, (0, 0), None, scale, scale)
# cv2.imshow('{bills}', imgR)
# cv2.waitKey(0)

