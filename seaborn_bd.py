import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def grafico_seaborn(df):

    fig, ax = plt.subplots(figsize=(10,5))

    sns.countplot(
        data=df,
        x="Region",
        hue="Producto",
        ax=ax
    )

    # Agregar etiquetas de datos
    for container in ax.containers:
        ax.bar_label(container)

    ax.set_title("Ventas por Región y Tipo de Producto")
    ax.set_xlabel("Región")
    ax.set_ylabel("Cantidad de Ventas")

    plt.xticks(rotation=45)

    st.pyplot(fig)


def grafico_seaborn2(df):

    fig2, ax2 = plt.subplots(figsize=(10,3))

    # Ordenar meses usando Num_Mes
    orden_meses = (
        df.sort_values("Num_Mes")["Mes"]
        .drop_duplicates()
        .tolist()
    )

    sns.countplot(
        data=df,
        x="Mes",
        hue="Tipo_Cliente",
        order=orden_meses,
        ax=ax2
    )

    # Etiquetas de datos más pequeñas
    for container in ax2.containers:
        ax2.bar_label(container, fontsize=8)

    ax2.set_title("Ventas por Tipo de Cliente y Mes")
    ax2.set_xlabel("Mes")
    ax2.set_ylabel("Cantidad de Ventas")

    plt.xticks(rotation=45)

    # Mover la leyenda del gráfico
    ax2.legend(title="Tipo de Cliente", bbox_to_anchor=(1.02, 1), loc="upper left")

    st.pyplot(fig2)