import streamlit as st

def create_card(label, value, border_color, reference_value=None, tipo = None):
    # Define o ícone da seta com base no valor de comparação
    arrow = ""
    arrow_color = ""
    if reference_value is not None:
        if tipo == 'P':
            if float(value) > reference_value:
                # arrow = "⬆️"  # Seta para cima
                arrow = "✔️"   # Seta para cima
                arrow_color = "green"
            elif float(value) < reference_value:
                arrow = "❌"  # Seta para baixo
                # arrow = "⬇️"  # Seta para baixo
                arrow_color = "red"
        elif tipo == 'N':
            if float(value) < reference_value:
                # arrow = "⬆️"  # Seta para cima
                arrow = "✔️"   # Seta para cima
                arrow_color = "green"
            elif float(value) > reference_value:
                arrow = "❌"  # Seta para baixo
                # arrow = "⬇️"  # Seta para baixo
                arrow_color = "red"


    # Estilos CSS
    card_css = f"""
    <style>
    .card {{
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 10px 12px 8px rgba(0,0,0,0.1);
        border: 2px solid {border_color};
        margin: 10px;
        text-align: center;
    }}
    .card .label {{
        font-size: 16px;
        font-weight: bold;
        color: {border_color};
    }}
    .card .value {{
        font-size: 24px;
        font-weight: bold;
        color: black;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .card .arrow {{
        font-size: 24px;
        color: {arrow_color};
        margin-left: 10px;
    }}
    </style>
    """

    # HTML do card
    card_html = f"""
    <div class="card">
        <div class="label">{label}</div>
        <div class="value">{value} <span class="arrow">{arrow}</span></div>
    </div>
    """
    
    st.markdown(card_css, unsafe_allow_html=True)
    st.markdown(card_html, unsafe_allow_html=True)

# Função para criar cards em colunas
def create_cards_in_columns(cards_data, columns_per_row=4, reference_values=None):
    tipo = None
    num_cards = len(cards_data)
    rows = num_cards // columns_per_row + (1 if num_cards % columns_per_row != 0 else 0)
    
    card_idx = 0
    for _ in range(rows):
        cols = st.columns(columns_per_row)
        for col in cols:
            if card_idx < num_cards:
                label, value, border_color, tipo = cards_data[card_idx]
                reference_value = reference_values[card_idx] if reference_values else None
                with col:
                    create_card(label, value, border_color, reference_value, tipo)
                card_idx += 1

# # Exemplo de uso
# cards_data = [
#     ("Vendas", 200, "#4CAF50"),
#     ("Despesas", 150, "#F44336"),
#     ("Lucro", 50, "#2196F3"),
#     ("Investimentos", 300, "#FF9800")
# ]

# # Valores de referência para comparação
# reference_values = [180, 160, 60, 280]

# # Criar os cards
# create_cards_in_columns(cards_data, columns_per_row=2, reference_values=reference_values)
