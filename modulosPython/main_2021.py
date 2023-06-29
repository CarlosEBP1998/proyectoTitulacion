import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

def main():
    st.title("Predicción de demanda de secuencias para el Plan 2021 Ingeniería en Informática")
    st.write("Por favor, sube los archivos de Excel:")

    uploaded_files = []
    for i in range(3):
        file = st.file_uploader(f"Agrega el Archivo de Excel anteriormente generado, Agrega el Historico no° {i+1}", type="xlsx")
        if file is not None:
            uploaded_files.append(file)

    if len(uploaded_files) == 3:
        data1 = pd.read_excel(uploaded_files[0])
        data2 = pd.read_excel(uploaded_files[1])
        data3 = pd.read_excel(uploaded_files[2])

        data = pd.concat([data1, data2, data3])

        data['total_estudiantes'] = data['Numero de Alumnos que Entren'] - data['Numero de Bajas Temporales'] - data['Numero de Bajas Definitivas'] + data['Numero de Reprobados']

        encoder = OneHotEncoder(sparse=False)
        encoded_semestre = encoder.fit_transform(data[['Semestre']])
        encoded_semestre_df = pd.DataFrame(encoded_semestre, columns=encoder.get_feature_names_out(['Semestre']))

        data = pd.concat([data.reset_index(drop=True), encoded_semestre_df], axis=1)

        semestres = data['Semestre'].unique()

        total_demand_in_groups = 0
        semestre_demand_in_groups = {}

        with st.sidebar:
            st.title("Semestres")
            st.write("Seleccione un semestre para ver las materias y la demanda total por semestre.")
            semestre_selected = st.radio("Semestre", ["Todos los semestres"] + list(semestres))

        for semestre in semestres:
            data_semestre = data[data['Semestre'] == semestre]

            if semestre_selected == "Todos los semestres" or semestre == semestre_selected:
                materias = data_semestre['Nombre de la Materia'].unique()
                demand_in_groups = 0
                results = []

                for materia in materias:
                    data_materia = data_semestre[data_semestre['Nombre de la Materia'] == materia]

                    if len(data_materia) < 2:
                        continue

                    X_materia = data_materia[['total_estudiantes'] + list(encoded_semestre_df.columns)]
                    y_materia = data_materia['Cupo por unidad de secuencia']

                    X_train, X_test, y_train, y_test = train_test_split(X_materia, y_materia, test_size=0.2, random_state=42)

                    model = LinearRegression()
                    model.fit(X_train, y_train)

                    predictions = model.predict(X_test)

                    min_students_per_group = 6
                    max_students_per_group = 40
                    materia_demand_in_groups = np.sum([np.ceil(prediction / max_students_per_group) for prediction in predictions])
                    results.append([materia, semestre, np.round(materia_demand_in_groups)])

                    demand_in_groups += materia_demand_in_groups

                df = pd.DataFrame(results, columns=['Materia', 'Semestre', 'Secuencias necesarias'])
                st.title(f"Semestre {semestre}")
                st.dataframe(df)

                if semestre_selected == "Todos los semestres":
                    semestre_demand_in_groups[semestre] = demand_in_groups

                total_demand_in_groups += demand_in_groups

        st.sidebar.title("Total de secuencias por semestre")
        for semestre, demanda in semestre_demand_in_groups.items():
            st.sidebar.write(f"Semestre {semestre}: {demanda:.0f} secuencias")

        st.sidebar.title("Sumatoria total de secuencias")
        st.sidebar.write(f"Total: {total_demand_in_groups:.0f} secuencias")

if __name__ == "__main__":
    main()