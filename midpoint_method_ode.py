from math import *

def midpoint(f, f_actual, t, y, p, h = None, n = None):
	if h == None:
		h = (p-t)/n
	if n == None:
		n = int((p-t)/h)

	print(f't\t\t|\tEstimate\t\t|\tExact\t\t\t|\tError')
	print("-"*100)
	print(f'{t:.3f}\t\t|\t{y:.9f}\t\t|\t{f_actual(t):.9f}\t\t|\t{abs(f_actual(t)-y):.9f}')

	for i in range(n):
		y = y + h*f(t + h/2, y + h/2*f(t, y))
		t += h
		actual = f_actual(t)
		print(f'{t:.3f}\t\t|\t{y:.9f}\t\t|\t{actual:.9f}\t\t|\t{abs(actual-y):.9f}')
	print("-"*100)

def main():
	# Define these functions depending on the problem.
	f = lambda t, y: 1 + y/t
	f_analytical = lambda t: t*(log(t) + 2)

	t0 = float(input("t0 = "))
	t = t0
	y0 = float(input("y0 = "))
	p = float(input("Evaluation point = "))
	h = ""
	n = ""
	while h.strip() == "" and n.strip() == "":
		h = input("Enter H [Leave blank if you want to enter N]: ")
		n = input("Enter N [Leave blank if H already inputted]: ")
	if h == "":
		n = int(n)
		h = None
	else:
		h = float(h)
		n = None
	midpoint(f, f_analytical, t0, y0, p, h, n)

if __name__ == '__main__':
	main()
