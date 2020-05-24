## Different approach for algorithms and data structure implementation
&emsp;&emsp;**list of group members：** Longfei Jiang、 Juntao Gao<br>
&emsp;&emsp;**laboratory work number：** 1<br>
&emsp;&emsp;**variant description：** Dynamic array (you can use built-in list inside node with fixed size)<br>
### Synopsis ###
&emsp;&emsp;Develop libraries for specific data structures on classic development tasks. The selected data structure should be implemented in two ways: <br>
&emsp;&emsp;&emsp;&emsp;1、as a mutable object ; <br>
&emsp;&emsp;&emsp;&emsp;2、as an immutable object.<br><br>
&emsp;&emsp;For each version of the library (variable and immutable), the following functions should be implemented:<br>
&emsp;&emsp;&emsp;&emsp;1. add a new element;<br>
&emsp;&emsp;&emsp;&emsp;2. remove an element;<br>
&emsp;&emsp;&emsp;&emsp;3. size;<br>
&emsp;&emsp;&emsp;&emsp;4. conversion from and to python lists;<br>
&emsp;&emsp;&emsp;&emsp;5. find element by specific predicate;<br>
&emsp;&emsp;&emsp;&emsp;6. filter data structure by specific predicate;<br>
&emsp;&emsp;&emsp;&emsp;7. map structure by specific function;<br>
&emsp;&emsp;&emsp;&emsp;8. reduce – process structure elements to build a return value by specific functions;<br>
&emsp;&emsp;&emsp;&emsp;9. data structure should be a monoid and implement mempty and mconcat functions or methods;<br>
&emsp;&emsp;&emsp;&emsp;10. iterator;<br><br>
&emsp;&emsp;At last,you should use two approaches to test your code:<br>
&emsp;&emsp;&emsp;&emsp;1、unit tests (for all features);<br>
&emsp;&emsp;&emsp;&emsp;2、property-based tests (for features with specific properties, such as monoid properties).
### Contribution summary for each group member ###
&emsp;&emsp;Longfei Jiang: Complete the mutable object and immutable object data structures, and most of test functions.<br>
&emsp;&emsp;Juntao Gao: Partial data structure methods are implemented, as well as some test functions and final experimental reports.<br>
### Explanation of taken design decisions and analysis ###
&emsp;&emsp;The data structure that our group needs to implement is a dynamic array. The difference between a dynamic array and a fixed array is that the length of the dynamic array is variable, so we implement our own dynamic array by encapsulating the static array.<br> &emsp;&emsp;Using static arrays as attributes of the Python class, you can use built-in lists within nodes of fixed size. Of course, what we have implemented is a dynamic array, which can be expanded by inserting data in the head or tail. Then complete some common methods of dynamic array required by the experiment, such as array length, map and iterator.<br>
### How to use developed software ###
***一、for the mutable object***<br>
&emsp;&emsp;1、size<br>
&emsp;&emsp;DA_mut([1, 2, 3]).size<br>
&emsp;&emsp;2、to_list<br>
&emsp;&emsp;DA_mut([1, 2, 3]).to_list()<br>
&emsp;&emsp;3、from_list<br>
&emsp;&emsp;
```python
    test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = DA_mut()
            lst.from_list(e)
```
<br>
&emsp;&emsp;4、add_to_head<br>
&emsp;&emsp;lst = DA_mut()<br>
&emsp;&emsp;lst.add_to_head('a')<br>
&emsp;&emsp;5、add_to_tail<br>
&emsp;&emsp;lst = DA_mut()<br>
&emsp;&emsp;lst.add_to_tail('a')<br>
&emsp;&emsp;6、map<br>
&emsp;&emsp;lst = DA_mut()<br>
&emsp;&emsp;lst.from_list([1, 2, 3])<br>
&emsp;&emsp;lst.map(str)<br>
&emsp;&emsp;7、reduce<br>
&emsp;&emsp;lst = DA_mut()<br>
&emsp;&emsp;lst.from_list([1, 2, 3])<br>
&emsp;&emsp;lst.reduce(lambda st, e: st + e, 0)<br>
&emsp;&emsp;8、find<br>
&emsp;&emsp;lst = DA_mut([1,2,3])<br>
&emsp;&emsp;lst.find(1)<br>
&emsp;&emsp;9、filter<br>
&emsp;&emsp;lst = DA_mut([1,2,1])<br>
&emsp;&emsp;lst.filter(1)<br>
&emsp;&emsp;10、mempty<br>
&emsp;&emsp;lst = DA_mut([1, 2, 3])<br>
&emsp;&emsp;lst.mconcat()<br>
&emsp;&emsp;11、filter<br>
&emsp;&emsp;lst1 = DA_mut([1, 2, 3])<br>
&emsp;&emsp;lst2 = DA_mut([1, 2, 3])<br>
&emsp;&emsp;lst1.mconcat(lst2)<br>
&emsp;&emsp;lst1.to_list()<br>
&emsp;&emsp;12、remove<br>
&emsp;&emsp;lst = DA_mut([1, 2, 3])<br>
&emsp;&emsp;lst.remove(1)<br>
&emsp;&emsp;13、iter<br>

```python
        x = [1, 2, 3]
        lst = DA_mut()
        lst.from_list(x)
        tmp = []
        for e in lst:
            tmp.append(e)
```

<br>

***二、for the immutable object***<br>
&emsp;&emsp;1、size<br>
&emsp;&emsp;size(DA_imm([])<br>
&emsp;&emsp;2、to_list<br>
&emsp;&emsp;lst = [1, 2]<br>
&emsp;&emsp;a = DA_imm(lst)<br>
&emsp;&emsp;b = to_list(a)<br>
&emsp;&emsp;3、from_list<br>
&emsp;&emsp;
```python
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = from_list(e)
```
<br>
&emsp;&emsp;4、add_to_head<br>
&emsp;&emsp;DA1 = add_to_head(DA_imm([]), 1)<br>
&emsp;&emsp;5、add_to_tail<br>
&emsp;&emsp;DA1 = add_to_tail(DA_imm([1, 2]), 1)<br>
&emsp;&emsp;6、map<br>
&emsp;&emsp;a = DA_imm([1,2,3])<br>
&emsp;&emsp;b = map(a,str)<br>
&emsp;&emsp;7、reduce<br>
&emsp;&emsp;lst = DA_mut()<br>
&emsp;&emsp;reduce(lst,(lambda st, e: st + e)<br>
&emsp;&emsp;8、find<br>
&emsp;&emsp;lst = DA_mut([1,2,3])<br>
&emsp;&emsp;find(a, 1)<br>
&emsp;&emsp;9、filter<br>
&emsp;&emsp;lst = DA_mut([1,2,1])<br>
&emsp;&emsp;b = filter(a,2)<br>
&emsp;&emsp;10、mconcat<br>
&emsp;&emsp;a = DA_imm([1,2])<br>
&emsp;&emsp;b = DA_imm([1,2])<br>
&emsp;&emsp;c = mconcat(a,b)<br>
&emsp;&emsp;11、iter<br>

```python
        x = [1, 2, 3,4]
        lst = from_list(x)
        tmp = []
        try:
            get_next = iterator(lst)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
```
<br>

### Conclusion ###
&emsp;&emsp;For mutable objects and immutable objects, we find that once a mutable object is created, it can be changed but the address will not change, that is, the variable points to the original object. Immutable objects are the opposite. They cannot be changed after creation. If they are changed, the variable points to a new object.<br>
&emsp;&emsp;During the iterator testing process, we found that when an empty object is passed in, it will cause an error in the dynamic array length measurement method, resulting in an error in the iterator. So we modified the size () function and added the treatment of empty objects To solve this problem.

