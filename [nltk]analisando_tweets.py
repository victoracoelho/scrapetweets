import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from twitterscraper import query_tweets
from datetime import datetime
from nltk.corpus import stopwords
import string
import collections
import seaborn as sns


### DEFININDO OS PERÍODOS UTILIZADOS PARA OS TWEETS.... Data atual do sistema como fim do período e um dia atrás como início 
atual = datetime.now().date()
inicio = atual.replace(day=atual.day - 1)


### DEFININDO LIMITE DE TWEETS A SEREM OBSERVADOS, LÍNGUA DOS TWEETS E PALAVRAS CHAVE PARA MANIPULAÇÃO AO FINAL
limit = 1000
lang = 'portuguese'
twt = ['bolsonaro', 'jair', 'jairbolsonaro', '…', 'pra', 'presidente', 'q', 'vai', 'vc', 'ser', 
       'Presidente', 'ter', 'tá', 'pode', 'quer', 'la', 'pq', 'aqui', 'ainda', 'porque', 'aí', 
       'todos', 'cara', 'gente', 'pessoas', 'nada', 'tudo', 'todo', 'el', 'agora', 'ver', 'en', 
       'faz', 'falar', 'outro', 'un', 'fala', 'fazer', 'ficar', 'tempo', 'vcs', 'fazendo', 
       'dá', 'dia', 'pro', 'y']

### CAPTANDO OS TWEETS
tweets = query_tweets('bolsonaro', begindate=inicio, enddate=atual, limit=limit, lang=lang)

### TRANSFORMAÇÃO DO RETORNO DA QUERY EM DATAFRAME, E DOS TWEETS EM FORMA DE TEXTO PARA SÉRIE
df = pd.DataFrame(t.__dict__ for t in tweets)

data = pd.Series(df['text'])

### DESCREVENDO OS DADOS
data.describe()


### FUNÇÃO DE LIST COMPREHENSION PARA TRATAR A SÉRIE
def txt_process(txt):
    nopont = [char for char in txt if char not in string.punctuation]
    nopont = ''.join(nopont)
    sms = [word for word in nopont.split() if word.lower() not in twt]
    sms = [word for word in sms if word.lower() not in stopwords.words('portuguese')]
    return sms

teste = data.apply(txt_process)

### TRANSFORMAÇÃO DA SÉRIE EM LISTA, DEPOIS EM ARRAY
lista_teste = list(teste)

new_lista_teste = []
new_lista_teste = sum(lista_teste, new_lista_teste)
array_teste = np.array(new_lista_teste)

### APLICANDO O CONTADOR DE PALAVRAS MAIS DIGITADAS
counter = collections.Counter(array_teste)

print(counter.most_common(n=50))

lista_words = []
lista_num = []

for p, v in counter.most_common(n=50):
    lista_words.append(p)
    lista_num.append(v)

### PLOTANDO O GRÁFICO COM AS PALAVRAS MAIS DIGITADAS
sns.barplot(lista_words[:8], lista_num[:8]) #seaborn

plt.figure(figsize=(12,6))
plt.bar(lista_words[:15], lista_num[:15]) #matplotlib







    
    
