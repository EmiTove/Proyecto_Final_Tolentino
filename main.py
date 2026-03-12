import streamlit as st
from pandas_bd import base_csv
from api_kpis import plot_kpis
from seaborn_bd import grafico_seaborn, grafico_seaborn2
from altair_bd import grafico_altair, grafico_altair2
from matplotlib_bd import grafico_matplotlib
from plotly_bd import grafico_plotly

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Ventas Móviles 2024", layout="wide", page_icon="📱")

# CARGAR BASE DE DATOS  

df_nuevo = base_csv() 

# PRESENTACIÓN 

st.title("📶 Altas Móviles en Perú - 2024 📲") 
st.divider() 

# SIDEBAR - FILTROS 

st.sidebar.title("🔎 Filtros") 
region = st.sidebar.multiselect("Región", sorted(df_nuevo["Region"].unique()) )

# Aplicar filtro 
if region:
    df_filtrado = df_nuevo[df_nuevo["Region"].isin(region)]
else:
    df_filtrado = df_nuevo

#Tabs
tab_bd, tab_Altair, tab_Seaborn, tab_Plotly, tab_Matplotlib = st.tabs(["📝 Base_Datos", "📊 Altair","📈 Seaborn", "📉 Plotly", "🗂️ Matplotlib"])

# TAB BASE DE DATOS
with tab_bd:
    st.header("Muestra de la base de datos")
    st.dataframe(df_filtrado)


    with tab_Altair:
        plot_kpis(df_filtrado)
        st.divider()

        grafico_altair(df_filtrado)
        st.divider()

        grafico_altair2(df_filtrado)
        st.divider()

    with tab_Seaborn:
        plot_kpis(df_filtrado)
        st.divider()

        grafico_seaborn(df_nuevo)
        st.divider()

        grafico_seaborn2(df_filtrado)
        st.divider()

    with tab_Plotly:
        plot_kpis(df_filtrado)
        st.divider()

        grafico_plotly(df_filtrado)

    with tab_Matplotlib:
        plot_kpis(df_filtrado)
        st.divider()

        grafico_matplotlib(df_filtrado)
        

    
    