# Proyecto Ciencia de Datos

## Integrantes
- Sara (Integrante A)
- Tomás (Integrante B)

## Fuente de los datos
El conjunto de datos utilizado en este proyecto fue obtenido de Kaggle:

[Spotify 1 Million Tracks](https://www.kaggle.com/datasets/amitanshjoshi/spotify-1million-tracks)

Para el desarrollo del proyecto se seleccionaron los primeros 1.500 registros del archivo original.

## Estructura de los datos
El conjunto de datos utilizado contiene 1.500 registros y 20 variables originales.

La información corresponde a canciones de Spotify e incluye datos sobre artistas, nombres de canciones, géneros musicales, popularidad y características musicales como duración, energía, ritmo y acústica.

Se identificaron los siguientes tipos de variables:
- **Categóricas:** artista, nombre de la canción y género musical.
- **Numéricas continuas:** danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo y duration_ms.
- **Numéricas discretas:** popularity, year, key, mode y time_signature.

Durante el análisis también se crearon dos variables nuevas: `duration_min` y `es_popular`.

## Diccionario de datos
### Diccionario de datos

- **Unnamed: 0:** Índice original del registro.
- **artist_name:** Nombre del artista.
- **track_name:** Nombre de la canción.
- **track_id:** Identificador único de la canción.
- **popularity:** Nivel de popularidad de la canción.
- **year:** Año de lanzamiento.
- **genre:** Género musical.
- **danceability:** Nivel de facilidad para bailar la canción.
- **energy:** Nivel de energía de la canción.
- **key:** Tonalidad musical.
- **loudness:** Volumen promedio de la canción en decibelios.
- **mode:** Modalidad musical (mayor o menor).
- **speechiness:** Presencia de palabras habladas en la canción.
- **acousticness:** Nivel de carácter acústico.
- **instrumentalness:** Probabilidad de que la canción sea instrumental.
- **liveness:** Presencia de características de una grabación en vivo.
- **valence:** Positividad o alegría transmitida por la canción.
- **tempo:** Velocidad de la canción en pulsaciones por minuto (BPM).
- **duration_ms:** Duración de la canción en milisegundos.
- **time_signature:** Compás musical.
- **duration_min:** Duración de la canción convertida a minutos.
- **es_popular:** Indica si la popularidad de la canción es igual o superior al promedio.

## Organización del repositorio
- `README.md`: documentación del proyecto.
- `analisis.py`: solución final.
- `datos/`: base de datos.
- `cuadernos/`: cuadernos de exploración de cada integrante.

## Conclusiones
Pendientes.
