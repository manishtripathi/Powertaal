import os
import shutil
from pathlib import Path

# Paden definiëren
base_dir = Path(__file__).resolve().parent
templates_dir = base_dir / 'templates'
main_dir = templates_dir / 'main'
nl_dir = templates_dir / 'nl'
en_dir = templates_dir / 'en'
de_dir = templates_dir / 'de'

# Zorg ervoor dat de doelmappen bestaan
os.makedirs(nl_dir, exist_ok=True)
os.makedirs(en_dir, exist_ok=True)
os.makedirs(de_dir, exist_ok=True)

# Bestanden die we willen kopiëren
files_to_copy = [
    'home.html',
    'about.html',
    'contact.html',
    'learn.html',
    'select_language.html',
    'type.html'
]

# Kopieer bestanden naar de Nederlandse map (originele versie)
for file in files_to_copy:
    source_file = main_dir / file
    if source_file.exists():
        print(f"Kopiëren van {file} naar nl map...")
        shutil.copy2(source_file, nl_dir)

# Kopieer bestanden naar de Engelse map
for file in files_to_copy:
    source_file = main_dir / file
    if source_file.exists():
        print(f"Kopiëren van {file} naar en map...")
        shutil.copy2(source_file, en_dir)

# Kopieer bestanden naar de Duitse map
for file in files_to_copy:
    source_file = main_dir / file
    if source_file.exists():
        print(f"Kopiëren van {file} naar de map...")
        shutil.copy2(source_file, de_dir)

print("Alle bestanden zijn gekopieerd!") 