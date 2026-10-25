# 🥊 Proyecto de Automatización: Explorador de Archivos y API de Boxeo

Este proyecto cumple con los requerimientos prácticos de la evaluación de Lenguaje de Programación II. Consiste en un módulo estructurado en Python que se conecta a Google Drive para listar archivos, extraer metadatos en tiempo real y parsear una base de datos en formato JSON para generar tarjetas visuales automatizadas.

## 📋 Características y Criterios Cumplidos
1. **Filtrado selectivo:** Filtra de forma exclusiva archivos de datos (`.json`, `.csv`) e imágenes (`.jpg`, `.jpeg`, `.png`).
2. **Metadatos en tiempo real:** Calcula el tamaño de los archivos en KB (`os.path.getsize`) y la fecha de última modificación (`os.path.getmtime`).
3. **Parseo y Validación:** Lee el archivo `inventario.json`, valida su estructura de registros y extrae la información.
4. **Retorno Modular:** Estructura un diccionario en memoria (Payload) ideal para el consumo de una API.
5. **Interfaz Visual:** Renderiza de forma secuencial una tarjeta con la fotografía de cada boxeador junto a su récord y nacionalidad almacenados en la base de datos.

## 📦 Estructura de la Base de Datos (`inventario.json`)
```json
[
  {
    "id": 1,
    "Boxeador": "Edwin Valero (Inca Valero)",
    "Record": "27-0-0",
    "Nacionalidad": "Venezuela"
  },
  {
    "id": 2,
    "Boxeador": "Gennady Golovkin (GGG)",
    "Record": "42-2-1",
    "Nacionalidad": "Kazajistán"
  }
]
```

## 🛠️ Tecnologías Utilizadas
- Python 3
- Librerías nativas: `os`, `json`, `datetime`
- Gestión de imágenes: `google.colab` y `IPython.display`
