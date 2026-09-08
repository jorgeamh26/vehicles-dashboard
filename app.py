import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de anuncios de vehículos')

st.write(
    'Explora la distribución del kilometraje y la relación '
    'entre kilometraje y precio de los vehículos.'
)

build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.write('Distribución del kilometraje de los vehículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Mostrar gráfico de dispersión')

if build_scatter:
    st.write('Relación entre kilometraje y precio')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)