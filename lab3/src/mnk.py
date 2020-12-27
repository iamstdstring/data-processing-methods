import numpy as np

class Mnk:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.N = len(X)

    def solve1(self):
        sum_x = sum(self.X)
        sum_x2 = sum([x**2 for x in self.X])

        sum_y = sum(self.Y)
        sum_xy = sum(self.Y[i] * self.X[i] for i in range(self.N))

        a = np.array([[self.N + 6, sum_x],[sum_x,sum_x2]])
        b = np.array([sum_y,sum_xy])

        coeffs = np.linalg.solve(a,b)

        return coeffs.tolist()


    def solve2(self):
        sum_x = sum(self.X)
        sum_x2 = sum([x**2 for x in self.X])
        sum_x3 = sum([x**3 for x in self.X])
        sum_x4 = sum([x**4 for x in self.X])

        sum_y = sum(self.Y)
        sum_xy = sum(self.Y[i] * self.X[i] for i in range(self.N))
        sum_x2y = sum(self.Y[i] * self.X[i]**2 for i in range(self.N))

        a = np.array([[self.N + 6, sum_x,sum_x2],[sum_x,sum_x2,sum_x3],[sum_x2,sum_x3,sum_x4]])
        b = np.array([sum_y,sum_xy,sum_x2y])

        coeffs = np.linalg.solve(a,b)

        return coeffs.tolist()

    def calc_error(X,Y):
        sum = 0
        for i in len(X):
            sum += (X[i]-Y[i])**2

        return np.sqrt(sum)
