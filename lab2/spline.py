import numpy as np
import tridiagonal as tdg

class Spline:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.H = []
        self.Q = []

        for i in range(len(X)-1):
            self.H.append(X[i+1]-X[i])

    def calc_q(self):
        coeffs = [[2/3,1/6]]
        for i in range(1,len(self.X)-3):
            coeffs.append([1/6, 2/3, 1/6])
        coeffs.append([1/6, 2/3])

        F = []

        for i in range(len(coeffs)):
            F.append( -(-self.Y[i+1]-self.Y[i])/self.H[i] + (self.Y[i+2]-self.Y[i+1])/self.H[i+1] )

        tdg_solver = tdg.Tridiag(coeffs,F)
        self.Q = tdg_solver.solve()
        self.Q.insert(0,0)
        self.Q.append(0)


    def build_spline(self,X_plot):
        self.calc_q()
        j = 0
        S = []

        for i in range(len(self.X)-1):
            h = self.H[i]
            q0 = self.Q[i]
            q1 = self.Q[i+1]
            x0 = self.X[i]
            x1 = self.X[i+1]
            y0 = self.Y[i]
            y1 = self.Y[i+1]
            # print("x1:",x1)

            if X_plot[j] == x0:
                # print("x_plot:",X_plot[j])
                S.append(y0)
                j += 1

            while True:
                xj = X_plot[j]
                # print("x_plot:",X_plot[j])
                if xj >= x1:
                    # print("break")
                    break

                Sj = q0 * (x1-xj)**3/(6*h) + q1 * (xj-x0)**3/(6*h) + (y0/h - q0*h/6)*(x1-xj) + (y1/h - q1*h/6)*(xj-x0)
                S.append(Sj)
                j += 1

                # print("x_plot:",X_plot[j])
            if X_plot[j] == x1:
                S.append(y1)
                j += 1

        return S

    def calc_error(X,Y):
        sum = 0
        for i in len(X):
            sum += (X[i]-Y[i])**2

        return np.sqrt(sum)
