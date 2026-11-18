# %% [markdown]
# # Proyecto Ciencia de Datos
# Integrantes: Sara, Tomás

# %%
# Librerías 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración para gráficos fondo blanco
sns.set_theme(style="whitegrid")

# Carga única de los primeros 1500 registros del dataset
df = pd.read_csv("datos/Base_datos_spotify.csv", nrows=1500, engine="python", on_bad_lines="warn")

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
# **Tratamiento aplicado:** Dado que el porcentaje de registros nulos es mínimo en comparación con los 1,500 registros totales, la estrategia recomendada y justificada para estos pocos casos es la eliminación de dichas filas vacías (`dropna()`), ya que eliminarlas no afectará de forma negativa el tamaño de la muestra ni sesgará los resultados de los siguientes ítems.

# %%
# Visualización de datos faltantes con mapa de calor
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title("Mapa de calor de valores faltantes en el conjunto de datos reducido")
plt.xlabel("Variables del Dataset")
plt.ylabel("Registros (Filas)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Limpieza y verificación de filas nulas puntuales
df_limpio = df.dropna()
print("Nulos después de limpiar:", df_limpio.isnull().sum().sum())
print("Nuevo tamaño del DataFrame tras eliminar nulos:", df_limpio.shape)

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
# %%
# 1. Identificación y tratamiento de registros duplicados
duplicados_totales = df.duplicated().sum()
print(f"Cantidad de registros duplicados exactos encontrados: {duplicados_totales}")

# Si existen duplicados, los eliminamos del DataFrame
if duplicados_totales > 0:
    df = df.drop_duplicates()
    print("Se han eliminado los registros duplicados.")
else:
    print("El conjunto de datos no presenta registros duplicados exactos.")

# 2. Identificación y tratamiento de valores inconsistentes en texto
print("\nGéneros antes de limpiar:", df['genre'].unique() if 'genre' in df.columns else "N/A")

# Limpiar espacios en blanco al inicio o final en todas las columnas de texto
cols_texto = df.select_dtypes(include=['object']).columns
for col in cols_texto:
    df[col] = df[col].astype(str).str.strip()

# Estandarizar la variable 'genre' a minúsculas para evitar discrepancias
if 'genre' in df.columns:
    df['genre'] = df['genre'].str.lower()

# Limpiar caracteres especiales sobrantes en columnas (ej. 'time_signature;;;')
if 'time_signature;;;' in df.columns:
    df['time_signature'] = df['time_signature;;;'].str.replace(';', '').str.strip()
    df = df.drop(columns=['time_signature;;;'])

# 3. Verificación final tras la limpieza
print("\nGéneros después de estandarizar:", df['genre'].unique() if 'genre' in df.columns else "N/A")
print(f"Forma final del DataFrame tras el Ítem 4: {df.shape}")

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
# %%
# 1. Canciones con alta energía y alta bailabilidad (energy > 0.8 y danceability > 0.7)
alta_energia_baile = df[(df['energy'] > 0.8) & (df['danceability'] > 0.7)]
print(f"1. Canciones de alta energía y bailable: {len(alta_energia_baile)} registros encontrados.")
print(alta_energia_baile[['artist_name', 'track_name', 'energy', 'danceability']].head(3))

# 2. Canciones con un nivel de acústica muy elevado (acousticness > 0.9)
alta_acustica = df[df['acousticness'] > 0.9]
print(f"\n2. Canciones altamente acústicas: {len(alta_acustica)} registros encontrados.")
print(alta_acustica[['artist_name', 'track_name', 'acousticness']].head(3))

# 3. Canciones de larga duración (duración mayor a 300,000 ms / 5 minutos)
canciones_largas = df[df['duration_ms'] > 300000]
print(f"\n3. Canciones con duración mayor a 5 minutos: {len(canciones_largas)} registros encontrados.")
print(canciones_largas[['artist_name', 'track_name', 'duration_ms']].head(3))

# 4. Canciones con un tempo muy rápido (tempo > 160 BPM)
tempo_rapido = df[df['tempo'] > 160]
print(f"\n4. Canciones con tempo superior a 160 BPM: {len(tempo_rapido)} registros encontrados.")
print(tempo_rapido[['artist_name', 'track_name', 'tempo']].head(3))

# 5. Filtrado por género específico
if 'genre' in df.columns:
    genero_afrobeat = df[df['genre'] == 'afrobeat']
    print(f"\n5. Canciones del género afrobeat: {len(genero_afrobeat)} registros encontrados.")
    print(genero_afrobeat[['artist_name', 'track_name', 'genre']].head(3))

# %% [markdown]
# **Conclusión del Ítem 6:**
# Los filtros aplicados mediante condiciones lógicas en `pandas` permiten segmentar eficazmente el conjunto de datos para identificar subconjuntos clave. Esto demuestra que características como el tempo, la energía y la acústica varían de manera independiente, facilitando un análisis detallado de los perfiles musicales presentes en la muestra.

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
# Generamos cinco (5) gráficos clave para analizar la distribución y relación entre las variables del conjunto de datos.

# %%
# 1. Gráfico 1: Histograma de la distribución de la energía (energy)
plt.figure(figsize=(8, 4))
sns.histplot(df['energy'], bins=30, kde=True, color='royalblue')
plt.title("Distribución de la Energía en las Pistas")
plt.xlabel("Nivel de Energía")
plt.ylabel("Frecuencia")
plt.show()

# 2. Gráfico 2: Diagrama de dispersión entre Tempo y Bailabilidad (danceability)
plt.figure(figsize=(8, 4))
sns.scatterplot(x='tempo', y='danceability', data=df, alpha=0.6, color='darkorange')
plt.title("Relación entre Tempo y Bailabilidad")
plt.xlabel("Tempo (BPM)")
plt.ylabel("Bailabilidad")
plt.show()

# 3. Gráfico 3: Gráfico de barras de la cantidad de canciones por género musical
plt.figure(figsize=(8, 4))
sns.countplot(x='genre', data=df, palette='viridis', hue='genre', legend=False)
plt.title("Cantidad de Canciones por Género Musical")
plt.xlabel("Género")
plt.ylabel("Cantidad")
plt.show()

# 4. Gráfico 4: Diagrama de caja (Boxplot) de la popularidad por género
plt.figure(figsize=(8, 4))
sns.boxplot(x='genre', y='popularity', data=df, palette='Set2', hue='genre', legend=False)
plt.title("Distribución de la Popularidad según el Género")
plt.xlabel("Género")
plt.ylabel("Popularidad")
plt.show()

# 5. Gráfico 5: Mapa de correlación entre variables numéricas principales
plt.figure(figsize=(8, 6))
numeric_cols = ['popularity', 'danceability', 'energy', 'acousticness', 'tempo', 'valence']
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlación entre Variables Numéricas")
plt.show()

# %% [markdown]
# **Conclusiones del Ítem 8:**
# * **Gráfico 1 (Distribución de la energía):** El histograma muestra una concentración heterogénea en los niveles de energía, permitiendo diferenciar temas relajados de producciones altamente enérgicas.
# * **Gráfico 2 (Tempo vs Bailabilidad):** La dispersión expone que la percepción rítmica bailable no depende de una velocidad de tempo extrema, sino de la estructura global.
# * **Gráfico 3 (Canciones por género):** Revela claramente el peso cuantitativo y la distribución de los registros entre los géneros de la muestra.
# * **Gráfico 4 (Popularidad por género):** Facilita la identificación de diferencias notables en la aceptación comercial entre las categorías evaluadas.
# * **Gráfico 5 (Matriz de correlación):** Ayuda a identificar asociaciones directas o inversas importantes entre las variables numéricas continuas y discretas.

# %% [markdown]
# ## 9. Conclusiones finales (Integrante A)
