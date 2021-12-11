import cv2
import os

scale = 0.7

path = "Resource/swiggy/RawBill"
RawBills = os.listdir(path)


imgCrop = []
y_val = []
x_val = []
w1_val = []
minArea = 1000
maxArea = 2000

def getcontours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for n,cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        # print (area)
        if minArea<area<maxArea:
            #print(area)
            cv2.drawContours(imgContour,cnt,-1,(255,255,0),1)
            peri = cv2.arcLength(cnt, True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            #print(len(approx))
            x, y, w1, h1 = cv2.boundingRect(approx)
            #print(x,y,w1,h1)
            #imgCrop.append(imgContour[y:y+h1,x:x+w1])

            y_val.append(y)
            x_val.append(x)
            w1_val.append(w1)


for bills in RawBills:
    print(bills)
    img = cv2.imread(path+"/"+bills)
    imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imggray,(7,7),1)
    imgcanny = cv2.Canny(imgblur,7,7)
    imgContour = img.copy()
    getcontours(imgcanny)
    count = 0
    y_val.reverse()
    x_val.reverse()
    w1_val.reverse()
    while count < (len(y_val) - 1):
        imgCrop.append(imgContour[y_val[count]:y_val[count + 1], x_val[count] - 5:x_val[count] + w1_val[count]])
        count += 1
    #print(y_val,x_val,w1_val)
    y_val.clear()
    x_val.clear()
    w1_val.clear()


for n,roi in enumerate(imgCrop):
    imgCropR = cv2.resize(roi, (0, 0), None, scale, scale)
    cv2.imshow(str(n),imgCropR)
    cv2.imwrite("Resource/swiggy/CroppedBills/" +str(n)+".png",roi)



print(y_val,x_val,w1_val)
print(f'{len(imgCrop)}'+' '+'Cropped bills has been saved.')
imgR = cv2.resize(imgContour, (0, 0), None, scale, scale)
cv2.imshow('{bills}', imgR)
cv2.waitKey(0)

