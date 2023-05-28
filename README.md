# Programación Emergente PRE803

# Equipo
- Rainier Peña (V-27.475.967)
- Carlos Salinas (V-26.763.118)
- Ivan Sanchez (V-27.163.406)
- Jose Planchart (V-22.030.870)

# Predicción del precio máximo de acciones de Amazon utilizando redes neuronales LSTM
Este proyecto utiliza redes neuronales LSTM (Long Short-Term Memory) para predecir el precio máximo de las acciones de Amazon (AMZN) en base a datos históricos. Se implementa utilizando el lenguaje de programación Python y las siguientes bibliotecas:

**numpy**: para realizar operaciones numéricas eficientes en matrices.
**matplotlib**: para visualizar los resultados en forma de gráficos.
**pandas**: para leer y manipular los datos en formato CSV.
**scikit-learn**: para normalizar los datos de entrenamiento.
**keras**: una biblioteca de alto nivel para construir y entrenar redes neuronales.

## Configuración y uso

Asegurese de tener instalado: **Python 3.x**

Una vez con el proyecto clonado y abierto en un editor de codigo proceda a instalar las dependencias necesarias.
Para ello haga lo siguiente:
- Abra una terminal de comando
- Asegurese que la terminal se encuentre en el directorio del proyecto
- Ejecute el comando ```pip install -r requirements.txt``` 
- Finalizada la instalacion de dependencias, ejecute el comando ```python predictor.py```


Este es un programa que predice el valor de la bolsa de valores de las acciones de Amazon para el 2023, tomando una data de la bolsa de valores de las acciones de Amazon que contiene el registro desde el 2022

Las redes neuronales LSTM son un tipo de arquitectura de redes neuronales recurrentes que se utilizan ampliamente en el campo del machine learning para modelar y predecir datos secuenciales, como series temporales.

En este caso, se utiliza una red neuronal LSTM para aprender patrones y relaciones en los datos históricos de las acciones de Amazon, y luego se utiliza para hacer predicciones sobre el precio máximo futuro. El modelo se entrena utilizando los datos de entrenamiento y se evalúa utilizando los datos de prueba.

El objetivo principal del proyecto es utilizar técnicas de machine learning para predecir el precio máximo de las acciones de Amazon, lo cual puede ser útil para inversores y analistas financieros que buscan tomar decisiones informadas sobre la compra o venta de acciones.

El código se divide en las siguientes secciones:

1. Lectura y preparación de los datos: se lee el archivo CSV utilizando la biblioteca pandas y se realiza la ordenación y normalización de los datos de entrenamiento.
2. Construcción y entrenamiento de la red neuronal: se crea un modelo de red neuronal LSTM utilizando la biblioteca keras, y se entrena con los datos normalizados.
3. Preparación y realización de predicciones: se normalizan los datos de prueba y se realizan las predicciones utilizando el modelo entrenado. Luego, se desescalan las predicciones para obtener valores reales.
4. Visualización de resultados: se muestra un gráfico comparando los valores reales del conjunto de prueba y las predicciones realizadas.


Las redes neuronales LSTM son una herramienta poderosa para predecir precios en series temporales, como el precio de las acciones. Su capacidad para capturar patrones y relaciones complejas en los datos históricos los convierte en una opción adecuada para problemas de predicción financiera.

El uso de datos históricos y técnicas de preprocesamiento, como la normalización, es esencial para entrenar y evaluar con precisión el modelo de red neuronal LSTM. La calidad y la preparación adecuada de los datos son fundamentales para obtener predicciones confiables.

El proyecto demuestra cómo el lenguaje de programación Python y las bibliotecas especializadas, como numpy, pandas, scikit-learn y keras, pueden combinarse para implementar y entrenar redes neuronales LSTM de manera eficiente.

Los resultados obtenidos en la predicción del precio máximo de las acciones de Amazon muestran una perspectiva prometedora. Sin embargo, es importante tener en cuenta que las predicciones de precios financieros siempre conllevan cierto grado de incertidumbre, y las decisiones de inversión deben basarse en un análisis completo que incorpore varios factores adicionales.

Por otra parte, la predicción puede variar en función de los datos del archivo Excel utilizado para entrenar y evaluar el modelo. La calidad y representatividad de los datos históricos son factores clave que pueden afectar la precisión de las predicciones.

El proyecto destaca el potencial de las redes neuronales LSTM en la predicción de precios de acciones y proporciona una base sólida para futuras investigaciones y mejoras en el ámbito de las predicciones financieras. Siendo conscientes de las limitaciones inherentes a las predicciones financieras, esta implementación sirve como punto de partida para analizar y comprender mejor los patrones y tendencias del mercado de valores.
