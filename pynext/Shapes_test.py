from . TpcEL import TpcEL
from pynext.system_of_units import *
from . Shapes import CylinderShell
from . Shapes import FlatPlate
from pytest import approx
from pytest import fixture
from math import pi

@fixture(scope='module')
def Next100PV():
    L    = 130 * cm
    R    =  52 * cm
    ts   =   1 * cm
    tc   =  10 * cm
    Rin  = R
    Rout = Rin + ts

    pv = CylinderShell(Rin, Rout, L)
    fp = FlatPlate(R, tc)
    return pv,fp


def test_cylinder_shell(Next100PV):
    pv, _ = Next100PV
    iv    =  pi * pv.Rin**2 * pv.L
    sv    =  pi * (pv.Rout**2 - pv.Rin**2) * pv.L
    ins   = 2 * pi * pv.Rin * pv.L
    os    = 2 * pi * pv.Rout * pv.L

    pv.Rin          / cm  == approx(52, rel=1e-3)
    pv.Rout         / cm  == approx(53, rel=1e-3)
    pv.L            / cm  == approx(130, rel=1e-3)
    pv.InnerVolume  / m3  == approx(1.10, rel=1e-3)
    pv.ShellVolume  / m3  == approx(4.29e-2, rel=1e-3)
    pv.InnerSurface / m2  == approx(4.25, rel=1e-3)
    pv.ShellSurface / m2  == approx(4.33, rel=1e-3)

    pv.InnerVolume        == approx(iv, rel=1e-7)
    pv.ShellVolume        == approx(sv, rel=1e-7)
    pv.InnerSurface       == approx(ins, rel=1e-7)
    pv.ShellSurface       == approx(os, rel=1e-7)


def test_flat_plate(Next100PV):
    _, fp = Next100PV

    s = pi * fp.R**2
    v = fp.S * fp.t
    fp.R / m  == approx(0.52, rel=1e-3)
    fp.t / cm == approx(10, rel=1e-3)
    fp.S / m2 == approx(0.85, rel=1e-3)
    fp.V / m3 == approx(8.49e-02, rel=1e-3)

    fp.S      == approx(s, rel=1e-7)
    fp.V      == approx(v, rel=1e-7)
