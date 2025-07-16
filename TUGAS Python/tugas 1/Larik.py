# Implementasi ADT Larik memakai python list.
class Larik :
# menciptakan array dengan 'size' elemen.
    def __init__( self, size ):
        # assert size > 0, "Array size must be > 0"
        self._size = size
        # menciptakan array kosong memakai list
        self._elements = []
        for i in range(size):
            self._elements.append(None)

    # memberikan 'size' dari array.
    def __len__( self ):
        return self._size
 # memberikan elemen sesuai index.
    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "indeks larik diluar batas"
        return self._elements[ index ]

    # mengganti elemen pada index dengan nilai value.
    def __setitem__( self, index, value ):
        #print('index = ',index)
        assert index >= 0 and index < len(self), "indeks larik diluar batas"
        self._elements[ index ] = value

    # mengganti semua elemen array menjadi value.
    def clear( self, value ):
        for i in range( len(self) ) :
            self._elements[i] = value

    # memberikan iterator dari array.
    def __iter__( self ):
        return _ArrayIterator( self._elements )

 # menyalin isi list L ke array
    def fromList(self,L):
        n = self._size
        m = len(L)
        if (m > n):
            self.__init__(m)
        i=0
        for x in L:
           self._elements[i] = x
           i += 1

    # menyalin nilai setiap huruf dari string Str ke array
    def fromString(self, Str):
        n = self._size
        m = len(Str)
        if (m > n):
            self.__init__(m)
        
        for i in range(m):
            self._elements[i]=ord(Str[i])
 # mengisi larik
    def isiLarik(self):
        n = self._size
        for i in range(n):
            print('indeks ',i)
            self._elements[i] = int(input(' : '))

    # mencari x dalam larik
    def cariX(self,x):
        n = self._size
        ketemu = False
        for i in range(n):
            if (x == self._elements[i]):
                print('Ketemu pd index ', i)
                ketemu = True
        if (not ketemu):
            print(x, ' tidak ada dalam larik')

    # menghapus x dari larik
    def hapusX(self,x):
        n = self._size
        ketemu = False
        for i in range(n):
            if (x == self._elements[i]):
                print('Ketemu pd index ',i)
                ketemu = True
                print('Sudah dihapus ')
                [i]=''
        if (not ketemu):
            print(x,' tidak ada dalam array ')
 #baca isi larik
    def bacaLarik(self):
        r = input('0-Semua-data  1-hanya satu data : ')
        r = int(r)
        if r < 1:
            for x in self._elements:
                print(x)
        else:
            i = int(input('index : '))
            print(self._elements[i])
# An iterator for the Array ADT.
class _ArrayIterator :
    def __init__( self, theArray ):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._curNdx < len( self._arrayRef ) :
            entry = self._arrayRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration
