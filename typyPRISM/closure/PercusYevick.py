from typyPRISM.closure.AtomicClosure import AtomicClosure
import numpy as np
class PercusYevick(AtomicClosure):
    '''Percus Yevick closure written in terms of a change of variables
    
    .. note::
    
        The change of variables is necessary in order to use potentials with
        hard cores. Written in the standard form, this closure diverges with
        divergent potentials, which makes it impossible to numerically solve. 
    
    .. math::
        
        c_{i,j}(r) = (exp(-U_{i,j}(r)) - 1.0) * (1.0 + \gamma_{i,j}(r))
        
        \gamma_{i,j}(r) =  h_{i,j}(r) - c_{i,j}(r)
    
    '''
    def __init__(self):
        self.potential = None
        self.value = None
        
    def __repr__(self):
        return '<AtomicClosure: PercusYevick>'
    
    def calculate(self,gamma):
        
        assert self.potential is not None,'Potential for this closure is not set!'
        
        assert len(gamma) == len(self.potential),'Domain mismatch!'
        
        self.value = (np.exp(-self.potential)-1.0)*(1.0+gamma)
        
        return self.value
        
        