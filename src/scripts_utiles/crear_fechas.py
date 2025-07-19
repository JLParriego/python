from datetime import date
from pathlib import Path

hoy = date.today().isoformat()
nueva_carpeta = Path("data") / f"carpeta_{hoy}"
nueva_carpeta.mkdir(exist_ok=True)
print(f"Creada: {nueva_carpeta}")
