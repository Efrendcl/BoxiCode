import os
import io
import html
import time
import base64
from dataclasses import dataclass
from datetime import datetime

from google.colab import drive
from IPython.display import display, Audio, Video, HTML, clear_output
import ipywidgets as widgets
from PIL import Image as PILImage, ImageOps

# ============================================================
# 1. CONFIGURACIÓN
# ============================================================
NOMBRE_CARPETA = 'Acoplamiento'          # <-- cambia por el nombre de tu carpeta nueva en Drive
DIRECTORIO = f'/content/drive/MyDrive/{NOMBRE_CARPETA}'
INCLUIR_SUBCARPETAS = True
MAX_POR_CATEGORIA = 12                  # cuántos archivos se muestran por sección

EXTENSIONES = {
    "Imágenes": ('.jpg', '.jpeg', '.png', '.gif', '.webp'),
    "Música":   ('.mp3', '.wav', '.ogg', '.m4a', '.aac'),
    "Videos":   ('.mp4', '.webm', '.mov', '.avi', '.mkv'),
}
CATEGORIAS = ["Imágenes", "Música", "Videos", "Archivos"]
ICONO = {"Imágenes": "🖼️", "Música": "🎵", "Videos": "🎬", "Archivos": "📄"}
ICONO_EXT = {'.pdf': '📕', '.doc': '📝', '.docx': '📝', '.txt': '📝', '.xls': '📊', '.xlsx': '📊',
             '.csv': '📊', '.ppt': '📽️', '.pptx': '📽️', '.zip': '🗜️', '.rar': '🗜️', '.json': '🧾'}


# ============================================================
# 2. ESCANEO DE LA CARPETA
# ============================================================
@dataclass
class Archivo:
    nombre: str
    ruta: str
    categoria: str
    tamano: int      # en bytes
    fecha: str       # 'AAAA-MM-DD HH:MM'

    @property
    def extension(self):
        return os.path.splitext(self.nombre)[1].lower()

    @property
    def icono(self):
        return ICONO_EXT.get(self.extension, ICONO[self.categoria]) if self.categoria == "Archivos" \
            else ICONO[self.categoria]


def categoria_de(nombre):
    for categoria, extensiones in EXTENSIONES.items():
        if nombre.lower().endswith(extensiones):
            return categoria
    return "Archivos"


def escanear(directorio):
    archivos = []
    for carpeta, subcarpetas, nombres in os.walk(directorio):
        for nombre in nombres:
            ruta = os.path.join(carpeta, nombre)
            try:
                st = os.stat(ruta)
            except OSError:
                continue
            archivos.append(Archivo(
                nombre, ruta, categoria_de(nombre), st.st_size,
                datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M')))
        if not INCLUIR_SUBCARPETAS:
            break
    return archivos


def formatear_tamano(n):
    for unidad in ("B", "KB", "MB"):
        if n < 1024:
            return f"{n:.0f} {unidad}" if unidad == "B" else f"{n:.1f} {unidad}"
        n /= 1024
    return f"{n:.1f} GB"


# ============================================================
# 3. ALGORITMOS DE ORDENAMIENTO  (comparaciones[0] cuenta las comparaciones)
# ============================================================
comparaciones = [0]


def quick_sort(lista, clave):
    if len(lista) <= 1:
        return lista
    pivote = clave(lista[len(lista) // 2])
    menores, iguales, mayores = [], [], []
    for x in lista:
        comparaciones[0] += 1
        (menores if clave(x) < pivote else iguales if clave(x) == pivote else mayores).append(x)
    return quick_sort(menores, clave) + iguales + quick_sort(mayores, clave)


def merge_sort(lista, clave):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq, der = merge_sort(lista[:medio], clave), merge_sort(lista[medio:], clave)
    resultado, i, j = [], 0, 0
    while i < len(izq) and j < len(der):
        comparaciones[0] += 1
        if clave(izq[i]) <= clave(der[j]):
            resultado.append(izq[i]); i += 1
        else:
            resultado.append(der[j]); j += 1
    return resultado + izq[i:] + der[j:]


def bubble_sort(lista, clave):
    a = lista[:]
    for i in range(len(a) - 1):
        hubo_cambio = False
        for j in range(len(a) - 1 - i):
            comparaciones[0] += 1
            if clave(a[j]) > clave(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                hubo_cambio = True
        if not hubo_cambio:
            break
    return a


def insertion_sort(lista, clave):
    a = lista[:]
    for i in range(1, len(a)):
        actual, j = a[i], i - 1
        while j >= 0:
            comparaciones[0] += 1
            if clave(a[j]) > clave(actual):
                a[j + 1] = a[j]; j -= 1
            else:
                break
        a[j + 1] = actual
    return a


ALGORITMOS = {"Quick Sort": quick_sort, "Merge Sort": merge_sort,
              "Bubble Sort": bubble_sort, "Insertion Sort": insertion_sort}
CAMPOS = {
    "Nombre":      lambda a: a.nombre.lower(),
    "Tamaño":      lambda a: a.tamano,
    "Fecha":       lambda a: a.fecha,
    "Extensión":   lambda a: a.extension,
}


def ordenar(archivos, algoritmo, campo, descendente):
    comparaciones[0] = 0
    inicio = time.perf_counter()
    resultado = ALGORITMOS[algoritmo](archivos, CAMPOS[campo])
    ms = (time.perf_counter() - inicio) * 1000
    return (resultado[::-1] if descendente else resultado), ms, comparaciones[0]


# ============================================================
# 4. VISTAS (cómo se muestra cada tipo de archivo)
# ============================================================
COLOR = {"Imágenes": "#8b5cf6", "Música": "#ec4899", "Videos": "#f59e0b", "Archivos": "#3b82f6"}

CSS = """
<style>
.xd-banner{background:linear-gradient(135deg,#6366f1,#8b5cf6 55%,#ec4899);color:#fff;border-radius:18px;
  padding:22px 26px;margin-bottom:14px;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
.xd-banner h2{margin:0 0 2px;font-size:26px;color:#fff}
.xd-banner p{margin:0;opacity:.85;font-size:14px}
.xd-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.xd-chip{background:rgba(255,255,255,.2);border-radius:999px;padding:5px 14px;font-size:13px}
.xd-panel{border:1px solid rgba(128,128,128,.3);border-radius:16px;padding:14px 16px;
  background:rgba(128,128,128,.06)}
.xd-search input{border-radius:999px!important;padding:0 20px!important;font-size:15px!important;height:44px!important}
.xd-info{display:inline-block;padding:6px 16px;border-radius:999px;background:rgba(99,102,241,.16);
  font-size:13px;margin:10px 0 2px;font-family:system-ui,sans-serif}
.xd-sec{display:flex;align-items:center;gap:10px;margin:22px 0 10px;padding-left:12px;
  border-left:5px solid var(--c);font-size:18px;font-weight:600;font-family:system-ui,sans-serif}
.xd-badge{color:#fff;border-radius:999px;padding:1px 11px;font-size:12px}
.xd-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:16px;width:100%}
.xd-card{border:1px solid rgba(128,128,128,.28);border-radius:14px;overflow:hidden;
  background:rgba(128,128,128,.07);transition:transform .15s,box-shadow .15s;font-family:system-ui,sans-serif}
.xd-card:hover{transform:translateY(-5px);box-shadow:0 10px 24px rgba(0,0,0,.28)}
.xd-card img{width:100%;height:150px;object-fit:cover;display:block}
.xd-ph{height:150px;display:flex;align-items:center;justify-content:center;font-size:44px}
.xd-cap{padding:9px 11px;font-size:12px}
.xd-cap b{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:13px}
.xd-cap span{opacity:.65}
.xd-row{display:flex;align-items:center;gap:14px;padding:9px 14px;border:1px solid rgba(128,128,128,.28);
  border-radius:14px;background:rgba(128,128,128,.07);margin:3px 0;width:100%;box-sizing:border-box;
  font-family:system-ui,sans-serif;transition:background .15s}
.xd-row:hover{background:rgba(128,128,128,.15)}
.xd-ico{width:42px;height:42px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:21px}
.xd-name{font-weight:600;font-size:14px}
.xd-meta{font-size:12px;opacity:.65;font-family:system-ui,sans-serif}
.xd-ext{margin-left:auto;font-size:11px;padding:3px 10px;border-radius:8px;background:rgba(128,128,128,.22);
  text-transform:uppercase;letter-spacing:.5px}
.xd-empty{text-align:center;padding:44px 20px;border:2px dashed rgba(128,128,128,.4);border-radius:18px;
  opacity:.8;font-size:15px;line-height:1.7;font-family:system-ui,sans-serif}
.xd-now{border-radius:14px;padding:10px 16px;background:rgba(236,72,153,.14);margin:10px 0 4px;
  font-family:system-ui,sans-serif}
</style>
"""

_CACHE_MINIATURAS = {}


def miniatura(ruta):
    """Devuelve la foto reducida como data-URI (rápida de cargar) o None si no se puede leer."""
    if ruta not in _CACHE_MINIATURAS:
        try:
            with PILImage.open(ruta) as im:
                im = ImageOps.exif_transpose(im).convert("RGB")
                im.thumbnail((320, 320))
                buffer = io.BytesIO()
                im.save(buffer, "JPEG", quality=80)
            _CACHE_MINIATURAS[ruta] = "data:image/jpeg;base64," + base64.b64encode(buffer.getvalue()).decode()
        except Exception:
            _CACHE_MINIATURAS[ruta] = None
    return _CACHE_MINIATURAS[ruta]


def vista_imagenes(grupo):
    tarjetas = []
    for a in grupo:
        src = miniatura(a.ruta)
        imagen = f'<img src="{src}" alt="">' if src else f'<div class="xd-ph">{ICONO["Imágenes"]}</div>'
        nombre = html.escape(a.nombre)
        tarjetas.append(
            f'<div class="xd-card">{imagen}<div class="xd-cap"><b title="{nombre}">{nombre}</b>'
            f'<span>{formatear_tamano(a.tamano)} · {a.fecha[:10]}</span></div></div>')
    return widgets.HTML(f'<div class="xd-grid">{"".join(tarjetas)}</div>',
                        layout=widgets.Layout(width="100%"))


def fila_archivo(a, al_reproducir=None):
    color = COLOR[a.categoria]
    contenido = widgets.HTML(
        f'<div class="xd-row"><div class="xd-ico" style="background:{color}26">{a.icono}</div>'
        f'<div><div class="xd-name">{html.escape(a.nombre)}</div>'
        f'<div class="xd-meta">{formatear_tamano(a.tamano)} · {a.fecha}</div></div>'
        f'<span class="xd-ext">{a.extension.strip(".") or "archivo"}</span></div>',
        layout=widgets.Layout(width="100%"))
    if not al_reproducir:
        return contenido
    boton = widgets.Button(description="▶", button_style="success", tooltip=f"Reproducir {a.nombre}",
                           layout=widgets.Layout(width="48px", height="48px"))
    boton.on_click(lambda _, arch=a: al_reproducir(arch))
    return widgets.HBox([boton, contenido], layout=widgets.Layout(align_items="center", width="100%"))


def mostrar(lista, al_reproducir, ver_todos=False):
    for categoria in CATEGORIAS:
        grupo = [a for a in lista if a.categoria == categoria]
        if not grupo:
            continue
        visibles = grupo if ver_todos else grupo[:MAX_POR_CATEGORIA]
        color = COLOR[categoria]
        display(widgets.HTML(
            f'<div class="xd-sec" style="--c:{color}">{ICONO[categoria]} {categoria} '
            f'<span class="xd-badge" style="background:{color}">{len(grupo)}</span></div>'))
        if categoria == "Imágenes":
            display(vista_imagenes(visibles))
        else:
            reproducible = al_reproducir if categoria in ("Música", "Videos") else None
            display(widgets.VBox([fila_archivo(a, reproducible) for a in visibles]))
        if len(grupo) > len(visibles):
            display(widgets.HTML(
                f'<div class="xd-meta">… y {len(grupo) - len(visibles)} más. '
                f'Activa «Mostrar todos» o usa el buscador.</div>'))


# ============================================================
# 5. INTERFAZ
# ============================================================
def construir_interfaz(archivos):
    display(HTML(CSS))

    conteo = {c: sum(a.categoria == c for a in archivos) for c in CATEGORIAS}
    chips = "".join(f'<span class="xd-chip">{ICONO[c]} {conteo[c]} {c.lower()}</span>' for c in CATEGORIAS)
    banner = widgets.HTML(
        f'<div class="xd-banner"><h2>📁 {html.escape(NOMBRE_CARPETA)}</h2>'
        f'<p>Explorador de archivos de Google Drive</p>'
        f'<div class="xd-chips">{chips}'
        f'<span class="xd-chip">💾 {formatear_tamano(sum(a.tamano for a in archivos))}</span></div></div>')

    caja = widgets.Text(placeholder="🔍  Buscar por nombre...", layout=widgets.Layout(width="100%"))
    caja.add_class("xd-search")
    filtro = widgets.ToggleButtons(
        options=[("✨ Todos", "Todos")] + [(f"{ICONO[c]} {c}", c) for c in CATEGORIAS],
        style={"button_width": "130px"}, button_style="info")
    algoritmo = widgets.Dropdown(options=list(ALGORITMOS), description="Algoritmo:",
                                 layout=widgets.Layout(width="230px"))
    campo = widgets.Dropdown(options=list(CAMPOS), description="Ordenar por:",
                             layout=widgets.Layout(width="230px"))
    descendente = widgets.Checkbox(description="Descendente", indent=False, layout=widgets.Layout(width="130px"))
    ver_todos = widgets.Checkbox(description="Mostrar todos", indent=False, layout=widgets.Layout(width="140px"))
    info = widgets.HTML()
    reproductor = widgets.Output()
    resultados = widgets.Output()

    def reproducir(a):
        with reproductor:
            clear_output(wait=True)
            display(widgets.HTML(f'<div class="xd-now">▶ Reproduciendo: <b>{html.escape(a.nombre)}</b></div>'))
            if a.categoria == "Música":
                display(Audio(filename=a.ruta, autoplay=True))
            elif a.tamano > 150 * 1024 * 1024:
                display(widgets.HTML('<div class="xd-meta">⚠️ El video pesa demasiado para reproducirlo '
                                     'aquí. Ábrelo desde Drive.</div>'))
            else:
                display(Video(a.ruta, embed=True, width=480))

    def refrescar(_=None):
        texto = caja.value.strip().lower()
        lista = [a for a in archivos
                 if texto in a.nombre.lower() and filtro.value in ("Todos", a.categoria)]
        lista, ms, comps = ordenar(lista, algoritmo.value, campo.value, descendente.value)
        info.value = (f'<span class="xd-info">⏱️ <b>{algoritmo.value}</b> · {ms:.3f} ms · '
                      f'{comps} comparaciones · <b>{len(lista)}</b> archivo(s)</span>')
        with resultados:
            clear_output(wait=True)
            if lista:
                mostrar(lista, reproducir, ver_todos.value)
            else:
                display(widgets.HTML('<div class="xd-empty">🔎<br><b>Sin resultados</b><br>'
                                     'Prueba con otro nombre o cambia el filtro.</div>'))

    for w in (caja, filtro, algoritmo, campo, descendente, ver_todos):
        w.observe(refrescar, names="value")

    panel = widgets.VBox([
        caja,
        filtro,
        widgets.HBox([algoritmo, campo, descendente, ver_todos],
                     layout=widgets.Layout(flex_flow="row wrap", align_items="center")),
    ], layout=widgets.Layout(width="100%"))
    panel.add_class("xd-panel")

    display(widgets.VBox([banner, panel, info, reproductor, resultados], layout=widgets.Layout(width="100%")))
    refrescar()


# ============================================================
# 6. EJECUCIÓN PRINCIPAL
# ============================================================
def main():
    print("🔐 Conectando con Google Drive...")
    drive.mount('/content/drive')

    if not os.path.isdir(DIRECTORIO):
        print(f"❌ No se encontró la carpeta '{NOMBRE_CARPETA}' en tu Drive.")
        raiz = '/content/drive/MyDrive'
        carpetas = sorted(n for n in os.listdir(raiz) if os.path.isdir(os.path.join(raiz, n)))
        print("📂 Carpetas disponibles en MyDrive:", ", ".join(carpetas) or "(ninguna)")
        return

    archivos = escanear(DIRECTORIO)
    print(f"✅ {len(archivos)} archivos encontrados en '{NOMBRE_CARPETA}'.")
    if archivos:
        construir_interfaz(archivos)


if __name__ == "__main__":
    main()
