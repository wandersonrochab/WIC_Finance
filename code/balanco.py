import streamlit as st
import pandas as pd

from datetime import datetime
from streamlit_option_menu import option_menu

from code.dataset import DadosBalanço
from code.table import Tabela
from code.funct_aux import TransformarNumero

from code.funct_aux import FiltrarDados
from code.style import create_cards_in_columns

def BP(df, lts):        
    lst = {
            '1.1': ['Ativo','Ativo Circulante'],  # Ativo
            '1.2': ['Ativo','Ativo Não Circulante'],  # Ativo
            '2.1': ['Passivo','Passivo Circulante'],  # Passivo
            '2.2': ['Passivo','Passivo Não Circulante'],  # Passivo
            '3.1': ['Patrimônio Líquido', 'Patrimônio Líquido'],  # Patrimônio Líquido
            '4.1': ['Demonstração de Resultado', 'Receitas'],
            '5.1': ['Demonstração de Resultado', 'Custos'],
            '5.2': ['Demonstração de Resultado', 'Despesas'],
            '5.3': ['Demonstração de Resultado', 'Receitas e Despesas Financeiras'],
            '5.4': ['Demonstração de Resultado', 'Outras Receitas/Despesas Não Operacionais'],
        }
    def classificar(conta):
        prefixo = '.'.join(conta.split()[0].split('.')[:2])
        if prefixo in lst:
            return pd.Series(lst[prefixo])
        else:
            return pd.Series(['Outro', 'Outro'])
    
    df['Datatm'] = df[lts[2]].dt.strftime('%b-%Y')
    df[['NV1', 'NV2']] = df['Conta'].apply(classificar)
           
    df = pd.pivot_table(df, values= lts[1], 
                        index=[lts[3], lts[4], 'NV1', 'NV2'],
                        columns='Datatm',
                        aggfunc='sum').reset_index()

    # ordenado o df com as colunas por data
    df.drop(columns=['Empresa'], inplace= True)
    fixed_columns = ['Conta', 'NV1', 'NV2']
    date_columns = sorted([col for col in df.columns if col not in fixed_columns], key=lambda x: pd.to_datetime(x, format='%b-%Y'))
    df['Total'] = df[date_columns].sum(axis=1)
    total = ['Total']
    new_column_order = fixed_columns + date_columns
    listaFormatoValor = date_columns
    listaFormatoValor.append('Total')
    new_column_order.append('Total')
    # Reordenando o DataFrame
    df = df[new_column_order]

    return df, new_column_order, fixed_columns


def Balanço(anos, empresa, lts):
    corlogo = '#64c4ac'
    
    def Indices(df, colunaDi, colunaDe, pDivi, pDeno):
        divi = df.loc[df[colunaDi] == pDivi].iloc[:, 3:].sum()
        deno = df.loc[df[colunaDe] == pDeno].iloc[:, 3:].sum()
        resu = divi/deno
        return resu.iloc[-1]
    
    df = DadosBalanço()
    df = FiltrarDados(df = df, 
                      lts_anos= anos, 
                      lts_empresa=empresa, 
                      lts_geral=lts, 
                      agrupar_dados= 'Agrupar')
    
    df, clsValor, fixedColumns = BP(df,lts)
    
    reference_values = [1, 1, 0.5, 1]
    LC = Indices(df, 'NV2','NV2', 'Ativo Circulante','Passivo Circulante')
    LG = Indices(df, 'NV1','NV1', 'Ativo','Passivo')
    EN = Indices(df, 'NV1','NV1', 'Passivo','Patrimônio Líquido')
    IM = Indices(df, 'Conta','NV2', '1.1.1 Caixa e Equivalentes de Caixa','Passivo Circulante')
    cards = [
        ('Liquidez Corrente', f"{TransformarNumero(df = LC, valorUnitarioTipo = 'N', valorUnitario='N')}", corlogo, 'P'),
        ('Liquidez Geral', f"{TransformarNumero(df = LG, valorUnitarioTipo = 'N', valorUnitario='N')}", corlogo, 'P'),
        ('Liquidez Imediata', f"{TransformarNumero(df = IM, valorUnitarioTipo = 'N', valorUnitario='N')}", corlogo, 'P'),
        ('Endividamento', f"{TransformarNumero(df = EN, valorUnitarioTipo = 'N', valorUnitario='N')}", corlogo, 'N')
        ]
    
    create_cards_in_columns(cards, columns_per_row=4,  reference_values = reference_values)

    nT1, nT2 = st.columns((0.2,1))
    with nT2:
        st.title('_Balanço Patrimonial_')
    

    
    cT01, cT02 = st.columns((1,0.01))
    Tabela(coluna= cT01, 
           df = df,
           clsValor=clsValor,
           lts = lts,
           fixedColumns=fixedColumns)