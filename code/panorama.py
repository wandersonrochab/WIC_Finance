import streamlit as st
import pandas as pd
# import numpy as np
# import openpyxl, os
#import plotly.express as px
#import plotly.graph_objects as go
from datetime import datetime
from streamlit_option_menu import option_menu
#from plotly.subplots import make_subplots

# from st_aggrid import AgGrid, GridOptionsBuilder
# from st_aggrid.shared import GridUpdateMode

from code.funct_aux import AgruparDados, TransformarNumero
from code.dataset import ImportarDados
from code.graphs import GraficoPanorama
# import funcoes

# @st.cache_data
# def ImportarDados():
#     df = pd.read_excel('base.xlsx')
#     df['Ano'] = df['Data'].dt.strftime('%Y')
#     df['Tipo'] = df['Valor $'].apply(lambda x: 'R' if x > 0 else 'D')
#     # print(df)

#     return df

def Panorama(anos, empresa, lts):
    col = st.columns(2)
    cards = st.columns(4)

    # receita_total = funcoes.AgruparDados(ImportarDados(), anos, empresa, ['R'])

    # saida_total = funcoes.AgruparDados(ImportarDados(), anos, empresa, ['D'])

    cards[0].metric(label = 'Receita Total',     
                    value = TransformarNumero(AgruparDados(ImportarDados(),
                                                                           anos, empresa, lts[1], ['R']), 
                                                      valorUnitarioTipo='Valor',
                                                        valorUnitario='valor'))
    cards[1].metric(label = 'Saídas Total',     
                    value = TransformarNumero(AgruparDados(ImportarDados(),
                                                            anos, empresa, lts[1], ['D']), 
                                                      valorUnitarioTipo='Valor',
                                                        valorUnitario='valor'))
    cards[2].metric(label = 'Sobra Total',     
                    value = TransformarNumero(AgruparDados(ImportarDados(),
                                                                           anos, 
                                                                           empresa, lts[1], ['D','R']), 
                                                      valorUnitarioTipo='Valor',
                                                        valorUnitario='valor'))
    cards[3].metric(label = '% da Sobra Total',     
                    value = TransformarNumero(AgruparDados(ImportarDados(),
                                                                           anos, 
                                                                           empresa, lts[1],['R','D'], 1), 
                                                      valorUnitarioTipo='Percentual',
                                                        valorUnitario='valor'))
    
    col01, col02 = st.columns((1,0.01))
    GraficoPanorama(col01, 
                            AgruparDados(ImportarDados(),anos, empresa,lts[1],['R'], 'grupo'),
                            AgruparDados(ImportarDados(),anos, empresa,lts[1], ['D'], 'grupo'),
                            AgruparDados(ImportarDados(),anos, empresa,lts[1], ['R','D'], 'grupo'),
                            'Data', 'Valor $')
    # col03, col04 = st.columns((1,0.01))


    # funcoes.GraficoVelocimetro(col03, saida_total,receita_total, 'Consumo de receitas pelas despesas')