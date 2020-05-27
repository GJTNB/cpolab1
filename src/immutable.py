import ctypes


class DA_imm(object):
    def __init__ (self,l=[]):
        self._n = 0 #Current array size
        self._capacity = 100    #Array capacity
        self._A = self._make_array(self._capacity)  #Open up space
        if len(l) >= self._capacity:     #Check if the current capacity is enough
            self._resize(2*len(l))
        for i in range(len(l)):
            self._A[i] = l[i]
            self._n = len(l) 

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
    
    def __eq__(self, other):
        for i in range(self._n):
            if self._A[i] != other._A[i]:
                return False
        return True
    
    def _make_array(self, c):
        return (c * ctypes.py_object)( )
    
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c   


def size(n:DA_imm()) -> int:
    return n._n

def to_list(n:DA_imm()) -> list:
    lst = []
    for e in n:
        lst.append(e)
    return lst


def from_list(lst:list):
    n = DA_imm()
    if len(lst) >= n._capacity:     #Check if the current capacity is enough
        n._resize(2*len(lst))
    for i in range(len(lst)):
        n._A[i] = lst[i]
    n._n=len(lst)
    return n


def add_to_head(n:DA_imm(), value):
    if n._n == n._capacity:    #Check if the current capacity is enough
        n._resize(2 * n._capacity)
    for j in range(n._n, 0, -1):    
        n._A[j] = n._A[j-1]
    n._A[0] = value
    n._n += 1
    return n


def add_to_tail(n:DA_imm(), value):
    if n._n == n._capacity:     #Check if the current capacity is enough
        n._resize(2 * n._capacity)
    n._A[n._n] = value    
    n._n += 1
    return n

def find(n:DA_imm(), value):
    for e in n:
        if e is value:
            return True
    return False


def remove(n:DA_imm(), value):
    l = []
    for i in range(size(n)):
        if i is not value:
            l.append(n._A[i])
    return DA_imm(l)


def filter(n:DA_imm(), value):
    l = []
    for e in n:
        if e is not value:
            l.append(e)
    return DA_imm(l)


def map(n:DA_imm(), f):
    l = []
    for e in n:
        l.append(f(e))
    return DA_imm(l)


def reduce(n:DA_imm(), f, initial_state):
    state = initial_state
    cur = 0
    for i in range(n._n):
        state = f(state, n._A[cur])
        cur += 1
    return state


def mempty():
    return DA_imm()


def mconcat(a:DA_imm(), b:DA_imm()):
    l1 = to_list(a)
    l2 = to_list(b)
    return DA_imm(l1 + l2)

def iterator(lst:DA_imm()):
    if lst is not None:
        length=size(lst)
    else:
        length=0
    da = lst
    index=0
    def foo():
        nonlocal da
        nonlocal length
        nonlocal index
        if ( (da is None) | (index >= length)) : raise StopIteration
        tmp = da._A[index]
        index=index+1
        return tmp
    return foo
