import pandas as pd

def Filter(df, col):
    return df[col].unique()

def TransformarNumero(df, coluna = None, tipoTransformado = None,
                      valorUnitario = None,
                      valorUnitarioTipo = None):
      
    if valorUnitario == None:
        if tipoTransformado == 'Valor':
            df = df.map('R$ {:,.0f}'.format)
    else:
        if valorUnitarioTipo == 'Valor':            
            df = f"R$ {df:,.0f}"
            df = df.replace(',',".")
        elif valorUnitarioTipo == "Percentual":
            df = f"{df:,.2f}%"
            df = df.replace(',',".")

    return df

def AgruparDados(df, ano, empresa, valor, tipo, tipoAgrupamento= None):    
    if tipoAgrupamento== None:
        df_tm = df.query(f"{'Ano'} in {ano} and {'Empresa'} in {empresa} and {'Tipo'} in {tipo}")    
        final = df_tm[valor].sum() 
    
    elif tipoAgrupamento == 'grupo':
        df_tm = df.query(f"{'Ano'} in {ano} and {'Empresa'} in {empresa} and {'Tipo'} in {tipo}")
        final = df_tm.groupby([
                        pd.Grouper(key='Data', freq='M', axis=0)
                        ]).sum(valor).reset_index()
    else:
        df_tmR = df.query(f"{'Ano'} in {ano} and {'Empresa'} in {empresa} and {'Tipo'} in {[tipo[0]]}")    
        finalR = df_tmR[valor].sum()

        df_tmD = df.query(f"{'Ano'} in {ano} and {'Empresa'} in {empresa} and {'Tipo'} in {tipo}")    
        finalD = df_tmD[valor].sum()

        final = finalD/finalR*100      
    
    return final