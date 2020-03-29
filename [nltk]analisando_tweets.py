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


atual = datetime.now().date()
inicio = atual.replace(day=atual.day - 1)


limit = 1000
lang = 'portuguese'

tweets = query_tweets('bolsonaro', begindate=inicio, enddate=atual, limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)

data = pd.DataFrame(df['text'])

phrases = list(df['text'])

data.describe()



def txt_process(txt):
    nopont = [char for char in txt if char not in string.punctuation]
    nopont = ''.join(nopont)
    sms = [word for word in nopont.split() if word.lower() not in stopwords.words('portuguese')]
    return sms

teste = data.apply(txt_process)


counter = collections.Counter(teste[0])

print(counter.most_common(n=50))

lista1 = list(counter.values())
lista2 = list(counter.keys())
lista3 = list(counter.most_common())



plt.figure(figsize=(12,6))
plt.bar(lista2[21:40], lista1[21:40])





### CÓDIGO EM ESTUDO...
'''proc = CountVectorizer(analyzer=txt_process).fit(data)
len(proc.vocabulary_)

proc_transform = proc.transform(data)
proc_transform.shape    

tfidf = TfidfTransformer()
tfidf = tfidf.fit(proc_transform)'''













    
    
