import matplotlib as plt


class Interpolate():
	def __init__(self,func,a,b,X,Y,eps,logfile=None):
		self.a = a
		self.b = b
		self.func = func
		self.X = X
		self.Y = Y
		self.eps = eps
		self.logfile = logfile

	def lagrLinear(self):
		polCnt = len(self.X)-1 # polynom count
		polynoms = []

		if self.logfile:
			logfile = open(self.logfile, 'w')
		else:
			logfile = None


		for i in range(polCnt):

			x0 = self.X[i]
			x1 = self.X[i+1]
			y0 = self.Y[i]
			y1 = self.Y[i+1]
			
			if logfile:
				print("Linear Lagrange Polynom for x: [", x0,",",x1,"]:",sep='',file=logfile)

			# F(x) = ax+b
			a = y0/(x0-x1) + y1/(x1-x0)
			b = y0*x1/(x1-x0) + y1*x0/(x0-x1)

			if logfile:
				if b < 0:
					print(a,"x - ", -b, "\n", sep='',file=logfile)
				else:
					print(a,"x + ", b, "\n", sep='',file=logfile)

			polynoms.append([a,b])

		X = [ i*self.eps for i in range(self.a, int(self.b/self.eps)+1) ]
		Y = []

		i = 0 # [x0,x1,x2,..]
		j = 0 # counter for plot points [a,a+eps,..]

		while j < len(X) and i < len(self.X):
			
			while True:

				x = X[j]

				a = polynoms[i][0]
				b = polynoms[i][1]

				Y.append(a*x+b)

				j += 1

				if x >= self.X[i+1]:
					break

			i += 1

		return Y

	def lagrQuadr(self):
		polCnt = len(self.X)-1 # polynom count
		polynoms = []

		if self.logfile:
			logfile = open(self.logfile, 'w')
		else:
			logfile = None


		for i in range(0,polCnt,2):

			x0 = self.X[i]
			x1 = self.X[i+1]
			x2 = self.X[i+2]
			y0 = self.Y[i]
			y1 = self.Y[i+1]
			y2 = self.Y[i+2]

			p1 = x0 - x1
			p2 = x0 - x2
			p3 = x1 - x2
			
			if logfile:
				print("Quadratic Lagrange Polynom for x: [", x0,",",x2,"]:",sep='',file=logfile)

			# F(x) = ax^2+bx+c
			a = y0/(p1*p2) + y1/(-p1*p3) + y2/(p2*p3)
			b = y0*(x1+x2)/(-p1*p2) + y1*(x0+x2)/(p1*p3) + y2*(x0+x1)/(-p2*p3)
			c = y0*(x1*x2)/(p1*p2) + y1*(x0*x2)/(-p1*p3) + y2*(x0*x1)/(p2*p3)

			if logfile:
				if b < 0:
					print(a,"x^2 - ", -b, "\n", sep='', end='', file=logfile)
				else:
					print(a,"x^2 + ", b, "\n", sep='', end='', file=logfile)

				if c < 0:
					print("x - ", -c, "\n", sep='', file=logfile)
				else:
					print("x + ", c, "\n", sep='', file=logfile)

			polynoms.append([a,b,c])

		X = [ i*self.eps for i in range(self.a, int(self.b/self.eps)+1) ]
		Y = []

		i = 0 # [x0,x1,x2,..]
		j = 0 # counter for plot points [a,a+eps,..]

		while j < len(X) and i < len(self.X):
			
			while True:
				x = X[j]

				a = polynoms[int(i/2)][0]
				b = polynoms[int(i/2)][1]
				c = polynoms[int(i/2)][2]

				Y.append(a*x**2+b*x+c)

				j += 1

				if x >= self.X[i+2]:
					break

			i += 2

		return Y


	def divDif(self, X):
		if len(X) == 1:
			return self.func(X[0])

		return (self.divDif(X[1:]) - self.divDif(X[:-1])) / (X[-1] - X[0])


	def Newton(self):
		x0, x1, x2, x3, x4 = self.X

		F0, F1, F2, F3, F4 = [self.divDif(self.X[:i]) for i in range(1,6,1)]

		# a*x^4 + b*x^3 + c*x^2 + d*x + e
		a = F4
		b = F3 - F4*(x0+x1+x2+x3)
		c = F2 - F3*(x0+x1+x2) + F4*(x0*x1+x0*x2+x0*x3+x1*x2+x1*x3+x2*x3)
		d = F1 - F2*(x0+x1) + F3*(x0*x1+x0*x2+x1*x2) - F4*(x0*x1*x2+x0*x1*x3+x0*x2*x3+x1*x2*x3)
		e = F0 - F1*x0 + F2*(x0*x1) - F3*(x0*x1*x2) + F4*(x0*x1*x2*x3)


		X = [ i*self.eps for i in range(self.a, int(self.b/self.eps)+1) ]
		Y = []

		i = 0 # [x0,x1,x2,..]
		j = 0 # counter for plot points [a,a+eps,..]

		for x in X:
			
			Y.append(a*x**4 + b*x**3 + c*x**2 + d*x + e)

		return Y




