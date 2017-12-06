from . TpcEL import TpcEL
from . Material import Material
from . Material import RadioactiveMaterial
from pynext.system_of_units import *

from pytest import approx
from pytest import fixture
from math import exp

@fixture(scope='module')
def materials():

    ti316 = RadioactiveMaterial(name='316Ti',
                                rho = 7.87 * g/cm3,
                                mu_over_rho = 0.039 * cm2/g,
                                ts = 1860 * MPa,
                                a_bi214 = 1.0 * mBq/kg,
                                a_tl208 = 0.4 * mBq/kg )

    cu =   RadioactiveMaterial(name='Cu',
                                rho = 8.96 * g/cm3,
                                mu_over_rho = 0.039 * cm2/g,
                                ts = 220*MPa,
                                a_bi214 = 3 * muBq/kg,
                                a_tl208 = 3 * muBq/kg )
    return ti316, cu

def test_material(materials):
    ti316, _ = materials
    g_cm3 = g / cm3
    cm2_g = cm2 / g
    icm   = 1 / cm
    mbq_kg = mBq / kg


    assert ti316.name                           == '316Ti'
    ti316.density / g_cm3                       == approx(7.87, rel=1e-3)
    ti316.mass_attenuation_coefficient / cm2_g  == approx(0.0039, rel=1e-3)
    ti316.attenuation_coefficient / icm         == approx(0.31, rel=1e-2)
    ti316.attenuation_length / cm               == approx(3.26, rel=1e-2)
    ti316.tensile_strength / MPa                == approx(1860, rel=1e-2)
    ti316.activity_bi214 / mbq_kg               == approx(1, rel=1e-3)
    ti316.activity_tl208 / mbq_kg               == approx(0.4, rel=1e-3)


def test_surface_activity(materials):
    _, rcu = materials
    t = 12 * cm

    SA = rcu.C * rcu.rho * (rcu.a_bi214 / rcu.mu) * (1 - exp(-t * rcu.mu))
    rcu.surface_activity(z=t, isotope='Bi214') / (mBq/m2) == approx(SA, rel=1e-5)
