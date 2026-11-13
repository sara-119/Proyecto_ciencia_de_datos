# Proyecto Ciencia de Datos

## Integrantes
- Sara (Integrante A)
- Tomás (Integrante B)

## Fuente de los datos
El conjunto de datos utilizado en este proyecto fue obtenido de Kaggle:

[Spotify 1 Million Tracks](https://www.kaggle.com/datasets/amitanshjoshi/spotify-1million-tracks)

Para el desarrollo del proyecto se seleccionaron los primeros 1.500 registros del archivo original.
## Descripción del conjunto de datos

El conjunto de datos fue obtenido de Kaggle y contiene aproximadamente 1 millón de canciones de Spotify. La información fue recopilada mediante la biblioteca de Python **Spotipy**, que permite acceder a los datos musicales proporcionados por la API de Spotify.

El dataset original contiene información de canciones publicadas entre los años 2000 y 2023. Cuenta con 19 características musicales y aproximadamente:

- 61.445 artistas diferentes.
- 82 géneros musicales.
- 1 millón de canciones.

El conjunto de datos permite analizar diferentes características musicales y estudiar patrones relacionados con la popularidad de las canciones. También puede utilizarse para desarrollar modelos predictivos mediante técnicas de aprendizaje automático.

Para este proyecto se trabajó con una muestra de los primeros **1.500 registros** del archivo original, con el fin de facilitar el procesamiento y análisis de los datos.

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
- **popularity:** Nivel de popularidad de la canción.(0 a 100)
- **year:** Año de lanzamiento.
- **genre:** Género musical.
- **danceability:** Nivel de facilidad para bailar la canción.(0,0 a 1,0)
- **energy:** Nivel de energía de la canción.(0,0 a 1,0)
- **key:** Tonalidad musical.(-1 a 11)
- **loudness:** Volumen promedio de la canción en decibelios.(-60 a 0 dB)
- **mode:** Modalidad musical (mayor´1' o menor'0').
- **speechiness:** Presencia de palabras habladas en la canción.
- **acousticness:** Nivel de carácter acústico.
- **instrumentalness:** Si las pistas contienen voces(0.0 a 1.0).
- **liveness:** indica la presencia de audiencia en la grabación.
- **valence:** Positividad musical (0.0 a 1.0).
- **tempo:** Velocidad de la canción en pulsaciones por minuto (BPM).
- **duration_ms:** Duración de la canción en milisegundos.
- **time_signature:** compás musical estimado.(3 a 7)
- **duration_min:** Duración de la canción convertida a minutos.
- **es_popular:** Indica si la popularidad de la canción es igual o superior al promedio.

## Organización del repositorio
- `README.md`: documentación del proyecto.
- `analisis.py`: solución final.
- `datos/`: base de datos.
- `cuadernos/`: cuadernos de exploración de cada integrante.

## Conclusiones
Pendientes.
