import numpy as np
import matplotlib.pyplot as plt
import mnk

def func(x):
    return x**4 * np.exp(x) + np.random.uniform(-0.1, 0.1)

n = 16
X = [i * (1/n) for i in range(n+1)]
Y = [func(x) for x in X]

#returns coeffs
mnk_base = mnk.Mnk(X,Y)

mnk_1 = mnk_base.solve1()
mnk_2 = mnk_base.solve2()

Y_mnk1 = [mnk_1[0]+mnk_1[1]*x for x in X]
Y_mnk2 = [mnk_2[0]+mnk_2[1]*x + mnk_2[2]*x**2 for x in X]

plt.plot(X,Y_mnk1,color='r')
plt.plot(X,Y_mnk2,color='g')
plt.plot(X,Y,color='b')

plt.show()

err1 = sum([(Y[i]-Y_mnk1[i])**2 for i in range(len(Y))])
err2 = sum([(Y[i]-Y_mnk2[i])**2 for i in range(len(Y))])

print("err 1 =", err1)
print("err 2 =", err2)