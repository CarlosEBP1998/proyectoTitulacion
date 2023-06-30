import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser

st.markdown(
    """
    <style>
    /* Estilos para el botón */
    .login_button {
        position: fixed;
        top: 10px;
        right: 10px;
        background-color: blue;
        color: white;
        padding: 8px 16px;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Leer datos
df = pd.read_excel('/mnt/c/Users/caedb/Downloads/REPROBADOS_PRUEBA/1_PRUEBA_FILTRO2010.xlsx')

def plot_materias():
    # Agrupar datos por 'Nombre de la Materia' y sumar 'Numero de Reprobados'
    materias = df.groupby('Nombre de la Materia')['Numero de Reprobados'].sum().sort_values(ascending=False)

    # Graficar las 10 materias con más reprobados
    fig, ax = plt.subplots(figsize=(10,6))
    ax.barh(materias.index[:10], materias.values[:10])
    plt.title('10 Materias con más reprobados')
    plt.xlabel('Número de Reprobados')
    plt.ylabel('Nombre de la Materia')

    return fig

def plot_profesores():
    # Agrupar datos por 'Nombre del Profesor' y sumar 'Numero de Reprobados'
    profesores = df.groupby('Nombre del Profesor')['Numero de Reprobados'].sum().sort_values(ascending=False)

    # Graficar los 5 profesores con más reprobados
    fig, ax = plt.subplots(figsize=(10,6))
    ax.barh(profesores.index[:5], profesores.values[:5])
    plt.title('5 Profesores con más reprobados')
    plt.xlabel('Número de Reprobados')
    plt.ylabel('Nombre del Profesor')

    return fig

# Título de la aplicación
st.title('Estadísticas relacionadas con distintos ámbitos de el Plan 2010 del programa académico de Ingeniería en Informática.')
st.write('En esta sección, se aborda la trayectoria académica de los alumnos de la Unidad Profesional Interdisciplinaria de Ingeniería y Ciencias Sociales y Administrativas (UPIICSA). Se exploran aspectos como el rendimiento académico, el índice de reprobación y el promedio de calificaciones . Además, se analiza la influencia de diferentes factores en la trayectoria académica, como la carga de trabajo, la participación en actividades extracurriculares y el apoyo recibido por parte de la institución. También se examinan las tendencias y patrones observados a lo largo de los diferentes ciclos escolares, con el objetivo de identificar áreas de mejora y diseñar estrategias para impulsar el éxito académico de los estudiantes.')
st.title('Gráficas')
st.write('Da clic para mostrar la gráfica')

# Botón para mostrar la gráfica de materias
if st.button('Mostrar 10 Materias con más reprobados'):
    st.pyplot(plot_materias())

# Botón para mostrar la gráfica de profesores
if st.button('Mostrar 5 Profesores con más reprobados'):
    st.pyplot(plot_profesores())

# Botón de login en la esquina superior derecha

if st.button("Login", key='login_button'):
    login_url = "http://localhost:8080"
    webbrowser.open_new_tab(login_url)
