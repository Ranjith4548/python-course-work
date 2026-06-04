Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1,1)
t=(1,1.1,'tryu',[])
t
(1, 1.1, 'tryu', [])
t=(10,20,0,40,50)
t
(10, 20, 0, 40, 50)
h=(90,80,70)
t+h
(10, 20, 0, 40, 50, 90, 80, 70)
t*4
(10, 20, 0, 40, 50, 10, 20, 0, 40, 50, 10, 20, 0, 40, 50, 10, 20, 0, 40, 50)
t
(10, 20, 0, 40, 50)
t[1]
20
t[2]
0
t[3]
40
t[4]
50
t[5]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t[5]
IndexError: tuple index out of range
t
(10, 20, 0, 40, 50)
t[:3]
(10, 20, 0)
t[3:]
(40, 50)
t[::2]
(10, 0, 50)
t[2::]
(0, 40, 50)
0int
SyntaxError: invalid syntax
10 in t
True
0 in t
True
>>> 50 in t
True
>>> 80 in t
False
>>> 90 in t
False
>>> t
(10, 20, 0, 40, 50)
>>> lrn(t)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lrn(t)
NameError: name 'lrn' is not defined. Did you mean: 'len'?
>>> len(t)
5
>>> min(t)
0
>>> max(t)
50
>>> sum(t)
120
>>> t.count(10)
1
>>> t.index(10)
0
>>> t=1,2,3,4,5,6,7
>>> t
(1, 2, 3, 4, 5, 6, 7)
>>> a,b,c=(1,2,3)
>>> a
1
>>> b
2
>>> c
3
>>> t=1,2,3,[4,5,6],7,8)
SyntaxError: unmatched ')'
>>> t=1,2,3,[4,5,6],7,8
>>> t[3]
[4, 5, 6]
>>> t[2]=4
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
