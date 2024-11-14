import nbformat
import argparse

# Configuration de argparse pour prendre des arguments de ligne de commande
parser = argparse.ArgumentParser(description="Fusionner plusieurs notebooks Jupyter en un seul fichier.")
parser.add_argument(
    'notebooks',
    metavar='N',
    type=str,
    nargs='+',
    help='Liste des fichiers notebook à fusionner'
)
parser.add_argument(
    '-o', '--output',
    type=str,
    required=True,
    help='Nom du fichier de sortie pour le notebook fusionné'
)

args = parser.parse_args()

# Création d'un nouveau notebook
merged_notebook = nbformat.v4.new_notebook()

# Parcourir tous les fichiers notebooks fournis
for file in args.notebooks:
    with open(file, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
        merged_notebook.cells.extend(notebook.cells)

# Écriture du fichier de sortie
with open(args.output, 'w', encoding='utf-8') as f:
    nbformat.write(merged_notebook, f)

print(f"Fichiers fusionnés dans {args.output}")
