# 📁 Explorador de archivos de Google Drive

Interfaz interactiva para **Google Colab** que permite **buscar, filtrar, ordenar y previsualizar** los archivos de una carpeta de Google Drive: imágenes, música, videos y documentos, sin salir del notebook.

La interfaz está diseñada en **XML** y funciona con **Python**: el XML describe cómo se ve y se comporta la pantalla, y Python la construye, escanea Drive, ordena los archivos y responde a los botones.

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Efrendcl/BoxiCode/blob/buscador-google-drive/explorador_carpeta_drive_bonito.ipynb)

---

## ✨ Características

### Explorar
- 🎬 **Animación de entrada** con olas y barra de carga, seguida de una aparición escalonada de la interfaz (respeta la opción de «reducir movimiento» del sistema).
- 🔍 **Barra de búsqueda** que filtra por nombre mientras escribes.
- 🗂️ **Filtros por tipo:** Todos, Imágenes, Música, Videos y Documentos.
- ↕️ **Ordenamiento** por nombre, tamaño, fecha o extensión, ascendente o descendente.
- ⚙️ **Algoritmo de ordenamiento automático por tipo**, implementado a mano y visible en la interfaz (junto con el tiempo y el número de comparaciones).
- 🌗 Diseño que se ve bien en modo claro y oscuro.

### Previsualizar
- 🖼️ **Visor de imágenes:** al hacer clic en una miniatura se abre a pantalla completa, con zoom (rueda del ratón o botones), arrastre, doble clic para ampliar, navegación entre fotos y atajos de teclado.
- 🎵🎬 **Mini reproductor de música y video:** barra flotante con anterior, reproducir/pausar, siguiente, barra de progreso para adelantar y retroceder, volumen y ecualizador animado. Los videos se muestran en una ventana flotante que se puede ampliar. Al terminar una pista pasa a la siguiente de la lista.
- 📖 **Lector de documentos:** abre PDF, Word (`.docx`), CSV/TSV (como tabla), JSON (formateado) y archivos de texto o código, con control de tamaño de letra.
- 📊 **Pestaña de almacenamiento:** gráfico de dona con el espacio ocupado por cada tipo de archivo, los 6 archivos más pesados y el uso de tu Google Drive.

## ⚙️ Algoritmos de ordenamiento

Cada tipo de archivo se ordena con el algoritmo que mejor se adapta a su naturaleza. La interfaz muestra cuál se está usando, pero no se puede cambiar desde ella.

| Tipo | Algoritmo | Motivo |
|---|---|---|
| 🖼️ Imágenes | Quick Sort | Muchas fotos con nombres casi únicos: es el más rápido en promedio |
| 🎵 Música | Merge Sort | Bibliotecas grandes y parcialmente ordenadas: garantiza n·log n y es estable |
| 🎬 Videos | Insertion Sort | Pocos archivos: tiene menos sobrecarga en listas pequeñas |
| 📄 Documentos | Merge Sort | Muchos empates (misma extensión o tamaño): es estable y conserva el orden previo |

Los cuatro algoritmos (Quick, Merge, Bubble e Insertion Sort) están implementados desde cero. Para cambiar la asignación, edita el diccionario `ALGORITMO_POR_CATEGORIA`. La pestaña de almacenamiento también usa Merge Sort para ordenar los archivos más pesados.

## 🚀 Cómo usarlo

1. Abre el notebook en [Google Colab](https://colab.research.google.com/) (con el botón de arriba o subiendo el archivo).
2. En la primera celda, cambia el valor de `NOMBRE_CARPETA` por el nombre de tu carpeta dentro de *Mi unidad* de Google Drive:

   ```python
   NOMBRE_CARPETA = 'Acoplamiento'
   ```

3. Ejecuta las celdas en orden. En la última, Colab te pedirá autorización para acceder a tu Google Drive.
4. Espera la animación de entrada y usa la interfaz:
   - **Archivos:** busca, filtra y ordena. Haz clic en una miniatura para abrir el visor, en ▶ para reproducir música o video, y en 📖 para leer un documento.
   - **Almacenamiento:** cambia a esta pestaña para ver el gráfico.

Si la carpeta no existe, el programa muestra las carpetas disponibles en tu Drive para que corrijas el nombre.

### Atajos de teclado

| Dónde | Tecla | Acción |
|---|---|---|
| Reproductor | `Espacio` | Reproducir / pausar |
| Visor de imágenes | `←` `→` | Foto anterior / siguiente |
| Visor de imágenes | `+` `-` `0` | Acercar / alejar / ajustar |
| Visor y lector | `Esc` | Cerrar |

## 🧩 Cómo funciona

El proyecto separa el diseño de la lógica:

| Parte | Qué contiene |
|---|---|
| **XML** (`INTERFAZ_XML`) | `<estilos>` (CSS y animaciones), `<plantillas>` (fragmentos HTML con `$variables`), `<diseno>` (árbol de la pantalla) y `<script>` (comportamiento en el navegador) |
| **Python** | Lee el XML con `xml.etree.ElementTree` y lo convierte en pantalla, escanea Drive, ordena con los algoritmos propios y responde a la interfaz mediante *callbacks* de Colab |

Para que audio, video e imágenes se vean fluidos, el notebook levanta un **pequeño servidor HTTP local** que Colab expone con `google.colab.kernel.proxyPort`. Así los archivos se transmiten por partes (se puede adelantar y retroceder sin cargar todo el archivo) y las miniaturas se piden en paralelo y solo cuando se ven. El servidor únicamente entrega los archivos de la carpeta escaneada y exige un token aleatorio generado en cada ejecución. Si el servidor no está disponible, la interfaz cambia automáticamente a un modo de respaldo (más lento) que envía los archivos codificados en base64.

No se usa la API de Google Drive: la carpeta se lee desde el Drive montado en Colab.

### Usar tu propio diseño XML

Si en `/content` existe un archivo llamado `interfaz_oceano_v2.xml`, se usa en lugar del diseño incluido en el código. Debe conservar los elementos con `id` que el programa necesita (buscador, filtros, vistas, visor, lector, mini reproductor, etc.); si falta alguno, se muestra un error indicando cuáles.

## 🛠️ Configuración

Estas variables están en la primera celda:

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `NOMBRE_CARPETA` | Carpeta de Drive que se explora | `'Acoplamiento'` |
| `INCLUIR_SUBCARPETAS` | Si también se leen las subcarpetas | `True` |
| `MAX_POR_CATEGORIA` | Archivos mostrados por sección (se pueden ver todos con «Mostrar todos») | `12` |
| `EXTENSIONES` | Formatos reconocidos como imagen, música o video | ver código |
| `ALGORITMO_POR_CATEGORIA` | Algoritmo de ordenamiento de cada tipo | ver tabla |
| `TEXTO_EXT` | Extensiones de texto que abre el lector | `.txt`, `.md`, `.py`, `.json`, `.csv`… |
| `LIMITE_TEXTO` | Caracteres máximos que se leen de un archivo de texto | `300 000` |
| `LIMITE_PDF` | Tamaño máximo de un PDF para el lector | `30 MB` |
| `XML_ARCHIVO` | Archivo XML opcional con un diseño propio | `'interfaz_oceano_v2.xml'` |

La altura de la aplicación (820 px) se cambia en el CSS del XML, en la regla `#xd-app`.

## 📌 Notas

- **Requisitos:** una cuenta de Google y acceso a Google Colab. Las librerías (`Pillow` y el resto) ya vienen instaladas en Colab; todo lo demás es de la librería estándar de Python.
- **Internet:** el lector de PDF descarga la librería [PDF.js](https://mozilla.github.io/pdf.js/) desde un CDN la primera vez que se usa. El resto funciona sin ella.
- **Videos:** `.mp4` y `.webm` son los formatos que mejor se reproducen en el navegador. Los `.mkv` y `.avi` normalmente no funcionan y se muestra un aviso. Con el servidor local ya no hay un límite práctico de tamaño; solo en el modo de respaldo se aplican límites (40 MB para música y 60 MB para video).
- **Documentos:** el lector no abre `.xlsx`, `.pptx` ni `.doc` antiguos; en esos casos el archivo se muestra en la lista pero sin vista previa. Los PDF muestran hasta las primeras 60 páginas.
- **Almacenamiento:** el dato de uso de Google Drive depende de que Colab lo informe; si no está disponible, esa tarjeta simplemente no aparece.
- **Primera carga:** si la carpeta tiene muchas fotos, las miniaturas se generan la primera vez que se ven y luego quedan en memoria.
- El programa solo **lee** los archivos de tu Drive: no modifica ni borra nada.

## 📁 Estructura del repositorio

```
.
├── explorador_archivo.ipynb   # Notebook con todo el código (Python + XML)
├── README.md                  # Este archivo
├── LICENSE                    # Licencia MIT
└── .gitignore                 # Archivos que Git debe ignorar
```

## 📄 Licencia

Distribuido bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
