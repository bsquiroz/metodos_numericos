# utilice la siguiente matrix para ingresar sus ecuacion 3 x 3 
# note que el termino independiente se incluye, por lo tanto es 3 x 4

matrix = [
    [1, -0.1, -0.2, 7.85],  
    [0.1, 7, -0.3, -19.3],
    [0.3, -0.2, 10, 71.4]   
]

def gauss_jordan(matrix):
    mat = [row[:] for row in matrix]

    n = len(mat)

    for i in range(n):
        pivot = mat[i][i]
        for k in range(n + 1):
            mat[i][k] /= pivot

        for j in range(n):
            if i != j:
                factor = mat[j][i]
                for k in range(n + 1):
                    mat[j][k] -= factor * mat[i][k]
        
    return [mat[i][-1] for i in range(n)]

solution = gauss_jordan(matrix)
print("Soluciones:")
print("x =", solution[0])
print("y =", solution[1])
print("z =", solution[2])
