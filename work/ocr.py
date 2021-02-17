import cv2
import numpy as np
import pytesseract
import re
import ocrutlis
import pattrn

#initializing the video and the captured image dimensions


def traitement(path):

    widthImg = 540
    heightImg = 740
    img = cv2.imread(path)
    img = cv2.resize(img, (widthImg, heightImg))
    #cv2.imshow("src img", img)
    imgContour = img.copy()
    imgThres = ocrutlis.preProcessing(img)
    biggest = ocrutlis.findmyContours(imgThres,imgContour)


    if biggest.size != 0:
        imgWarped = ocrutlis.getWarp(img, biggest)
        # imageArray = ([img,imgThres],
        #           [imgContour,imgWarped])
        #imageArray = ([imgContour, imgWarped])
        # cod of chracters boxing and to string the text using pytesseract
        h, w, c = imgContour.shape
        workon = ocrutlis.Processing(imgWarped)
        custom_config = r'--oem 3 --psm 6'
        x = pytesseract.image_to_string(workon, config=custom_config)
        searchObj = re.search(r'MONOPRIX', x)
        if searchObj:
            r = pattrn.pattrMonoprix(x)
            print('------------------------- MONOPRIX -------------------------')
        searchObj = re.search(r'IDEAL', x)
        if searchObj:
            r = pattrn.pattrIdeal(x)
            print('------------------------- IDEAL -------------------------')




        boxes = pytesseract.image_to_boxes(imgWarped)


        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(imgWarped, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (255, 0, 0), 1)

        # Adding custom options
        custom_config = r'--oem 3 --psm 6'
        #pytesseract.image_to_string(imgWarped, config=custom_config)
        #cv2.imshow('img', imgContour)
        # cod
        # cv2.imshow("ImageWarped", img)
        # cv2.waitKey(0)

    else:
        # imageArray = ([img, imgThres],
        #               [img, img])
        #imageArray = ([imgContour, img])

        #stackedImages = stackImages(0.6, imageArray)
        pimg = ocrutlis.Processing(img)
        custom_config = r'--oem 3 --psm 6'
        x = pytesseract.image_to_string(pimg, lang='eng+fra', config=custom_config)
        print(x)
        searchObj = re.search(r'MONOPRIX', x)
        if searchObj:
            print('------------------------- MONGPRIX -----------------------')
            r = pattrn.pattrMonoprix(x)

        searchObj = re.search(r'IDEAL', x)
        if searchObj:
            print('------------------------- IDEAL -------------------------')
            r = pattrn.pattrIdeal(x)




        h, w, c = img.shape
        boxes = pytesseract.image_to_boxes(pimg)

        for b in boxes.splitlines():
            b = b.split(' ')
            pimg = cv2.rectangle(pimg, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (255, 0, 0), 1)
        # cv2.imshow("WorkFlow", pimg)
            #cv2.waitKey(0)
            return r



#traitement("tik3.jpeg")