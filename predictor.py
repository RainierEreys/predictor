import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout


"""SE LEE EL ARCHIVO EXCEL USANDO PANDAS (ARCHIVO EXCEL)--->EL CAMPO 'FECHA' SERÁ EL INDICE DE LA TABLA Y POR ESO SE PARSEA"""
dataset = pd.read_csv('AMZN.csv', sep=";", index_col='date', parse_dates=['date'], dayfirst=True)
dataset = dataset.sort_index()

""" 
AQUI SE SELECCIONA EL CONJUNTO DE ENTRENAMIENTO Y EL CONJUNTO DE PRUEBA 
NOS BASAREMOS EN EL PRECIO MAS ALTO DE LA ACCIÓN (COLUMNA 'High')
"""
trainingSet = dataset['2022':].iloc[:, [False, False, True, False, False, False]]
testSet = dataset[:'2023'].iloc[:, [False, False, True, False, False, False]]

"""NORMALIZACION DEL SET DE ENTRENAMIENTO (COLOCAR UN RANGO BINARIO 0 Y 1)"""
sc = MinMaxScaler(feature_range=(0,1))
trainingSetScaled = sc.fit_transform(trainingSet)

"""SE ENTRENA LA RED PROPORCIONANDO 100 DATOS DE ENTRADA Y 1 DE SALIDA EN CADA ITERACION"""
timeSteps = 100

"""lista de listas"""
xTrain = []

"""valores de salida"""
yTrain = []

for i in range(0, len(trainingSetScaled)-timeSteps):
    xTrain.append(trainingSetScaled[i:i+timeSteps, 0])
    yTrain.append(trainingSetScaled[i+timeSteps,0])
    
"""CONVERTIR ARRAYS EN NUMPY ARRAYS"""
xTrain, yTrain = np.array(xTrain), np.array(yTrain)

"""xTrain de dos dimensiones a tres dimensiones para que pueda ser tratado por keras"""
xTrain = np.reshape(xTrain, (xTrain.shape[0], xTrain.shape[1], 1))

"""PARAMETROS A PROPORCIONAR A KERAS"""
dim_entrada = (xTrain.shape[1], 1)
dim_salida = 1
"""numero de neuronas"""
na = 50

"""ININCIALIZAR EL MODELO"""
regresor = Sequential()

"""donde 'units' = neuronas de la capa | 'return_sequences' = para verificar si hay mas capas | 'input_shape' = dimension de entrada |
    Dropout(%) = Numero de neuronas que queremos ignorar en la capa de regularización"""

"""capa 1"""
regresor.add(LSTM(units=na, input_shape=dim_entrada))

"""capa output"""
regresor.add(Dense(units=dim_salida))

regresor.compile(optimizer='rmsprop', loss='mse')

"""ENCAJAR RED NEURONAL EN SET DE ENTRENAMIENTO"""

regresor.fit(xTrain,yTrain, epochs=20, batch_size=32)

"""NORMALIZAR EL CONJUNTO DE TEST Y REALIZAMOS LAS MISMAS OPERACIONES QUE ANTERIORMENTE"""
auxTest = sc.transform(testSet.values)
xTest = []

for i in range(0, len(auxTest)-timeSteps):
    xTest.append(auxTest[i:i+timeSteps,0])
    
xTest = np.array(xTest)
xTest = np.reshape(xTest, (xTest.shape[0], xTest.shape[1], 1))

"""REALIZAMOS LA PREDICCIÓN"""
prediccion = regresor.predict(xTest)

"""DESESCALAMOS LA PREDICCION PARA QUE SE ENCUENTRE ENTRE VALORES NORMALES"""
prediccion = sc.inverse_transform(prediccion)


""" FUNCION PARA GRAFICAR LOS RESULTADOS DE LAS PREDICCIONES """
def visualizar(real, prediccion):
    plt.plot(real[0:len(prediccion)], color='red', label='Precio maximo real de la accion')
    plt.plot(prediccion, color='blue', label='Prediccion de la accion')
    plt.xlabel('Tiempo')
    plt.ylabel('Precio de la accion')
    plt.legend()
    plt.show()

""" LLAMANDO A LA FUNCION CON LOS VALORES REALES DEL CONJUNTO DE PRUEBA Y LAS PREDICCIONES REALIZADAS """
visualizar(testSet.values,prediccion)
