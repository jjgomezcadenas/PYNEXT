"""
Physical Volume
Defines a material medium + Shape
"""

from math import pi, exp, log
from . system_of_units import *
from . Shapes import CylinderShell
from . Shapes import SphereShell
from . Shapes import Disk
from . Material import PVMaterial

from collections import namedtuple

PVParams = namedtuple('PVParams', """name rho mu_over_rho
                                          a_bi214 a_tl208 Sm
                                          body_R body_t body_L
                                          flange_L flange_t
                                          head_t""")
CSParams = namedtuple('CSParams', """a_bi214 a_tl208 ics_t""")

class PhysicalVolume:
    def __init__(self,name, material,shape):
        """
       Defines a physical volume

       """
        self.name     = name
        self.material = material
        self.shape    = shape
        self.M        = self.shape.V * self.material.rho

    @property
    def V(self):
        return self.shape.V

    @property
    def S(self):
        return self.shape.S

    @property
    def mass(self):
        return self.M

    @property
    def activity_bi214(self):
        return self.M * self.material.mass_activity_bi214

    @property
    def activity_tl208(self):
        return self.M * self.material.mass_activity_tl208

    def activity_bi214_self_shield(self, z):
        return self.S * self.material.surface_activity(z, isotope='Bi214')

    def activity_tl208_self_shield(self, z):
        return self.S * self.material.surface_activity(z, isotope='Tl208')

    def __str__(self):

        s =  """ Physical Volume:
        Shape    = %s
        Material = %s
        Volume   = %7.2f m3
        Surface  = %7.2f m2
        Mass     = %7.2f kg
        activity Bi-214 = %7.2e Bq
        activity Tl-208 = %7.2e Bq
    """%(self.shape, self.material,
         self.V / m3, self.S / m2, self.M / kg,
         self.activity_bi214 / Bq,
         self.activity_tl208 / Bq)

        return s

    __repr__ = __str__

class PressureVessel:


    def __init__(self, pvp, csp):

        self.pvp = pvp
        self.csp = csp
        # pressure vessel shell
        pvs            = CylinderShell(Rin=pvp.body_R, Rout=pvp.body_R + pvp.body_t,
                                       L = pvp.body_L)
        # copper shield shell
        css            = CylinderShell(Rin=pvp.body_R - csp.ics_t, Rout=pvp.body_R,
                                       L = pvp.body_L)
        # copper head (end-cap)
        csh            = Disk         (R=pvp.body_R, t=csp.ics_t)
        # PV flange
        pvf            = CylinderShell(Rin=pvp.body_R, Rout=pvp.body_R + pvp.flange_L,
                                       L = pvp.flange_t)
        # PV head (end-cup)
        pvh            = Disk         (R=pvp.body_R, t=pvp.head_t)
        # PV material
        pvm            = PVMaterial   (name=pvp.name, rho=pvp.rho,
                                       mu_over_rho=pvp.mu_over_rho,
                                       a_bi214=pvp.a_bi214,
                                       a_tl208=pvp.a_tl208,
                                       Sm=pvp.Sm)
        # copper shield material
        csm           = RadioactiveMaterial(name='Cu',
                                             rho = 8.96 * g/cm3,
                                             mu_over_rho = 0.039 * cm2/g,
                                             a_bi214 = csp.a_bi214,
                                             a_tl208 = csp.a_tl208 )

        self.pvBody    = PhysicalVolume('pvBody'  , pvm, pvs)
        self.pvFlange  = PhysicalVolume('pvFlange', pvm, pvf)
        self.pvHead    = PhysicalVolume('pvHead'  , pvm, pvh)
        self.csBody    = PhysicalVolume('csBody'  , csm, css)
        self.csHead    = PhysicalVolume('csHead'  , csm, csh)

    def __str__(self):

        s =  """ Pressure Vessel:
        body    = %s
        flange  = %s
        head    = %s
        Copper Shield:
        body    = %s
        flange  = %s
        head    = %s

    """%(self.pvBody, self.pvFlange, self.pvHead,
         self.csBody, self.csHead)

        return s

    __repr__ = __str__


def Angel():
    Lf=130*cm
    Rf=53*cm

    xeShape = Cylinder(Rf,Lf)
    xeMat = Material('GXe',15)
    xe = PhysicalVolume("XenonVolume",xeMat,xeShape)

    Rbuff = 3*cm
    Zbuff = 8*cm

    print( """
    Angel fiducial Radius = %7.2f cm
    Angel fiducial Length = %7.2f cm
    """%(Rf/cm,Lf/cm))

    LbuffShape = CylinderShell(Rf,Rf+Rbuff,Lf+Zbuff)
    ZbuffShape = FlatPlate(Rf+Rbuff,Zbuff)
    buffMat = Material('GXe',15)
    xeLbuff = PhysicalVolume("XenonLBuffer",buffMat,LbuffShape)
    xeZbuff = PhysicalVolume("XenonZBuffer",buffMat,ZbuffShape)

    print( """
    Angel fiducial Volume = %7.2f m3
    Angel fiducial mass = %7.2f kg
    """%(xe.Volume()/m3,xe.Mass()/kg))

    print( """
    Angel radial buffer radius = %7.2f cm (E/P ~ 2)
    Angel Z buffer radius = %7.2f cm   (E/P~1)
    """%(Rbuff/cm,Zbuff/cm))

    print( """
    Angel long buffer Volume = %7.2f m3
    Angel long buffer mass = %7.2f kg
    """%(xeLbuff.Volume()/m3,xeLbuff.Mass()/kg))

    print( """
    Angel z buffer Volume = %7.2f m3
    Angel z buffer mass = %7.2f kg
    """%(xeZbuff.Volume()/m3,xeZbuff.Mass()/kg))

if __name__ == '__main__':
   #Angel()
   ct =  Tube(Rin=1*cm,t=1*mm,L=44*cm,Mat='Cu10')
   print( "copper tube")
   print( ct)
