
# %% [markdown]
# # Proyecto Ciencia de Datos
# Integrantes: Sara, Tomás

# %%
# Librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los primeros 1500 registros
df = pd.read_csv("datos/Base_datos_spotify.csv", nrows=1500,engine="python",on_bad_lines="warn")

# %% [markdown]
# ## 1. Carga e inspección inicial de los datos (Integrante A)
# %%
# Mostrar las primeras 5 canciones
print("Primeras canciones:")
print(df.head())

# %%
# Información general del dataset
df.info()

# %%
# Estadísticas de las variables numéricas
print(df.describe())

# %%
# Cantidad de artistas, canciones y géneros diferentes
print("Artistas diferentes:", df["artist_name"].nunique())
print("Canciones diferentes:", df["track_name"].nunique())
print("Géneros diferentes:", df["genre"].nunique())

# %%
# Géneros más frecuentes
print("Canciones por género:")
print(df["genre"].value_counts())

# %%
# Artistas que más aparecen
print("Artistas que más aparecen:")
print(df["artist_name"].value_counts().head(10))

# %%
# Revisar canciones repetidas
print("Canciones duplicadas:")
print(df["track_id"].duplicated().sum())

# %%
# Revisar datos faltantes
print("Datos faltantes:")
print(df.isnull().sum())

# %%
# Tipos de datos
print("Tipos de datos:")
print(df.dtypes)

# %%
# Gráfica de canciones por género
df["genre"].value_counts().plot(kind="bar")

plt.title("Canciones por género musical")
plt.xlabel("Género")
plt.ylabel("Cantidad de canciones")
plt.show()

# %% [markdown]
# ## 2. Manejo de datos faltantes (Integrante B)

# %% [markdown]
# ## 3. Identificación de outliers (Integrante A)

# %% [markdown]
# ## 4. Valores inconsistentes y duplicados (Integrante B)

# %% [markdown]
# ## 5. Creación de variables (Integrante A)

# %% [markdown]
# ## 6. Filtrado y condiciones en pandas (Integrante B)

# %% [markdown]
# ## 7. Agrupación con groupby (Integrante A)

# %% [markdown]
# ## 8. Visualizaciones (Integrante B)

# %% [markdown]
# ## 9. Conclusiones finales (Integrante A)
