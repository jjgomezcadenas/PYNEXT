from . system_of_units import *
from math import *

R50=50*ohm

class PMT:

    def __init__(self,name='R1141',gain=1e+6,D=3*2.5*cm, serFWHM=25*ns,filterRT=50*ohm*200*pF,ampliGain=10,
                 QE=0.3,AU=2*becquerel*1e-3,ATh=2*becquerel*1e-3):
        """
        Defines a PMT of diameter D, quantum efficiency QE and Activity A
        AU -->U chain (TL-208)
        Ath--> Th chain (Bi-214)
        """
        self.name=name
        self.R=D/2.
        self.D=D
        self.QE=QE
        self.AU=AU
        self.ATh = ATh
        self.S=pi*self.R**2
        self.gain =gain
        self.tfil=filterRT
        self.again = ampliGain
        self.iser = self.gain*QE/serFWHM
        self.iserf = self.iser*serFWHM/self.tfil
        self.vser = self.iser*R50
        self.vserf=self.iserf*R50
        self.vserfa=self.vserf*self.again

    def VSER(self):
        return self.vserfa

    def __str__(self):
        s="""
        PMT name = %s
        Gain = %7.2e
        I single electron response iSER = %7.2f milliampere
        V single electron response vSER = %7.2f millivolt
        filter raise time = %7.2e nanoseconds
        V single electron response after RC filter = %7.2f millivolt
        V single electron response after RC filter (amplified) = %7.2f millivolt
        PMT Diameter = %7.2f cm
        PMT Surface = %7.2f cm2
        PMT QE = %7.2f
        U activity = %7.2f mBq
        Th activity = %7.2f mBq
        """%(self.name,self.gain,self.iser/milliampere, self.vser/millivolt,self.tfil/ns, self.vserf/millivolt,
             self.vserfa/millivolt,
             self.D/cm,self.S/cm2,self.QE,self.AU/(becquerel*1e-3),
             self.ATh/(becquerel*1e-3))
        return s

class SiPM:

    def __init__(self,name='Hamamatsu',L=1.0*mm, QE=0.5,TPB=0.5,
                 AU=2*becquerel*1e-5,ATh=2*becquerel*1e-5):
        """
        Defines a SiPM of size L, quantum efficiency QE and TPB efficiency TPB
        """
        self.name=name
        self.L=L
        self.QE=QE
        self.TPB=TPB
        self.PDE = QE*TPB
        self.S=L**2
        self.AU=AU
        self.ATh = ATh

    def __str__(self):
        s="""
        SiPM name = %s
        SiPM size = %7.2f mm
        SiPM Surface = %7.2f mm2
        SiPM QE = %7.2f
        SiPM TPB eff = %7.2f
        SiPM global PDE = %7.2f
        U activity = %7.2f muBq
        Th activity = %7.2f muBq
        """%(self.name,self.L/mm, self.S/mm2,self.QE,self.TPB,
             self.PDE, self.AU/(becquerel*1e-6),
             self.ATh/(becquerel*1e-6))
        return s

class Digitizer:
    """
    Defines a digitizer
    """

    def __init__(self,pmt,name='UPV',bits=12,noiseBits=2,dRange=1*volt,samplingTime=25*ns):
        self.name=name
        self.bits=bits
        self.ebits=bits-1
        self.nbits=noiseBits
        self.maxc = 2**self.ebits
        self.noisec = 2**self.nbits
        self.pmt=pmt
        self.drange=dRange
        self.npes=self.drange/self.pmt.VSER()
        self.cpes = self.maxc/self.npes
        self.stn = self.cpes/self.noisec
        self.st =samplingTime

    def SamplingTime(self):
        return self.st

    def NPes(self):
        return self.npes
    def __str__(self):
        s="""
        Digitizer name = %s
        sampling time = %7.2f  ns
        dynamic range = %7.2f volts
        number of bits = %d, number of useful bits = %d, noise bits = %d
        max number of adc counts = %d, noise counts = %d
        pmt name = %s
        pmt VSER = %7.2f millivolt
        number of pes = %7.2f
        number of counts per pes = %7.2f
        signal to noise = %7.2f
        """%(self.name,self.st/ns,self.drange/volt,self.nbits, self.ebits,self.nbits, self.maxc,
             self.noisec,
             self.pmt.name,self.pmt.VSER()/mV, self.npes,self.cpes, self.stn)
        return s
