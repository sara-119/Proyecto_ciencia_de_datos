
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
# %%
# Crear una columna con la duración en minutos
df["duration_min"] = df["duration_ms"] / 60000

# %%
# Crear una columna para identificar canciones populares
promedio = df["popularity"].mean()
df["es_popular"] = df["popularity"] >= promedio

# %%
# Mostrar las nuevas variables
print(df[["track_name", "duration_min", "popularity", "es_popular"]].head())

# %% [markdown]
# ## 6. Filtrado y condiciones en pandas (Integrante B)

# %% [markdown]
# ## 7. Agrupación con groupby (Integrante A)
# %%
# Calcular la popularidad promedio por género
popularidad_genero = df.groupby("genre")["popularity"].mean()

print("Popularidad promedio por género:")
print(popularidad_genero)

# %%
# Contar la cantidad de canciones por género
cantidad_genero = df.groupby("genre")["track_name"].count()

print("Cantidad de canciones por género:")
print(cantidad_genero)

# %% [markdown]
# ## 8. Visualizaciones (Integrante B)


# %% [markdown]
# ## 9. Conclusiones finales (Integrante A)
#
# 1. El análisis de los 1.500 registros permitió identificar
# que la base de datos presenta una estructura adecuada para
# estudiar las características musicales. En la revisión
# inicial no se encontraron valores faltantes ni canciones
# con track_id duplicado. Sin embargo, en la revisión de Tomás
# se reportaron algunos valores nulos puntuales y se aplicaron
# procedimientos de limpieza y normalización de textos.
# También se identificaron 107 valores atípicos en la duración
# y 36 en la popularidad, los cuales se conservaron para no
# perder información relevante.
#
# 2. La comparación entre los géneros Acoustic y Afrobeat
# mostró diferencias en su representación y popularidad.
# Acoustic presentó 968 canciones y una popularidad promedio
# de 16.43, mientras que Afrobeat presentó 532 canciones y
# un promedio de 10.98. Esto indica que Acoustic tuvo mayor
# representación y popularidad promedio en la muestra inicial.
#
# 3. Los filtros permitieron identificar diferentes perfiles
# musicales. Se encontraron 57 canciones con alta energía
# y bailabilidad, 109 con alta acústica, 234 con duración
# superior a cinco minutos y 143 con tempo superior a 160 BPM.
# Estos resultados muestran la variedad de características
# musicales presentes en las canciones analizadas.
#
# 4. La creación de las variables duration_min y es_popular
# permitió ampliar el análisis de la información. La primera
# facilita interpretar la duración de las canciones en minutos,
# mientras que la segunda permite clasificarlas según su
# popularidad con respecto al promedio general.
#
# 5. Las visualizaciones complementaron los resultados
# estadísticos. El histograma permitió observar la distribución
# de la energía, el diagrama de dispersión mostró la relación
# entre tempo y bailabilidad, y los gráficos por género
# facilitaron comparar la cantidad y popularidad de las
# canciones. La matriz de correlación permitió explorar
# posibles relaciones entre las características musicales.

