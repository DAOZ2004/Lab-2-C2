import pandas as pd

sentaiDatos = pd.read_csv("sentai_datos.csv")
#Resumen estadistico del dataset
print(sentaiDatos.describe())

#identificacion de los tipos de datos
print(sentaiDatos.dtypes)

