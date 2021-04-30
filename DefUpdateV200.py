from DefEqnV200 import Equations as eqn

class update:
    def __init__(self,x1,x2,x3,y1,y2,y3,a1,a2,a3,alpha1,alpha2,alpha3,omega1,omega2,omega3,eta2,eta3,kappa1,kappa2):

        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.alpha1 = alpha1
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.omega1 = omega1
        self.omega2 = omega2
        self.omega3 = omega3
        self.eta2 = eta2
        self.eta3 = eta3
        self.kappa1 = kappa1
        self.kappa2 = kappa2

    def __repr__ (self):
        return 'x1{0},x2{1},x3{2},y1{3},y2{4},y3{5},a1{6},a2{7},a3{8},alpha1{9},alpha2{10},alpha3{11},omega1{12},omega2{13},omega3{14},eta2{15},eta3{16},kappa1{17},kappa2{18}'.format(self.x1,self.x2,self.x3,self.y1,self.y2,self.y3,self.a1,self.a2,self.a3,self.alpha1,self.alpha2,self.alpha3,self.omega1,self.omega2,self.omega3,self.eta2,self.eta2,self.kappa1,self.kappa2)

    def RunKut(self,step):
        x1k1 = step * eqn.x1dot(self,self.x1,self.y1,self.x2,self.x3,self.alpha1,self.a1,self.omega1,self.eta2,self.eta3,self.kappa1)
        y1k1 = step * eqn.y1dot(self,self.x1,self.x2,self.x3,self.y1,self.y2,self.y3,self.alpha1,self.a1,self.omega1,self.eta2,self.eta3,self.kappa1)
        x2k1 = step * eqn.x2dot(self,self.x2,self.x3,self.y2,self.alpha2,self.a2,self.omega2,self.kappa2)
        y2k1 = step * eqn.y2dot(self,self.x2,self.x3,self.y2,self.alpha2,self.a2,self.omega2,self.kappa2)
        x3k1 = step * eqn.x3dot(self,self.x2,self.x3,self.y3,self.alpha3,self.a3,self.omega3)
        y3k1 = step * eqn.y3dot(self,self.x2,self.x3,self.y3,self.alpha3,self.a3,self.omega3)

        x1k2 = step * eqn.x1dot(self, (self.x1 + (x1k1/2)), (self.y1 + (y1k1/2)), self.x2 + (x2k1/2), self.x3 + (x3k1/2),self.alpha1,self.a1,self.omega1,self.eta2,self.eta3,self.kappa1)
        y1k2 = step * eqn.y1dot(self, (self.x1 + (x1k1/2)), self.x2 + (x2k1/2),self.x3 + (x3k1/2),self.y1 + (y1k1/2),self.y2 + (y2k1/2),self.y3 + (y3k1/2),self.alpha1,self.a1,self.omega1,self.eta2,self.eta3,self.kappa1)
        x2k2 = step * eqn.x2dot(self,self.x2 + (x2k1/2),self.x3 + (x3k1/2),self.y2 + (y2k1/2),self.alpha2,self.a2,self.omega2,self.kappa2)
        y2k2 = step * eqn.y2dot(self,self.x2 + (x2k1/2),self.x3 + (x3k1/2),self.y2 + (y2k1/2),self.alpha2,self.a2,self.omega2,self.kappa2)
        x3k2 = step * eqn.x3dot(self,self.x2 + (x2k1/2),self.x3 + (x3k1/2),self.y3 + (y3k1/2),self.alpha3,self.a3,self.omega3)
        y3k2 = step * eqn.y3dot(self,self.x2 + (x2k1/2),self.x3+(x3k1/2),self.y3+(y3k1/2),self.alpha3,self.a3,self.omega3)

        x1k3 = step * eqn.x1dot(self, (self.x1 + (x1k2/2)), (self.y1 + (y1k2/2)), self.x2 + (x2k2/2), self.x3 + (x3k2/2),self.alpha1,self.a1,self.omega1,self.eta2,self.eta3,self.kappa1)
        y1k3 = step * eqn.y1dot(self,self.x1 + (x1k2/2),self.x2 + (x2k2/2), self.x3 + (x3k2/2),self.y1 + (y1k2/2),self.y2 + (y2k2/2),self.y3 + (y3k2/2),self.alpha1,self.a1,self.omega1,self.eta2,self.eta3,self.kappa1)
        x2k3 = step * eqn.x2dot(self,self.x2 + (x2k2/2),self.x3 + (x3k2/2),self.y2 + (y2k2/2),self.alpha2,self.a2,self.omega2,self.kappa2)
        y2k3 = step * eqn.y2dot(self,self.x2 + (x2k2/2),self.x3 + (x3k2/2),self.y2 + (y2k2/2),self.alpha2,self.a2,self.omega2,self.kappa2)
        x3k3 = step * eqn.x3dot(self,self.x2 + (x2k2/2),self.x3 + (x3k2/2),self.y3 + (y3k2/2),self.alpha3,self.a3,self.omega3)
        y3k3 = step * eqn.y3dot(self,self.x2 + (x2k2/2),self.x3+(x3k2/2),self.y3+(y3k2/2),self.alpha3,self.a3,self.omega3)

        x1k4 = step * eqn.x1dot(self, (self.x1 + (x1k3)), (self.y1 + (y1k3)), self.x2 + (x2k3), self.x3 + (x3k3),self.alpha1,self.a1,self.omega1,self.eta2,self.eta3,self.kappa1)
        y1k4 = step * eqn.y1dot(self,self.x1 + (x1k3),self.x2 + (x2k3), self.x3 + (x3k3),self.y1 + (y1k3),self.y2 + (y2k3),self.y3 + (y3k3),self.alpha1,self.a1,self.omega1,self.eta2,self.eta3,self.kappa1)
        x2k4 = step * eqn.x2dot(self,self.x2 + (x2k3),self.x3 + (x3k3),self.y2 + (y2k3),self.alpha2,self.a2,self.omega2,self.kappa2)
        y2k4 = step * eqn.y2dot(self,self.x2 + (x2k3),self.x3 + (x3k3),self.y2 + (y2k3),self.alpha2,self.a2,self.omega2,self.kappa2)
        x3k4 = step * eqn.x3dot(self,self.x2 + (x2k3),self.x3 + (x3k3),self.y3 + (y3k3),self.alpha3,self.a3,self.omega3)
        y3k4 = step * eqn.y3dot(self,self.x2 + (x2k3),self.x3+(x3k3),self.y3+(y3k3),self.alpha3,self.a3,self.omega3)

        self.x1 = self.x1 + ( (1/6) * (x1k1 + (2 * x1k2) + (2 * x1k3) + x1k4) )
        self.y1 = self.y1 + ( (1/6) * (y1k1 + (2 * y1k2) + (2 * y1k3) + y1k4) )
        self.x2 = self.x2 + ( (1/6) * (x2k1 + (2 * x2k2) + (2 * x2k3) + x2k4) )
        self.y2 = self.y2 + ( (1/6) * (y2k1 + (2 * y2k2) + (2 * y2k3) + y2k4) )
        self.x3 = self.x3 + ( (1/6) * (x3k1 + (2 * x3k2) + (2 * x3k3) + x3k4) )
        self.y3 = self.y3 + ( (1/6) * (y3k1 + (2 * y3k2) + (2 * y3k3) + y3k4) )

