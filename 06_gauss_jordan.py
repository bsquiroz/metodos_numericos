# utilice la siguiente matrix para ingresar sus ecuacion 3 x 3 
# note que el termino independiente se incluye, por lo tanto es 3 x 4

matrix = [
    [2, 2, -6, 8],
    [-3, -5, 1, -20],
    [7, 1, -2, 5],  
]


# matrix = [
#     [1, -0.1, -0.2, 7.85],  
#     [0.1, 7, -0.3, -19.3],
#     [0.3, -0.2, 10, 71.4]   
# ]

def gauss_jordan(matrix):
    mat = [row[:] for row in matrix]

    if(mat[0][0] == 1):
        if not mat[1][0] == 0:
            piv = mat[1][0]

            mat[1][0] = mat[1][0] - ((piv) * mat[0][0])
            mat[1][1] = mat[1][1] - ((piv) * mat[0][1])
            mat[1][2] = mat[1][2] - ((piv) * mat[0][2])
            mat[1][3] = mat[1][3] - ((piv) * mat[0][3])

        if not mat[2][0] == 0:
            piv = mat[2][0]

            mat[2][0] = mat[2][0] - ((piv) * mat[0][0])
            mat[2][1] = mat[2][1] - ((piv) * mat[0][1])
            mat[2][2] = mat[2][2] - ((piv) * mat[0][2])
            mat[2][3] = mat[2][3] - ((piv) * mat[0][3])
    else:
        num = mat[0][0]

        mat[0][0] = mat[0][0] / num 
        mat[0][1] = mat[0][1] / num 
        mat[0][2] = mat[0][2] / num 
        mat[0][3] = mat[0][3] / num 

        if not mat[1][0] == 0:
            piv = mat[1][0]

            mat[1][0] = mat[1][0] - ((piv) * mat[0][0])
            mat[1][1] = mat[1][1] - ((piv) * mat[0][1])
            mat[1][2] = mat[1][2] - ((piv) * mat[0][2])
            mat[1][3] = mat[1][3] - ((piv) * mat[0][3])

        if not mat[2][0] == 0:
            piv = mat[2][0]

            mat[2][0] = mat[2][0] - ((piv) * mat[0][0])
            mat[2][1] = mat[2][1] - ((piv) * mat[0][1])
            mat[2][2] = mat[2][2] - ((piv) * mat[0][2])
            mat[2][3] = mat[2][3] - ((piv) * mat[0][3])
    
    print('\nPrimera parte: \n')
    for row in mat:
        print(row)

    if(mat[1][1] == 1):
        if not mat[0][1] == 0:
            piv = mat[0][1]

            mat[0][0] = mat[0][0] - ((piv) * mat[1][0])
            mat[0][1] = mat[0][1] - ((piv) * mat[1][1])
            mat[0][2] = mat[0][2] - ((piv) * mat[1][2])
            mat[0][3] = mat[0][3] - ((piv) * mat[1][3])

        if not mat[2][1] == 0:
            piv = mat[2][1]

            mat[2][0] = mat[2][0] - ((piv) * mat[1][0])
            mat[2][1] = mat[2][1] - ((piv) * mat[1][1])
            mat[2][2] = mat[2][2] - ((piv) * mat[1][2])
            mat[2][3] = mat[2][3] - ((piv) * mat[1][3])
    else:
        num = mat[1][1]

        mat[1][0] = mat[1][0] / num 
        mat[1][1] = mat[1][1] / num 
        mat[1][2] = mat[1][2] / num 
        mat[1][3] = mat[1][3] / num 

        if not mat[0][1] == 0:
            piv = mat[0][1]

            mat[0][0] = mat[0][0] - ((piv) * mat[1][0])
            mat[0][1] = mat[0][1] - ((piv) * mat[1][1])
            mat[0][2] = mat[0][2] - ((piv) * mat[1][2])
            mat[0][3] = mat[0][3] - ((piv) * mat[1][3])

        if not mat[2][1] == 0:
            piv = mat[2][1]

            mat[2][0] = mat[2][0] - ((piv) * mat[1][0])
            mat[2][1] = mat[2][1] - ((piv) * mat[1][1])
            mat[2][2] = mat[2][2] - ((piv) * mat[1][2])
            mat[2][3] = mat[2][3] - ((piv) * mat[1][3])

    print('\nSegunda parte: \n')
    for row in mat:
        print(row)

    if(mat[2][2] == 1):
        if not mat[0][2] == 0:
            piv = mat[0][2]

            mat[0][0] = mat[0][0] - ((piv) * mat[2][0])
            mat[0][1] = mat[0][1] - ((piv) * mat[2][1])
            mat[0][2] = mat[0][2] - ((piv) * mat[2][2])
            mat[0][3] = mat[0][3] - ((piv) * mat[2][3])

        if not mat[1][2] == 0:
            piv = mat[1][2]

            mat[1][0] = mat[1][0] - ((piv) * mat[2][0])
            mat[1][1] = mat[1][1] - ((piv) * mat[2][1])
            mat[1][2] = mat[1][2] - ((piv) * mat[2][2])
            mat[1][3] = mat[1][3] - ((piv) * mat[2][3])
    else:
        num = mat[2][2]

        mat[2][0] = mat[2][0] / num 
        mat[2][1] = mat[2][1] / num 
        mat[2][2] = mat[2][2] / num 
        mat[2][3] = mat[2][3] / num 

        if not mat[0][2] == 0:
            piv = mat[0][2]

            mat[0][0] = mat[0][0] - ((piv) * mat[2][0])
            mat[0][1] = mat[0][1] - ((piv) * mat[2][1])
            mat[0][2] = mat[0][2] - ((piv) * mat[2][2])
            mat[0][3] = mat[0][3] - ((piv) * mat[2][3])

        if not mat[1][2] == 0:
            piv = mat[1][2]

            mat[1][0] = mat[1][0] - ((piv) * mat[2][0])
            mat[1][1] = mat[1][1] - ((piv) * mat[2][1])
            mat[1][2] = mat[1][2] - ((piv) * mat[2][2])
            mat[1][3] = mat[1][3] - ((piv) * mat[2][3])

    print('\nTercera parte: \n')
    for row in mat:
        print(row)

    solution = [row[-1] for row in mat]

    print(f"\n\nX: {solution[0]}\nY: {solution[1]}\nZ: {solution[2]}")

gauss_jordan(matrix)