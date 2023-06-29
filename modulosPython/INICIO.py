import streamlit as st

def main():
    st.title("BIENVENIDO AL:")
    st.markdown("PROTOTIPO  DE SISTEMA DE ESTIMACIÓN DE DATOS BASADO EN INTELIGENCIA ARTIFICIAL PARA LA PRESENTACIÓN DE INFORMACIÓN COMO APOYO EN EL PROCESO DE LA ASIGNACIÓN DE SECUENCIAS DE LAS UNIDADES DE APRENDIZAJE DE LA CARRERA DE INGENIERÍA EN INFORMÁTICA PARA LOS PLANES 2010-2021 DE UPIICSA")
    st.markdown("En esta página encontrarás los pasos necesarios para realizar el cálculo de predicción de las secuencias de los planes 2010 y 2021 de Ing. en Informática.")

    if st.button('PLAN 2021'):
        st.write('Redirigiendo al cálculo para el PLAN 2021...')
        st.markdown("[Ir al cálculo para el PLAN 2021](http://localhost:8504)")

    if st.button('PLAN 2010'):
        st.write('Redirigiendo al cálculo para el PLAN 2010...')
        st.markdown("[Ir al cálculo para el PLAN 2010](http://localhost:8501)")

if __name__ == "__main__":
    main()
