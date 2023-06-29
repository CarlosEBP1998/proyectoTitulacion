import streamlit as st
import pandas as pd
import base64

from io import BytesIO

import webbrowser

def select_columns(df, index):
    st.write(f"Selecciona las columnas que deseas utilizar en el Archivo que se usará para realizar la predicción de secuencias{index}:")
    columns = df.columns.tolist()
    selected_columns = st.multiselect(f"Columnas Histórico No° {index}", columns, key=f"multiselect_{index}")
    selected_df = df[selected_columns]
    return selected_df

def download_excel(df, file_name):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    excel_data = output.read()
    b64 = base64.b64encode(excel_data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">Descargar archivo</a>'
    return href

def main():
    st.title("Selección de columnas a usar para el PLAN 2010")
    st.write(f"Selecciona las columnas que deseas utilizar en el archivo que se usará para realizar la predicción de secuencias del plan de estudio 2010 de Ing. en Informática.")

    uploaded_files = []
    for i in range(3):
        file = st.file_uploader(f"Archivo {i+1}", type="xlsx")
        if file is not None:
            uploaded_files.append((file, i+1))

    if len(uploaded_files) == 3:
        dfs = []
        for file, index in uploaded_files:
            df = pd.read_excel(file)
            dfs.append((df, index))

        selected_dfs = []
        for df, index in dfs:
            st.subheader(f"Archivo {index}")
            selected_df = select_columns(df, index)
            selected_dfs.append(selected_df)

        if st.button("Descargar archivos"):
            for selected_df, index in zip(selected_dfs, range(1, len(selected_dfs)+1)):
                file_name = f"datos{index}_plan2010.xlsx"
                download_link = download_excel(selected_df, file_name)
                st.markdown(download_link, unsafe_allow_html=True)
                st.success(f"Archivo {file_name} descargado exitosamente.")

        st.markdown("---")
        if st.button("Predicción de demanda de secuencias para el Plan 2010"):
            st.write("Redirigiendo al programa de predicción...")
            # URL de redirección
            url = "http://localhost:8502"
            webbrowser.open_new_tab(url)

if __name__ == "__main__":
    main()
