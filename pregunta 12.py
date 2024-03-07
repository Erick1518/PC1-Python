# Obtener el tipo de MIME de un archivo a partir de su nombre

def obtener_tipo_mime(nombre_archivo):
    extension = nombre_archivo.lower().split(".")[-1]
    tipos_mime = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/png",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }   
    return tipos_mime.get(extension, "application/octet-stream")

# solicitar nombre de archivo
nombre_archivo = input("ingrese el nombre del archivo: ")

# ubicar el tipo mime
tipo_mime = obtener_tipo_mime(nombre_archivo)

# el tipo mime del archivo
print(f"Tipo mime: {tipo_mime}")