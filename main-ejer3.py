class Matrix:
    def __init__ (self, v1, v2, v3, v4, v5, v6,dotVector):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.v5 = v5
        self.v6 = v6
        self.matriz1 = [self.v1,
                self.v2,
                self.v3]
        self.matriz2 = [self.v4,
                self.v5,
                self.v6]
        self.dotVector = dotVector

# Todos los métodos a mejorar, deberia iterar la lista de listas y manejarse con los indices automaticamente

    def myMatrix(self):
        print(self.matriz1)
        print(self.matriz2)

    def suma(self):
        print(self.v1[0]+self.v2[0]+self.v3[0],self.v1[1]+self.v2[1]+self.v3[1],self.v1[2]+self.v2[2]+self.v3[0])

        print(self.matriz1[0][0] + self.matriz2[0][0], self.matriz1[0][1] + self.matriz2[0][1], self.matriz1[0][2] + self.matriz2[0][2],
        self.matriz1[1][0] + self.matriz2[1][0], self.matriz1[1][1] + self.matriz2[1][1], self.matriz1[1][2] + self.matriz2[1][2],
        self.matriz1[2][0] + self.matriz2[2][0], self.matriz1[2][1] + self.matriz2[2][1], self.matriz1[2][2] + self.matriz2[2][2])

    def resta(self):
        print(self.matriz1[0][0] - self.matriz2[0][0], self.matriz1[0][1] - self.matriz2[0][1], self.matriz1[0][2] - self.matriz2[0][2],
        self.matriz1[1][0] - self.matriz2[1][0], self.matriz1[1][1] - self.matriz2[1][1], self.matriz1[1][2] - self.matriz2[1][2],
        self.matriz1[2][0] - self.matriz2[2][0], self.matriz1[2][1] - self.matriz2[2][1], self.matriz1[2][2] - self.matriz2[2][2])

    def multPorUnVector(self):

        print(self.matriz1[0][0] * self.dotVector[0] + self.matriz1[0][1] * self.dotVector[1] + self.matriz1[0][2] * self.dotVector[2], 
        self.matriz1[1][0] * self.dotVector[0] + self.matriz1[1][1] * self.dotVector[1] + self.matriz1[1][2] * self.dotVector[2], 
        self.matriz1[2][0] * self.dotVector[0] + self.matriz1[2][1] * self.dotVector[1] + self.matriz1[2][2] * self.dotVector[2])


# La matriz a crear recibe la lista de los 6 vectores a sumar (dos matrices de 3x3) y un vector de 3x1 para multiplicar. Para 'dividir' por un vector
# escribir el último vector como 1/vector. Ejemplo: 1/1, 1/2, 1/3 

A = Matrix([2,1,3],[1,3,4],[4,5,2],[1,5,2],[5,3,1],[2,4,6],[1,2,3])
A.myMatrix()
A.suma()
A.resta()
A.multPorUnVector()
