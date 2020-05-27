import ctypes

class DA_mut:
    def __init__ (self,l=[]):
        self._n = 0 #Current array size
        self._capacity = 100    #Array capacity
        self._A = self._make_array(self._capacity) #Open up space
        if len(l) >= self._capacity:    #Check if the current capacity is enough
            self._resize(2*len(l))
        for i in range(len(l)):
            self._A[i] = l[i]
            self._n = len(l) 

    def size(self) -> int:
        return self._n
    
    def to_list(self) -> list:
        lst = []
        for k in range(self._n):
                lst.append(self._A[k])
        return lst

    def from_list(self, lst:list):
        if len(lst) >= self._capacity:    #Check if the current capacity is enough
            self._resize(len(lst))
        if len(lst) > 0:
            for i in range(len(lst)):
                self._A[i] = lst[i]
        self._n = len(lst)
        return self

    def append_to_tail(self, obj):
        if self._n == self._capacity:    #Check if the current capacity is enough
            self._resize(2 * self._capacity)
        self._A[self._n] = obj    
        self._n += 1
    
    def append_to_head(self, value):
        if self._n == self._capacity:    #Check if the current capacity is enough
            self._resize(2 * self._capacity)
        for j in range(self._n, 0, -1):   
            self._A[j] = self._A[j-1]
        self._A[0] = value
        self._n += 1

    def map(self, f:str):
        for i in range(self._n):
            self._A[i] = f(self._A[i])

    def reduce(self, f, initial_state):
        state = initial_state
        cur = 0
        for i in range(self._n):
            state = f(state, self._A[cur])
            cur += 1
        return state

    def find(self, value):
        for v in self.to_list():
            if v is value:
                return True
        return False     

    def filter(self, value):
        lst_filter = []
        for i in self._A[:self._n]:
            if i is not value:
                lst_filter.append(i)
        return lst_filter

    def mempty(self):
        return None

    def mconcat(self,DA1,DA2):
        if DA1 is  None:
            if (DA2._n) >= self._capacity:    #Check if the current capacity is enough
                self._resize((DA2._n)*2)
            for e in range(DA2._n):
                self._A[e]=DA2._A[e]
                self._n+=1
        elif DA2 is  None:
            if (DA1._n) >= self._capacity:    #Check if the current capacity is enough
                self._resize((DA1._n)*2)
            for e in range(DA1._n):
                self._A[e]=DA1._A[e]
                self._n+=1
        else:
            if (DA1._n+DA2._n) >= self._capacity:    #Check if the current capacity is enough
                self._resize((DA1._n+DA2._n)*2)
            for e in range(DA1._n):
                self._A[e]=DA1._A[e]
                self._n+=1
            for e in range(DA1._n,DA1._n+DA2._n):
                self._A[e]=DA2._A[e-DA1._n]
                self._n+=1

    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:   
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]  
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError( 'value not found' )

    def _make_array(self, c):
        return (c * ctypes.py_object)( )
    
    def _resize(self, c:int):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c   

    def is_empty(self):
        return self._n == 0
    
    def __getitem__ (self, k):
        if not 0 <= k < self._n:
            raise ValueError('invalid index') 
        return self._A[k]
    
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < self._n:
            x = self._A[self.a]
            self.a += 1
            return x
        else:
            raise StopIteration
