class Tridiag:
    def __init__(self, coeffs, F):
        self.coeffs = coeffs # list of lists
        self.F = F
        self.n = len(coeffs)

    def solve(self):
        Alph = [-self.coeffs[0][1]/self.coeffs[0][0]]
        Bet = [self.F[0]/self.coeffs[0][0]]

        for i in range(1,len(self.F)-1):
            A = self.coeffs[i][0]
            B = self.coeffs[i][1]
            C = self.coeffs[i][2]
            Fi = self.F[i]

            Alph.append(-C/(Alph[i-1]*A+B))
            Bet.append((Fi-A*Bet[i-1])/(Alph[i-1]*A+B))

        X = [(self.F[-1] - self.coeffs[-1][0] * Bet[-1]) / (self.coeffs[-1][1] + (self.coeffs[-1][0] * Alph[-1]))]

        for i in range(len(self.F)-2,-1,-1):
            X.append(Alph[i]*X[-1] + Bet[i])

        # print("Alph:",Alph)
        # print("Bet:",Bet)
        X.reverse()

        return X
