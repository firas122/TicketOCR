
import re

import datetime
class tickt:
    def __init__(self, name, total, rest, tup):
        self.name = name
        self.total = total
        self.rest = rest
        self.tup = tup
        #self.datim = datim



def pattrIdeal(x):

    prod = []
    for line in x.splitlines():
        searchObj = re.match(r'\d[a-zA-Z\d{2,4}ÉÈÊ\W\sÀÁÂÄOEÚÙ-]*\d[,.]+\d{3}\s\d[,.]+\d{3}', line)
        if searchObj:
            prod.append(line)
        else:
            if re.search(r'TOTAL', line):
                print('********************************')
                print('************* total ************* ')
                total = re.findall("\d+[,\.]\d+", line)
                print(total)
                print('********************************\n\n ')
            if re.search(r'RENDU', line):
                print('*************  rest  ************* ')
                rest = re.findall("\d+[,\.]\d+", line)
                print(rest)
                print('********************************\n\n ')

            if re.search(r'[0-9][0-9]:[0-9][0-9]', line):
                x = re.search(r'[0-9][0-9]:[0-9][0-9]', line)
                print('*************  time ************* ')
                print(x.group())
                print('********************************\n\n ')
            if re.search(r'([0-9][0-9]/[0-9][0-9]/[0-9][0-9])', line):
                x = re.search(r'(\d+/\d+/\d+)', line)
                print('*************  date ************* ')
                print(x.group())
                print('********************************\n\n ')
    print('*********** products ******************')
    print(prod)
    tup = []
    for i in range(len(prod)):
        name = re.search(r'\d+(.*?)\d[,\.]\d{3}', prod[i])
        if name:
            print('product name : ', name[1])
            s = re.split(r'\s', prod[i])
            print('Quantity : ', s[0])
            q = int(s[0])
            print('unit price : ', s[len(s)-2])
            upri = s[len(s)-2]
            upri = float(upri.replace(',', '.'))
            print(upri)
            tup.append((name[1], q, upri))
            print('********************************\n\n ')
    p = tickt('Ideal', total, rest, tup)
    print('\n\n**************tsssssst****************** ')
    print('name of store :', p.name, '\ntotal : ', p.total, '\nrsst : ', p.rest, '\nprods : ', p.tup)
    return p



def pattrMonoprix(x):
    prod = []
    print('*********** products ******************')
    for line in x.splitlines():
        searchObj = re.match(r'[a-zA-Z\d{2,4}ÉÈÊ\W\sÀÁÂÄOEÚÙ]*\d{1,2}[\sxXÀÁÂ\W]*[\d{3,4}\W]*', line)
        if searchObj:
            if re.match(r'TOT', line):
                print('********************************\n\n\n ')
                print('****************total ************* ')
                print(line)
                total = re.findall("\d{4}", line)
                print('********************************\n\n\n ')

            if re.match(r'Rendu', line):
                print('*********  rest  ****************** ')
                print(line)
                print('********************************\n\n\n ')

            if re.search(r'[0-9][0-9]:[0-9][0-9]:[0-9][0-9]', line):
                x = re.search(r'[0-9][0-9]:[0-9][0-9]:[0-9][0-9]', line)
                print('*********  time ****************** ')
                print(x.group())
                print('********************************\n\n\n ')
            if re.search(r'([0-9][0-9]/[0-9][0-9]/[0-9][0-9])', line):
                x = re.search(r'(\d+/\d+/\d+)', line)
                print('*********  date ****************** ')
                print(x.group())
                print('********************************\n\n\n ')
            else:
                prod.append(line)
                print(line)
    tup = []
    for i in range(len(prod)):
        name = re.search(r'[A-Za-z0-9\s\.]*\d\s+[xX]+', prod[i])
        if name:
            print('********************************\n ')
            s = re.split(r'\d+\s[xX]*\s', prod[i])
            print('product name : ', s[0])
            s = re.split(r'\s', prod[i])
            print('Quantity : ', s[len(s)-3])
            q = s[len(s)-3]
            print('unit price : ', s[len(s) - 1])
            upri = s[len(s) - 1]
            upri = float(upri.replace(',', '.'))
            print(upri)
            tup.append((name[0], q, upri))
            print('********************************\n\n ')

    p = tickt('Monoprix', total, 0, tup)
    print('\n\n**************tsssssst****************** ')
    #print('name of store :', p.name, '\ntotal : ', p.total, '\nrest : ', p.rest, '\nprods : ', p.tup)
    return p
