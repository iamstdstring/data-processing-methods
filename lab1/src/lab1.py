import numpy as np
import matplotlib.pyplot as plt
import interpolate as my_ip
from datetime import datetime

def func(x):
	return x**4 * np.exp(x)

date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
log = "logs/lab1_"+date_time+".log"

X = [0,1/4,1/2,3/4,1]
Y = []
a = 0
b = 1

for x in X:
	Y.append(func(x))

eps = 0.01
X_prec = [i * eps for i in range(a,int(b/eps)+1)]
Y_prec = [func(x) for x in X_prec]

ip = my_ip.Interpolate(func,a,b,X,Y,eps)

while True:
	print("Choose interpolation method:")
	print("1. Linear Lagrange")
	print("2. Quadratic Lagrange")
	print("3. Newton")

	try:
		x = int(input("\n"))
	except ValueError:
		print("bad input\n")
		continue

	if x == 1:
		Y_ipl = ip.lagrLinear()
		break

	elif x == 2:
		Y_ipl = ip.lagrQuadr()
		break

	elif x == 3:
		Y_ipl = ip.Newton()
		break

	else:
		print("bad input\n")

plt.plot(X_prec,Y_prec,color='r')
plt.plot(X_prec,Y_ipl,color='b')
plt.plot(X,Y,'ro')
plt.show()