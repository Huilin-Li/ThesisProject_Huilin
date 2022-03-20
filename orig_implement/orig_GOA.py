import numpy as np
import copy
from UNIOA_Framework.NatureOpt import NatureOpt
from sklearn.metrics import pairwise_distances


# original GOA framework
# synchronous Evaluation + synchronous Global calculation

class GOA_orig(NatureOpt):
    def __init__(self, func ,hyperparams_set, budget_factor = 1e4):
        super().__init__(func, budget_factor)
        self.M = hyperparams_set.get('popsize', 100)


    def __call__(self):
        cMax=1
        cMin=0.00004
        l = 1 # they use 2

        # initialization
        GrassHopperPositions = np.random.uniform(self.lb_x, self.ub_x, (self.M, self.n))
        # evaluation
        GrassHopperFitness = self.Evaluate_X(X=GrassHopperPositions)

        # Find the best grasshopper (target) in the first population
        ind = np.argmin(GrassHopperFitness)
        TargetPosition = GrassHopperPositions[ind].copy()
        TargetFitness = copy.copy(GrassHopperFitness[ind])
        
        # Main loop
        while not self.stop:
            c=cMax-l*((cMax-cMin)/self.budget) # Eq. (2.8) in the paper, self.budget =  Max_iter
            Dist = pairwise_distances(GrassHopperPositions, metric='euclidean')
            temp = GrassHopperPositions.copy()
            for i in range(self.M):
                S_i = np.zeros(self.n)
                for j in list(range(i)) + list(range(i+1, self.M)):
                    D=Dist[i,j]
                    r_ij_vec=(temp[i]-temp[j])/(D + 2.2204e-16) # xj-xi/dij in Eq. (2.7)
                    xj_xi=2+np.remainder(D,2) #|xjd - xid| in Eq. (2.7)
                    s_ij=((self.ub_x - self.lb_x)*c/2)*(0.5*np.exp(-xj_xi/1.5)-np.exp(-xj_xi)) *r_ij_vec # The first part inside the big bracket in Eq. (2.7)
                    S_i=S_i+s_ij

                X_new = c * S_i + TargetPosition
                # deal with outliers
                GrassHopperPositions[i] = np.clip(X_new, self.lb_x, self.ub_x)

            # evaluate new pop
            GrassHopperFitness = self.Evaluate_X(X=GrassHopperPositions)
            # no selection

            # update global best = named Target Position here
            for i in range(self.M):
                if GrassHopperFitness[i]<TargetFitness:
                    TargetPosition = GrassHopperPositions[i].copy()
                    TargetFitness = copy.copy(GrassHopperFitness[i])
            l = l + 1
            
        
                
                
     
        
        
        
        
        
         
        
    