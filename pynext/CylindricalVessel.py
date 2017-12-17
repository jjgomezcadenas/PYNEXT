"""
Physical Volume
Defines a material medium + Shape
"""

from math import pi, exp, log
from . system_of_units import *
from . PhysicalVolume import PhysicalVolume
from . Shapes import CylinderShell
from . Shapes import SphereShell
from . Shapes import Disk
from . Material import PVMaterial
from . Material import RadioactiveMaterial
from collections import namedtuple

# Cylindrical Vessel Dimensions (CVD)
CVD = namedtuple('CVD', 'name R th_body L th_head')

# Cylindrical Vessel Activity (CVA)
CVA = namedtuple('CVA', """name
                           body_bi214 head_bi214
                           body_tl208 head_tl208""")

class CylindricalVessel:
    def __init__(self, name, material, cvd):
        """material fill the Vessel
           body is a cylindrical shell
           head is a disk
           cvd is namedtuple (CVD = Cylindrical Vessel Dimensions)
           """

        CV = namedtuple('CV', 'name material body head')

        self.cvd = cvd
        cs =      CylinderShell(Rin=cvd.R, Rout=cvd.R + cvd.th_body, L=cvd.L)
        ch =      Disk         (R=cvd.R, t=cvd.th_head)

        self.cv = CV(name = name,
                     material = material,
                     body     = PhysicalVolume(name, material, cs),
                     head     = PhysicalVolume(name, material, ch))

    @property
    def name(self):
        return self.cvd.name

    @property
    def material_name(self):
        return self.cv.material.name

    @property
    def radius(self):
        return self.cvd.R

    @property
    def length(self):
        return self.cvd.L

    @property
    def body_thickness(self):
        return self.cvd.th_body

    @property
    def head_thickness(self):
        return self.cvd.th_head

    @property
    def body_surface(self):
        return self.cv.body.S

    @property
    def body_volume(self):
        return self.cv.body.volume

    @property
    def body_mass(self):
        return self.cv.body.mass

    @property
    def head_surface(self):
        return self.cv.head.S

    @property
    def head_volume(self):
        return self.cv.head.volume

    @property
    def head_mass(self):
        return self.cv.head.mass

    @property
    def body_activity_bi214(self):
        return self.cv.body.activity_bi214

    @property
    def body_activity_tl208(self):
        return self.cv.body.activity_tl208

    @property
    def head_activity_bi214(self):
        return self.cv.head.activity_bi214

    @property
    def head_activity_tl208(self):
        return self.cv.head.activity_tl208

    @property
    def body_self_shield_activity_bi214(self):
        return self.cv.body.activity_bi214_self_shield(self.cvd.th_body)

    @property
    def body_self_shield_activity_tl208(self):
        return self.cv.body.activity_tl208_self_shield(self.cvd.th_body)

    @property
    def head_self_shield_activity_bi214(self):
        return self.cv.head.activity_bi214_self_shield(self.cvd.th_head)

    @property
    def head_self_shield_activity_tl208(self):
        return self.cv.head.activity_tl208_self_shield(self.cvd.th_head)

    @property
    def body_transmittance(self):
        return self.cv.body.transmittance(self.cvd.th_body)

    @property
    def head_transmittance(self):
        return self.cv.head.transmittance(self.cvd.th_head)

    @property
    def body_absorption(self):
        return self.cv.absorption_at_qbb(self.cvd.th_body)

    @property
    def head_absorption(self):
        return self.cv.absorption_at_qbb(self.cvd.th_head)

    def __str__(self):

        s = """
        Cylindrical Vessel:

        ----------------
        name      = {:s}
        material  = {:s}

        specific activity of material:
        Bi-214    = {:7.2f} mBq/kg
        Tl-208    = {:7.2f} mBq/kg

        body:
        R         = {:7.2f} mm
        thickness = {:7.2f} mm
        length    = {:7.2f} mm
        surface   = {:7.2e} mm2
        volume    = {:7.2e} mm3
        mass      = {:7.2f} kg
        activity Bi-214 = {:7.2f} mBq, self-shielded ={:7.2f} mBq
        activity Tl-208 = {:7.2f} mBq, self-shielded ={:7.2f} mBq
        transmittance   = {:7.2e}

        heads:
        thickness = {:7.2f} mm
        surface   = {:7.2e} mm2
        volume    = {:7.2e} mm3
        mass      = {:7.2f} kg
        activity Bi-214 = {:7.2f} mBq, self-shielded ={:7.2f} mBq
        activity Tl-208 = {:7.2f} mBq, self-shielded ={:7.2f} mBq
        transmittance   = {:7.2e}

        """.format(self.name, self.material_name,
                   self.cv.material.mass_activity_bi214 / (mBq/kg),
                   self.cv.material.mass_activity_tl208 / (mBq/kg),
                   self.radius / mm,
                   self.body_thickness / mm,
                   self.length / mm,
                   self.body_surface / mm2,
                   self.body_volume / mm3,
                   self.body_mass / kg,
                   self.body_activity_bi214 / mBq,
                   self.body_self_shield_activity_bi214 / mBq,
                   self.body_activity_tl208 / mBq,
                   self.body_self_shield_activity_tl208 / mBq ,
                   self.body_transmittance,
                   self.head_thickness / mm,
                   2 * self.head_surface / mm2,
                   2 * self.head_volume / mm3,
                   2 * self.head_mass / kg,
                   self.head_activity_bi214 / mBq,
                   self.head_self_shield_activity_bi214 / mBq,
                   self.head_activity_tl208 / mBq,
                   self.head_self_shield_activity_tl208 / mBq,
                   self.head_transmittance
                  )
        return s

    __repr__ = __str__
