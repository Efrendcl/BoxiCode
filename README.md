# 📁 Explorador de archivos de Google Drive

Interfaz interactiva para **Google Colab** que permite **buscar, filtrar y ordenar** los archivos de una carpeta de Google Drive: imágenes, música, videos y documentos.

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://google.com)



---

## ✨ Características

- 🔍 **Barra de búsqueda** que filtra por nombre mientras escribes.
- 🗂️ **Filtros por tipo:** Todos, Imágenes, Música, Videos y Documentos.
- ↕️ **Ordenamiento** por nombre, tamaño, fecha o extensión, ascendente o descendente.
- 🖼️ **Imágenes** en tarjetas con miniatura.
- 🎵🎬 **Música y videos** con botón ▶ para reproducirlos dentro del notebook.
- 📄 **Documentos** con ícono según el tipo (PDF, Word, Excel, etc.), tamaño y fecha.
- ⚙️ **Algoritmo de ordenamiento automático por tipo**, implementado a mano y visible en la interfaz (junto con el tiempo y el número de comparaciones).
- 🌗 Diseño que se ve bien en modo claro y oscuro.

## ⚙️ Algoritmos de ordenamiento

Cada tipo de archivo se ordena con el algoritmo que mejor se adapta a su naturaleza. La interfaz muestra cuál se está usando, pero no se puede cambiar desde ella.

| Tipo | Algoritmo | Motivo |
|---|---|---|
| 🖼️ Imágenes | Quick Sort | Muchas fotos con nombres casi únicos: es el más rápido en promedio |
| 🎵 Música | Merge Sort | Bibliotecas grandes y parcialmente ordenadas: garantiza n·log n y es estable |
| 🎬 Videos | Insertion Sort | Pocos archivos: tiene menos sobrecarga en listas pequeñas |
| 📄 Documentos | Merge Sort | Muchos empates (misma extensión o tamaño): es estable y conserva el orden previo |

Los cuatro algoritmos (Quick, Merge, Bubble e Insertion Sort) están implementados desde cero en el notebook. Para cambiar la asignación, edita el diccionario `ALGORITMO_POR_CATEGORIA`.

## 🚀 Cómo usarlo

1. Abre `explorador_archivo.ipynb` en [Google Colab](https://colab.research.google.com/) (con el botón de arriba o subiendo el archivo).
2. En la primera celda, cambia el valor de `NOMBRE_CARPETA` por el nombre de tu carpeta dentro de *Mi unidad* de Google Drive:

   ```python
   NOMBRE_CARPETA = 'Acoplamiento'
   ```

3. Ejecuta las celdas en orden. En la última, Colab te pedirá autorización para acceder a tu Google Drive.
4. Usa la barra de búsqueda, los filtros y el selector de orden.

Si la carpeta no existe, el notebook muestra las carpetas disponibles en tu Drive para que corrijas el nombre.

## 🛠️ Configuración

Estas variables están en la primera celda:

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `NOMBRE_CARPETA` | Carpeta de Drive que se explora | `'Acoplamiento'` |
| `INCLUIR_SUBCARPETAS` | Si también se leen las subcarpetas | `True` |
| `MAX_POR_CATEGORIA` | Archivos mostrados por sección (se pueden ver todos con «Mostrar todos») | `12` |
| `EXTENSIONES` | Formatos reconocidos como imagen, música o video | ver notebook |
| `ALGORITMO_POR_CATEGORIA` | Algoritmo de ordenamiento de cada tipo | ver tabla |

## 📌 Notas

- **Requisitos:** una cuenta de Google y acceso a Google Colab. Las librerías (`ipywidgets`, `Pillow`) ya vienen instaladas en Colab.
- **Videos:** los formatos `.mp4` y `.webm` son los que mejor se reproducen en el navegador. Los videos de más de 150 MB no se reproducen dentro del notebook.
- **Primera carga:** si la carpeta tiene muchas fotos, la primera vez que se muestran puede tardar un poco; después quedan en memoria.
- El notebook solo **lee** los archivos de tu Drive: no modifica ni borra nada.

## 📁 Estructura del repositorio

```
.
├── explorador_archivo.ipynb   # Notebook con todo el código
├── README.md                  # Este archivo
├── LICENSE                    # Licencia MIT
└── .gitignore                 # Archivos que Git debe ignorar
```

## 📄 Licencia

Distribuido bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
