import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tenis = pd.read_csv('tennis.csv')
tenis

def GS_0_16():
    tenis1 = tenis[tenis.Round=='The Final']
    tenis2 = tenis1[tenis1.Series=='Grand Slam']
    return tenis2

GS_0_16()
GS_0_16().Winner.value_counts()

sns.countplot(y=GS_0_16().Winner)

data2 = GS_0_16().loc[17708:]  # Filtro por es fila porque es la fecha en la que empieza el primer torne de 2006
data2

data2.Winner.value_counts()

sns.countplot(y=data2.Winner)

def Roger_gs_weak_era():   
    data3 = GS_0_16().loc[:17707] # Realizo esta función para saber cuantos Grand Slams ganó Federer antes de que sus rivales verdaderos comenzaran en el circuito ATP
    return data3.Winner.value_counts()

Roger_gs_weak_era() 

def wins_Rafa():
    tenis1 = tenis[tenis.Winner=='Nadal R.']
    tenis2 = tenis1[tenis1.Loser=='Federer R.']
    return tenis2.Winner.value_counts()

wins_Rafa()

def wins_Roger():
    tenis1 = tenis[tenis.Winner=='Federer R.']
    tenis2 = tenis1[tenis1.Loser=='Nadal R.']
    return tenis2.Winner.value_counts(
wins_Roger()

api_df = api_df.drop(['Unnamed: 0', 'race_ranking'], axis = 1)
api_df
çtop_count = api_df.country.value_counts()
top_count[:10].plot(kind='barh')