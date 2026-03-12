import plotly.express as px
import streamlit as st

def grafico_plotly(df):

    conteo = df["Categoria_Cargo"].value_counts().reset_index()
    conteo.columns = ["Categoria", "Cantidad"]

    fig = px.pie(
        conteo,
        names="Categoria",
        values="Cantidad",
        title="Distribución de Categorías por Cargo",
        width=700,  
        height=500   
    )

    # Editar etiquetas
    fig.update_traces(
        textinfo="percent",   
        textfont_size=18         
    )

    st.plotly_chart(fig)