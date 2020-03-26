import numpy as np
m=int(input('cantidad de filas:')) #filas
n=int(input('cantidad de columnas:')) #columnas
matrix = np.zeros((m,n)) 
x=np.zeros((m))  #vector solucion

vector=np.zeros((n))
comp=np.zeros((m))
error=[]


print ('Ingrese la matriz de coeficientes y el vector solución')
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"] "))
    vector[(r)]=float(input('b['+str(r+1)+']: '))
tol=float(input("Ingrese la tolerancia: "))
itera=int(input("Ingrese el numero máximo de iteraciones: "))


k=0
while k<itera:
    suma=0
    k=k+1
    for r in range(0,m):
        suma=0
        for c in range(0,n):
            if (c != r):
                suma=suma+matrix[r,c]*x[c]               
        x[r]=(vector[r]-suma)/matrix[r,r]  #Despeje
        print("x["+str(r)+"]: "+str(x[r]))
    del error[:]
    
    
    #Comprobación
    
    for r in range(0,n):
        suma=0
        for c in range(0,n):
            suma=suma+matrix[r,c]*x[c]
        comp[r]=suma
        dif=abs(comp[r]-vector[r])
        error.append(dif)
        print("error en x[",r,"]= ",error[r])
    print("Iteraciones: ",k)
    if all( i<=tol for i in error) ==True:
        break
        
