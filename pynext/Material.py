"""
Material
Defines a material medium
"""
from . system_of_units import *
from math import pi, exp, log
import sys

class Material:
    def __init__(self, name, rho, mu_over_rho, ts):
        self.name        = name
        self.rho         = rho
        self.mu_over_rho = mu_over_rho
        self.mu          = mu_over_rho * rho
        self.Latt        = 1 / self.mu
        self.ts           = ts
    @property
    def density(self):
        return self.rho

    @property
    def mass_attenuation_coefficient(self):
        return self.mu_over_rho

    @property
    def attenuation_coefficient(self):
        return self.mu

    @property
    def attenuation_length(self):
        return self.Latt

    @property
    def tensile_strength(self):
        return self.ts

    def __str__(self):
        g_cm3 = g / cm3
        cm2_g = cm2 / g
        icm   = 1 / cm

        s= """
        material                                   = %s
        density (rho)                              = %7.2f g/cm3
        mass attenuation coefficient (mu_over_rho) = %7.2f cm2/g
        attenuation coefficient (mu)               = %7.2f cm^-1
        attenuation length (Latt)                  = %7.2f cm
        tensile strenght (ts)                      = %7.2f MPa
    """%(self.name,
         self.density / g_cm3,
         self.mass_attenuation_coefficient / cm2_g,
         self.attenuation_coefficient / icm,
         self.attenuation_length / cm,
         self.tensile_strength / MPa
         )

        return s

    __repr__ = __str__


class RadioactiveMaterial(Material):
    def __init__(self, name, rho, mu_over_rho, ts, a_bi214, a_tl208):
        super().__init__(name, rho, mu_over_rho, ts)
        self.a_bi214        = a_bi214
        self.a_tl208        = a_tl208
        self.C = 1 / 3
    @property
    def activity_bi214(self):
        return self.a_bi214

    @property
    def activity_tl208(self):
        return self.a_tl208

    def surface_activity(self, z, isotope='Bi214'):
        """If the material has an specific activity A0 (Bq/kg) and a thickness z (cm)
           then the Surface Activity that escapes the material (not self-shielded) is given by

           SA = C * rho * X
           X = A0/mu (1 - exp (-z*mu))
           Where C is at least 1/2 (half of the activity is emitted towards negative z)
        """

        self.SA =  self.C * self.rho * (self.a_bi214 / self.mu) # Bi 214 by default
        if isotope == 'Tl208':
            self.SA =  self.C * self.rho * (self.a_tl208 / self.mu)
        return self.SA * (1 - exp(-z * self.mu))

    def __str__(self):
        bq_kg = Bq / kg

        s = super().__str__() + """
        activity Bi-214                = %7.2e Bq /kg
        activity Tl-208                = %7.2e Bq /kg
    """%(self.activity_bi214 / bq_kg,
         self.activity_tl208 / bq_kg)

        return s

    __repr__ = __str__
