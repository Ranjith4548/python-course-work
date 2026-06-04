Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={1,2,3}
s
{1, 2, 3}
s={1,1,1,1,1}
s
{1}
s={2,3,443,54,34}
s
{2, 3, 34, 54, 443}
s=set()
s.add
<built-in method add of set object at 0x0000023F593E35A0>
s.add(1)
s
{1}
s.add(kfh)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.add(kfh)
NameError: name 'kfh' is not defined
s.add("kfh")
s
{1, 'kfh'}
s.add(True)
s
{1, 'kfh'}
1 i s
SyntaxError: invalid syntax
1 in s
True
2 in s
False
false not in s
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    false not in s
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> False not in s
True
>>> a={1,2,3,4,5,6,7,8,9,10}
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> b = {6,7,8}
>>> a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> a.intersection(b)
{8, 6, 7}
>>> a&b
{8, 6, 7}
>>> a-b
{1, 2, 3, 4, 5, 9, 10}
>>> a^b
{1, 2, 3, 4, 5, 9, 10}
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> a<{1,2,3,4,5,6,7,8,9}
False
>>> a<+{1,2,3,4,5,6,7,8,9}
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a<+{1,2,3,4,5,6,7,8,9}
TypeError: bad operand type for unary +: 'set'
>>> a<={1,2,3,4,5,6,7,8,}
False
>>> a.isdisjoint(b)
False
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> a.add(17)
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17}
>>> a.remove(10)
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 17}
>>> a.discard(10)
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 17}
>>> a.clear()
>>> a
set()
