import os

import cv2
import numpy as np
import pytesseract
import re
import urllib.request
from PIL import Image
import ocrutlis
import pattrn
from wand.image import Image as Im
import extract


def traitement(path):

    with urllib.request.urlopen(path) as url:
        with open('temp.jpeg', 'wb') as f:
            f.write(url.read())
    img = np.array(Image.open('temp.jpeg'))
    with Im(filename='temp.jpeg') as i:
        i.morphology(method='erode', kernel='diamond')
        i.save(filename='morph-dilate.jpeg')
    ocrutlis.correct_skew(img)
    widthImg = 540
    heightImg = 740
    img = cv2.resize(img, (widthImg, heightImg))
    pytesseract.pytesseract.tesseract_cmd = os.environ.get(
        "TESSERACT_CMD", "tesseract"
    )
    pimg = ocrutlis.Processing(img)
    pimg1 = ocrutlis.Processing1(img)
    pimg2 = ocrutlis.Processing2(img)
    pimg3 = ocrutlis.Processing3(img)
    custom_config = r'--oem 3 --psm 6 tessedit_char_blacklist=aA'

    x1 = pytesseract.image_to_string(img, lang='eng+fra', config=custom_config)
    x2 = pytesseract.image_to_string(pimg, lang='eng+fra', config=custom_config)
    x3 = pytesseract.image_to_string(pimg1, lang='eng+fra', config=custom_config)
    x4 = pytesseract.image_to_string(pimg2, lang='eng+fra', config=custom_config)
    x5 = pytesseract.image_to_string(pimg3, lang='eng+fra', config=custom_config)
    x6 = extract.treat(path)
    searchObj1 = re.search(r'MONOPR', x1)
    searchObj2 = re.search(r'MONOPR', x2)
    searchObj3 = re.search(r'MONOPR', x3)
    searchObj4 = re.search(r'MONOPR', x4)
    searchObj5 = re.search(r'MONOPR', x5)
    searchObj6 = re.search(r'MONOPR', x6)
    if searchObj1 or searchObj2 or searchObj3 or searchObj4 or searchObj5 or searchObj6:

        print('------------------------- MONOPRIX -----------------------')
        r1 = pattrn.pattrMonoprix(x1)
        r2 = pattrn.pattrMonoprix(x2)
        r3 = pattrn.pattrMonoprix(x3)
        r4 = pattrn.pattrMonoprix(x4)
        candidates = {'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4}
        r = max(candidates.values(), key=lambda c: len(c.tup))

    searchObj1 = re.search(r'CARREFOUR', x1)
    searchObj2 = re.search(r'CARREFOUR', x2)
    searchObj3 = re.search(r'CARREFOUR', x3)
    searchObj4 = re.search(r'CARREFOUR', x4)
    searchObj6 = re.search(r'CARREFOUR', x6)
    if searchObj1 or searchObj2 or searchObj3 or searchObj4 or searchObj6:

        print('------------------------- CARREFOUR -----------------------')
        r1 = pattrn.pattrcarrf(x1)
        r2 = pattrn.pattrcarrf(x2)
        r3 = pattrn.pattrcarrf(x3)
        r4 = pattrn.pattrcarrf(x4)
        r6 = pattrn.pattrcarrf(x6)
        candidates = {'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4, 'r6': r6}
        r = max(candidates.values(), key=lambda c: len(c.tup))

    searchObj1 = re.search(r'AZIZA', x1)
    searchObj2 = re.search(r'AZIZA', x2)
    searchObj3 = re.search(r'AZIZA', x3)
    searchObj4 = re.search(r'AZIZA', x4)
    searchObj6 = re.search(r'AZIZA', x6)

    if searchObj1 or searchObj2 or searchObj3 or searchObj4 or searchObj6:
        print('------------------------- AZIZA -----------------------')
        r1 = pattrn.pattraziza(x1)
        r2 = pattrn.pattraziza(x2)
        r3 = pattrn.pattraziza(x3)
        r4 = pattrn.pattraziza(x4)
        r6 = pattrn.pattraziza(x6)
        candidates = {'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4, 'r6': r6}
        r = max(candidates.values(), key=lambda c: len(c.tup))

    searchObj1 = re.search(r'CITY MARKET', x1)
    searchObj2 = re.search(r'CITY MARKET', x2)
    searchObj3 = re.search(r'CITY MARKET', x3)
    searchObj4 = re.search(r'CITY MARKET', x4)

    if searchObj1 or searchObj2 or searchObj3 or searchObj4:

        print('------------------------- CITY MARKET -----------------------')
        r1 = pattrn.pattrcitymarket(x1)
        r2 = pattrn.pattrcitymarket(x2)
        r3 = pattrn.pattrcitymarket(x3)
        r4 = pattrn.pattrcitymarket(x4)
        candidates = {'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4}
        r = max(candidates.values(), key=lambda c: len(c.tup))

    return r
