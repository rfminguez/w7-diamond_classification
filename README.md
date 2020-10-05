# Proyecto Clasificacion de Diamantes.

Este es el proyecto de la semana 7 del bootcamp de IronHack.

Consiste en analizar un dataset de datos de diamantes y hacer una predicción del precio con algoritmos de Machine Learning. Tras lo que hay que generar un fichero CSV que se debe mandar a la competición de Kaggle creada para el proyecto.

Los métodos de transformación  que he probado son:
- `label encoder` para los datos categóricos.
- `get\_dummies()` también para los datos categóricos. Al no darme mejores resultados en la predicción he prescindido del mismo.
- `Normalizer()` para normalizar los datos. Ídem, he decidido no usarlo porque las predicciones no mejoraban.
- `StandardScaler()` para transformar los datos de modo que la desviación típica de cada columna sea 1 y su media sea 0.

Para aplicar estas transformaciones he utilizado una pipeline.

Los algoritmos de Machine Learning que he utilizado son:
- SVM para regresión (he probado varios kernels).
- Linear Regression.
- K-nearest neighbors.
- X Gradient Boosting.

Las métricas para evaluar las predicciones que he utilizado son:
- Root Mean Squared Error (RMSE).
- R^2.

El análisis preliminar del set de datos está en el Jupyter Notebook `01 Analisis Preliminar.ipynb`.

La limpieza y evaluación de los algoritmos está en el Jupyter Notebook `main.ipynb`.

Además de eso he separado el código en varios ficheros dentro del directorio `src`:
- `diamonds_data.py`: parseo de los ficheros de datos.
- `transform_toolbox.py`: transformaciones de datos, gestión del pipeline de transformaciones y exportación de datos a CSV para la competición.

Los datos se importan desde el directorio `input` y los csv con las predicciones se guardan en el directorio `output`. El fichero `.gitignore` está configurado para evitar que git monitorice estos ficheros.

