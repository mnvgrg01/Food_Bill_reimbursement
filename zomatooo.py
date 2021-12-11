import cv2
import pytesseract
import os


df_roi = [[(21, 210), (264, 281), 'text', 'Default'],
          [(13, 362), (470, 410), 'Number', 'Date&Time'],
          [(151, 100), (762, 145),'text', 'Location'],
          [(159, 56), (808, 93),  'text', 'Restro'],
          [(18, 251), (962, 310), 'text', 'Order'],
          [(827, 54), (1002, 97), 'Number', 'Final Amount']]

var1_roi = [[(21, 210), (264, 281), 'text', 'Delivered'],
       [(16, 437), (905, 491), 'Number','Date&Time'],
       [(151, 100), (762, 145),'text', 'Location'],
       [(159, 56), (808, 93),  'text', 'Restro'],
       [(18, 329), (932, 383), 'text','Order'],
       [(827, 54), (1002, 97), 'Number', 'Final Amount']]

var2_roi = [[(18, 367), (240, 405), 'text', 'ORDERED ON'],
       [(16, 408), (605, 456), 'Number', 'Date&Time'],
       [(151, 100), (762, 145),'text', 'Location'],
       [(159, 56), (808, 93),  'text', 'Restro'],
       [(13, 248), (959, 337), 'Text', 'Order'],
       [(827, 54), (1002, 97), 'Number', 'Final Amount']]

var3_roi = [[(18, 475), (383, 527), 'text', 'Payment Incomplete']]

roi = [df_roi, var1_roi,var2_roi ,var3_roi]

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

path1 = "Resource/zomato/CroppedBills"
myTestImgs = os.listdir(path1)
print(myTestImgs)
for j,y in enumerate(myTestImgs):
    img = cv2.imread(path1+"/"+y)
    imgshow = img.copy()


    myData = []

    roiN = roi[0]
    for r in roi:
        #print(r)
        imgroi = img[r[0][0][1]:r[0][1][1], r[0][0][0]:r[0][1][0]]
        # cv2.imshow("imgroi",imgroi)
        var = pytesseract.image_to_string(imgroi)
        # print(var1)
        if var == r[0][3]:
            roiN = r
            break


    print(f'##################Extracting data from {y}##################')
    for x,r in enumerate(roiN):
        imgshow = cv2.rectangle(imgshow,(r[0][0],r[0][1]),(r[1][0],r[1][1]),(0,0,255),1)
        #imgshow = cv2.addWeighted(imgshow,0.99,imgmask,0.1,0)
        if x != 0:
            imgcrop = img[r[0][1]:r[1][1],r[0][0]:r[1][0]]
            #cv2.imshow(str(x),imgcrop)

            #cong = r'--oem 3 --psm 6 outputbase digits'
            print(f'{r[3]}:{pytesseract.image_to_string(imgcrop)}')
            myData.append(pytesseract.image_to_string(imgcrop))


    with open ('Resource/zomato/Zomato_data.csv','a+') as f:
        for data in myData:
            f.write( (str(data))+'/')
        f.write('\n')

    scale = 0.37

    imgshow = cv2.resize(imgshow,None,None,scale,scale)
    cv2.imshow(y  ,imgshow)
    print(myData)


cv2.waitKey(0)