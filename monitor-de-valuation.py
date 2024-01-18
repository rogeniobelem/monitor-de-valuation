#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from sys import displayhook
# from tkinter.tix import DisplayStyle
import requests
import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

url = "https://statusinvest.com.br/category/advancedsearchresultexport?search=%7B%22Sector%22%3A%22%22%2C%22SubSector%22%3A%22%22%2C%22Segment%22%3A%22%22%2C%22my_range%22%3A%22-20%3B100%22%2C%22forecast%22%3A%7B%22upsideDownside%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22estimatesNumber%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22revisedUp%22%3Atrue%2C%22revisedDown%22%3Atrue%2C%22consensus%22%3A%5B%5D%7D%2C%22dy%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_L%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22peg_Ratio%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_VP%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_Ativo%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22margemBruta%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22margemEbit%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22margemLiquida%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_Ebit%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22eV_Ebit%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22dividaLiquidaEbit%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22dividaliquidaPatrimonioLiquido%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_SR%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_CapitalGiro%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_AtivoCirculante%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22roe%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22roic%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22roa%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22liquidezCorrente%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22pl_Ativo%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22passivo_Ativo%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22giroAtivos%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22receitas_Cagr5%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22lucros_Cagr5%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22liquidezMediaDiaria%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22vpa%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22lpa%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22valorMercado%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%7D&CategoryType=1"


def baixar_arquivo(url, local):
    """_summary_

    Args:
        url (_type_): _description_
        local (_type_): _description_
    """
    # Faz requisição ao servidor
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML,\
           like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    resposta = requests.get(url, headers=hdr, timeout=50)
    if resposta.status_code == requests.codes.OK:
        with open(local, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print(f"Donwload finalizado. Salvo em: {local}.")
    else:
        resposta.raise_for_status()


baixar_arquivo(url, 'si-acoes.csv')

dados = pd.read_csv("si-acoes.csv",
                    sep=';',
                    thousands='.',
                    decimal=',',
                    skipinitialspace=True)

dados.columns = ['Ticker', 'Preco', 'DY', 'P/L', 'P/VP', 'P/Ativos', 'Marg_bruta',
                 'Marg_EBIT', 'Marg_liq', 'P/EBIT', 'EV/EBIT',
                 'Div_liq/EBIT', 'Div_liq/Patrim', 'PSR', 'P/CAP. Giro',
                 'P.AtCirLiq.', 'LiqCorrente', 'ROE', 'ROA', 'ROIC',
                 'Patrim/Ativos', 'Passivos/Ativos', 'GiroAtivos',
                 'CAGR_Rec_5anos', 'CAGR_lucros_5anos', 'LiqMediaDia',
                 'VPA', 'LPA', 'PEG_Ratio', 'ValorMercado']

# Criação de novas colunas
DY = (dados['DY'] / 100).fillna(0)
dpa = dados['Preco'] * DY
dados['Risco'] = 0.0881
CAGR_lucros_5anos = dados['CAGR_lucros_5anos'].apply(
    lambda x: x/100 if x > 0 else 0)
d1 = dpa * (1 + CAGR_lucros_5anos)
Preco_gordon = d1/(dados['Risco'] - CAGR_lucros_5anos)
vpa = dados['VPA'].apply(lambda x: x if x > 0 else 0)
lpa = dados['LPA'].apply(lambda x: x if x > 0 else 0)
payout = (dpa / lpa).fillna(0)
roe = dados['ROE'] / 100
crescimento_esperado = ((1 - payout) * roe).replace(np.inf, 0)

# Média de Crescimento


def mc(x, y):
    if (x == 0):
        return y
    elif (y == 0):
        return x
    else:
        return (x + y) / 2


tabtemp = pd.DataFrame()

tabtemp['CL5'] = CAGR_lucros_5anos
tabtemp['CE'] = crescimento_esperado

tabtemp['Media_Crescimento'] = tabtemp.apply(
    lambda x: mc(x['CL5'], x['CE']), axis=1)

# Desconto de Bazin
dados['Desc_Bazin'] = (dpa / 0.06).fillna(0)

# Desconto de Graham
Graham = (22.5 * vpa * lpa) ** 0.5

dados['Desc_Graham'] = (Graham - dados['Preco']) / Graham

dados['Desc_Graham'] = dados['Desc_Graham'].replace(-np.inf, 0)

# Desconto de Gordon
Desc_gordon = (Preco_gordon - dados['Preco']) / Preco_gordon
dados['Desc_gordon'] = (Desc_gordon.replace(-np.inf, 0)).fillna(0)

# Importar classificação.csv
classificacao = pd.read_csv('csv-auxiliar/classificacao.csv')
classificacao.columns = ['Ticker', 'Nome', 'Setor', 'Subsetor', 'Segmento']

# Criação da tabela 'acao'
acao = pd.DataFrame()
acao['Ticker'] = dados['Ticker']
acao = pd.merge(acao, classificacao, how='left', on='Ticker')

acao['Desc_Bazin'] = dados['Desc_Bazin']
acao['Desc_Graham'] = dados['Desc_Graham']
acao['Desc_Gordon'] = dados['Desc_gordon']
acao['Indice_PEG'] = dados['PEG_Ratio']
acao['Preco'] = dados['Preco']
acao['DY'] = DY
acao['LPA'] = lpa
acao['VPA'] = vpa
acao['Risco'] = dados['Risco']
acao['Payout'] = payout
acao['ROE'] = roe
acao['CAGR_lucros_5anos'] = CAGR_lucros_5anos
acao['Cresc_esperado'] = crescimento_esperado
acao['Media_Crescimento'] = tabtemp['Media_Crescimento']

acao.to_csv("csv-auxiliar/acao.csv", index=False)

# Exibição na página
# Filtro de ações por setor, subsetor e segmento
setores = acao['Setor'].unique()
setor = st.sidebar.selectbox(
    'Setor', setores, index=None, placeholder='Selecione o setor...')

subsetores = acao['Subsetor'][acao['Setor'] == setor].unique()
subsetor = st.sidebar.selectbox(
    'Subsetor', subsetores, index=None, placeholder='Selecione o subsetor...')

segmentos = acao['Segmento'][acao['Subsetor'] == subsetor].unique()
segmento = st.sidebar.selectbox(
    'Segmento', segmentos, index=None, placeholder='Selecione o segmento...')

if setor is None:
    info_acao = acao
elif subsetor is None:
    info_acao = acao[acao['Setor'] == setor]
elif segmento is None:
    info_acao = acao[acao['Subsetor'] == subsetor]
else:
    info_acao = acao[acao['Segmento'] == segmento]

st.dataframe(info_acao)
