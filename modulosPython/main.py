import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

st.title("Programa para predecir la demanda de secuencias en UPIICSA")

st.write("Para el debido funcionamiento del programa tendrá que subir los históricos de 3 semestres atrás para poder hacer un predicción de cuántos secuencias se podrán aperturar.")
st.write("Dichos archivos de Excel tendrán que tener como nombre 'file1' , 'file2' y 'file3' ")
uploaded_file1 = st.file_uploader("Por favor suba el histórico en formato Excel con nombre 'file1' ", type=['xlsx'])
uploaded_file2 = st.file_uploader("Por favor suba el histórico en formato Excel con nombre 'file2' ", type=['xlsx'])
uploaded_file3 = st.file_uploader("Por favor suba el histórico en formato Excel con nombre 'file3' ", type=['xlsx'])

if uploaded_file1 is not None and uploaded_file2 is not None and uploaded_file3 is not None:
    # Leer los archivos de Excel
    file1 = pd.read_excel(uploaded_file1)
    file2 = pd.read_excel(uploaded_file2)
    file3 = pd.read_excel(uploaded_file3)

    # Combinar los datos en un solo DataFrame
    data = pd.concat([file1, file2, file3])

    # Crear una columna para el total de estudiantes
    data['total_estudiantes'] = data['Numero de Alumnos que Entren'] - data['Numero de Bajas Temporales'] - data['Numero de Bajas Definitivas']

    # Codificación One-Hot para la variable 'Semestre'
    encoder = OneHotEncoder(sparse_output=False)
    encoded_semestre = encoder.fit_transform(data[['Semestre']])
    encoded_semestre_df = pd.DataFrame(encoded_semestre, columns=encoder.get_feature_names_out(['Semestre']))

    # Agregar las columnas codificadas al DataFrame original
    data = pd.concat([data.reset_index(drop=True), encoded_semestre_df], axis=1)

    # Obtener una lista de todas las materias
    materias = data['Nombre de la Materia'].unique()

    # Inicializar un contador para la demanda total de secuencias
    total_demand_in_groups = 0

    # Para cada materia, entrenar un modelo y predecir la demanda
    for materia in materias:
        # Solo usar los datos para la materia actual
        data_materia = data[data['Nombre de la Materia'] == materia]

        # Si no hay suficientes datos para esta materia, continuamos con la siguiente
        if len(data_materia) < 2:
            continue

        # Asegúrate de que X y y solo contienen datos para la materia actual
        X_materia = data_materia[['total_estudiantes', 'Semestre_Semestre1', 'Semestre_Semestre2']]
        y_materia = data_materia['Cupo por unidad de secuencia']

        # Dividir los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X_materia, y_materia, test_size=0.2, random_state=42)

        # Crear y entrenar el modelo de regresión lineal
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predecir la demanda para el conjunto de prueba
        predictions = model.predict(X_test)

        # Calcular la demanda real de secuencias (grupos que necesitan ser formados)
        min_students_per_group = 6
        max_students_per_group = 40
        demand_in_groups = np.sum([np.ceil(prediction / max_students_per_group) for prediction in predictions])

        # Si la predicción es menor que 6 (el mínimo requerido por secuencia), entonces establecemos el número de grupos a 1
        demand_in_groups = np.where(demand_in_groups < 1, 1, demand_in_groups)

        st.title("RESULTADOS")

        st.write(f"La demanda estimada de secuencias (grupos que necesitan ser formados) para la {materia} es de aproximadamente {demand_in_groups:.0f}")

        # Sumar la demanda de esta materia a la demanda total
        total_demand_in_groups += demand_in_groups

    # Imprimir la demanda total de secuencias
    st.title("DEMANDA TOTAL")
    st.write(f"La demanda total estimada de secuencias (grupos que necesitan ser formados) es de aproximadamente {total_demand_in_groups:.0f}")
else:
    st.write("Por favor, suba los tres archivos Excel para iniciar el proceso.")
