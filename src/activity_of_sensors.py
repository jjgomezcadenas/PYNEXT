
import numpy as np
import pandas as pd

from math import sqrt, pi

from pynext.system_of_units import *
from pynext.NextData import next100_PV

from pynext.Sensors import PMT
from pynext.Sensors import SiPM
from pynext.Sensors import KDB

from pynext.activity_functions import activity_table
from pynext.activity_functions import pmt_activity
from pynext.activity_functions import sipm_activity


def sensor_activity():

    # Pressure Vessel
    n100_pv = next100_PV()

    pmt = PMT()
    sipm = SiPM()
    kdb = KDB(L = 110  * mm,
              pitch    = 10   * mm,
              nof_sipm = 64,
              a_bi214  = 31 * muBq, a_tl208= 15 * muBq)

    nof_kdb = n100_pv.head_surface / kdb.S
    nof_sipm = nof_kdb * kdb.nof_sipm

    pmtActivity = pmt_activity('PMT activity', 60, pmt)
    sipmActivity = sipm_activity('SiPM activity', nof_sipm, sipm)
    kdbActivity = sipm_activity('KDB activity', nof_kdb , kdb)

    act_sensor_table =activity_table([pmtActivity, sipmActivity, kdbActivity])
    return act_sensor_table
