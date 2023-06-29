import pandas as pd
from random import randint, shuffle, choice

# Número de filas (puedes ajustarlo a tus necesidades)
num_rows = 500

# Niveles y materias
niveles = ['Nivel I', 'Nivel II', 'Nivel III', 'Nivel IV', 'Nivel V']
materias_por_nivel = {
    'Nivel I': ['PLAN DE VIDA', 'COMUNICACIÓN PROFESIONAL', 'ESTUDIO DE LA INDUSTRIA NACIONAL DEL SOFTWARE',
                'SOCIEDAD, TECNOLOGÍA Y DEONTOLOGÍA', 'ESTUDIO DE LA INDUSTRIA CONTINENTAL DEL SOFTWARE',
                'ESTUDIO DE LA INDUSTRIA MUNDIAL DEL SOFTWARE', 'PSICOLOGÍA EN EL TRABAJO', 'ÁLGEBRA LINEAL',
                'CÁLCULO DIFERENCIAL E INTEGRAL', 'PROBABILIDAD', 'ESTADÍSTICA', 'CONTABILIDAD DE COSTOS',
                'ADMINISTRACIÓN INTEGRAL', 'LEGISLACIÓN INFORMÁTICA', 'MATEMÁTICAS DISCRETAS', 'FÍSICA PARA INFORMÁTICOS',
                'SISTEMAS DIGITALES', 'APLICACIONES DE SISTEMAS DIGITALES', 'LÓGICA DE PROGRAMACIÓN'],
    'Nivel II': ['ESTRUCTURAS DE DATOS', 'TEORÍA DE LA COMPUTACIÓN', 'ARQUITECTURA Y ORGANIZACIÓN DE COMPUTADORAS',
                 'FUNDAMENTOS DE PROGRAMACIÓN ORIENTADA A OBJETOS', 'PROGRAMACIÓN LINEAL APLICADA', 'MÉTODOS NUMÉRICOS',
                 'PRESUPUESTOS Y FINANZAS', 'PLANEACIÓN ESTRATÉGICA', 'FUNDAMENTOS DE INTELIGENCIA ARTIFICIAL',
                 'HERRAMIENTAS AUTOMATIZADAS', 'FUNDAMENTOS DE INGENIERÍA DE SOFTWARE', 'TELEINFORMÁTICA',
                 'PROGRAMACIÓN ORIENTADA A OBJETOS', 'ELECTIVA'],
    'Nivel III': ['SIMULACIÓN DE SISTEMAS', 'ECONOMÍA', 'ECONOMÍA DE LA INGENIERÍA', 'INGENIERÍA DEL CONOCIMIENTO',
                  'INGENIERÍA DE REQUERIMIENTOS', 'SEGURIDAD INFORMÁTICA', 'CONSTRUCCIÓN DE BASE DE DATOS',
                  'ALGORITMOS COMPUTACIONALES', 'SISTEMAS OPERATIVOS', 'REDES', 'DISPOSITIVOS PROGRAMABLES',
                  'PROGRAMACIÓN WEB', 'OPTATIVA I'],
    'Nivel IV': ['INGENIERÍA DE DISEÑO', 'ADMINISTRACIÓN DE BASES DE DATOS', 'SISTEMAS EN TIEMPO REAL', 'COMPILADORES',
                 'ADQUISICIÓN DE DATOS', 'HABILIDADES DIRECTIVAS', 'OPTATIVA II', 'OPTATIVA III',
                 'METODOLOGÍA DE LA INVESTIGACIÓN INTERDISCIPLINARIA', 'FORMULACIÓN Y EVALUACIÓN DE PROYECTOS',
                 'CALIDAD Y NORMALIZACIÓN DE SOFTWARE', 'APLICACIONES DE REDES'],
    'Nivel V': ['PROYECTO DE TITULACIÓN', 'GESTIÓN DE PROYECTOS', 'INFORMÁTICA EMPRESARIAL', 'INGENIERÍA DE PRUEBAS',
                'ADMINISTRACIÓN DE TECNOLOGÍAS', 'PRACTICA PROFESIONAL']
}
# Lista de nombres de profesores ficticios
profesores = ['Prof. Garcia', 'Prof. Martinez', 'Prof. Rodriguez', 'Prof. Hernandez', 'Prof. Lopez']
# Generar datos para cada nivel
nivel = []
nombre_materia = []
entrantes = []
bajas_temp = []
bajas_def = []
ocupacion_materias = []
reprobados = []
num_salon = []
nombre_profesor = []
duracion_clase = []

for nivel_key in niveles:
    materias = materias_por_nivel[nivel_key]
    shuffle(materias)  # Mezclar las materias

    for i in range(num_rows // len(niveles)):  # Asegurar que la cantidad total de filas sea igual a num_rows
        nivel.append(nivel_key)
        nombre_materia.append(choice(materias))
        entrantes.append(randint(600, 700))  # Número de estudiantes que entran
        bajas_temp.append(randint(200, 250))  # Número de bajas temporales
        bajas_def.append(randint(100, 120))  # Número de bajas definitivas
        ocupacion = randint(6, 40)  # Cupo por unidad de secuencia
        ocupacion_materias.append(ocupacion)
        reprobados.append(randint(0, ocupacion - 1))  # Número de reprobados (menor que el cupo por unidad de secuencia)
        num_salon.append(randint(1, 10))  # Número de salón
        nombre_profesor.append(choice(profesores))  # Nombre del profesor
        duracion_clase.append(randint(1, 3))  # Duración de la clase en horas

# Crear DataFrame
df = pd.DataFrame({
    'Nivel': nivel,
    'Numero de Alumnos que Entren': entrantes,
    'Numero de Bajas Temporales': bajas_temp,
    'Numero de Bajas Definitivas': bajas_def,
    'Cupo por unidad de secuencia': ocupacion_materias,
    'Numero de Reprobados': reprobados,
    'Nombre de la Materia': nombre_materia,
    'Numero de Salón': num_salon,
    'Nombre del Profesor': nombre_profesor,
    'Duración de la Clase (horas)': duracion_clase
})

# Guardar en un archivo Excel
df.to_excel('PRUEBA_FILTRO2.xlsx', index=False)
