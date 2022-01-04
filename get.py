# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests, json
import pandas as pd

from cred import databaseId, token

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    print(res.text)

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
        
    return data   
 
data = readDatabase(databaseId, headers)

df = pd.json_normalize(data['results'])

df2 = pd.json_normalize(df['properties.Name.title'])
