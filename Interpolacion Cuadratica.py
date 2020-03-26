import numpy as np
from sympy import solve_linear_system,Matrix
import sympy as sp

#puntos=np.zeros((3,2))#Este es por si quieres introducir los datos uno por uno
puntos=np.array([[3,10]
                ,[2,3]
                ,[-1,6]])
#Por si desea meter los datos uno por uno
'''for i in range(0,3):
    puntos[i][0]=float(input("Valor para X"+str(i+1)+" :"))
    puntos[i][1]=float(input("Valor para Y"+str(i+1)+" :"))'''
    
print(puntos)    
#hay que poner 3x4 ya que la ultima columna es donde estan los valores del igual 
coeficientes=np.zeros((3,4))
x, y, z = sp.symbols('x y z')

for i in range(0,3):
    coeficientes[i][0]=puntos[i][0]**2
    coeficientes[i][1]=puntos[i][0]
    coeficientes[i][2]=1
    coeficientes[i][3]=puntos[i][1]
    
sistema=Matrix(coeficientes)   
print(coeficientes)
#para resolver el sistema de ecuaciones se utilizo una libreria de sympy
r=solve_linear_system(sistema,x,y,z) 
funcion = r.get(x)*x**2+r.get(y)*x+r.get(z) 

print(funcion)