
#Importamos librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import matplotlib.patches as mpatches

#Análisis exploratorio y visualización:
redes_soc = pd.read_csv('redes_sociales.csv')
print("\nPerfiles:\n", redes_soc)


#Promedio de seguidores de los 10 primeros perfiles
print("\nPrimeros 10 perfiles según número de seguidores\n", redes_soc["Número de Seguidores"].head(10))

prom_seg = redes_soc["Número de Seguidores"].head(10)
print("\nPromedio: ", prom_seg.mean())


#Gráfico de dispersión entre seguidores y publicaciones
x = redes_soc['Cantidad de Publicaciones']
y = redes_soc['Número de Seguidores']

fig, ax = plt.subplots(figsize=(15,15))
ax.scatter(x, y, marker='^', color='forestgreen', edgecolor= "k", s = 200)
plt.title("\nAnálisis de seguidores en función de sus publicaciones\n", fontsize = 16, fontweight = 'bold')
plt.xlabel("\nPublicaciones\n")
plt.ylabel("\nSeguidores\n")
plt.grid()
plt.show()


#Orden descendente de los seguidores
redes_soc = redes_soc.sort_values('Número de Seguidores', ascending=False)
print("\nNúmero de seguidores\n", redes_soc.head(10))


#Perfiles con más interacciones
redes_soc = redes_soc.sort_values('Cantidad de Interacciones', ascending=False)
print("\nPerfiles con más interacciones\n", redes_soc.head(10))

perfil_mas_interactivo = redes_soc["Cantidad de Interacciones"].argmax()
print("\nPerfil más interactivo:\n")
print("\n", redes_soc.loc[29], "\n")


#Perfiles con más de 100 publicaciones y menos de 3000 seguidores
print("\nPerfiles con más de 100 publicaciones y menos de 3000 seguidores\n", redes_soc[(redes_soc['Cantidad de Publicaciones'] > 100) & 
                                                                                        (redes_soc['Número de Seguidores'] < 3000)], "\n")


#Perfiles con más de 10 publicaciones y menos de 1000 seguidores
print("\nPerfiles con más de 10 publicaciones y menos de 1000 seguidores\n", redes_soc[(redes_soc['Cantidad de Publicaciones'] > 10) & 
                                                                                       (redes_soc['Número de Seguidores'] < 1000)], "\n")