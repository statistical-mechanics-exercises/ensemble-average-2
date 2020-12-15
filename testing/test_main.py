import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_hamiltonian(self) :
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            sumspins = sum( spins )
            meanspin = sumspins / len(spins)
            self.assertTrue( np.abs(hamiltonian( spins )+4*meanspin*sumspins)<1e-7, "The Hamiltonian is implemented incorrectly" )
            
    def test_averages(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        numer, pfunc = len(temperatures)*[0], len(temperatures)*[0]
        for i in range(2**8) :
            num, spins = i, 8*[0]
            for j in range(8) :
                spins[j] = np.floor( num / 2**(7-j) )
                num = num - spins[j]*2**(7-j)
                if spins[j]==0 : spins[j] = -1
            eee = hamiltonian( spins )
            for k in range(len(temperatures)) :
                numer[k] = numer[k] + eee*np.exp( -eee / temperatures[k] )
                pfunc[k] = pfunc[k] + np.exp( -eee / temperatures[k] )
        for k in range(len(temperatures)) :
            self.assertTrue( np.abs( temperatures[k] - this_x[k])<1e-7, "The ensemble average of the energy is implemented incorrectly" )
            self.assertTrue( np.abs( numer[k]/pfunc[k] - this_y[k])<1e-7, "The ensemble average of the energy is implemented incorrectly" )
