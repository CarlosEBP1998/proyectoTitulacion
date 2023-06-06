import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Función para cargar los datos de Excel
def load_data(sheet_name):
    data = pd.read_excel('data.xlsx', sheet_name=sheet_name)
    return data

# Función para entrenar el modelo
def train_model(data):
    X_train, X_test, y_train, y_test = train_test_split(data.drop('target', axis=1), data['target'], test_size=0.2)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def main():
    st.title('Predicción de Demanda de Secuencias en UPIICSA')

    # Carga los datos
    reprobacion_data = load_data('Índices de Reprobación').copy()
    bajas_data = load_data('Dictámenes de Baja').copy()
    ocupabilidad_data = load_data('Ocupabilidad de Materias').copy()
    entrada_data = load_data('Entrada de Alumnos por Semestre').copy()

    # Calcula el número promedio de alumnos por secuencia
    ocupabilidad_data['Alumnos por Secuencia'] = ocupabilidad_data['Total de Alumnos'] / ocupabilidad_data['Secuencia'].nunique()

    # Calcula el número de secuencias que se necesitan para cada semestre
    entrada_data['Secuencias Necesarias'] = entrada_data['Entrada de Alumnos'] / ocupabilidad_data['Alumnos por Secuencia'].mean()

    # Crea el DataFrame que usarás para entrenar tu modelo
    data = entrada_data.copy()  # Comienza con los datos de entrada
    data['target'] = data['Secuencias Necesarias']  # Esto es lo que estás tratando de predecir

    # Selecciona todas las columnas de tipo 'object' (que suelen ser cadenas de texto en Pandas)
    categorical_columns = data.select_dtypes(include=['object']).columns
    # Codifica las columnas categóricas con One-Hot Encoding
    data_encoded = pd.get_dummies(data, columns=categorical_columns)

    # Verifica si hay columnas faltantes en los datos codificados
    expected_columns = set(entrada_data.columns)
    actual_columns = set(data_encoded.columns)
    missing_columns = expected_columns.difference(actual_columns)
    if missing_columns:
        for column in missing_columns:
            data_encoded[column] = 0

    # Entrena el modelo con los datos codificados
    model = train_model(data_encoded)

    # Interfaz de usuario para ingresar los valores de entrada y hacer la predicción
    st.subheader('Ingrese los valores de entrada:')
    input_values = {}
    for column in data.drop(['target'], axis=1).columns:
        input_values[column] = st.number_input(column, value=0.0)

    # Genera una lista de valores de entrada en el mismo orden que las columnas del DataFrame
    input_data = [[input_values[column] for column in data.drop(['target'], axis=1).columns]]

    # Realiza la predicción
    prediction = model.predict(input_data)

    # Muestra el resultado de la predicción
    st.subheader('Resultado de la predicción:')
    st.write('Número de secuencias necesarias:', prediction[0])

if __name__ == "__main__":
    main()
