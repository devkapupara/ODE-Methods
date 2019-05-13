from math import *

def rk4(f, f_actual, t, y, p, h, analytical = False):
	n = int((p-t)/h)

	separator = "-"*100 if analytical else "-"*40
	if analytical:
		print(f'\nt\t\t|\tEstimate\t\t|\tExact\t\t\t|\tError\n{separator}')
		print(f'{t:.3f}\t\t|\t{y:.9f}\t\t|\t{f_actual(t):.9f}\t\t|\t{abs(f_actual(t)-y):.9f}')
	else:
		print(f'\nt\t\t|\tEstimate\n{separator}')
		print(f'{t:.3f}\t\t|\t{y:.9f}')

	for i in range(n):
		k1 = h*f(t, y)
		k2 = h*f(t + h/2, y + k1/2)
		k3 = h*f(t + h/2, y + k2/2)
		k4 = h*f(t + h, y + k3)
		y = y + (k1 + 2*k2 + 2*k3 + k4)/6
		t += h
		actual = f_actual(t)
		print(f'{t:.3f}\t\t|\t{y:.9f}', end = '')
		print(f'\t\t|\t{actual:.9f}\t\t|\t{abs(actual-y):.9f}' if analytical else '')
	print(separator)

def main():

	# Define these functions depending on the problem.
	f = lambda t, y: -20*(y-t*t) + 2*t
	f_analytical = lambda t: t*t + exp(-20*t)/3

	choice = int(input("1) RK-4 Estimator\n2) RK-4 Analytical\n"))
	if choice == 2:
		print("Make sure you have defined the analytic function correctly.")

	t0 = float(input("t0 = "))
	y0 = float(input("y0 = "))
	p = float(input("Evaluation point = "))
	h = float(input("Step-Size = "))
	rk4(f, f_analytical, t0, y0, p, h, choice == 2)

if __name__ == '__main__':
	main()
