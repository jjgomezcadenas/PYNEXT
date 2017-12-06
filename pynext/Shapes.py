"""
Shapes
Defines a material shape
"""
from . system_of_units import *
from math import pi
import sys

class Sphere:

    def __init__(self, R):
        """
       Defines a sphere of radius R
       """
        self.R = R

    @property
    def V(self):
        return (4 /3) * pi * self.R**3

    @property
    def S(self):
        return 4 * pi * self.R**2

    def RV(self,V):
        return ((3/(4 * pi)) * V )**(1./3.)

    def __str__(self):

        s= """
        Sphere(R = %7.2e, V = %7.2e, S = %7.2e)
        """%(self.R,
             self.V,
             self.S)

        return s

    __repr__ = __str__


class Brick:

    def __init__(self, width, heigth, thickness):
        """
       Defines a Brick of dimensions Width, Heigth, Thickness
       """
        self.w = width
        self.h = heigth
        self.t = thickness
    @property
    def width(self):
        return self.w

    @property
    def heigth(self):
        return self.h

    @property
    def thickness(self):
        return self.t

    @property
    def V(self):
        return self.w * self.h * self.t
    @property
    def S(self):
        return 2 * self.w * self.h + 2 * self.w * self.t + 2 * self.h * self.t

    def __str__(self):

        s= """
        Brick(width = %7.2e, heigth = %7.2e, thickness = %7.2e, V = %7.2e, S = %7.2e)
        """%(self.width, self.heigth, self.thickness,
             self.V,
             self.S)

        return s

    __repr__ = __str__

class Wall:
    """
    A wall made of bricks
    """
    def __init__(self, brick):
        self.b = brick

    def number_of_bricks(self, w, h, t):
        nw = w * 1 / self.b.w
        nh = h * 1 / self.b.h
        nt = t * 1 / self.b.t

        return nw * nh * nt


class SphereShell(Sphere):

    def __init__(self, R , t):
        """
        Defines a spherical shell of radius R and thickness t
        """

        Sphere.__init__(self, R)
        self.t = t

    @property
    def V(self):
        V0 = (4/3) * pi * self.R**3
        V1 = (4/3) * pi * (self.R + self.t)**3
        return V1-V0
    @property
    def S(self):
        return 4 * pi * (self.R + self.t)**2

    def inner_surface(self):
        return 4 * pi * self.R**2

    def __str__(self):

        s= """
        SphereShell(R = %7.2e, t = %7.2e, V = %7.2e, S = %7.2e)
        """%(self.R,
             self.t,
             self.V,
             self.S)

        return s

    __repr__ = __str__

class SemiSphereShell(SphereShell):

    def __init__(self, R, t):
        """
       Defines a semi-spherical shell of radius R and thickness t
       """

        SphereShell.__init__(self, R, t)

    @property
    def V(self):
        return SphereShell.V / 2


    def S(self):
        return SphereShell.S / 2

    def inner_surface(self):
        return SphereShell.inner_surface() / 2


class Cylinder:

    def __init__(self, R, L):
        """
       Defines a cylinder of radius R and length L
       """
        self.R = R
        self.L = L

    @property
    def EndCapSurface(self):
        return pi * self.R**2

    @property
    def V(self):
        return pi * self.R**2 * self.L

    @property
    def ShellSurface(self):
        return 2 * pi * self.R * self.L

    @property
    def S(self):
        return self.ShellSurface + self.EndCapSurface

    def __str__(self):

        s= """
        Cylinder(R = %7.2e, L = %7.2e, V = %7.2e, S = %7.2e)
        Surface End-cap = %7.2e; Surface Shell = %7.2e
        """%(self.R, self.L,
             self.V,
             self.S,
             self.EndCapSurface,
             self.ShellSurface
             )

        return s

    __repr__ = __str__


class CylinderShell:

    def __init__(self,Rin,Rout,L):
        """
       Defines a cylinder shell of:
       Rin:   - internal radius
       Rout:  - external radius
       Length - L
       """

        self.Rin = Rin
        self.Rout = Rout
        self.L = L

    @property
    def InnerVolume(self):
        return pi * self.Rin**2 * self.L

    @property
    def ShellVolume(self):
        return pi * (self.Rout**2 - self.Rin**2) * self.L

    @property
    def InnerSurface(self):
        return 2 * pi * self.Rin * self.L

    @property
    def ShellSurface(self):
        return 2 * pi * self.Rout * self.L

    def __str__(self):

        s= """
        CylinderShell(Rin = %7.2e, Rout = %7.2e, L = %7.2e)
        Inner Volume  = %7.2e; Shell Volume = %7.2e
        Inner Surface = %7.2e; Shell Surface = %7.2e
        """%(self.Rin,
             self.Rout,
             self.L,
             self.InnerVolume,
             self.ShellVolume,
             self.InnerSurface,
             self.ShellSurface
             )

        return s

    __repr__ = __str__


class Disk:

    def __init__(self,R,t):
        """
        Defines a Disk of radius R and thickness t
        """
        self.R = R
        self.t = t

    @property
    def S(self):
        return pi * self.R**2

    @property
    def V(self):
        return self.S * self.t

    def __str__(self):

        s= """
        Disk(R = %7.2e, t = %7.2e, S = %7.2e, V = %7.2e)
        """%(self.R,
             self.t,
             self.S,
             self.V
             )

        return s

    __repr__ = __str__

FlatPlate = Disk



def Spheres():
    R=0.43*m
    R2=1*m
    t=1*cm
    sp = Sphere(R)
    print("""
    Sphere of radius %7.1f cm
    Volume %7.2f m3
    Surface %7.2f m2
    Radius for Volume is  %7.1f cm
    """%(R/cm,sp.V()/m3, sp.S()/m2, sp.RV(sp.V())/cm))

    ssp=SphereShell(R2,t)
    print( """
    Sphere Shell of radius %7.1f cm
    Volume %7.2f m3
    Surface %7.2f m2
    """%(R2/cm,ssp.V()/m3, ssp.S()/m2))

    ssp2=SemiSphereShell(R2,t)
    print("""
    Semi Sphere Shell of radius %7.1f cm
    Volume %7.2f m3
    Surface %7.2f m2
    """%(R2/cm,ssp2.V()/m3, ssp2.S()/m2))

if __name__ == '__main__':

    Next100()
    Spheres()
