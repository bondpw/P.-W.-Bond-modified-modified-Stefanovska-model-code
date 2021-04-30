import math as ma

class Equations:
    def x1dot(self,x1,y1,x2,x3,alpha,a,omega1,eta2,eta3,kappa1):
        return -(x1 * alpha * ( ma.sqrt( x1**2 + y1**2 )  - a ) ) - ( y1 * (omega1 + (kappa1 * ( x2 + x3 ) ) ) ) + ( x2 * eta2 ) - ( x3 * eta3 )

    def y1dot(self,x1,x2,x3,y1,y2,y3,alpha,a,omega1,eta2,eta3,kappa1):
        return -(y1 * alpha * ( ma.sqrt( x1**2 + y1**2 )  - a ) ) + ( x1 * (omega1 + (kappa1 * ( x2 + x3 ) ) ) ) + ( y2 * eta2 ) - ( y3 * eta3 )

    def x2dot(self,x2,x3,y2,alpha,a,omega2,kappa2):
        return -(x2 * alpha * ( ma.sqrt( x2**2 + y2**2 )  - a ) ) - ( y2 * ( omega2 + (kappa2 * ( x3 ) ) ) ) 

    def y2dot(self,x2,x3,y2,alpha,a,omega2,kappa2):
        return -(y2 * alpha * ( ma.sqrt( x2**2 + y2**2 )  - a ) ) + ( x2 * ( omega2 + (kappa2 * ( x3 ) ) ) )

    def x3dot(self,x2,x3,y3,alpha,a,omega3):
        return -(x3 * alpha * ( ma.sqrt( x3**2 + y3**2 )  - a ) ) - ( y3 * omega3 ) 

    def y3dot(self,x2,x3,y3,alpha,a,omega3):
        return -(y3 * alpha * ( ma.sqrt( x3**2 + y3**2 )  - a ) ) + ( x3 * omega3 ) 

