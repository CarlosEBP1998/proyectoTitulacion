import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Función para cargar los datos de Excel
@st.cache
def load_data(sheet_name):
    data = pd.read_excel('data.xlsx', sheet_name=sheet_name)
    return data

# Función para entrenar el modelo
def train_model(data):
    X_train, X_test, y_train, y_test = train_test_split(data.drop('Secuencias Necesarias', axis=1), data['Entrada de Alumnos'], test_size=0.2)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def main():
    st.title('Predicción de Demanda de Secuencias en UPIICSA')

    # Carga los datos
    reprobacion_data = load_data('Índices de Reprobación')
    bajas_data = load_data('Dictámenes de Baja')
    ocupabilidad_data = load_data('Ocupabilidad de Materias')
    entrada_data = load_data('Entrada de Alumnos por Semestre')

    # Calcula el número promedio de alumnos por secuencia
    ocupabilidad_data['Alumnos por Secuencia'] = ocupabilidad_data['Total de Alumnos'] / ocupabilidad_data['Secuencia'].nunique()

    # Calcula el número de secuencias que se necesitan para cada semestre
    entrada_data['Secuencias Necesarias'] = entrada_data['Entrada de Alumnos'] / ocupabilidad_data['Alumnos por Secuencia'].mean()

    # Crea el DataFrame que usarás para entrenar tu modelo
    data = entrada_data.copy()  # Comienza con los datos de entrada

    # Verifica que la columna 'Secuencias Necesarias' exista en el DataFrame
    if 'Secuencias Necesarias' not in data.columns:
        st.error("Error: La columna 'Secuencias Necesarias' no existe en los datos.")
        return

    # Selecciona las características necesarias para la predicción
    features = ['Semestre', 'Entrada de Alumnos']

    # Filtra el DataFrame para incluir solo las características necesarias
    data_filtered = data[features]

    # Verifica que la columna 'Entrada de Alumnos' exista en el DataFrame filtrado
    if 'Entrada de Alumnos' not in data_filtered.columns:
        st.error("Error: La columna 'Entrada de Alumnos' no existe en los datos filtrados.")
        return

    # Entrena el modelo con los datos filtrados
    model = train_model(data_filtered)

    # Interfaz de usuario para ingresar los valores de entrada y hacer la predicción
    st.subheader('Ingrese los valores de entrada:')
    input_values = {}
    for column in data_filtered.columns:
        input_values[column] = st.number_input(column, value=0.0)

    # Genera una lista de valores de entrada en el mismo orden que las columnas del DataFrame
    input_data = [[input_values[column] for column in data_filtered.columns]]

    # Realiza la predicción
    prediction = model.predict(input_data)

    # Muestra el resultado de la predicción
    st.subheader('Resultado de la predicción:')
    st.write('Número de secuencias necesarias:', prediction[0])

if __name__ == "_main_":
    main()