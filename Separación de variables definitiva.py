# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:53:07 2021

@author: Ever Ortega Calderón
"""
#Se llaman las bibliotecas requeridas 
import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt

"""
Función Parte_temporal 
Recibe:
    D= constante del problema, corresponde a 0.5
    n=coeficientes n 
    t=valores correspondientes al tiempo
    lx=longitud del espacio
Retorna:
    temporal= valor de la parte temporal

"""
def Parte_temporal(D,n,t,lx):
    temporal=np.exp(-D*t*((n*np.pi/lx)**2))
    return temporal
"""
Función Parte_espacial
Recibe:
    n=coeficientes n 
    x=valores correspondientes al espacio
    lx=longitud del espacio
Retorna=
    espacial=valor de la parte espacial

"""
def Parte_espacial(n,x,lx):
    espacial=np.sin(n*np.pi*x/lx)
    return espacial
"""
Función Coeficientes
Recibe:
    x0= constante del problema correspondiente 5.0
    l=constante del problema correspondiente 1.5
    n=coeficientes n
    x=se refeire al valor de posición que se desee evalaur en su momento
    A=constante del problema correspondiente 2.0
    lx=longitud del espacio
Retorna:
    coefi=valor de los oceficientes n

"""
def Coeficientes(x0,l,n,x,A,lx):
    funcion=lambda x: ((np.exp(-(((x-x0)**2)/l)))*np.sin(n*np.pi*x/lx))
    integral,err=spint.quad(funcion,0,lx)
    
    coefi=integral*(2*A/lx)
    
    return coefi



#Definir constantes
A=2.0
l=1.5
x0=5
D=0.5
lx=10.0
lt=lx
cant_puntos=50

#Se definen los valores de tiempo para trabajar
t=np.linspace(0,lt,cant_puntos)
#Se definen los valores de espacio para trabajar
x=np.linspace(0,lx,cant_puntos)
#Definimos los n que queremos
n=10
#Se inicializa el arreglo rho, que contendrá los valores de la difusión
rho=np.zeros((len(x),len(t)))

#Se calcula la solución de la dispersión, primer for itera el tiempo, el segundo itera el espacio, el tercer for hace la sumatoria en los n
for m in range(0,len(t)):
    for j in range(0,len(x)):
        
        for i in range(1,n):
            
            rho[m,j]=rho[m,j]+Parte_temporal(D,i,t[m],lx)*Parte_espacial(i,x[j],lx)*Coeficientes(x0,l,i,x[j],A,lx)
            
#Se realiza el gráfico 3D
X, T = np.meshgrid(x, t)
plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_zlabel('Difusión')
ax.plot_surface(T,X, rho, rstride=1, cstride=1, cmap='cividis', edgecolor='none')
ax.set_title('Aproximacion ecuación difusión por separación de variables')
plt.show()
