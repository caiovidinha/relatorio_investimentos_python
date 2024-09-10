import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk
import win32com.client as win32
from datetime import date

tickers = ["^BVSP","^GSPC","BRL=X"]
dados_mercado = yf.download(tickers, period="6mo")
dados_mercado = dados_mercado["Adj Close"]
dados_mercado = dados_mercado.dropna()
dados_mercado.columns = ["DOLAR", "IBOVESPA", "S&P500"]

plt.style.use("cyberpunk")

plt.plot(dados_mercado["DOLAR"])
plt.title("DOLAR")
plt.savefig("dolar.png")
plt.clf()

plt.plot(dados_mercado["IBOVESPA"])
plt.title("IBOVESPA")
plt.savefig("ibovespa.png")
plt.clf()

plt.plot(dados_mercado["S&P500"])
plt.title("S&P500")
plt.savefig("s&p500.png")
plt.clf()


retornos_diarios = dados_mercado.pct_change()
retorno_dolar = round(retornos_diarios["DOLAR"].iloc[-1] * 100,2)
retorno_ibovespa = round(retornos_diarios["IBOVESPA"].iloc[-1] * 100,2)
retorno_sp = round(retornos_diarios["S&P500"].iloc[-1] * 100,2)

retorno_dolar = str(retorno_dolar)+"%"
retorno_ibovespa = str(retorno_ibovespa)+"%"
retorno_sp = str(retorno_sp)+"%" 

""" Enviar e-mail """
outlook = win32.Dispatch("outlook.application")
email = outlook.CreateItem(0)

email.To = "caiomdavidinha@gmail.com"
email.Subject = f"Relatório de Mercado{date.today()}"
email.Body = f'''Prezado diretor, segue o relatório de mercado:
* O Ibovespa teve o retorno de {retorno_ibovespa}
* O Dólar teve o retorno de {retorno_dolar}
* O S&P500 teve o retorno de {retorno_sp}

Segue em anexo a performance dos ativos nos últimos 6 meses.

Att,
Melhor estagiário do mundo


'''

anexo_dolar = r"D:\Documentos\Projetos\relatorio_mercado\dolar.png"
anexo_ibovespa = r"D:\Documentos\Projetos\relatorio_mercado\ibovespa.png"
anexo_sp = r"D:\Documentos\Projetos\relatorio_mercado\s&p500.png"

email.Attachments.Add(anexo_ibovespa)
email.Attachments.Add(anexo_dolar)
email.Attachments.Add(anexo_sp)

email.Send()