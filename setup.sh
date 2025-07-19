#!/bin/bash

echo "🛠️ Creando entorno virtual..."
python3 -m venv .venv

echo "📦 Activando entorno virtual..."
source .venv/bin/activate

echo "📥 Instalando dependencias necesarias..."
pip install --upgrade pip
pip install black flake8 mypy pytest requests

echo "✅ Entorno virtual configurado y dependencias instaladas."
