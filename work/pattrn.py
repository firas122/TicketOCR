import json
import re
from json import JSONEncoder
class prodline:
    def __init__(self, pname, pquantity, pupri, ptotal):
        self.pname = pname
        self.pquantity = pquantity
        self.pupri = pupri
        self.ptotal = ptotal

class prodlineEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class tickt:
    def __init__(self, name, total, tup, date, time, marketid):
        self.name = name
        self.total = total
        self.tup = tup
        self.date = date
        self.time = time
        self.marketid = marketid

    def __hash__(self):
        # print('The hash is:')
        return hash((self.name, self.total, str(self.tup), self.date, self.total))

def pattrIdeal(x):
    prod = []
    for line in x.splitlines():
        searchObj = re.match(r'\d[a-zA-Z\d{2,4}ÉÈÊ\W\sÀÁÂÄOEÚÙ-]*\d[,.]+\d{3}\s\d[,.]+\d{3}', line)
        if searchObj:
            prod.append(line)
        else:
            if re.search(r'TOTAL', line):
                # print('********************************')
                # print('************* total ************* ')
                total = re.findall("\d+[,\.]\d+", line)
                #print(total)
                # print('********************************\n\n ')

            if re.search(r'[0-9][0-9]:[0-9][0-9]', line):
                x = re.search(r'[0-9][0-9]:[0-9][0-9]', line)
                # print('*************  time ************* ')
                tim = x.group()
                # print(x.group())
                # print('********************************\n\n ')
            if re.search(r'([0-9][0-9]/[0-9][0-9]/[0-9][0-9])', line):
                x = re.search(r'(\d+/\d+/\d+)', line)
                # print('*************  date ************* ')
                # print(x.group())
                d = x.group()
                # print('********************************\n\n ')
    # print('*********** products ****************')
    # print(prod)
    tup = []
    for i in range(len(prod)):
        name = re.search(r'\d+(.*?)\d[,\.]\d{3}', prod[i])
        if name:
            # print('product name : ', name[1])
            s = re.split(r'\s', prod[i])
            # print('Quantity : ', s[0])
            try:
                q = int(s[0])
            except:
                q = s[0]

            # print('unit price : ', s[len(s)-2])
            upri = s[len(s)-2]
            try:
                upri = float(upri)
            except:
                upri = upri
            upri = float(upri.replace(',', '.'))
            # print(upri)
            tup.append([['name:', name[1]], ['quantity', s[0]], ['unit price', upri], ['total price', q*upri]])
            # print('********************************\n\n ')
    p = tickt('Ideal', 0, tup, d+' '+tim, 0)
    # print('\n\n**************tsssssst****************** ')
    # print('name of store :', p.name, '\ntotal : ', p.total, '\nprods : ', p.tup, '\ndatim: ', p.datim)
    return p

def pattrMonoprix(x):
    prod = []
    total = 0
    d = tim = ''

    # print('*********** products ******************')
    for line in x.splitlines():
        searchObj = re.match(r'[a-zA-Z\d{2,4}ÉÈÊ\W\sÀÁÂÄOEÚÙ]+\d{1,2}\s*[xX%\W]+[\d{3,6}]+', line)
        if searchObj:

            if re.search(r'[0-9][0-9]:[0-9][0-9]', line):
                x = re.search(r'[0-9][0-9]:[0-9][0-9]', line)
                print('*********  time ****************** ')
                print(x.group())
                if x.group():
                    tim = x.group()
                else:
                    break
                # print('********************************\n\n\n ')
            if re.search(r'([0-9][0-9]/[0-9][0-9]/[0-9][0-9])', line):
                x = re.search(r'(\d+/\d+/\d+)', line)
                print('*********  date ****************** ')
                print(x.group())
                if x.group():
                    d = x.group()
                else:
                    break
                # print('********************************\n\n\n ')
            else:
                prod.append(line)
                print(line)
    tup = []
    for i in range(len(prod)):
        name = re.search(r'[A-Za-z0-9\s\.]+\d+\s*[xX%]+', prod[i])
        if name:
            print('********************************\n ')
            s = re.split(r'\d+\s*[xX%\W]+', prod[i])
            print(s)
            print('product name : ', s[0])
            name = s[0]
            print('unit price : ', s[len(s) - 1])
            try:
                upri = float(s[len(s) - 1])
            except:
                upri = s[len(s) - 1]
            s = re.split(r'\s*[xX%\W]+\s\d{3,6}', prod[i])
            s = re.split(r'\s', s[0])
            print('Quantity : ', s[len(s) - 1])

            try:
                q = int(s[len(s) - 1])
            except:
                q = s[len(s) - 1]



            try:
                totalp = q * upri
            except:
                totalp = 0

            try:
                total = total + totalp
            except:
                totalp = total + 0

            l = prodline(name, q, upri, totalp)
            prodlineJSONData = json.dumps(l, indent=4, cls=prodlineEncoder)
            l = json.loads(prodlineJSONData)
            tup.append(l)

    p = tickt('Monoprix', total, tup, d, tim, 1)
    # print('\n\n**************tsssssst****************** ')
    # print('name of store :', p.name, '\ntotal : ', p.total, '\nprods : ', p.tup, '\ndate : ', p.date, '\ntime : ', p.time)
    return p

def pattrcarrf(x):
    prod = []
    totalp = 0
    total = 0
    d = tim = ''
    print('*********** products ******************')
    l = x.splitlines()
    print(l[0])
    n = len(l)
    for i in range(0, n-1):

        searchObj1 = re.match(r'[a-zA-Z\d\s\W_-]*[,.\s]+\d{4}\W*', l[i])
        searchObj2 = re.search(r'\d{13}', l[i+1])
        if searchObj1 and searchObj2:

            if re.search(r'[0-9][0-9]:[0-9][0-9]', l[i]):
                x = re.search(r'[0-9][0-9]:[0-9][0-9]', l[i])
                print('*********  time ****************** ')
                if x.group():
                    tim = x.group()
                else:
                    break
            if re.search(r'([0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9])', l[i]):
                x = re.search(r'(\d+/\d+)', l[i])
                print('*************  date ****************** ')
                print(x.group())
                if x.group():
                    d = x.group()
                else:
                    break
            else:
                prod.append(l[i])
                print(l[i])
    tup = []
    for i in range(len(prod)):
        name = re.search(r'[a-zA-Z\d\s\W_-]*[,.\s]+\d{4}\W*', prod[i])
        if name:
            print('********************************\n ')
            s = re.split(r'\d{1,2}[,.]', prod[i])
            print('product name : ', s[0])
            n = s[0]
            s = re.split(r'\s', prod[i])

            try:
                q = int(s[0])
            except:
                q = s[0]
            print('Quantity : ', q)
            try:
                upri = float(s[len(s) - 1])
            except:
                upri = s[len(s) - 1]
            print('unit price : ', upri)

            try:
                totalp = totalp + q*upri

            except:

                totalp = totalp + 0

            total = total + totalp
            l = prodline(n, q, upri, totalp)
            prodlineJSONData = json.dumps(l, indent=4, cls=prodlineEncoder)
            l = json.loads(prodlineJSONData)
            tup.append(l)
            print('********************************\n\n ')
    p = tickt('CARREFOUR', total, tup, d, tim, 2)
    print('\n\n**************tsssssst****************** ')
    print('name of store :', p.name, '\ntotal : ', p.total, '\nprods : ', p.tup, '\ndatetime : ', p.date, p.time)
    return p

def pattraziza(x):
    prod = []
    tup = []
    total = k = 0
    d = tim = ''
    print('*********** products ******************')
    for line in x.splitlines():
        searchObj1 = re.match(r'[a-zA-Z\d{2,4}ÉÈÊ\W\sÀÁÂÄOEÚÙ]*[=]\s\W*\d{1,3}[.]\d{3}', line)
        searchObj2 = re.match(r'[a-zA-Z\d{2,4}ÉÈÊ\W\sÀÁÂÄOEÚÙ]*\d{1,3}[xX]\s\d{1,3}[.,]\d{3}\s[=]\s\d{1,3}[.]\d{3}', line)

        if searchObj2:
            if re.search(r'RENDU', line):
                print('*********  rest  ****************** ')
                print(line)
                rst = re.findall("\d{2,4}", line)
                rst = re.findall("\d{1,3}[.,\W]*\d{3}", line)
                print('********************************\n\n\n ')
            if re.search(r'[0-9][0-9]:[0-9][0-9]', line):
                x = re.search(r'[0-9][0-9]:[0-9][0-9]', line)
                print('*********  time ****************** ')
                if x.group():
                    tim = x.group()
                    print(tim)

            if re.search(r'(\d{1,2}/\d{1,2}/\d{4})', line):
                x = re.search(r'(\d+/\d+/\d+)', line)
                print('*********  date *********** ')
                if x.group():
                    d = x.group()
                    print(d)

            else:
                prod.append(line)

            for i in range(k, len(prod)):
                name = re.search(r'[a-zA-Z\d{2,3}ÉÈÊ\sÀÁÂÄOEÚÙ]*\d{1,3}[xX]\s\d{1,3}[.,]\d{3}', prod[i])
                if name:
                    print('********************************\n ')
                    s = re.split(r'\d+[xX]', prod[i])
                    print('product name2 : ', s[0])
                    n = s[0]
                    s = re.split(r'=', s[1])
                    print('unit price : ', s[0])
                    try:
                        upri = float(s[0].replace(',', '.'))
                    except:
                        upri = s[0].replace(',', '.')

                    s = re.search(r'\d+[xX]', prod[i])
                    s = re.split(r'[xX]', s.group())
                    print('quantity : ', s[0])
                    try:
                        q = int(s[0])
                    except:
                        q = s[0]
                    try:
                        totalp = upri*q
                    except:
                        totalp = 0
                    try:
                        total = total + totalp
                    except:
                        total = total + 0
                    l = prodline(n, q, upri, totalp)
                    prodlineJSONData = json.dumps(l, indent=4, cls=prodlineEncoder)
                    l = json.loads(prodlineJSONData)
                    tup.append(l)
            k = k + 1



        else:
            if searchObj1:
                if re.search(r'RENDU', line):
                    print('*********  rest  ****************** ')
                    print(line)
                    rst = re.findall("\d{1,3}[.,\W]*\d{3}", line)
                if re.search(r'[0-9][0-9]:[0-9][0-9]', line):
                    x = re.search(r'[0-9][0-9]:[0-9][0-9]', line)
                    print('*********  time ****************** ')
                    if x.group():
                        tim = x.group()
                        print(tim)

                if re.search(r'\d{1,2}/\d{1,2}/\d{4}', line):
                    x = re.search(r'\d+/\d+/\d+', line)
                    print('*********  date ****************** ')
                    if x.group():
                        d = x.group()
                        print(d)

                else:
                    prod.append(line)


                for i in range(k, len(prod)):
                    name = re.search(r'[a-zA-Z\d{2,3}ÉÈÊ\sÀÁÂÄOEÚÙ]*[=]\s\W*\d{1,3}[.]\d{3}', prod[i])
                    if name:
                        print('********************************\n ')
                        s = re.split(r'=', prod[i])
                        print('product name1 : ', s[0])
                        n = s[0]
                        print('unit price : ', s[1])
                        try:
                            upri = float(s[1].replace(',', '.'))
                        except:
                            upri = s[1].replace(',', '.')
                        print('quantity : ', 1)
                        total = float(total + upri)
                        l = prodline(n, 1, upri, upri)
                        prodlineJSONData = json.dumps(l, indent=4, cls=prodlineEncoder)
                        print(prodlineJSONData)
                        l = json.loads(prodlineJSONData)
                        tup.append(l)

                k = k + 1


    p = tickt('Aziza', total, tup, d, tim, 3)

    return p

def pattrcitymarket(x):
    prod = []
    total = 0
    d = tim = ''
    print('*********** products ******************')
    for line in x.splitlines():
        searchObj = re.match(r'\d{1,3}\s[a-zA-Z\d{2,4}ÉÈÊ\W\sÀÁÂÄOEÚÙ]*\d{1,3}[.,\W]*\d{3}', line)
        if searchObj:
            if re.search(r'RENDU', line):
                # print('*********  rest  ****************** ')
                # print(line)
                rst = re.findall("\d{2,4}", line)
                rst = re.findall("\d{1,3}[.,\W]*\d{3}", line)

            if re.search(r'[0-9][0-9]:[0-9][0-9]', line):
                x = re.search(r'[0-9][0-9]:[0-9][0-9]', line)
                print('*********  time ****************** ')
                if x.group():
                    tim = x.group()

                print('********************************\n\n\n ')
            if re.search(r'[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]', line):
                x = re.search(r'[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]', line)
                print('*********  date ****************** ')
                if x.group():
                    d = x.group()

                print(x.group())
            else:
                prod.append(line)
                # print(line)
    tup = []
    for i in range(len(prod)):
        name = re.search(r'\d{1,3}\s[a-zA -Z\d{2,4}ÉÈÊ\W\sÀÁÂÄOEÚÙ]*\d{1,3}[.,\W]*\d{3}', prod[i])
        if name:

            s = re.split(r'\s', name[0], 1)
            print('Quantity : ', s[0])
            try:
                q = int(s[0])
            except:
                q = s[0]
            s = re.split(r'\d{1,3}[.,\W]*\d{3}', s[1], 1)
            print('name : ', s[len(s) - 2])
            name = s[len(s) - 2]
            print('unit price : ', s[len(s) - 1])
            try:
                upri = float(s[len(s) - 1].replace(',', '.'))
            except:
                upri = s[len(s) - 1].replace(',', '.')

            try:
                totalp = upri * q
            except:
                totalp = 0

            try:
                total = float(q*upri + total)
            except:
                total = float(total + 0)

            l = prodline(name, q, upri, totalp)
            prodlineJSONData = json.dumps(l, indent=4, cls=prodlineEncoder)
            l = json.loads(prodlineJSONData)
            tup.append(l)

    p = tickt('City Market', total, tup, d, tim, 4)
    print('\n\n**************tsssssst****************** ')
    print('name of store : ', p.name, '\ntotal : ', p.total, '\nprods : ', p.tup, '\ndate : ', p.date, p.time)
    return p