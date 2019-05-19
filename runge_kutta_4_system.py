from math import *

def rk4_system(f, f_actual, t, y, p, h, N):
	n = int((p-t)/h)
	zeroes = [0 for i in range(N)]
	k = [zeroes.copy() for i in range(4)]
	y_temp = zeroes.copy()
	results = [zeroes.copy() for i in range(n)]

	for i in range(n):

		for j in range(N):												# Filling in the k1_x for all given functions
			k[0][j] = h*f[j](t, *y)

		for j in range(N):												# Updating y to pass into the next k2_x calculations
			y_temp[j] = y[j] + k[0][j]/2

		for j in range(N):												# Filling in the k2_x for all given functions
			k[1][j] = h*f[j](t+h/2, *y_temp)

		for j in range(N):												# Again need to update the y's for k3_x calculations
			y_temp[j] = y[j] + k[1][j]/2

		for j in range(N):												# Filling in the k3_x for all given functions
			k[2][j] = h*f[j](t+h/2, *y_temp)

		for j in range(N):												# Again need to update the y's for k3_x calculations
			y_temp[j] = y[j] + k[2][j]

		for j in range(N):												# Filling in the k4_x for all given functions
			k[3][j] = h*f[j](t+h, *y_temp)

		for j in range(N):												# Finally, we calculate the y and prepare for the next iteration
			y[j] += (k[0][j] + 2*k[1][j] + 2*k[2][j] + k[3][j])/6
			results[i][j] = y[j]										# I add the final intermediate y to results in order to store them.

		t += h

	return results


def main():
	# Define these functions depending on the problem.
	f = [
		lambda t, u1, u2, u3, u4: u3,
		lambda t, u1, u2, u3, u4: u4,
		lambda t, u1, u2, u3, u4: -u1*(u1*u1 + u2*u2)**(-1.5),
		lambda t, u1, u2, u3, u4: -u2*(u1*u1 + u2*u2)**(-1.5)
	]
	

	f_analytical = [
		lambda t: (exp(5*t) - exp(-t))/3 + exp(2*t), 
		lambda t: (exp(5*t) - 2*exp(-t))/3 + t*t*exp(t)
	]

	N = len(f)
	y = [0]*N

	t0 = float(input("t0 = "))

	for i in range(N):
		y[i] = float(input(f"y0_{i+1} = "))
	p = float(input("Evaluation point = "))
	h = float(input("Enter Step-Size: "))

	print(rk4_system(f, f_analytical, t0, y, p, h, N))

if __name__ == '__main__':
	main()
