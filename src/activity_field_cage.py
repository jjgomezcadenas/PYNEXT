import numpy as np
import pandas as pd

from pynext.system_of_units import *


from pynext.activity_functions import Activity
from pynext.CylindricalVessel import CylindricalDetector
from pynext.CylindricalVessel import NextFieldCage

from pynext.Material import vacuum, ti316, cu12, cu03, pb, poly
from pynext.activity_functions import activity_table


def field_cage_activity():
    electrodeFC = CylindricalDetector(name='ElectrodeFieldCage',
                                      inner_diameter  = 1050 * mm,
                                      length          =   10 * mm,
                                      thickness       =    6 * mm,
                                      material        = cu12)


    resitstorActivityFC = Activity(name = 'ActivityResistorFC',
                                   bi214 = 17.9 * muBq,
                                   tl208 = 3.1  * muBq)

    nfc = NextFieldCage(name='Next100FieldCage',
                        inner_diameter  = 1050 * mm  ,
                        length          = 1300 * mm  ,
                        thickness       =   20 * mm  ,
                        electrode_pitch =   12 * mm  ,
                        material        = poly       ,
                        electrode       = electrodeFC,
                        resitstorActivityFC = resitstorActivityFC)

    act_fc_table =activity_table([nfc.activity_electrodes, nfc.activity_resistors, nfc.activity_poly])
    return act_fc_table
