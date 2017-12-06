"""
Physical Volume
Defines a material medium + Shape
"""
from . Material import *
from . Shapes import *

class PhysicalVolume:
    def __init__(self,name, material,shape):
        """
       Defines a physical volume

       """
        self.name=name
        self.material = material
        self.shape=shape


    def Volume(self):
        return self.shape.V()
    def Surface(self):
        return self.shape.S()
    def Mass(self):
        return self.shape.V()*self.material.rho
    def Activity(self,t):
        return self.Surface()*self.material.A(t)




class SphericalCan:
    """
    A sphere shell filled with some material
    Rin --> inner radius of shell
    Rout --> outer radious of shell

    """

    def __init__(self,Rin=100*cm,t=1*cm,Mat='Cu10',FillFactor=1.,TensileStrength=3300*MPa):
        self.Rin=Rin
        self.t= t
        self.Rout = Rin+t
        self.F=FillFactor
        self.Mat = RMaterial(name=Mat, S=TensileStrength)

        self.ShellShape = SphereShell(Rin,t)
        self.Shell =  PhysicalVolume("Can",self.Mat,self.ShellShape)

    def Material(self):
        return self.Mat

    def MaterialName(self):
        return self.Mat.Name()

    def Volume(self):
        return self.Shell.Volume()

    def Surface(self):
        return self.Shell.Surface()

    def InnerSurface(self):
        return self.ShellShape.InnerSurface()

    def InnerRadius(self):
        return self.Rin

    def OuterRadius(self):
        return self.Rout

    def FillFactor(self):
        return self.F

    def Mass(self):
        mass = self.Shell.Mass()
        return mass*self.F

    def Activity(self):
        a= self.Shell.Activity(self.t)/(1./year)*self.F
        return a

    def ThicknessToPressure(self,P):
        """
        Thickness of a sphere of radius R under pressure P
        """
        return (P/self.Mat.TensileStrength())*(self.Rout/2.)


    def __str__(self):
        s= """
        Material = %s
        Inner Radius = %7.2e cm
        Outer Radius = %7.2e cm
        Fill Factor = %7.2f
        """%(self.Material(), self.InnerRadius()/cm,self.OuterRadius()/cm, self.FillFactor())

        s+= """
        Volume = %7.2e m3
        Outer Surface = %7.2e cm2
        Inner Surface = %7.2e cm2
        mass = %7.2e kg
        activity = %7.2e c/year  =%7.2e Bq
        """%(self.Volume()/m3,self.Surface()/cm2,self.InnerSurface()/cm2,self.Mass()/kg,
             self.Activity(),self.Activity()*second/year)

        return s

class Tube(SphericalCan):
    """
    A tube filled with some material
    """
    def __init__(self,Rin=1*cm,t=1*mm,L=120*cm,Mat='Cu10',FillFactor=1.,TensileStrength=3300*MPa):
        SphericalCan.__init__(self,Rin,t,Mat,FillFactor,TensileStrength)
        self.ShellShape = CylinderShell(Rin,self.Rout,L)
        self.Shell =  PhysicalVolume("Tube",self.Mat,self.ShellShape)

def Angel():
    Lf=130*cm
    Rf=53*cm

    xeShape = Cylinder(Rf,Lf)
    xeMat = Material('GXe',15)
    xe = PhysicalVolume("XenonVolume",xeMat,xeShape)

    Rbuff = 3*cm
    Zbuff = 8*cm

    print( """
    Angel fiducial Radius = %7.2f cm
    Angel fiducial Length = %7.2f cm
    """%(Rf/cm,Lf/cm))

    LbuffShape = CylinderShell(Rf,Rf+Rbuff,Lf+Zbuff)
    ZbuffShape = FlatPlate(Rf+Rbuff,Zbuff)
    buffMat = Material('GXe',15)
    xeLbuff = PhysicalVolume("XenonLBuffer",buffMat,LbuffShape)
    xeZbuff = PhysicalVolume("XenonZBuffer",buffMat,ZbuffShape)

    print( """
    Angel fiducial Volume = %7.2f m3
    Angel fiducial mass = %7.2f kg
    """%(xe.Volume()/m3,xe.Mass()/kg))

    print( """
    Angel radial buffer radius = %7.2f cm (E/P ~ 2)
    Angel Z buffer radius = %7.2f cm   (E/P~1)
    """%(Rbuff/cm,Zbuff/cm))

    print( """
    Angel long buffer Volume = %7.2f m3
    Angel long buffer mass = %7.2f kg
    """%(xeLbuff.Volume()/m3,xeLbuff.Mass()/kg))

    print( """
    Angel z buffer Volume = %7.2f m3
    Angel z buffer mass = %7.2f kg
    """%(xeZbuff.Volume()/m3,xeZbuff.Mass()/kg))

if __name__ == '__main__':
   #Angel()
   ct =  Tube(Rin=1*cm,t=1*mm,L=44*cm,Mat='Cu10')
   print( "copper tube")
   print( ct)
