### Introduction à Bokeh

**Bokeh** est une bibliothèque de visualisation interactive pour Python, qui permet de créer des graphiques dynamiques et interactifs. Elle est parfaite pour générer des visualisations web modernes et est particulièrement utile pour les scientifiques des données et les développeurs qui souhaitent des graphiques interactifs.

---

### Sources de Données : `ColumnDataSource`

**`ColumnDataSource`** est un objet central de Bokeh utilisé pour gérer les données des graphiques. Cet objet peut être créé à partir de dictionnaires Python, de tableaux NumPy, ou de DataFrames Pandas.

- **Exemple de création avec un dictionnaire** :
  ```python
  from bokeh.models import ColumnDataSource

  data = {
      'x': [1, 2, 3, 4, 5],
      'y': [3, 7, 8, 5, 1]
  }
  source = ColumnDataSource(data=data)
  ```
- **Exemple de création avec un DataFrame Pandas** :
  ```python
  import pandas as pd
  from bokeh.models import ColumnDataSource

  df = pd.DataFrame({
      'x': [1, 2, 3, 4, 5],
      'y': [3, 7, 8, 5, 1]
  })
  source = ColumnDataSource(df)
  ```

Vous pouvez utiliser `ColumnDataSource` pour partager des données entre différents éléments d'un graphique.

---

### Création de Graphiques avec Bokeh

**Créer des graphiques** est simple en utilisant des méthodes de Bokeh comme `p.circle`, `p.line`, etc.

- **Exemple de graphique en utilisant `ColumnDataSource`** :
  ```python
  from bokeh.plotting import figure, show
  from bokeh.io import output_notebook

  output_notebook()

  # Créer une figure
  p = figure(width=400, height=400, title="Exemple de graphique Bokeh")

  # Ajouter des cercles avec ColumnDataSource
  p.circle('x', 'y', size=15, color="blue", source=source)

  # Afficher le graphique
  show(p)
  ```

---

### Formattage des Étiquettes de Ticks

**Les étiquettes des ticks** peuvent être formatées pour rendre les graphiques plus lisibles.

- **Exemple d'utilisation de `DatetimeTickFormatter`** :
  ```python
  from math import pi
  from bokeh.plotting import figure, show
  from bokeh.models import DatetimeTickFormatter
  from bokeh.sampledata.glucose import data as glucose_data

  # Sélectionner un sous-ensemble des données
  week = glucose_data.loc['2010-10-01':'2010-10-08']

  # Créer un graphique avec des dates
  p = figure(x_axis_type="datetime", title="Données de Glucose", height=350, width=800)
  p.xaxis.formatter = DatetimeTickFormatter(days='%m/%d/%Y')
  p.xaxis.major_label_orientation = pi/3

  p.line(week.index, week.glucose)
  show(p)
  ```

- **Exemple d'utilisation de `NumeralTickFormatter`** :
  ```python
  from bokeh.plotting import figure, show
  from bokeh.models import NumeralTickFormatter

  p = figure(width=400, height=400, title="Graphique avec NumeralTickFormatter")
  p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

  # Formater les axes
  p.xaxis.formatter = NumeralTickFormatter(format="0.0%")
  p.yaxis.formatter = NumeralTickFormatter(format="$0.00")

  show(p)
  ```

---

### Transformations

**Les transformations** permettent de modifier les données directement dans le navigateur pour des visualisations interactives.

- **Exemple de transformation avec `cumsum`** :
  ```python
  from math import pi
  import pandas as pd
  from bokeh.palettes import Category20c
  from bokeh.transform import cumsum
  from bokeh.plotting import figure, show

  data = pd.Series({
      'États-Unis': 157, 'Royaume-Uni': 93, 'Japon': 89,
      'Chine': 63, 'Allemagne': 44, 'Inde': 42
  }).reset_index(name='valeur').rename(columns={'index': 'pays'})

  data['angle'] = data['valeur'] / data['valeur'].sum() * 2 * pi
  data['color'] = Category20c[len(data)]

  p = figure(height=350, title="Diagramme Circulaire", toolbar_location=None, tools="hover")
  p.wedge(x=0, y=1, radius=0.4,
          start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
          line_color="white", fill_color='color', legend_field='pays', source=data)

  p.axis.axis_label = None
  p.axis.visible = False
  p.grid.grid_line_color = None

  show(p)
  ```

---

### Colormapping avec Bokeh

**Le colormapping** peut être appliqué aux données pour une meilleure visualisation.

- **Exemple d'utilisation de `linear_cmap`** :
  ```python
  import numpy as np
  from bokeh.plotting import figure, show
  from bokeh.transform import linear_cmap

  N = 4000
  data = dict(x=np.random.random(size=N) * 100,
              y=np.random.random(size=N) * 100,
              r=np.random.random(size=N) * 1.5)

  p = figure()
  p.circle('x', 'y', radius='r', source=data, fill_alpha=0.6,
           color=linear_cmap('x', 'Viridis256', 0, 100))

  show(p)
  ```

- **Exemple avec `factor_cmap` pour les catégories** :
  ```python
  from bokeh.plotting import figure, show
  from bokeh.models import ColumnDataSource
  from bokeh.transform import factor_cmap
  from bokeh.palettes import Category10
  from bokeh.sampledata.penguins import data

  data = data.dropna(subset=['species', 'flipper_length_mm', 'body_mass_g'])
  source = ColumnDataSource(data)
  species_list = data['species'].unique()

  p = figure(width=600, height=400, title="Nuage de Points des Pingouins")
  p.circle('flipper_length_mm', 'body_mass_g', size=10, source=source,
           color=factor_cmap('species', palette=Category10[len(species_list)], factors=species_list))

  show(p)
  ```

---

### Personnalisation des Axes et de la Grille

**Les axes et la grille** peuvent être personnalisés pour améliorer l'apparence des graphiques.

- **Exemple de personnalisation des axes** :
  ```python
  from bokeh.plotting import figure, show

  p = figure(width=500, height=400, title="Personnalisation des Axes")
  p.line([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], line_width=2)

  p.xaxis.axis_label = "Température"
  p.yaxis.axis_label = "Pression"
  p.axis.major_label_text_color = "orange"
  p.axis.minor_tick_line_color = "gray"

  show(p)
  ```

- **Exemple de personnalisation de la grille** :
  ```python
  from bokeh.plotting import figure, show

  p = figure(width=400, height=400, title="Personnalisation de la Grille")
  p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

  p.xgrid.grid_line_color = None  # Supprimer les lignes de la grille verticale
  p.ygrid.grid_line_dash = [6, 4]  # Lignes de la grille horizontale en pointillé

  show(p)
  ```

---

### Conclusion

**Bokeh** est un outil puissant pour la visualisation interactive. Avec `ColumnDataSource`, des transformations, et la personnalisation des axes et de la grille, vous pouvez créer des visualisations dynamiques et intuitives. Pour plus d'informations, consultez la https://bokeh.org/.