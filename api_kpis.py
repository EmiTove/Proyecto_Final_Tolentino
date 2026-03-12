import streamlit as st

def kpi(title, icon, value):
    st.markdown(
        f"""
    <div class="kpi-card">
        <div class="kpi-title">{icon} {title}</div>
        <div class="kpi-value">{value:,}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
# ---- KPI LAYOUT FUNCTION ----

#Creas una funcion dnde le pasas el datafream filtrado de la hoja de main
def plot_kpis(df):
    total_departamentos = df["Departamento"].nunique() #cuantos departamentos hay
    total_pedidos = len(df)
    promedio_cf = int(df["Cargo_Fijo"].mean())
    #largest_area = df["area"].max()

    c1, c2, c3 = st.columns(3)

    with c1:
        kpi("Total Departamentos", "🌍", total_departamentos)

    with c2:
        kpi("Total Pedidos", "👥", total_pedidos)

    with c3:
        kpi("Promedio Cargo Fijo", "📊", promedio_cf)

