import pandas as pd
import streamlit as st

# Cargar Base de Datos
def base_csv():

    df_base = pd.read_csv('Ventas_Moviles.csv', sep=";", encoding="latin1")

    # Renombrar columnas para el reporte
    df_base.rename(columns={
    'ï»¿SUBSCRIBER_KEY': 'Codigo_Venta',
    'FECHA_TRANX': 'Fecha_Venta',
    'Segmento': 'Tipo_Cliente',
    'Canal': 'Canal_Venta',
    }, inplace=True)
    
    #Seleccionar columnas 
    df_nuevo = df_base[[
        "Codigo_Venta",
        "Fecha_Venta",
        "Geografia",
        "Region",
        "Departamento",
        "Producto",
        "Tipo_Cliente",
        "Canal_Venta",
        "Cargo_Fijo"
    ]].copy()

    # Crear columna según condiciones
    def clasificar_cargo(cargo):
        if cargo == 0:
            return "Sin cargo"
        elif cargo <= 30:
            return "Cargo bajo"
        elif cargo <= 90:
            return "Cargo medio"
        else:
            return "Cargo alto"

    df_nuevo["Categoria_Cargo"] = df_nuevo["Cargo_Fijo"].apply(clasificar_cargo)

    # Establecer el índice solicitado
    df_nuevo.set_index("Codigo_Venta", inplace=True)

    # Convertir fecha correctamente
    #df_nuevo["Fecha_Venta"] = pd.to_datetime(df_nuevo["Fecha_Venta"], dayfirst=True)
    df_nuevo["Fecha_Venta"] = pd.to_datetime(df_nuevo["Fecha_Venta"],format="%d/%m/%Y")

    # Crear columna Mes para análisis
    df_nuevo["Mes"] = df_nuevo["Fecha_Venta"].dt.to_period("M").astype(str)

    # Crear columna que me de el numero de mes
    df_nuevo["Num_Mes"] = df_nuevo["Fecha_Venta"].dt.month

    return df_nuevo