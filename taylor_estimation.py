from math import *

g = 9.8
kbym = 0.002/0.11
print(kbym)

yp = lambda t, y: -g - kbym*y*abs(y)
ypp = lambda t, y, ypv: -kbym*(ypv*abs(y)+y*abs(ypv))

series = lambda h, y, yp, ypp: y + h*yp + h*h*ypp/2

a = 0
b = 1
t0 = 0
y0 = 8
h = 0.1
n = int((b-t0)/h)

for i in range(n):
	d1 = yp(t0, y0)
	d2 = ypp(t0, y0, d1)
	print(f"y({t0:.3f}) = {y0}\ny'({t0:.3f}) = {d1}\ny''({t0:.3f}) = {d2}")
	result = series(h, y0, d1, d2)
	t0 += h
	print(f'y({t0:.3f}) = {result:.9f}\n')
	y0 = result
	