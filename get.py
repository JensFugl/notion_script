# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests, json
import pandas as pd

from config import databaseId, token

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
    df = pd.json_normalize(data['results'])
    #, record_path = ['properties', ['Task', ['title']] ]
    #print(res.text)
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

    return df  
 
df = readDatabase(databaseId, headers)

df = df.drop(columns = ['object', 'id', 'cover', 'icon',
       'archived', 'url', 'created_by.object', 'created_by.id',
       'last_edited_by.object', 'last_edited_by.id', 'parent.type',
       'parent.database_id', 'properties.Date Created.id',
       'properties.Date Created.type',
       'properties.Milestones.id', 'properties.Milestones.type',
       'properties.Milestones.relation', 'properties.Last edited (done).id',
       'properties.Last edited (done).type',
       'properties.Last edited (done).last_edited_time',
       'properties.Status.id', 'properties.Status.type',
       'properties.Status.select.id',
       'properties.Status.select.color', 'properties.Actual time spent.id',
       'properties.Actual time spent.type',
       'properties.Actual time spent.formula.type',
       'properties.Actual time spent.formula.number', 'properties.Tag.id',
       'properties.Tag.type', 'properties.Tag.multi_select',
       'properties.Date.id', 'properties.Date.type',
       'properties.Date.date.start', 'properties.Date.date.end',
       'properties.Date.date.time_zone', 'properties.Task.id',
       'properties.Task.type', 'properties.Task.title',
       'properties.Time estimate.id', 'properties.Time estimate.type',
       'properties.Time estimate.number', 'properties.Reward.id',
       'properties.Reward.type', 'properties.Reward.number',
       'properties.Effort.id', 'properties.Effort.type',
       'properties.Effort.number'])


'''
df = pd.json_normalize(data)

df2 = pd.json_normalize(data['results'][0]['properties'])
'''
