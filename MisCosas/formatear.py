from docx import Document

# Leer el archivo docx
doc = Document('/home/jesus/ano1880.docx')

# Iterar a través de cada párrafo
for para in doc.paragraphs:
    # Reemplazar los saltos de línea duplicados o saltos de línea seguidos de un espacio y otro salto de línea
    para.text = para.text.replace('\n\n', '\n')
    para.text = para.text.replace('\n \n', '\n')

# Guardar el documento modificado
doc.save('tu_archivo_modificado.docx')
