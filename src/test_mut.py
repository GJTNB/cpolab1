from mutable import *
import hypothesis.strategies as st
from hypothesis import given
import unittest

class TestMutableList(unittest.TestCase):
    def test_addNone(self):
        lst = DA_mut()
        lst.append_to_head(None)
        self.assertEqual(lst.to_list(), [None])
        lst2 = DA_mut([1,None,2])
        self.assertEqual(lst2.to_list(), [1,None,2])

    def test_size(self):
        self.assertEqual(DA_mut().size(), 0)
        self.assertEqual(DA_mut([1, 2, 3]).size(), 3)

    def test_to_list(self):
        self.assertEqual(DA_mut().to_list(), [])
        self.assertEqual(DA_mut([1, 2, 3]).to_list(), [1, 2, 3])

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = DA_mut()
            lst.from_list(e)
            self.assertEqual(lst.to_list(), e)

    def test_append_to_head(self):
        lst = DA_mut()
        self.assertEqual(lst.to_list(), [])
        lst.append_to_head('a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.append_to_head('b')
        self.assertEqual(lst.to_list(), ['b', 'a'])

    def test_add_to_tail(self):
        lst = DA_mut()
        self.assertEqual(lst.to_list(), [])
        lst.append_to_tail('a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.append_to_tail('b')
        self.assertEqual(lst.to_list(), ['a', 'b'])

    def test_map(self):
        lst = DA_mut()
        lst.map(str)
        self.assertEqual(lst.to_list(), [])
        lst = DA_mut()
        lst.from_list([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.to_list(), ["1", "2", "3"])

    def test_reduce(self):
        # sum of empty list
        lst = DA_mut()
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)
        # sum of list
        lst = DA_mut()
        lst.from_list([1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)
        # size
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = DA_mut()
            lst.from_list(e)
            self.assertEqual(lst.reduce(lambda state, _: state + 1, 0), lst.size())

    def test_find(self):
        lst = DA_mut()
        self.assertEqual(lst.find(1), False)
        lst = DA_mut([1, 2, 3])
        self.assertEqual(lst.find(1), True)

    def test_filter(self):
        lst = DA_mut()
        self.assertEqual(lst.filter(1), [])
        lst = DA_mut([1, 2, 3])
        self.assertEqual(lst.filter(1), [2, 3])

    def test_mconcat(self):
        lst=DA_mut()
        lst1 =DA_mut([1, 2, 3])
        lst2 =DA_mut([1, 2, 3])
        lst.mconcat(lst1,lst2)
        self.assertEqual(lst.to_list(), [1, 2, 3, 1, 2, 3])

    def test_remove(self):
        lst = DA_mut([1, 2, 3])
        lst.remove(1)

        self.assertEqual(lst.to_list(), [2,3])

    @given(st.lists(st.integers(), min_size=100))
    def test_from_list_to_list_equality(self, a):
        lst = DA_mut()
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst2 = DA_mut()
        lst2.from_list(a)
        self.assertEqual(lst2.size(), len(a))

    @given(st.lists(st.integers(), min_size=100))
    def test_monoid_identity(self,li):
        lst = DA_mut()
        lst.from_list(li)
        lst_test1=DA_mut()
        lst_test2=DA_mut()
        lst_test1.mconcat(lst.mempty(), lst)
        lst_test2.mconcat(lst, lst.mempty())
        self.assertEqual(lst_test1.to_list(),li)
        self.assertEqual(lst_test2.to_list(),li)


    @given(a=st.lists(st.integers(), min_size=100),b=st.lists(st.integers()),c=st.lists(st.integers()))
    def test_monoid_associativity(self,a,b,c):
        lst_test1=DA_mut()
        lst1 = DA_mut()
        lst2 = DA_mut()
        lst3= DA_mut()
        lst1 = lst1.from_list(a)
        lst2 = lst2.from_list(b)
        lst3 = lst3.from_list(c)
        lst_test1_1=  DA_mut()
        lst_test1_1.mconcat(lst1,lst2)
        lst_test1.mconcat(lst_test1_1,lst3)

        lst_test2=DA_mut()
        lst1 = DA_mut()
        lst2 = DA_mut()
        lst3= DA_mut()
        lst1 = lst1.from_list(a)
        lst2 = lst2.from_list(b)
        lst3 = lst3.from_list(c)
        lst_test2_2= DA_mut()
        lst_test2_2.mconcat(lst2,lst3)
        lst_test2.mconcat(lst1,lst_test2_2)

        self.assertEqual(lst_test1.to_list(),lst_test2.to_list())
 

    def test_iter(self):
        x = [1, 2, 3]
        lst = DA_mut()
        lst.from_list(x)
        tmp = []
        for e in lst:
            tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(lst.to_list(), tmp)
        i = iter(DA_mut())
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()
