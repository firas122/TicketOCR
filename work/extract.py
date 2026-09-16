import json
import os

import requests


def treat(path):
    url = "https://app.nanonets.com/api/v2/OCR/FullText"

    payload = {'urls': [path]}

    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload,
                                auth=requests.auth.HTTPBasicAuth(os.environ["NANONETS_API_KEY"], ''))
    return json.loads(response.text)["results"][0]["page_data"][0]["raw_text"]

