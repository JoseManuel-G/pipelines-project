import pandas as pd
def GS_0_16():
    tenis1 = tenis[tenis.Round=='The Final']
    tenis2 = tenis1[tenis1.Series=='Grand Slam']
    return tenis2
def Roger_gs_weak_era():   
    data3 = GS_0_16().loc[:17707] # Realizo esta función para saber cuantos Grand Slams ganó Federer antes de que sus rivales verdaderos comenzaran en el circuito ATP
    return data3.Winner.value_counts()
def wins_Rafa():
    tenis1 = tenis[tenis.Winner=='Nadal R.']
    tenis2 = tenis1[tenis1.Loser=='Federer R.']
    return tenis2.Winner.value_counts()
def wins_Roger():
    tenis1 = tenis[tenis.Winner=='Federer R.']
    tenis2 = tenis1[tenis1.Loser=='Nadal R.']
    return tenis2.Winner.value_counts()