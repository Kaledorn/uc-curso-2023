import pandas as pd
from docx import Document

# Leer archivo docx
doc = Document('/home/jesus/ano1880.docx')

# Extraer lineas
lines = [para.text for para in doc.paragraphs if para.text]

# Crear listas para las columnas A y B
col_a = lines[::2] # Lineas impares
col_b = lines[1::2] # Lineas pares

# Hacerlas del mismo tamaño
if len(col_a) > len(col_b):
    col_b += [''] * (len(col_a) - len(col_b))
elif len(col_b) > len(col_a):
    col_a += [''] * (len(col_b) - len(col_a))

# Crear DataFrame
df = pd.DataFrame({'A': col_a, 'B': col_b})

# Guardar en Excel
df.to_excel('salida.xlsx', index=False)
