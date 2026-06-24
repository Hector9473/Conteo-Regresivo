import streamlit as st
import time
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Cuenta Regresiva", page_icon="⏰", layout="centered")

st.title("⏰ Mi Contador Regresivo")

# Configura tu fecha objetivo aquí (Año, Mes, Día, Hora, Minuto, Segundo)
fecha_objetivo = datetime(2029, 12, 31, 23, 59, 59)

# Contenedor para que el diseño no parpadee al actualizarse
placeholder = st.empty()

while True:
    ahora = datetime.now()
    diferencia = fecha_objetivo - ahora

    with placeholder.container():
        if diferencia.total_seconds() <= 0:
            st.success("🎉 ¡El gran momento ha llegado! 🎉")
            break
        else:
            dias = diferencia.days
            horas = diferencia.seconds // 3600
            minutos = (diferencia.seconds // 60) % 60
            segundos = diferencia.seconds % 60
            
            # Diseño adaptable para computadoras y celulares
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Días", dias)
            col2.metric("Horas", horas)
            col3.metric("Minutos", minutos)
            col4.metric("Segundos", segundos)
            
    time.sleep(1)
