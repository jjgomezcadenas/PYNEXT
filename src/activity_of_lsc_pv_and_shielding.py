
import numpy as np
import pandas as pd

from math import sqrt, pi
from pynext.system_of_units import *

from pynext.NextData import RFlux
from pynext.NextData import next100_lead_shield
from pynext.NextData import next100_PV
from pynext.NextData import next100_copper_shield
from pynext.NextData import next100_envelop

from pynext.CylindricalVessel import CylindricalVessel
from pynext.Material import vacuum, ti316, cu12, cu03, pb

from pynext.activity_functions import activity_lsc_gammas_through_CV
from pynext.activity_functions import activity_gammas_transmitted_CV
from pynext.activity_functions import activity_of_CV
from pynext.activity_functions import print_activity_of_CV
from pynext.activity_functions import print_activity
from pynext.activity_functions import activity_table


def lsc_activity():
    # Flux from LSC
    lsc_gamma_flux = RFlux()
    lsc_gamma_flux

    # Pressure Vessel
    n100_pv = next100_PV()

    # NEXT-100 envelop
    n100_envelop = next100_envelop()
    lsc_activity_next_100 = activity_lsc_gammas_through_CV('LSC activity ',
                                                           n100_envelop, lsc_gamma_flux)

    # ## Shielding provided by the Lead Castle
    n100_pb = next100_lead_shield()
    lsc_activity_transmitted_pb = activity_gammas_transmitted_CV('activity after Pb',n100_pb ,
                                                                  lsc_activity_next_100)

    # ## Shielding provided by the ICS
    n100_cu = next100_copper_shield()
    lsc_activity_transmitted_cu = activity_gammas_transmitted_CV('activity after Cu', n100_cu ,
                                                                  lsc_activity_transmitted_pb)

    act_lsc =activity_table([lsc_activity_next_100,
                             lsc_activity_transmitted_pb,
                             lsc_activity_transmitted_cu])
    return act_lsc

def shield_and_pv_activity():

    n100_pv = next100_PV()
    n100_pb = next100_lead_shield()
    n100_cu = next100_copper_shield()

    # ## Activity due to Lead shield
    pb_activity = activity_of_CV('activity of Pb (ss)', n100_pb)
    pb_activity_transmitted_cu = activity_gammas_transmitted_CV('PB activity after Cu',
                                                                 n100_cu, pb_activity)

    # ## Activity due to PV
    pv_activity = activity_of_CV('activity of PV (ss)', n100_pv)
    pv_activity_transmitted_cu = activity_gammas_transmitted_CV('PV activity after Cu',
                                                                 n100_cu, pv_activity)
    # ## Activity due to CS

    cs_activity = activity_of_CV('activity of CS (ss)', n100_cu)


    act_shield_and_pv =activity_table([pb_activity_transmitted_cu,
                                  pv_activity_transmitted_cu,
                                  cs_activity])
    return act_shield_and_pv
