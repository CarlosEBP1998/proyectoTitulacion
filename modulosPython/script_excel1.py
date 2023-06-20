import pandas as pd
import numpy as np
from random import randint, choice

# Número de filas (puedes ajustarlo a tus necesidades)
num_rows = 500

# Crear datos aleatorios para cada columna
semestre = ['Semestre1' if i < num_rows//2 else 'Semestre2' for i in range(num_rows)]

# Generamos una lista de posibles materias
materias = ['Materia' + str(i) for i in range(1, 21)]

# Generar datos para el semestre 1
entrantes_sem1 = [600 for _ in range(num_rows//2)] # Número de estudiantes que entran
bajas_temp_sem1 = [200 for _ in range(num_rows//2)] # Número de bajas temporales
bajas_def_sem1 = [100 for _ in range(num_rows//2)] # Número de bajas definitivas
ocupacion_materias_sem1 = [randint(6, 40) for _ in range(num_rows//2)] # Ocupación de materias por salón
nombre_materia_sem1 = [choice(materias) for _ in range(num_rows//2)] # Nombre de la materia

# Generar datos para el semestre 2 basándose en los del semestre 1
entrantes_sem2 = [700 for _ in range(num_rows//2, num_rows)] # Número de estudiantes que entran
bajas_temp_sem2 = [250 for _ in range(num_rows//2, num_rows)] # Número de bajas temporales
bajas_def_sem2 = [120 for _ in range(num_rows//2, num_rows)] # Número de bajas definitivas
ocupacion_materias_sem2 = [randint(6, 40) for _ in range(num_rows//2, num_rows)]
nombre_materia_sem2 = [choice(materias) for _ in range(num_rows//2, num_rows)]

# Unir los datos de ambos semestres
entrantes = entrantes_sem1 + entrantes_sem2
bajas_temp = bajas_temp_sem1 + bajas_temp_sem2
bajas_def = bajas_def_sem1 + bajas_def_sem2
ocupacion_materias = ocupacion_materias_sem1 + ocupacion_materias_sem2
nombre_materia = nombre_materia_sem1 + nombre_materia_sem2

# Crear DataFrame
df = pd.DataFrame({
    'Semestre': semestre,
    'Numero de Alumnos que Entren': entrantes,
    'Numero de Bajas Temporales': bajas_temp,
    'Numero de Bajas Definitivas': bajas_def,
    'Ocupación de Materias por Salon': ocupacion_materias,
    'Nombre de la Materia': nombre_materia
})

# Guardar en un archivo Excel
df.to_excel('datos.xlsx', index=False)
