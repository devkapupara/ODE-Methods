from math import *

correctors = [
	[2, 3, -1],
	[12, 23, -16, 5],
	[24, 55, -59, 37, -9],
	[720, 1901, -2774, 2616, -1274, 251]
]

def abN_actual(f, f_actual, t, y, p, h, N):
	corrector = correctors[N-2]
	n = int((p-t)/h)
	time = [t+h*i for i in range(n+1)]
	values = [f_actual(time[i]) for i in range(N)]

	for i in range(N, n+1):
		fix = 0
		for j in range(N):
			fix += corrector[j+1] * f(time[i-j-1], values[i-j-1])
		y = values[i-1] + h/corrector[0]*fix
		values.append(y)

	print(f"AB-{N} Method")
	print("-"*40)
	print(f't\t\t|\tEstimate')
	print("-"*40)

	for i in range(len(values)):
		print(f'{time[i]:.3f}\t\t|\t{values[i]:.9f}')
	print("-"*40)

def abN_rk4(f, f_actual, t, y, p, h, N, correction = False):
	corrector = correctors[N-2]
	n = int((p-t)/h)
	time = [t+h*i for i in range(n+1)]
	y_values = [y]

	for i in range(1,N):
		y_values.append(rk4(f, time[i-1], y_values[i-1]))

	for i in range(N, n+1):
		fix = 0
		for j in range(N):
			fix += corrector[j+1] * f(time[i-j-1], y_values[i-j-1])
		yn = y_values[i-1] + h/corrector[0]*fix

		# This is a special case of AB-4 Predictor Corrector, hence the correction parameter for adjustment.
		if N == 4 and correction:
			fix = 9*f(time[i], yn)
			coeffs = [19, -5, 1]
			for j in range(len(coeffs)):
				fix += coeffs[j] * f(time[i-j-1], y_values[i-j-1])
			yn = y_values[i-1] + h/24*fix

		y_values.append(yn)

	print(f"AB-{N} {'Predictor-Corrector' if correction else ''} Method")
	print("-"*70)
	print(f't\t\t|\tEstimate\t\t|\tActual')
	print("-"*70)

	for i in range(len(y_values)):
		print(f'{time[i]:.3f}\t\t|\t{y_values[i]:.9f}\t\t|\t{f_actual(time[i]):.9f}')
	print("-"*70)

def rk4(f, t, y):
	k1 = h*f(t, y)
	k2 = h*f(t + h/2, y + k1/2)
	k3 = h*f(t + h/2, y + k2/2)
	k4 = h*f(t + h, y + k3)
	return y + (k1 + 2*k2 + 2*k3 + k4)/6

if __name__ == '__main__':

	f = lambda t, y: cos(2*t) + sin(3*t)

	f_actual = lambda t: sin(2*t)/2 - cos(3*t)/3 + 4/3

	t = float(input("t0: "))
	y = float(input("y0: "))
	p = float(input("Evaluation point: "))
	h = float(input("Step size: "))
	N = int(input("Which AB-N method to use? [2-5]: "))
	#abN_actual(f, f_actual, t, y, p, h, N)
	abN_rk4(f, f_actual, t, y, p, h, N, True)
