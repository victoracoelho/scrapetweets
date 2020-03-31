import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from twitterscraper import query_tweets
from datetime import datetime
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import collections
from googletrans import Translator
import itertools


atual = datetime.now().date()
inicio = atual.replace(day=atual.day - 1)


limit = 1000
lang = 'portuguese'
twt = 'bolsonaro'

tweets = query_tweets('bolsonaro', begindate=inicio, enddate=atual, limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)

data = pd.Series(df['text'])

phrases = list(df['text'])

data.describe()

trans = Translator()

def txt_process(txt):
    nopont = [char for char in txt if char not in string.punctuation]
    nopont = ''.join(nopont)
    sms = [word for word in nopont.split() if word.lower() not in twt]
    sms = [word for word in sms if word.lower() not in stopwords.words('portuguese')]
    return sms

teste = data.apply(txt_process)

new_lista_teste = []
lista_teste = list(teste)

new_lista_teste = sum(lista_teste)
array_teste = np.array(new_lista_teste)


counter = collections.Counter(array_teste)

print(counter.most_common(n=50))

lista_words = []
lista_num = []

for p, v in counter.most_common(n=50):
    lista_words.append(p)
    lista_num.append(v)


plt.figure(figsize=(12,6))
plt.bar(lista_words[:15], lista_num[:15])







    
    
