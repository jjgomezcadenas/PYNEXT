from . TpcEL import TpcEL
from pynext.system_of_units import *
from . Shapes import Sphere
from . Shapes import SphereShell
from . Shapes import SemiSphereShell
from . Shapes import Cylinder
from . Shapes import CylinderShell
from . Shapes import Brick
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

def test_sphere():
    sp = Sphere(1)
    assert sp.R               == 1
    assert sp.V               == approx((4/3) * pi, rel=1e-5)
    assert sp.S               == approx(4 * pi, rel=1e-5)
    assert sp.V               == sp.volume()
    assert sp.S               == sp.outer_surface()
    assert sp.inner_surface() == 0
    assert sp.thickness()     == 0


def test_sphere_shell():
    sp = SphereShell(R = 1, t = 1)
    sp2 = SemiSphereShell(R = 1, t = 1)
    v0 = (4/3) * pi * sp.R**3
    v1 = (4/3) * pi * (sp.R + sp.t)**3

    assert sp.R               == 1
    assert sp.t               == 1
    assert sp.thickness()     == 1
    assert sp.volume()        == approx(v1 - v0, rel=1e-5)
    assert sp.inner_surface() == approx(4 * pi * sp.R**2, rel=1e-5)
    assert sp.outer_surface() == approx(4 * pi * (sp.R + sp.t)**2, rel=1e-5)

    assert sp2.R               == sp.R
    assert sp2.t               == sp.t
    assert sp2.thickness()     == sp.thickness()
    assert sp2.volume()        == sp.volume() / 2
    assert sp2.inner_surface() == sp.inner_surface() / 2
    assert sp2.outer_surface() == sp.outer_surface() / 2

def test_cylinder():
    c = Cylinder(R=1, L=1)
    assert c.R               == 1
    assert c.L               == 1
    assert c.EndCapSurface   == pi
    assert c.ShellSurface    == 2 * pi
    assert c.S               == approx(3 * pi, rel=1e-5)
    assert c.V               == c.volume()
    assert c.S               == c.outer_surface()
    assert c.inner_surface() == 0
    assert c.thickness()     == 0


def test_cylinder_shell(Next100PV):
    pv, _ = Next100PV
    iv    =  pi * pv.Rin**2 * pv.L
    sv    =  pi * (pv.Rout**2 - pv.Rin**2) * pv.L
    ins   = 2 * pi * pv.Rin * pv.L
    os    = 2 * pi * pv.Rout * pv.L

    assert pv.Rin          / cm  == approx(52, rel=1e-3)
    assert pv.Rout         / cm  == approx(53, rel=1e-3)
    assert pv.L            / cm  == approx(130, rel=1e-3)
    assert pv.InnerVolume  / m3  == approx(1.10, rel=1e-2)
    assert pv.ShellVolume  / m3  == approx(4.29e-2, rel=1e-3)
    assert pv.InnerSurface / m2  == approx(4.25, rel=1e-3)
    assert pv.ShellSurface / m2  == approx(4.33, rel=1e-3)

    assert pv.InnerVolume        == approx(iv, rel=1e-7)
    assert pv.ShellVolume        == approx(sv, rel=1e-7)
    assert pv.InnerSurface       == approx(ins, rel=1e-7)
    assert pv.ShellSurface       == approx(os, rel=1e-7)

def test_brick():

    b = Brick(1, 1, 1)
    assert b.width           == 1
    assert b.heigth          == 1
    assert b.length          == 1
    assert b.V               == 1
    assert b.S               == 6
    assert b.volume()        == b.V
    assert b.outer_surface() == b.S
    assert b.inner_surface() == 0
    assert b.thickness()     == 0


def test_flat_plate(Next100PV):
    _, fp = Next100PV

    s = pi * fp.R**2
    v = fp.S * fp.t
    assert fp.R / m  == approx(0.52, rel=1e-3)
    assert fp.t / cm == approx(10, rel=1e-3)
    assert fp.S / m2 == approx(0.85, rel=1e-3)
    assert fp.V / m3 == approx(8.49e-02, rel=1e-3)

    assert fp.S      == approx(s, rel=1e-7)
    assert fp.V      == approx(v, rel=1e-7)
