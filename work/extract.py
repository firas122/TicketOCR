import re

import requests
import json
def treat(path):
    T = []

    url = "https://app.nanonets.com/api/v2/OCR/FullText"

    payload = {'urls': [path]}

    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=requests.auth.HTTPBasicAuth('ysfRJ8nsLf3yN592IGbQldq5SUcfZ1wq', ''))
    # print(response.text)
    a = json.loads(response.text)["results"][0]["page_data"][0]["raw_text"]
    return a
    #print(a)
    search1 = re.findall(r'[a-zA-Z\s]+\s\d\s[xX]\s\d{3,6}', a)

    for i in search1:
        print(i, "*")
        T.append(i)
        a = a.replace(i, '')


    search2 = re.findall(r'[a-zA-Z%\d\s]+\s[xX]\s\d{3,6}', a)
    for j in search2:
        print(j, "**")
        T.append(j)

