from . system_of_units import *
from collections import namedtuple

class RFlux:
    def __init__(self,
                 name  = 'LSC2010',
                 U238  = 0.55 * Bq / cm2,
                 Th232 = 0.36 * Bq / cm2
                 ):
        self.name  = name
        self.U238  = U238
        self.Th232 = Th232
        self.Bi214 = self.U238 * (0.7 / 100)
        self.Tl208 = self.Th232 * (13.65 / 100)
        self.energy_gamma_bi214 = 2447.9 * keV
        self.energy_gamma_tl208 = 2614.5 * keV

    def __str__(self):

        s = """

        {:s}
        ------------------

        U238  flux  = {:7.2f} mBq / cm2
        Th232 flux  = {:7.2f} mBq / cm2
        Bi214 flux  = {:7.2f} mBq / cm2
        Tl208 flux  = {:7.2f} mBq / cm2

    """.format(self.name,
               self.U238 / (mBq / cm2),
               self.Th232 / (mBq / cm2),
               self.Bi214 / (mBq / cm2),
               self.Tl208 / (mBq / cm2))
        return s

    __repr__ = __str__


class NextPVData:
    def __init__(self,
                 name='Next100PVData',
                 pv_inner_diameter = 1360 * mm,
                 pv_length         = 1600 * mm,
                 pv_body_thickness =   10 * mm,
                 pv_head_thickness =   12 * mm,
                 cs_body_thickness =  120 * mm,
                 cs_head_thickness =  120 * mm,
                 pb_body_thickness =  200 * mm,
                 pb_head_thickness =  200 * mm,
                 ):
        self.name              = name
        self.pv_inner_diameter = pv_inner_diameter
        self.pv_length         = pv_length
        self.pv_body_thickness = pv_body_thickness
        self.pv_head_thickness = pv_head_thickness
        self.pv_inner_radius   = self.pv_inner_diameter / 2.
        self.pv_outer_diameter = self.pv_inner_diameter + self.pv_body_thickness
        self.pv_outer_radius   = self.pv_outer_diameter / 2.

        self.cs_head_thickness = cs_head_thickness
        self.cs_body_thickness = cs_body_thickness
        self.cs_inner_diameter = self.pv_inner_diameter - self.cs_body_thickness
        self.cs_length         = self.pv_length
        self.cs_inner_radius   = self.cs_inner_diameter / 2.
        self.cs_outer_diameter = self.pv_inner_diameter
        self.cs_outer_radius   = self.cs_outer_diameter / 2.

        self.pb_head_thickness = pb_head_thickness
        self.pb_body_thickness = pb_body_thickness
        self.pb_inner_diameter = self.pv_outer_diameter
        self.pb_length         = self.pv_length
        self.pb_inner_radius   = self.pb_inner_diameter / 2.
        self.pb_outer_diameter = self.pb_inner_diameter + pb_body_thickness
        self.pb_outer_radius   = self.pb_outer_diameter / 2.

    def __str__(self):

        s = """

        {:s}
        ------------------

        PV :
        inner diameter  = {:7.2f} mm
        inner radius    = {:7.2f} mm
        outer diameter  = {:7.2f} mm
        outer radius    = {:7.2f} mm
        body thickness  = {:7.2f} mm
        head thickness  = {:7.2f} mm
        length          = {:7.2f} mm

        CS :
        inner diameter  = {:7.2f} mm
        inner radius    = {:7.2f} mm
        outer diameter  = {:7.2f} mm
        outer radius    = {:7.2f} mm
        body thickness  = {:7.2f} mm
        head thickness  = {:7.2f} mm
        length          = {:7.2f} mm

        PB :
        inner diameter  = {:7.2f} mm
        inner radius    = {:7.2f} mm
        outer diameter  = {:7.2f} mm
        outer radius    = {:7.2f} mm
        body thickness  = {:7.2f} mm
        head thickness  = {:7.2f} mm
        length          = {:7.2f} mm

    """.format(self.name,
               self.pv_inner_diameter / mm,
               self.pv_inner_radius / mm,
               self.pv_outer_diameter / mm,
               self.pv_outer_radius / mm,
               self.pv_body_thickness / mm,
               self.pv_head_thickness / mm,
               self.pv_length,
               self.cs_inner_diameter / mm,
               self.cs_inner_radius / mm,
               self.cs_outer_diameter / mm,
               self.cs_outer_radius / mm,
               self.cs_body_thickness / mm,
               self.cs_head_thickness / mm,
               self.cs_length,
               self.pb_inner_diameter / mm,
               self.pb_inner_radius / mm,
               self.pb_outer_diameter / mm,
               self.pb_outer_radius / mm,
               self.pb_body_thickness / mm,
               self.pb_head_thickness / mm,
               self.pb_length)
        return s

    __repr__ = __str__



# VE_TH = 1 * mm # fake thickness used for envelop
#
#
#
# #Field cage
# BG_R = 1*cm # radius buffer gas
# BG_CTH = 5*cm # thickness of buffer gas in cathode
# BG_ATH = 5*cm # thickness of buffer gas in cathode
#
# FC_ID = 105*cm  # FC inner diameter
# FC_TH = 2.5*cm  # FC thickness (poly)
# FC_OD = FC_ID + 2*FC_TH
#
# FC_IR = FC_ID/2.
# FC_OR = FC_OD/2.
# FC_PLATE_TH = 1*mm # thickness of lead
#
# FC_Z = 130*cm
# FC_MAT='Poly'
# FC_MAT2='Poly2'
#
#
#
# #Lead Castle
# LC_ID=PV_OD + 20*cm  #10 cm of air to be filled with lead in the future
# LC_TH = 25*cm
# LC_OD = LC_ID +2*LC_TH
# LC_IR = LC_ID/2.
# LC_OR = LC_OD/2.
# LC_PLATE_TH = 25*cm # thickness of lead
# LC_Z=230*cm + 10*cm
# LC_MAT='Pb'
#
# #tracking plane
# m_DB=250*gram
# n_DB=110
#
# #Energy plane
# n_PMT=60
# n_resistor_PMT=20
# n_cap_PMT=7
