import pandas as pd

sentaiDatos = pd.read_csv("sentai_datos.csv")
#Resumen estadistico del dataset
print(sentaiDatos.describe())

#identificacion de los tipos de datos
print(sentaiDatos.dtypes)


#mostrando los primeros ultimos registros del data set 
print(sentaiDatos.head())

print(sentaiDatos.tail())
# Ordenar por rating (de mayor a menor)
print(sentaiDatos.sort_values(by="rating", ascending=False).head(10))

# Ordenar por número de episodios (de menor a mayor)
print(sentaiDatos.sort_values(by="number_of_episode", ascending=True).head(10))

#Seleccionar una columna y, calcular al menos dos de las siguientes medidas:
#a. Media
#b. Mediana
#c. Desviación estándar
# nosotros escogimos hacer las tres 
print(f"Media: {sentaiDatos['rating'].mean()}")
print(f"Mediana : {sentaiDatos['rating'].median()}")
print(f"Varianza : {sentaiDatos['rating'].var()}")
print(f"Desviacion estandar : {sentaiDatos['rating'].std()}")