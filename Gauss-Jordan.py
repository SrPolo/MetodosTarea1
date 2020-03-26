import numpy as np

coeficientes=np.array([[3,-0.1,-0.2],
                       [0.1,7,-0.3],
                       [0.3,-0.2,10]])

valor=np.array([7.85,-19.3,71.4])

#Para saber el numero de filas que hay

fila=coeficientes.shape[0]

#Para saber el numero de columnas que hay

columna=coeficientes.shape[1]

for i in range(0,fila):
     for j in range(i+1,fila):
        factor=coeficientes[j,i]/coeficientes[i,i]
        valor[j]=valor[j]-(factor*valor[i])
        for k in range(0,columna):
            coeficientes[j,k]=coeficientes[j,k]-factor*coeficientes[i,k]
            
i=0;j=0;k=0;
for i in range(fila-1,-1,-1):
    for j in range(i-1,-1,-1):
        factor=coeficientes[j,i]/coeficientes[i,i]
        valor[j]=valor[j]-(factor*valor[i])
        for k in range(columna-1,0,-1):
            coeficientes[j,k]=coeficientes[j,k]-factor*coeficientes[i,k]
        
for i in range(0,fila):
    valor[i]=valor[i]/coeficientes[i][i]
    coeficientes[i][i]=coeficientes[i][i]/coeficientes[i][i]
print(coeficientes, valor)