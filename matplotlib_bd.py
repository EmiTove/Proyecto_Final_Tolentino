import matplotlib.pyplot as plt
import streamlit as st

def grafico_matplotlib(df):

    tabla = df.groupby(["Region","Categoria_Cargo"]).size().unstack()

    fig, ax = plt.subplots()

    tabla.plot(kind="bar", ax=ax)

    ax.set_title("Clasificación de Cargo por Mes")
    ax.set_xlabel("Region")
    ax.set_ylabel("Cantidad de Ventas")

    plt.xticks(rotation=45)

    st.pyplot(fig)
