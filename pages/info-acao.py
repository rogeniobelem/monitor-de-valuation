# import requests
import pandas as pd
import streamlit as st
# import numpy as np

st.set_page_config(layout="wide")

acao = pd.read_csv('csv-auxiliar/acao.csv')

papeis = acao['Ticker'].unique()
papel = st.sidebar.selectbox("Papel", papeis)

info_papel = acao[acao['Ticker'] == papel]

st.write(info_papel)

papel_ticker = info_papel['Ticker'].iloc[0]
papel_nome = info_papel['Nome'].iloc[0]
papel_setor = info_papel['Setor'].iloc[0]
papel_subsetor = info_papel['Subsetor'].iloc[0]
papel_segmento = info_papel['Segmento'].iloc[0]

st.title(f"{papel_ticker} - {papel_nome}")
col1,col2,col3 = st.columns(3)
col1.metric('Setor', papel_setor)
col2.metric('Subsetor', papel_subsetor)
col3.metric('Segmento', papel_segmento)
