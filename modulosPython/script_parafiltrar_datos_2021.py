import pandas as pd
from random import randint, shuffle, choice

# Número de filas (puedes ajustarlo a tus necesidades)
num_rows = 500

# Semestres y materias
semestres = ['1er Semestre', '2do Semestre', '3er Semestre', '4to Semestre', '5to Semestre', '6to Semestre', '7mo Semestre', '8vo Semestre']

materias_por_semestre = {
    '1er Semestre': ['Matemáticas Discretas', 'Fundamentos de Física', 'Física General Experimental', 'Comunicación Profesional Interdisciplinaria',
                     'Responsabilidad Social y Ética', 'Fundamentos de Administración', 'Lógica de Programación'],
    '2do Semestre': ['Cálculo Diferencial e Integral', 'Psicología en el Trabajo', 'Metodología de la Investigación', 'Sistemas Digitales',
                     'Aplicación de Sistemas Digitales', 'Fundamentos de Ingeniería de Software', 'Estructura de Datos', 'Programación de Bajo Nivel'],
    '3er Semestre': ['Probabilidad', 'Ingeniería de Requerimientos', 'Diseño de Interfaces de usuario', 'Arquitectura y Organización de las Computadoras',
                     'Construcción de Bases de Datos', 'Algoritmos Computacionales', 'Programación Orientada a Objetos'],
    '4to Semestre': ['Estadística', 'Dispositivos Programables', 'Ingeniería de Diseño', 'Administración de Bases de Datos', 'Seguridad Informática',
                     'Sistemas Operativo', 'Adquisición de Datos'],
    '5to Semestre': ['Álgebra Lineal', 'Métodos Numéricos', 'Contabilidad Financiera y de Costos', 'Aplicaciones de la Ciencia Económica',
                     'Teoría de la Computación y Compiladores', 'Comunicación de Datos', 'Programación WEB', 'Optativa I'],
    '6to Semestre': ['Modelos Determinísticos de Investigación de Operaciones', 'Ingeniería Económica', 'Presupuesto y Finanzas', 'Redes y Conectividad',
                     'Fundamentos de Inteligencia Artificia', 'Ingeniería de Pruebas', 'Programación Móvil', 'Optativa II'],
    '7mo Semestre': ['Redes y Modelos de Simulación', 'Administración Estratégica', 'Legislación Informática', 'Formulación y Evaluación de Proyectos',
                     'Ingeniería del Conocimiento', 'Internet de las Cosas', 'Seguridad en Redes', 'Optativa III'],
    '8vo Semestre': ['Habilidades Directivas', 'Informática Empresarial', 'Proyecto de Titulación', 'Gestión de Proyectos',
                     'Calidad y Normalización de Software', 'Administración de Tecnologías', 'Fundamentos de Analítica de Datos', 'Computación en la Nube']
}

# Lista de nombres de profesores ficticios
profesores = ['Prof. Garcia', 'Prof. Martinez', 'Prof. Rodriguez', 'Prof. Hernandez', 'Prof. Lopez']

# Generar datos para cada semestre
semestre = []
nombre_materia = []
entrantes = []
bajas_temp = []
bajas_def = []
ocupacion_materias = []
reprobados = []
numero_salon = []  # Nueva lista para el número de salón
nombre_profesor = []  # Nueva lista para el nombre del profesor
duracion_clase = []  # Nueva lista para la duración de la clase

for semestre_key in semestres:
    materias = materias_por_semestre[semestre_key]
    shuffle(materias)  # Mezclar las materias

    for i in range(num_rows // len(semestres)):  # Asegurar que la cantidad total de filas sea igual a num_rows
        semestre.append(semestre_key)
        nombre_materia.append(choice(materias))
        entrantes_val = randint(600, 700)  # Número de estudiantes que entran
        entrantes.append(entrantes_val)
        bajas_temp_val = randint(200, 250)  # Número de bajas temporales
        bajas_temp.append(bajas_temp_val)
        bajas_def_val = randint(100, 120)  # Número de bajas definitivas
        bajas_def.append(bajas_def_val)
        ocupacion_materias_val = randint(6, 40)  # Cupo por unidad de secuencia
        ocupacion_materias.append(ocupacion_materias_val)
        reprobados.append(randint(0, min(entrantes_val - bajas_temp_val - bajas_def_val, ocupacion_materias_val)))  # Número de reprobados
        numero_salon.append(randint(100, 300))  # Número de salón
        nombre_profesor.append(choice(profesores))  # Nombre del profesor
        duracion_clase.append(randint(1, 3))  # Duración de la clase en horas

# Crear DataFrame
df = pd.DataFrame({
    'Semestre': semestre,
    'Numero de Alumnos que Entren': entrantes,
    'Numero de Bajas Temporales': bajas_temp,
    'Numero de Bajas Definitivas': bajas_def,
    'Cupo por unidad de secuencia': ocupacion_materias,
    'Numero de Reprobados': reprobados,
    'Nombre de la Materia': nombre_materia,
    'Numero de Salon': numero_salon,  # Nueva columna para el número de salón
    'Nombre del Profesor': nombre_profesor,  # Nueva columna para el nombre del profesor
    'Duracion de la Clase (horas)': duracion_clase  # Nueva columna para la duración de la clase
})

# Guardar en un archivo Excel
df.to_excel('3_PRUEBAS_FILTRO2021.xlsx', index=False)