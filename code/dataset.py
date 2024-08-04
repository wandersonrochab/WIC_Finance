import pandas as pd
import streamlit as st

@st.cache_data
def ImportarDados():
    # df = pd.read_excel('base.xlsx')
    df = pd.read_parquet("base.parquet", engine='pyarrow')
    df['Ano'] = df['Data'].dt.strftime('%Y')
    df['Tipo'] = df['Valor $'].apply(lambda x: 'R' if x > 0 else 'D')    
    return df

if __name__ == "__main__":
    ImportarDados()