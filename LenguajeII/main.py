import os
import json
from datetime import datetime
from google.colab import drive
from IPython.display import display, Image

# Nombre exacto de tu carpeta en Google Drive
NOMBRE_CARPETA = 'Lenguaje_II'
DIRECTORIO = f'/content/drive/MyDrive/{NOMBRE_CARPETA}'

def list_files_in_directory(directorio):
    # 1. Conectar automáticamente con Google Drive
    print("🔐 Conectando con Google Drive...")
    drive.mount('/content/drive')
    print("✅ Drive conectado con éxito.\n")

    # Validar que la carpeta exista en tu almacenamiento de Drive
    if not os.path.isdir(directorio):
        return {
            "status": "error", 
            "mensaje": f"Directorio '{NOMBRE_CARPETA}' no encontrado en tu Google Drive. Verifica el nombre."
        }

    # Extensiones permitidas 
    extensiones = ('.json', '.csv', '.jpg', '.jpeg', '.png')
    archivos = []
    imagenes_encontradas = [] 
    
    inventario = {
        "existe": False,
        "es_valido": False,
        "total_registros": 0,
        "datos": []
    }

    print(f"📂 Explorando archivos en: {directorio}\n")

    for nombre in os.listdir(directorio):
        ruta = os.path.join(directorio, nombre)

        # Filtrar solo archivos con las extensiones configuradas
        if os.path.isfile(ruta) and nombre.lower().endswith(extensiones):

            # Metadatos (Tamaño en KB y la fecha exacta del archivo en Drive)
            tamano_kb = round(os.path.getsize(ruta) / 1024, 2)
            fecha = datetime.fromtimestamp(os.path.getmtime(ruta)).strftime('%Y-%m-%d %H:%M:%S')

            # Diferenciación visual e inclusión de imágenes
            if nombre.lower().endswith(('.jpg', '.jpeg', '.png')):
                print(f" 🖼️  {nombre} (Imagen) | {tamano_kb} KB | Modificado: {fecha}")
                
                # Extraemos el texto limpio del nombre sin la extensión
                nombre_sin_extension = os.path.splitext(nombre)[0]
                imagenes_encontradas.append({"nombre_boxeador": nombre_sin_extension, "ruta": ruta})
            else:
                print(f" 📄 {nombre} | {tamano_kb} KB | Modificado: {fecha}")

            archivos.append({
                "nombre": nombre,
                "tamano_kb": tamano_kb,
                "fecha": fecha
            })

            # Parseo y validación de inventario.json
            if nombre.lower() == 'inventario.json':
                inventario["existe"] = True
                try:
                    with open(ruta, 'r', encoding='utf-8') as f:
                        datos = json.load(f)

                    # Validar estructura de lista de registros [{}, {}]
                    if isinstance(datos, list) and all(isinstance(item, dict) for item in datos):
                        inventario["es_valido"] = True
                        inventario["total_registros"] = len(datos)
                        inventario["datos"] = datos
                        print(f"    ✅ inventario.json es válido ({len(datos)} registros)")
                    else:
                        print("    ⚠️ inventario.json no contiene una lista válida de registros")

                except json.JSONDecodeError:
                    print("    ❌ Error: inventario.json tiene formato JSON inválido")

    # Retorno estructurado
    return {
        "status": "success",
        "total_archivos": len(archivos),
        "archivos": archivos,
        "inventario": inventario,
        "lista_imagenes": imagenes_encontradas  
    }

# REEMPLAZA DESDE AQUÍ HASTA EL FINAL:
if __name__ == "__main__":
    resultado = list_files_in_directory(DIRECTORIO)
    
    # Clonamos la lista de imágenes para no alterar el diccionario original de la API
    imagenes = resultado.get("lista_imagenes", [])
    
    # Mostrar el retorno estructurado puro 
    print("\n📦 Respuesta Final (Payload para API requerido en Criterio 4):")
    # Limpiamos la propiedad temporal
    payload_limpio = {k: v for k, v in resultado.items() if k != 'lista_imagenes'}
    print(json.dumps(payload_limpio, indent=2, ensure_ascii=False))
    
    print("\n" + "="*60 + "\n")
    
    # Tarjetas automatizadas de boxeo ordenadas abajo
    if imagenes:
        print("🥊 --- TARJETAS DE BOXEO AUTOMATIZADAS ---")
        boxeadores_json = resultado["inventario"]["datos"] if resultado["inventario"]["es_valido"] else []
        for img in imagenes:
            datos_boxeador = None
            
            # Buscamos si el nombre del archivo coincide con el campo "Boxeador" del JSON
            for b in boxeadores_json:
                nombre_json = str(b.get("Boxeador", "")).strip().lower()
                nombre_archivo = str(img["nombre_boxeador"]).strip().lower()
                
                if nombre_json == nombre_archivo:
                    datos_boxeador = b
                    break
            
            # Muestra la foto del púgil primero
            display(Image(filename=img['ruta'], width=220))
            
            # Muestra los detalles técnicos del JSON justo abajo de su respectiva foto
            if datos_boxeador:
                print(f"👤 Boxeador: {datos_boxeador.get('Boxeador').strip()}")
                print(f"📊 Récord Histórico: {datos_boxeador.get('Record')}")
                print(f"🌍 Nacionalidad: {datos_boxeador.get('Nacionalidad')}")
            else:
                print(f"👤 Archivo encontrado: {img['nombre_boxeador']}.jpg")
                print("⚠️ No se encontraron detalles de este boxeador en el archivo JSON.")
                print("💡 Asegúrate de que el archivo de imagen se llame EXACTAMENTE igual que en el JSON.")
                
            print("-" * 60)
    else:
        print("ℹ️ No se encontraron imágenes de boxeadores en la carpeta.")

