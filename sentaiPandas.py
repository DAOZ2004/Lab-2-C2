import pandas as pd

sentaiDatos = pd.read_csv("sentai_datos.csv")
#Resumen estadistico del dataset
print(sentaiDatos.describe())

#identificacion de los tipos de datos
print(sentaiDatos.dtypes)


# Identificar valores únicos en las eras
print(sentaiDatos['era'].value_counts())

# Promedio de episodios por era
print(sentaiDatos.groupby('era')['number_of_episode'].mean())
