# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:42:35 2022

@author: jensr
"""

import pandas as pd
import matplotlib.pyplot as plt
from creds import api_key, notion_database_url
import notion_df
import seaborn as sns

plt.close('all')

sns.set_style('whitegrid')

df = notion_df.download(notion_database_url, api_key=api_key, resolve_relation_values=True)


new = df[~df['Time estimate'].isnull()  & ~df['Actual time spent'].isnull()]


sns.jointplot(data=new, x='Time estimate',y='Actual time spent')


df['Day'] = df['Date'].dt.date
new = df.groupby('Day').sum()
new['Quality'] = new['Reward'] - new['Effort']


fig, ax = plt.subplots(figsize=(15, 8))
sns.lineplot(data=new, x ='Day', y = 'Quality', markers = True)

df['Milestones'] = [','.join(map(str, l)) for l in df['Milestones']]
new2 = df.groupby('Milestones').sum()

fig1, ax = plt.subplots()
new2['Actual time spent'].hist()
