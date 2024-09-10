from datetime import datetime, date
from matplotlib import pyplot as plt
import numpy as np
from bcb import sgs

data_inicial = date(2000,1,1)
data_final = date(2022,3,31)

taxa_selic = sgs.get({"selic": 11}, start=data_inicial, end=data_final)
taxa_selic = taxa_selic/100

janelas_500_dias = ((1 + taxa_selic).rolling(window=500).apply(np.prod) - 1)
janelas_500_dias = janelas_500_dias.reset_index()
janelas_500_dias["data_inicial"] = janelas_500_dias["Date"].shift(500)
janelas_500_dias = janelas_500_dias.dropna()
janelas_500_dias.columns = ["data_final","retorno_selic_500d","data_inicial"]

maior_retorno = janelas_500_dias["retorno_selic_500d"].max()

gabarito = janelas_500_dias[janelas_500_dias["retorno_selic_500d"] == maior_retorno]
print(gabarito)

