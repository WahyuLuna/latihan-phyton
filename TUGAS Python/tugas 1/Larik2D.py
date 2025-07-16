from Larik import Larik

class Larik2D:
    
    def __init__(self,numRows,numCols):
        self.theRows = Larik(numRows)
        
        for i in range(numRows):
            self.theRows[i] = Larik(numCols)
            
    def numRows(self):
        return(self.theRows)
    
    def numCols(self):
        return len(self.theRows[0])
    
    def clear(self,value):
        for row in range(self.numRows()):
            self.theRows[row].clear(value)
            
    def __getitem__(self,ndxtuple):
        assert len(ndxtuple) == 2,"invalid number of array subscripts"
        row = ndxtuple[0]
        col = ndxtuple[1]
        assert row >= 0 and row < self.numRows()\
            and col >= 0 and col < self.numCols(),\
                "array subscripts out of range"
        the1darray = self.theRows[row]
        return the1darray[col]
    
    def __setitem__(self,ndxtuple,value):
        assert len(ndxtuple) == 2,"invalid number of array subscripts"
        row = ndxtuple[0]
        col = ndxtuple[1]
        assert row >= 0 and row < self.numRows()\
            and col >= 0 and col < self.numCols(),\
                "array subscripts out of range"
        the1darray = self.theRows[row]
        the1darray[col] = value
    
    def isi2d(self):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                print('index [%d, %d]:'%(i,j))
                self[i,j]=int(input(':'))
                
    def dispArr2D(self):
        for i in range(self.numRows()):
            myRow = []
            for j in range(self.numCols()):
                myRow.append(self[i,j])
            print(myRow)
            


B = Larik2D(3,3)
B.isi2d()

B.dispArr2D()

B.numRows() 

B.numCols()

print(B[1,1])

B[1,1]=6
B.dispArr2D()
