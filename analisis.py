
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
# %%
# Revisar valores atípicos en la duración
Q1 = df["duration_ms"].quantile(0.25)
Q3 = df["duration_ms"].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_duracion = df[(df["duration_ms"] < limite_inferior) |
                       (df["duration_ms"] > limite_superior)]

print("Outliers en duración:", len(outliers_duracion))

# %%
# Revisar valores atípicos en la popularidad
Q1 = df["popularity"].quantile(0.25)
Q3 = df["popularity"].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_popularidad = df[(df["popularity"] < limite_inferior) |
                          (df["popularity"] > limite_superior)]

print("Outliers en popularidad:", len(outliers_popularidad))

# %%
# Mostrar las gráficas
plt.boxplot(df["duration_ms"])
plt.title("Outliers en duración")
plt.show()

plt.boxplot(df["popularity"])
plt.title("Outliers en popularidad")
plt.show()

# %% [markdown]
# Se encontraron 107 valores atípicos en la duración
# y 36 en la popularidad. Estos valores se identificaron,
# pero no se eliminaron del dataset.


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
