from pathlib import Path
import shutil

CARPETA = Path.home() / "Downloads"
DESTINOS = {
    ".pdf": CARPETA / "PDFs",
    ".jpg": CARPETA / "Imágenes",
    ".png": CARPETA / "Imágenes",
    ".zip": CARPETA / "Comprimidos"
}

for archivo in CARPETA.iterdir():
    destino = DESTINOS.get(archivo.suffix)
    if destino:
        destino.mkdir(exist_ok=True)
        shutil.move(str(archivo), str(destino / archivo.name))
