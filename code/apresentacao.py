# app_functions.py
import streamlit as st

def display_app():
    st.title("W.I.C W. Inteligência e Consultoria")

    st.markdown("""
    **Bem-vindo à W.I.C - W Inteligência e Consultoria em Dados e Finanças**
    Olá, sou Wanderson, fundador da W.I.C, e estou muito feliz que você esteja visitando essa página.
    """)

    st.markdown("#  Projeto WIC Financial and management information")
    st.markdown("## Sobre o Projeto")
    st.markdown("""
    Este projeto é muito especial para mim, pois marca o início formal da minha jornada como Analista Autônomo. 
                Aqui, trago soluções financeiras eficientes e inovadoras para o seu negócio, oferecendo uma nova perspectiva sobre sua operação.

    Frequentemente, empresários se perdem nas atividades diárias de suas empresas e deixam de lado a análise crítica baseada em dados financeiros. É aí que entramos: na W.I.C, combinamos expertise em análise de dados com conhecimentos profundos em finanças para oferecer:
    """)

    with st.expander("Nossas Competências e Serviços"):
        st.markdown("""
        - **Análises Financeiras Detalhadas**: Avaliação precisa da saúde financeira da sua empresa.
        - **Consultoria Estratégica**: Desenvolvimento de estratégias financeiras eficazes para otimização de recursos.
        - **Gestão de Riscos**: Identificação e mitigação de riscos financeiros para proteger seu negócio.
        - **Planejamento Financeiro**: Criação de planos financeiros robustos que suportem o crescimento sustentável.
        - **Soluções Personalizadas**: Adaptação das soluções às necessidades específicas do seu negócio.
        
        Nosso objetivo é ajudar você a entender melhor os números do seu negócio e tomar decisões informadas que promovam o sucesso e a sustentabilidade da sua empresa.
        """)

    st.markdown("## Contato")
    st.markdown("""
    Se tiver alguma dúvida ou quiser saber mais sobre como podemos ajudar seu negócio, não hesite em entrar em contato!

    - [Perfil da W.I.C no LinkedIn](https://www.linkedin.com/company/wic-finance/)
    - [Meu Currículo Lattes](http://lattes.cnpq.br/2806443539014450)
    - [Meu Perfil no LinkedIn](https://www.linkedin.com/in/wanderson-bittencourt-8985a3b6/)
    - [Meu GIT](https://github.com/wandersonrochab/WIC_Finance)
                
    Muito obrigado por visitar meu GitHub. Espero que você encontre as soluções que está procurando.
    """)
    st.markdown("## Parceiros de Negócios:")
    with st.expander("Nossos parceiros"):
        st.markdown("""
            - [Alldax Contabilidade](https://alldax.com/): Soluções contábeis e tributárias para seu negócio. 
        """)
    
    st.markdown("## Projetos")
    with st.expander("Nossos Projetos"):
        st.markdown("""
        1. [Financial and management information](#): Soluções para análises financeiras.
        2. [Análise de Dados](#): Análise de dados do seu projeto.
        """)

    st.markdown("## Experimento 01")
    st.markdown("""
    Essa é a versão 01 de um conjunto de demonstrações a serem elaboradas para mostrar o meu trabalho. 
                Já faz tempo que tenho tal interesse, contudo os códigos estavam sendo produzidos, porém não mostrados os resultados. 
                Para esse projeto criei de maneira aleatória algumas bases de dados. 
                A primeira tem 3.000.000 de linhas com 8 colunas com o propósito de mostrar a capacidade de processamento e visualização dos dados.
    """)

# Certifique-se de que o módulo não seja executado diretamente
if __name__ == "__main__":
    display_app()
