import cv2
import numpy as np
import pymongo
from PIL import Image
from fuzzywuzzy import process
from scipy.ndimage import interpolation as inter
from wand.image import Image as Im

widthImg = 540
heightImg = 740


def autocorrect(tup):
    p = []
    client = pymongo.MongoClient("mongodb://farouk:Frouga1@pfe-shard-00-00.di1sy.mongodb.net:27017,pfe-shard-00-01.di1sy.mongodb.net:27017,pfe-shard-00-02.di1sy.mongodb.net:27017/?ssl=true&replicaSet=atlas-2c3pjn-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.pfe
    products = db.products.find({}, {"_id": 1, "name": 1})
    a = db.products.count_documents({})
    for i in range(a):
        p.append(products[i]["name"])
        print(p[i])
    for i in range(len(tup) - 1):
        highest = process.extractOne(tup[i]['pname'], p)
        print(tup[i]['pname'])
        print('highest match', highest)
        if highest[1] > 70:
            tup[i]['pname'] = highest[0]
    return tup


# def set_image_dpi(file_path):
#     im = Image.open(file_path)
#     length_x, width_y = im.size
#     factor = min(1, float(1024.0 / length_x))
#     size = int(factor * length_x), int(factor * width_y)
#     im_resized = im.resize(size, Image.ANTIALIAS)
#     temp_file = temp_file.NamedTemporaryFile(delete=False,   suffix='.png')
#     temp_filename = temp_file.name
#     im_resized.save(temp_filename, dpi=(300, 300))
#     return temp_filename

def Processing(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 250, 1, 1, 5, 3)
    # imgAdaptiveThre = cv2.bitwise_not(img)
    # imgAdaptiveThre = cv2.medianBlur(img, 3)
    # kernel = np.ones((3, 3), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    ret2, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.imshow("Process", img)
    # cv2.waitKey(0)
    return img


def Processing1(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (3, 3), 1)
    img = cv2.Canny(img, 100, 100)
    kernel = np.ones((3, 3))
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # cv2.imshow("Process1", img)
    # cv2.waitKey(0)
    return img


def Processing2(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (3, 3), 1)
    # imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 250, 1, 1, 5, 3)
    # imgAdaptiveThre = cv2.bitwise_not(img)
    # imgAdaptiveThre = cv2.medianBlur(img, 3)
    # kernel = np.ones((3, 3), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    ret2, img = cv2.threshold(img, 0, 127, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.imshow("Process2", img)
    # # cv2.waitKey(0)
    return img


def Processing3(img):
    with Im(filename='temp.jpeg') as i:
        i.morphology(method='erode', kernel='diamond')
        i.save(filename='morph-dilate.jpeg')
    img = np.array(Image.open('morph-dilate.jpeg'))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret2, img = cv2.threshold(img, 0, 127, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow("Process3", img)
    cv2.waitKey(0)
    return img


def preProcessing(img):
    # imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    # imgCanny = cv2.Canny(imgBlur,200,200)
    # kernel = np.ones((5,5))
    # imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    # imgThres = cv2.erode(imgDial,kernel,iterations=1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # kernel = np.ones((1, 1), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)
    ret2, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.imshow("ImageWarped", img)
    # cv2.waitKey(0)
    return img


def findmyContours(img, imgContour):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 9000000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)

    return biggest


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew


def getWarp(img, biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    imgCropped = imgOutput[20:imgOutput.shape[0] - 20, 20:imgOutput.shape[1] - 20]
    imgCropped = cv2.resize(imgCropped, (widthImg, heightImg))

    return imgCropped

    # def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def correct_skew(image, delta=1, limit=5):
    def determine_score(arr, angle):
        data = inter.rotate(arr, angle, reshape=False, order=0)
        histogram = np.sum(data, axis=1, dtype=float)
        score = np.sum((histogram[1:] - histogram[:-1]) ** 2, dtype=float)
        return histogram, score

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    scores = []
    angles = np.arange(-limit, limit + delta, delta)
    for angle in angles:
        histogram, score = determine_score(thresh, angle)
        scores.append(score)

    best_angle = angles[scores.index(max(scores))]

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, best_angle, 1.0)
    corrected = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC,
                               borderMode=cv2.BORDER_REPLICATE)
    #cv2.imshow("ImageWarped", image)
    #cv2.imshow("ImageWad", corrected)
    #cv2.waitKey(0)
    return best_angle, corrected
