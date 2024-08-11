import pandas as pd
import streamlit as st

@st.cache_data
def ImportarDados():
    df = pd.read_parquet("base.parquet")
    df['Ano'] = df['Data'].dt.strftime('%Y')
    df['Tipo'] = df['Valor $'].apply(lambda x: 'R' if x > 0 else 'D')    
    return df

@st.cache_data
def DadosBalanço():
    df = pd.read_parquet(r'baseBalanco.parquet', engine='pyarrow')
    df['Ano'] = df['Data'].dt.strftime('%Y')
    if 'Valor $' not in df.columns:
        if 'Valor' in df.columns:
            df.rename(columns={'Valor': 'Valor $'}, inplace= True)
    # print(df)   
    return df


if __name__ == "__main__":
    ImportarDados()
    DadosBalanço()
