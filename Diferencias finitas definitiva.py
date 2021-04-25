# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:39:21 2021

@author: Ever Ortega Calderón
"""
#Se llaman las bibliotecas requeridas 
import numpy as np
import matplotlib.pyplot as plt
"""
Función Aproximacion
Recibe:
    rho=matriz de valores de difusión, tendrá ceros, menos los valores donde tenga la condición inicial
    px=corresponde a la cantidad de puntos en los que se discretiza el espacio
    pt=corresponde a la cantidad de puntos en los que se discretiza el tiempo
    separacionx=corresponde a la separación que existe en los puntos del espacio
    separaciont=corresponde a la separación que existe en los puntos del tiempo
    D= constante del problema, corresponde a 0.5
Retorna:
    rho=arreglo con los valores solución de difusión   

"""
def Aproximacion(rho, px,pt, separacionx,separaciont,D):
    for n in range(0, pt-1, 1):
        for m in range(1, px-1, 1):
            rho[m,n+1]=(D*separaciont)*((rho[m+1,n]-2*rho[m,n]+rho[m-1,n])/(separacionx**2))+rho[m,n]

    valorAprox = rho
    return valorAprox
"""
Función Grafico 
Recibe:
    No recibe nada
Retorna:
    No retorna nada, pero en ella corre el gráfico
"""
def Grafico():
#Se definen condiciones del problema y la longitud del espacio y de tiempo
    D=0.5
    A=2.0
    x0=5
    l=1.5
    extension=10
    tiempo=10
   
#Se definen la cantidad de puntos que se quieren en x y t

    puntosx = 100
    puntost=1000
#Se define el universo de valores de x y t 
    x = np.linspace(0, extension, puntosx)
    t = np.linspace(0, tiempo, puntost)
    
    
#Se define el arreglo que contendrá la solución de difusión
    rhoi = np.zeros((puntosx, puntost), float)
    
#Se almacena la condición inicial 
    for i in range(0, puntosx): 
        rhoi[i,0] = A*np.exp(-((x[i]-x0)**2)/l)
#Se calculan las separaciones de los espacios en x y t
#Tener en cuenta que separacionx debe dar alrededor de 0.1 y separaciont alrededor de 0.01 para tener un buen resultado
    separacionx=extension/puntosx
    separaciont=tiempo/puntost
  
#Se realiza el gráfico   
    Z = Aproximacion(rhoi,puntosx,puntost,separacionx,separaciont,D)
    
    X, T = np.meshgrid(x, t)
    plt.figure(figsize=(10,6))
    ax = plt.axes(projection='3d')
    ax.set_xlabel('t')
    ax.set_ylabel('x')
    ax.set_zlabel('Difusión')
    ax.plot_surface(T,X, Z.T, rstride=1, cstride=1, cmap='cividis', edgecolor='none')
    ax.set_title('Aproximacion ecuación de difusión por Diferencias finitas')
    plt.show()
  
    return
#Se llama la función Grafico
Grafico()
