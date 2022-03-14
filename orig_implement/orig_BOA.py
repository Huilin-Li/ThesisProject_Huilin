import numpy as np
from UNIOA_Framework.NatureOpt import NatureOpt
import copy

# original BOA framework
# asynchronous Evaluation + asynchronous Global calculation



class BOA_orig(NatureOpt):
    def __init__(self, func ,hyperparams_set, budget_factor = 1e4):
        super().__init__(func, budget_factor)
        self.M = hyperparams_set.get('popsize', 50)
        self.prob_switch = hyperparams_set.get('probability_switch', 0.8)
        self.power_exponent = hyperparams_set.get('power_exponent', 0.1) #= a/alpha
        self.initial_sensory_modality = hyperparams_set.get('initial_sensory_modality', 0.01)# =c
        
        
    def sensory_modality_NEW(self, x, Ngen):
        return x+(0.025/(x*Ngen))

    def __call__(self):
        # initialization part
        Sol = self.Init_X.Init_X(M=self.M, n=self.n, lb_x=self.lb_x, ub_x=self.ub_x)
        fitness = self.Evaluate_X(X = Sol)
        # find the global best
        ind = np.argmin(fitness)
        best_pos = Sol[ind].copy()
        fmin = copy.copy(fitness[ind])

        sensory_modality = self.initial_sensory_modality
        while not self.stop:
            for i in range(self.M):
                FP= sensory_modality*(fitness[i]**self.power_exponent)
                if np.random.rand()>self.prob_switch:
                    dis = np.random.rand()**2*best_pos - Sol[i]
                    x = Sol[i]+dis*FP
                else:
                    epsilon=np.random.rand()
                    JK = np.random.choice(self.M, 2, replace=False)
                    dis=epsilon**2*Sol[JK[0]]-Sol[JK[1]]
                    x=Sol[i]+dis*FP  #Eq. (3) in paper
                   
                #Check if the simple limits/bounds are OK
                x = np.clip(x, self.lb_x, self.ub_x)
                  
                # Evaluate new solutions
                Fnew = self.fitness_function(x) #Fnew represents new fitness values
                    
                # If fitness improves (better solutions found), update then = selection
                if Fnew <= fitness[i]:
                    Sol[i] = x.copy()
                    fitness[i] = copy.copy(Fnew)

                # Update the current global best_pos
                if fitness[i]<=fmin:
                    best_pos=Sol[i].copy()
                    fmin=copy.copy(fitness[i])

        
            #Update sensory_modality
            sensory_modality=self.sensory_modality_NEW(sensory_modality, Ngen=self.budget)

              
    
            
        
        
        

        
    