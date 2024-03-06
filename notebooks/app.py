import pandas as pd
import plotly.express as px
import streamlit as st




car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis exploratorio de datos de vehículos')




hist_button = st.button('Construir histograma')




if hist_button:
   
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
   
   
    fig = px.histogram(car_data, x="odometer")
   
   
    st.plotly_chart(fig, use_container_width=True)


build_histogram = st.checkbox('Construir un histograma')


if build_histogram:
    
    st.write('Construir un histograma para la columna odómetro')
    
    
    fig = px.histogram(car_data, x="odometer")
    
    
    st.plotly_chart(fig, use_container_width=True)


build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    
    st.write('Construir un gráfico de dispersión para las columnas odometer y price')
    
    
    fig = px.scatter(car_data, x="odometer", y="price")
    
    
    st.plotly_chart(fig, use_container_width=True)
