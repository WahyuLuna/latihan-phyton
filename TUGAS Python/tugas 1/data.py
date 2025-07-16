from Larik2D import Larik2D

class Matriks :
    # Creates a matrix of size numRows x numCols initialized to 0.
    def __init__( self, numRows, numCols ):
        self._theGrid = Larik2D( numRows, numCols )
        self._theGrid.clear( 0 )

    # Returns the number of rows in the matrix.
    def numRows( self ):
        return self._theGrid.numRows()

    # Returns the number of columns in the matrix.
    def numCols( self ):
        return self._theGrid.numCols()

# Returns the value of element (i, j): x[i,j]
    def __getitem__( self, ndxTuple ):
        return self._theGrid[ ndxTuple[0], ndxTuple[1] ]

    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__( self, ndxTuple, scalar ):
        self._theGrid[ ndxTuple[0], ndxTuple[1] ] = scalar

    # Scales the matrix by the given scalar.
    def scaleBy( self, scalar ):
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                self[ r, c ] *= scalar

# Creates and returns a new matrix that is the transpose of this matrix.
    # added by Suarga
    def tranpose( self ):
        bar = self.numRows()
        kol = self.numCols()
        temp = Matrix(kol, bar)
        for i in range(bar):
            for j in range(kol):
                temp[j,i] = self[i,j]
        return temp

    # Creates and returns a new matrix that results from matrix addition.
    def __add__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
                rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the add operation."
        # Create the new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] + rhsMatrix[ r, c ]
        return newMatrix

# Creates and returns a new matrix that results from matrix subtraction.
    # completed by Suarga
    def __sub__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
                rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the add operation."
        # Create the new matrix.
        newMatrix = Matriks( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] - rhsMatrix[ r, c ]
        return newMatrix

    def __mul__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numCols(), \
               "Matrix sizes not compatible for the multiplication."
        # create the new matrix
        newMatrix = Matriks( self.numRows(), rhsMatrix.numCols() )
        # multiply the matrices
        for r in range( self.numRows() ):
            for c in range( rhsMatrix.numCols() ):
                newMatrix[r, c] = 0
                for k in range( rhsMatrix.numRows() ):
                    newMatrix[r, c] += self[r,k] * rhsMatrix[k, c]
        return newMatrix

    # display matrix
    def dispMatrix( self ):
        for i in range(self.numRows()):
            myRow=[]
            for j in range(self.numCols()):
                myRow.append(self[i,j])
            print(myRow)
 # isi matriks
    def isiMatriks( self ):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                print('index [%d, %d]: ' % (i,j))
                self[i,j] = int(input(' : ')) 

