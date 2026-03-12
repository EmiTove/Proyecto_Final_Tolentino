import altair as alt
import streamlit as st

def grafico_altair(df):

    ventas_mes = df.groupby("Mes").size().reset_index(name="Total_Ventas")

    # Línea
    linea = alt.Chart(ventas_mes).mark_line(
        color="#dc7738",
        strokeWidth=5
    ).encode(
        x=alt.X("Mes:N", title="Mes"),
        y=alt.Y(
            "Total_Ventas:Q",
            title="Total de Ventas",
            scale=alt.Scale(domain=[3700, 3900])
        ),
        tooltip=["Mes", "Total_Ventas"]
    )

    # Marcadores circulares rellenos
    puntos = alt.Chart(ventas_mes).mark_point(
        shape="circle",
        filled=True,
        fill="#dc7738",
        stroke="orange",
        strokeWidth=4,
        size=120
    ).encode(
        x="Mes:N",
        y="Total_Ventas:Q"
    )

    # Etiquetas
    etiquetas = alt.Chart(ventas_mes).mark_text(
        dy=-25,
        size=14,
        color="orange"
    ).encode(
        x="Mes:N",
        y="Total_Ventas:Q",
        text="Total_Ventas:Q"
    )

    chart = (linea + puntos + etiquetas).properties(
        title="Total de Ventas por Mes"
    )

    st.altair_chart(chart, use_container_width=True)


def grafico_altair2(df):

    chart = alt.Chart(df).mark_bar().encode(
        y=alt.Y("Departamento:N", title="Departamento", sort="-x"),
        x=alt.X("count()", title="Cantidad de Ventas"),
        color=alt.Color(
            "Departamento:N",
            legend=None,
            scale=alt.Scale(scheme="tableau10")
        ),
        tooltip=["Departamento", "count()"]
    ).properties(
        title="Cantidad de Ventas por Departamento"
    )

    st.altair_chart(chart, use_container_width=True)