from datetime import datetime, date
from matplotlib import pyplot as plt
import numpy as np
from bcb import sgs

# capital = float(input("Digite o capital investido: "))
# freq = input("Digite a frequência do período (Y, M, D): ").upper()
# inicio = input("Digite a data inicial (Pós 1995/01/01)[YYYY/MM/DD]: ")
# fim = input("Digite a data [YYYY/MM/DD]: ")

capital = 1000.00
freq = "M"
inicio = "1996/01/02"
fim = "2024/01/01"

data_inicial = datetime.strptime(inicio, "%Y/%m/%d")
data_final = datetime.strptime(fim, "%Y/%m/%d")

taxa_selic = sgs.get({"selic": 11}, start=data_inicial, end=data_final)
taxa_selic = taxa_selic/100

capital_acumulado = capital * (1+taxa_selic["selic"]).cumprod() - 1

capital_com_frequencia = capital_acumulado.resample(freq).last()