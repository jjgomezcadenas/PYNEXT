"""
Shapes
Defines a material shape
"""
from . system_of_units import *
from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    """An abstract class representing a geometrical shape.
    In the most general case, the shape is assumed to have a thickness
    (e.g., a sphericall shell or a cylinder shell), and thus the interface
    is defined by 5 methos:
    volume, which corresponds to the volume enclosed by the shape
    shell_volume, which corresponds to the volume of the shell of thickness t
    inner_surface which defines the inner surface of the shape
    outer_surface which defines the outer surface of the shape
    thickness_surface which defines the surface of the shape due to its thickness
    thickness which defines the thickness of the shell
    """

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def shell_volume(self):
        pass

    @abstractmethod
    def inner_surface(self):
        pass

    @abstractmethod
    def outer_surface(self):
        pass

    @abstractmethod
    def thickness_surface(self):
        pass

    @abstractmethod
    def thickness(self):
        pass


class Sphere(Shape):

    def __init__(self, R):
        """
       Defines a sphere of radius R
       Notice that a Sphere has thickness = 0

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

    def volume(self):
        return self.V

    def shell_volume(self):
        return 0

    def inner_surface(self):
        return self.S

    def outer_surface(self):
        return self.S

    def thickness_surface(self):
        return 0

    def thickness(self):
        return 0

    def __str__(self):

        s= """
        Sphere(R = %7.2e, V = %7.2e, S = %7.2e)
        """%(self.R,
             self.V,
             self.S)

        return s

    __repr__ = __str__

class SphereShell(Shape):

    def __init__(self, R , t):
        """
        Defines a spherical shell of radius R and thickness t
        """

        self.R = R
        self.t = t

    @property
    def V(self):
        v0 = (4/3) * pi * self.R**3
        v1 = (4/3) * pi * (self.R + self.t)**3
        return v1 - v0

    @property
    def S(self):
        return self.inner_surface() + self.outer_surface() + self.thickness_surface()

    def volume(self):
        return (4/3) * pi * self.R**3

    def shell_volume(self):
        return self.V

    def inner_surface(self):
        return 4 * pi * self.R**2

    def outer_surface(self):
        return 4 * pi * (self.R + self.t)**2

    def thickness_surface(self):
        return 0

    def thickness(self):
        return self.t

    def __str__(self):

        s= """
        SphereShell(R = %7.2e, t = %7.2e, V = %7.2e)
        inner surface = %7.2e
        outer surface = %7.2e
        """%(self.R,
             self.t,
             self.V,
             self.inner_surface(),
             self.outer_surface())

        return s

    __repr__ = __str__


class SemiSphereShell(Shape):

    def __init__(self, R, t):
        """
            Defines a semi-spherical shell of radius R and thickness t
        """
        self.R = R
        self.t = t
        self.ss_ = SphereShell(R, t)

    @property
    def V(self):
        return self.ss_.V / 2

    def S(self):
        return self.inner_surface() + self.outer_surface() + self.thickness_surface()

    def volume(self):
        return 0.5 * (4/3) * pi * self.R**3

    def shell_volume(self):
        return self.V

    def inner_surface(self):
        return self.ss_.inner_surface() / 2

    def outer_surface(self):
        return self.ss_.outer_surface() / 2

    def thickness_surface(self):
        return 2 * pi * self.R + self.t

    def thickness(self):
        return self.t

    def __str__(self):

        s= """
        SemiSphereShell(R = %7.2e, t = %7.2e, V = %7.2e)
        inner surface = %7.2e
        outer surface = %7.2e
        """%(self.R,
             self.t,
             self.V,
             self.inner_surface(),
             self.outer_surface())

        return s

    __repr__ = __str__


class Brick(Shape):

    def __init__(self, width, heigth, length):
        """
       Defines a Brick of dimensions width, heigth, length
       """
        self.width  = width
        self.heigth = heigth
        self.length = length

    @property
    def V(self):
        return self.width * self.heigth * self.length

    @property
    def S(self):
        w, h, l = self.width, self.heigth, self.length
        return 2 * (w * h + w * l + h * l)

    def volume(self):
        return self.V

    def shell_volume(self):
        return 0

    def inner_surface(self):
        return self.S

    def outer_surface(self):
        return self.S

    def thickness_surface(self):
        return 0

    def thickness(self):
        return 0

    def __str__(self):

        s= """
        Brick(width = %7.2e, heigth = %7.2e, length = %7.2e, V = %7.2e, S = %7.2e)
        """%(self.width, self.heigth, self.length,
             self.V,
             self.S)

        return s

    __repr__ = __str__


class Cylinder(Shape):

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
        return self.ShellSurface

    def volume(self):
        return self.V

    def shell_volume(self):
        return 0

    def inner_surface(self):
        return self.S

    def outer_surface(self):
        return self.S

    def thickness_surface(self):
        return 0

    def thickness(self):
        return 0

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


class CylinderShell(Shape):

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

    def volume(self):
        return self.InnerVolume

    def shell_volume(self):
        return self.ShellVolume

    def inner_surface(self):
        return self.InnerSurface

    def outer_surface(self):
        return self.ShellSurface

    def thickness_surface(self):
        return 2 * pi * self.Rin + self.thickness()

    def thickness(self):
        return self.Rout - self.Rin


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


class Disk(Shape)::

    def __init__(self,R,t):
        """
        Defines a Disk of radius R and thickness t
        """
        self.R = R
        self.t = t

    @property
    def S(self):
        return self.inner_surface() + self.outer_surface() + self.thickness_surface()

    @property
    def V(self):
        return pi * self.R**2 * self.t

    def volume(self):
        return self.V

    def shell_volume(self):
        return 0

    def inner_surface(self):
        return pi * self.R**2

    def outer_surface(self):
        return pi * self.t**2

    def thickness_surface(self):
        return 2 * pi *  self.R * self.t

    def thickness(self):
        return self.t

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


class Wall:
    """
    A wall made of identical bricks
    """
    def __init__(self, brick):
        self.b = brick

    def number_of_bricks(self, w, h, t):
        nw = w * 1 / self.b.width
        nh = h * 1 / self.b.heigth
        nt = t * 1 / self.b.length

        return nw * nh * nt
