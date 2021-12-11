import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

df_roi =   [[(2, 68), (482, 80), 'Text', 'Default'],
            [(2, 42), (461, 70), 'Text', 'Restro'],
           [(2, 66), (478, 90), 'Text', 'location'],
           [(2, 95), (82, 122), 'Number', 'Amount'],
           [(2, 154), (497, 182), 'Text', 'Order'],
           [(2, 185), (135, 207), 'Number', 'date&Time']]

var1_roi = [[(6, 248), (254, 300), 'Text', 'REORDER'],
            [(2, 42), (461, 70), 'Text', 'Restro'],
            [(2, 66), (478, 90), 'Text', 'location'],
            [(2, 95), (82, 122), 'Number', 'Amount'],
            [(4, 154), (497, 203), 'Text', 'Order'],
            [(4, 208), (179, 230), 'Number', 'Date&Time']]

roi = [df_roi,var1_roi]


path = "Resource/swiggy/CroppedBills"
crpbill = os.listdir(path)
print(crpbill)


for n,crp in enumerate(crpbill):
    img = cv2.imread(path+'/'+crp)
    imgshow = img.copy
    #cv2.imshow(str(n),img)


    mydata = []

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

    print(f'##################Extracting data from {n}##################')
    for x, r in enumerate(roiN):
        if x != 0:
            imgshow = cv2.rectangle(img, (r[0][0], r[0][1]), (r[1][0], r[1][1]), (0, 0, 255), 1)
            imgcrop = img[r[0][1]:r[1][1], r[0][0]:r[1][0]]
            #cv2.imshow(str(x),imgcrop)
            # cong = r'--oem 3 --psm 6 outputbase digits'
            print(f'{r[3]}:{pytesseract.image_to_string(imgcrop)}')
            mydata.append(pytesseract.image_to_string(imgcrop))


    with open ('Resource/swiggy/swiggy_data.csv','a+') as f:
        for data in mydata:
            f.write( (str(data))+'/')
        f.write('\n')

    scale = 1

    imgshow = cv2.resize(imgshow,None,None,scale,scale)
    cv2.imshow(str(n),imgshow)
    print(mydata)

#cv2.imshow("img", img)
cv2.waitKey(0)

