import plotly.express as px
import plotly.graph_objects as go

def GraficoPanorama(coluna, df01, df02, df03, colunaData, colunaValor):
    
    fig = go.Figure()
    # primeiro grafico barras positivas
    fig.add_trace(go.Bar(x = df01[colunaData],
                         y = df01[colunaValor],
                         name= 'Receita',
                         marker_color = 'steelblue'))
    # segund grafico barras negativas
    fig.add_trace(go.Bar(x = df02[colunaData],
                         y = df02[colunaValor],
                         name= 'Despesas',
                         marker_color = 'firebrick'))
    fig.add_trace(go.Scatter(x = df03[colunaData],
                             y = df03[colunaValor],
                             name= 'Resultado',
                             marker_color = 'yellow'))
    
    # parametros gerais dos graficos
    fig.update_layout(barmode = 'overlay',
                      xaxis_tickangle = -45,
                      title = {'x':0.5,
                               'y':1,
                               'yanchor': 'top',
                               'xanchor': 'center'})

    fig.update_layout(xaxis = dict(tickmode = 'linear',
                                   dtick = 'M1'),
                                   title = {'text':'Panorama Geral: Receita, '+ 
                                            'Despesa e Resultado Operacional'})

    return coluna.plotly_chart(fig, use_container_width = True)