class Larik():
    def __init__(self,size):
        self._size=size
        self._element=[]
        for i in range(size):
            self._element.append(None)
            
    def __len__(self):
        return len(self._size)
    
    def __getitem__(self,index):
        assert index >= 0 and index < len(self)
        return self._element[index]
    
    def __setitem__(self,index,value):
        assert index >= 0 and index < len(self)
        self._element[index] = value
        
    def isiLarik(self):
        n = self._size
        for i in range(n):
            print("index ",i)
            self._element[i] =int(input(" : "))
    
    def cacah(self,angka):
        self._angka = angka
        b = self._element
        ccah = b.count(self._angka)
        if ccah >0 :
            print(f"angka {self._angka} berjumlah = {ccah}")
        else:
            print(f"Angka {self._angka} tidak ada dalam larik")
        
        
    
A = Larik(10)
A.isiLarik()
A.cacah(10)



