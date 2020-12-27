import spline
import numpy as np
import matplotlib.pyplot as plt
import tridiagonal as tdg

def func(x):
    return x**4 * np.exp(x)

X = [0,1/4,1/2,3/4,1]
Y = [func(x) for x in X]

eps = 0.0005
X_plot = [i * eps for i in range(round(1/eps) + 1)]
Y_plot = [func(x) for x in X_plot]

spl = spline.Spline(X,Y)
S = spl.build_spline(X_plot)
# print(spl.X)
# print(len(S))
# print(len(X_plot))

plt.plot(X_plot,S,color='r')
plt.plot(X_plot,Y_plot,color='b')
plt.plot(X,Y,'ro')
plt.show()

err = [np.sqrt((S[i]-Y_plot[i])**2) for i in range(len(Y_plot))]

plt.plot(X_plot,err,color='r')
plt.show()

#
# test=[[2,-1],[5,4,2],[1,-3]]
# f_test = [3,6,2]
#
# tdg_solve = tdg.Tridiag(test,f_test)
# print(tdg_solve.solve())
