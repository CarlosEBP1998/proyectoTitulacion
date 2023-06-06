import pandas as pd

# Crear dataframes con datos
reprobacion_data = pd.DataFrame({
    'Semestre': ['2023/1', '2023/2'],
    'Materia': ['Calc I', 'Calc II'],
    'Secuencia': ['S1', 'S2'],
    'Total de Alumnos': [40, 50],
    'Número de Reprobaciones': [10, 15]
})

bajas_data = pd.DataFrame({
    'Semestre': ['2023/1', '2023/2'],
    'Materia': ['Calc I', 'Calc II'],
    'Secuencia': ['S1', 'S2'],
    'Bajas Temporales': [2, 3],
    'Bajas Definitivas': [1, 2]
})

ocupabilidad_data = pd.DataFrame({
    'Semestre': ['2023/1', '2023/2'],
    'Materia': ['Calc I', 'Calc II'],
    'Secuencia': ['S1', 'S2'],
    'Total de Alumnos': [40, 50]
})

entrada_data = pd.DataFrame({
    'Semestre': ['2023/1', '2023/2'],
    'Entrada de Alumnos': [600, 700]
})

# Crea un escritor de Excel pandas con un nombre de archivo
writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')

# Escribe cada dataframe en una hoja diferente.
reprobacion_data.to_excel(writer, sheet_name='Índices de Reprobación', index=False)
bajas_data.to_excel(writer, sheet_name='Dictámenes de Baja', index=False)
ocupabilidad_data.to_excel(writer, sheet_name='Ocupabilidad de Materias', index=False)
entrada_data.to_excel(writer, sheet_name='Entrada de Alumnos por Semestre', index=False)

# Guarda el archivo de Excel
writer.save()
