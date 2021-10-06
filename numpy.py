# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:33:57 2021

@author: eposymu
"""

import numpy as np

a = np.arange(15).reshape(3,5)
a.shape
a.ndim
a.dtype.name
a.itemsize
a.size
type(a)
b = np.array([1,2.,3])
b.dtype
c = np.array([[1,2,3], [4,5,6]])
c
d = np.array([(1,2,3), (4,5,6)], dtype=complex)
d

e = np.zeros((3,4,2), dtype=np.int64)
e

np.arange(10,70,4.)

np.linspace(0,2,9)
x = np.linspace(0, 2*np.pi, 100)
x
f = np.sin(x)
f


print(np.arange(10000).reshape(100,100))

a = np.array([11,22,33,44])
b = np.arange(4)
print(b-a)
print(b**2)
print(10*np.sin(a))

#mask/filters
print(a < 20)
print(a[a>20])


c = np.arange(16).reshape(4,4)
print(c>=6)
print(c[c>=6])


print(c[:,1:3])

print(a*b)
print(a@b)
print(a.dot(b))
print(b.dot(a))


rg = np.random.default_rng(1)
a = np.ones((2,3), dtype=int)
b=rg.random((2,3))

a*=3
print(a)
print(b)
b += a
print(b)

a = np.ones(10, dtype=np.int32)
b = np.linspace(0, np.pi, 10)
c = a + b
print(c)
print(c.dtype.name)
d = np.exp(c * 1j)
print(d)
print(d.dtype.name)
print(d.max())
print(d.min())
print(d.sum())

c = np.arange(20).reshape(4,5)
c.sum(axis=0)
c.sum(axis=1)
c.cumsum(axis=1)


c = np.sqrt(c)
print(type(c))
c
c.argmax()
c.argmin()
np.all(c>=0)
np.any(c<=0)
c

b=rg.random((2,3))
b
np.sort(b,axis=None)
np.argsort(b,axis=None)

c = np.arange(20).reshape(4,5)
np.trace(c)

np.where(c<10, c*10, c)
c


t = (0,0)
type(t)





























