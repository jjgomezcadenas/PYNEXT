from . system_of_units import *
from math import *

class PMT:
    def __init__(self,name='R1141', D=3*2.5*cm, QE=0.3,
                 a_bi214=1 * mBq, a_tl208= 1* mBq):
        """
        Defines a PMT of diameter D, quantum efficiency QE and Activity A
        """
        self.name    = name
        self.D       = D
        self.R       = D / 2
        self.QE      = QE
        self.a_bi214 = a_bi214
        self.a_tl208 = a_tl208
        self.S       = pi*self.R**2

    def __str__(self):
        s="""
        PMT name = %s
        PMT Diameter = %7.2f cm
        PMT Surface = %7.2f cm2
        PMT QE = %7.2f
        bi214 activity = %7.2f mBq
        tl208 activity = %7.2f mBq
        """%(self.name, self.D / cm, self.S / cm2, self.QE,
             self.a_bi214/mBq,
             self.a_tl208/mBq)
        return s

    __repr__ = __str__


class SiPM:

    def __init__(self,name='Hamamatsu',L=1.0*mm, QE=0.5,TPB=0.5,
                 a_bi214=1 * muBq, a_tl208= 1* muBq):
        """
        Defines a SiPM of size L, quantum efficiency QE and TPB efficiency TPB
        """
        self.name = name
        self.L       = L
        self.QE      = QE
        self.TPB     = TPB
        self.PDE     = QE*TPB
        self.S       = L**2
        self.a_bi214 = a_bi214
        self.a_tl208 = a_tl208

    def __str__(self):
        s="""
        SiPM name = %s
        SiPM size = %7.2f mm
        SiPM Surface = %7.2f mm2
        SiPM QE = %7.2f
        SiPM TPB eff = %7.2f
        SiPM global PDE = %7.2f
        bi214 activity = %7.2f muBq
        bi214 activity = %7.2f muBq
        """%(self.name, self.L / mm, self.S / mm2, self.QE, self.TPB,
             self.PDE, self.a_bi214/muBq,
             self.a_tl208 / muBq)
        return s

    __repr__ = __str__
