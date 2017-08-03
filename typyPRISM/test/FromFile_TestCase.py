from typyPRISM.intraMolCorr.FromFile import FromFile
import unittest
import numpy as np

class FromFile_TestCase(unittest.TestCase):
    def test_create(self):
        '''Can we create a FromFile intraMolCorr?'''
        k = np.arange(0.75,3.5,0.05)
        fname = 'FromFileTestCase.dat'
        
        np.savetxt(fname,k)
        
        FF = FromFile(fname).calculate(k)
        
        os.remove(fname)
    def test_error_check(self):
        '''Does FromFile correctly check the domain?'''
        fname = 'FromFileTestCase.dat'
        
        k = np.arange(0.75,3.5,0.05)
        dummy = np.array([k,k]).T
        
        np.savetxt(fname,dummy)
        
        k = np.arange(0.75,3.5,0.01)
        with self.assertRaises(AssertionError):
            FF = FromFile(fname).calculate(k)
        
        os.remove(fname)
        
        