from . system_of_units import *

G = 0.13 * becquerel/cm2 # gamma activity in Canfranc for Tl-208
G_TL = 0.13 * becquerel/cm2 # gamma activity in Canfranc for Tl-208
G_BI = 0.006 * becquerel/cm2 # gamma activity in Canfranc for Tl-208

TL_Inconel_f = 0.2  # assuming mass of Inconel 718 50 kg and specific activity 5 mBq/kg
BI_Inconel_f =0.125  # assuming mass of Inconel 718 50 kg and s.a. 6 mBq/kg

#Pressure
PP = 15 # pressure in bar units not used exceptionally

#11.3 mg/resistor
# 17 mg/capacitor

# PV = pressure vessel
PV_MAT = 'Fe'
PV_ID = 136*cm  # PV inner diameter
PV_TH = 1.8*cm # PV thickness
PV_PLATE_TH = 1*cm # thickness of end-cup plate
PV_OD =PV_ID + 2*PV_TH  # PV outer diameter
PV_Z=160*cm  # z

PV_IR = PV_ID/2.
PV_OR = PV_OD/2.

#Field cage
BG_R = 1*cm # radius buffer gas
BG_CTH = 5*cm # thickness of buffer gas in cathode
BG_ATH = 5*cm # thickness of buffer gas in cathode

FC_ID = 105*cm  # FC inner diameter
FC_TH = 2.5*cm  # FC thickness (poly)
FC_OD = FC_ID + 2*FC_TH

FC_IR = FC_ID/2.
FC_OR = FC_OD/2.
FC_PLATE_TH = 1*mm # thickness of lead

FC_Z = 130*cm
FC_MAT='Poly'
FC_MAT2='Poly2'

# Inner copper shield
ICS_TH=12*cm   #thickness of ICS
ICS_ID = FC_OD
ICS_OD = ICS_ID +2*ICS_TH

ICS_IR = ICS_ID/2.
ICS_OR = ICS_OD/2.
ICS_PLATE_TH = 12*cm # thickness of lead

ICS_Z=160*cm
ICS_MAT='Cu10'

#Lead Castle
LC_ID=PV_OD + 20*cm  #10 cm of air to be filled with lead in the future
LC_TH = 25*cm
LC_OD = LC_ID +2*LC_TH
LC_IR = LC_ID/2.
LC_OR = LC_OD/2.
LC_PLATE_TH = 25*cm # thickness of lead
LC_Z=230*cm + 10*cm
LC_MAT='Pb'

#tracking plane
m_DB=250*gram
n_DB=110

#Energy plane
n_PMT=60
n_resistor_PMT=20
n_cap_PMT=7
