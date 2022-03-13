import numpy as np
import copy
from UNIOA_Framework.NatureOpt import NatureOpt

# original CSA framework
# asynchronous Evaluation


class CSA_orig(NatureOpt):
    def __init__(self, func ,hyperparams_set, budget_factor=1e4):
        super().__init__(func, budget_factor)
        self.M = hyperparams_set.get('popsize',20)
        self.AP = hyperparams_set.get('awareness_probability', 0.1)
        self.fl = hyperparams_set.get('flight_length', 2)

    def __call__(self):
        X = self.Init_X.Init_X(M=self.M, n=self.n, lb_x=self.lb_x, ub_x=self.ub_x)
        fitness = self.Evaluate_X(X = X)
        Mem=X.copy() # = Memory is the personal best
        fit=fitness.copy()

        # generate xnew
        Xnew = X.copy()
        while not self.stop:
            for i in range(self.M):
                if np.random.rand() > self.AP:
                    new = X[i]+self.fl*np.random.rand()*(Mem[np.random.randint(self.M)] - X[i])
                else:
                    new = np.random.uniform(self.lb_x, self.ub_x, self.n)
                # check position ==> another kind of selection ==> mixing selection and fixing outliers
                if np.all(new >=self.lb_x) & np.all(new <= self.ub_x):
                    Xnew[i] = new

            # evaluate fitness of assistant
            fitness = self.Evaluate_X(X = Xnew)

            # NO selection
            # update personal best Mem
            for i in range(self.M):
                if fitness[i] < fit[i]:
                    Mem[i] = Xnew[i].copy()
                    fit[i] = copy.copy(fitness[i])

            X = Xnew.copy()






            
                        
                    
            

            
            
        

    
   
        
            
 