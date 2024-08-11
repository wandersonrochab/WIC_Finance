import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import st_aggrid as st_ag

from datetime import datetime
from st_aggrid import JsCode
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
from st_aggrid.shared import GridUpdateMode


def Tabela(coluna, df, clsValor = None, lts = None, fixedColumns = None):
    # def mes_para_data(mes):
    #     return datetime.strptime(mes, '%b-%Y')
    
    formatoValor = st_ag.JsCode("""
        function(params){
            return (params.value == null) ? params.value: params.value.toLocaleString('pt-BR',{'style': 'currency', 'currency':'BRL'});
        }
    """)
    
    formato_percent = st_ag.JsCode("""
        function(params){
            return (params.value == null) ? params.value: params.value.toLocaleString('pt-BR',{'style': 'percent','minimumFractionDigits':2});
        }
    """)

    # fixed_columns = ['Nivel1', 'Nível2','Nome do fornecedor/cliente']
    # date_columns = sorted([col for col in df.columns if col not in fixed_columns], key=lambda x: pd.to_datetime(x, format='%b-%Y'))

    # df['Total'] = df[date_columns].sum(axis = 1)
    # # Combinando as colunas
    # total = ['Total']
    # new_column_order = fixed_columns + date_columns
    # listaFormatoValor = date_columns
    # listaFormatoValor.append('Total')
    # new_column_order.append('Total')
    # # Reordenando o DataFrame
    # df = df[new_column_order]

    numeroLinhas = df[lts[4]].unique()
    
    options = GridOptionsBuilder.from_dataframe(df,
                                                enableRowGroup=True,
                                                enableValue=True,
                                                enablePivot=True
                                                )

    options.configure_side_bar()
    
    if clsValor == None:
        pass
    else:
        for col in clsValor:
            options.configure_column(col, aggFunc='sum',  valueFormatter = formatoValor, columnGroupShow='open')
    
    # if ListaFormatoPercet == None:
    #     pass
    # else:
    #     for col in ListaFormatoPercet:
    #         options.configure_column(col, aggFunc='sum',  valueFormatter = formato_percent, columnGroupShow='open')

    options.configure_selection("single")
    if fixedColumns == None:
        pass
    else:
        if len(fixedColumns) ==1:
            print(1)
        if len(fixedColumns) ==2:
            print(2)
        if len(fixedColumns) ==3:
            options.configure_column(fixedColumns[1], rowGroup=True, hide=True, rowGroupIndex=0, pinned = 'left')
            options.configure_column(fixedColumns[2], rowGroup=True, hide=True, rowGroupIndex=1, pinned = 'left')
            options.configure_column(fixedColumns[0], rowGroup=True, hide=True, rowGroupIndex=2,pinned = 'left')

    # corlogo = '#64c4ac'
    # listaFormatacaoAdicional = [
    #     ('Nivel1', '1.000 Receita Prestação de Serviços', corlogo),
    #     ('Nivel1', '3.000 Resultado Após a Folha', corlogo),
    #     ('Nivel1', '4.000 Resultado Operacional', corlogo),
    #     ('Nivel1', '5.000 Resultado após Investimentos', corlogo),
    #     ('Nivel1', '6.000 Resultado após Financeiro', corlogo),
    #     ('Nivel1', '7.000 Resultado Não Operacional', corlogo),
    #     ('Nivel1', '8.000 Resultado após Empréstimos', corlogo),
        
    # ]
    # try:        
    #     jscode = gerar_jscode_formatacao_linha(listaFormatacaoAdicional)
    #     options.configure_grid_options(getRowStyle=jscode)
    # except:
    #     pass
    
    options.configure_grid_options(suppressAggFuncInHeader = True,
                                   groupDefaultExpanded=True)  

    # options.configure_grid_options(onFirstDataRendered=JsCode("""
    #     function(params) {
    #         params.api.sizeColumnsToFit();
    #     };
    #     """))
    options.configure_grid_options(domLayout='autoHeight')

    gb = options.build()
    # # fixar a coluna agrupado - Estilo congelar paineis excel
    gb['autoGroupColumnDef'] = {'headerName': 'Grupos',
                                'cellRendererParams': {'suppressCount': True},
                                'field': 'Grupo',
                                'pinned': 'left'}
 
    selection= AgGrid(df,
                    enable_enterprise_modules=True,
                    gridOptions = gb, #options.build(), 
                    height=(50+30*len(numeroLinhas)),                                       
                    update_mode=GridUpdateMode.MODEL_CHANGED, 
                    # fit_columns_on_grid_load=True, # ajustar a coluna
                    columns_auto_size_mode=True,
                    allow_unsafe_jscode=True)
    return coluna.selection




