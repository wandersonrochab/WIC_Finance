import streamlit as st
from streamlit_option_menu import option_menu  # modulo precisa ser importado a parte
from PIL import Image
import pandas as pd
import os

# importar os arquivos das paginas individuais
# import panorama
# import receitas
# import despesas
# import dre
# import dfc
# import orcamento
# import pessoas
# import funcoes


@st.cache_data
def ImportarDados():
    df = pd.read_excel('base.xlsx')
    df['Ano'] = df['Data'].dt.strftime('%Y')
    df['Tipo'] = df['Valor $'].apply(lambda x: 'R' if x > 0 else 'D')
    # print(df)

    return df

class Apresentacao():
    def __init__(self) -> None:
        self.logo = Image.open('Imagens/LogoW.png') # importar a logo da consultoria

    def Modelo(self):
        st.set_page_config(layout = 'wide')
        with st.sidebar:
            st.sidebar.image(self.logo, use_column_width = True)
            choose = option_menu('MENU',
                         ['Lembretes', 'Panorama', 'Receitas', 'Despesas', 
                          'DRE', "DFC", 'Orçamento', 'Pessoal'],
                         icons = ['bookmark-check', 'cash','coin', 'wallet2', #https://icons.getbootstrap.com/?q=person
                                          'cash','cash', 'eye','person'],
                        menu_icon = 'list', 
                        default_index = 0,
                        styles ={"container": {"padding": "5!important", 
                                                        "background-color": "rgba(3,29,68,1"},
                                        "icon": {"color": "non photo blue", "font-size": "20px"},
                                        "nav-link": {"font-size": "18px", "text-align": "left",
                                                     "margin":"0px", 
                                                     "--hover-color": "#427aa1"},
                                        "nav-link-selected": {"background-color": "#031d44"}}
                        )
        # with open('style.css') as f: # retirar os rodape da apresentacao
        #     st.markdown(f'<style>{f.read()}</style>',
        #                  unsafe_allow_html = True)
        n_empresas = os.listdir('Imagens/empresas')
        c = st.columns(len(n_empresas))
        with c[0]:
            st.image(os.path.join('Imagens/empresas', n_empresas[0]), width=250)
        with c[1]:
            st.image(os.path.join('Imagens/empresas', n_empresas[1]), width=250)
        with c[2]:
            st.image(os.path.join('Imagens/empresas', n_empresas[2]), width=250)
        with c[3]:
            st.image(os.path.join('Imagens/empresas', n_empresas[3]), width=250)
        with c[4]:
            st.image(os.path.join('Imagens/empresas', n_empresas[4]), width=250)
        

        # def Selecao():
        #     col = st.columns(2)
        #     with col[0]:
        #         anos = st.multiselect('Selecione um período!', 
        #                             funcoes.Filtro(ImportarDados(), 'Ano', 'vazia'),
        #                             default = sorted(funcoes.Filtro(ImportarDados(), 
        #                                                             'Ano', 'vazia'))[-1]
        #                             )
                
        #     with col[1]:
        #         empresa = st.multiselect('Selecione uma empresa!', 
        #                             funcoes.Filtro(ImportarDados(), 'Empresa', 'vazia'),
        #                             default =sorted(funcoes.Filtro(ImportarDados(), 
        #                                                             'Empresa', 'vazia'))[0]
        #                             )
        #     return anos, empresa          
        
        
        # anos, empresa = Selecao()
        # if choose == 'Lembretes':
        #     pass
        # elif choose == 'Panorama':
        #     panorama.Panorama(anos, empresa)
        # elif choose == 'Receitas':
        #     receitas.Receitas(anos, empresa)
        # elif choose == 'Despesas':
        #     despesas.Despesas(anos, empresa)
        # elif choose == 'DRE':
        #     dre.DRE(anos, empresa)
        # elif choose == 'DFC':
        #     dfc.DFC()
        # elif choose == 'Orçamento':
        #     orcamento.Orcamento()
        # elif choose == 'Pessoal':
        #     pessoas.Pessoas()
        # else:
        #     pass





funcao = Apresentacao()
funcao.Modelo()
        