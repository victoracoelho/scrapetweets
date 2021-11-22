# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 20:30:28 2021

@author: vitin
"""

import pandas as pd
import numpy as np
import string
import collections
import nltk
from nltk.corpus import stopwords

df = pd.read_excel("cardano_twt.xlsx")

content = df['content']

'''twt = ['crypto', 'Crypto', 'time', 'last', 'unvaccinatedlivesmatter', 'buy', 'like', 
       'purchase', 'bought', 'target', 'sell', 'profit', 'less', 'reduce', 'impact', 'volatility', 
       'oversall', 'CLICK', 'track', 'movements', 'cryptocurrency', 'project', 
       'get', 'one', 'amp', 'good', 'see', 'CryptoBroski1', 'great', 'de', 'news', 
       'Done', 'new', 'would', 'day', 'people', 'ShillRonin', 'know', 'us', 'got', 
       'money', 'dont', 'price', 'think', 'trading', 'imayonaisee']'''

twt = stopwords.words('english')

def txt_process(txt):
    nopont = [char for char in txt if char not in string.punctuation]
    nopont = ''.join(nopont)
    sms = [word for word in nopont.split() if word.lower() not in twt]
    sms = [word for word in sms if word.lower() not in stopwords.words('english')]
    return sms

data = content.apply(txt_process)

lista = list(data)

new_lista = []
new_lista = sum(lista, new_lista)
array_teste = np.array(new_lista)

array_teste = np.array(new_lista)

counter = collections.Counter(array_teste)

print(counter.most_common(n=50))