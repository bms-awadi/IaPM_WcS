# Fusionnner +ieurs fichiers notebook

Voici un script python qui permet de fusionner des fichiers notebook :

```python
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
```

## Instructions d'utilisation

- Installez d'abord le package **nbformat** avec `pip install nbformat`
- Enregistrez ce script dans un fichier Python, par exemple `merge_notebooks.py`.
- Pour exécuter le script, utilisez la ligne de commande comme ceci :

```bash
python merge_notebooks.py notebook1.ipynb notebook2.ipynb ... -o output.ipynb
```

- `notebook1.ipynb`, `notebook2.ipynb`, etc. : Les fichiers notebooks que vous souhaitez fusionner (vous pouvez en fournir autant que vous le souhaitez).
- `-o output.ipynb` : Le nom du fichier de sortie où les notebooks fusionnés seront enregistrés.
