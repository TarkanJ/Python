#!/usr/bin/env python3

# result of on-line programming during the third lecture
# of A4B99RPH - Problem solving and (other) games; 2011-10-12
# provided for sake of completeness. It is not a final polished
# code
# Tomas Svoboda, svobodat@fel.cvut.cz, 2011

# code for matrix multiplication taken from
# http://www.syntagmatic.net/matrix-multiplication-in-python/

class Matrices:
    def __init__(self,matrix):
        self.matrix = matrix

    def multiply(self,other_matrix_object):
        matrix1 = self.matrix # lazy assignment for backward compatibility
        matrix2 = other_matrix_object.matrix
        if len(matrix1[0]) != len(matrix2):
            # number of columns of the first matrix must be equal
            # to the number of rows of the second matrix
            return(None)
        else:
            # Multiply if correct dimensions
            new_matrix = zero(len(matrix1),len(matrix2[0]))
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
            return(Matrices(new_matrix))

    def __mul__(self,other_matrix_object):
        """just a quick wrapper around the multiply method
        overloading the * operator
        """
        return(self.multiply(other_matrix_object))
        
    def __str__(self):
        """Convert a matrix - 2D list into a simple string"""
        rows = []
        for row in self.matrix:
            rows.append(str(row))
        return(str(rows))

        
def zero(m,n):
    """Create zero matrix"""
    new_matrix = [[0 for row in range(n)] for col in range(m)]
    return new_matrix


def show(mat):
    """simple matrix printing row by row"""
    for row in mat:
        print(row)

    
if __name__ == "__main__":
    mat1 = Matrices([[1,2],[4,5]])
    mat2 = Matrices([[6,5],[3,5]])
    mat3 = mat1*mat2
    # mat3 = mat1.multiply(mat2)
    print(mat3)
    show(mat3.matrix)
