import math
import copy
import numpy as np
from UNIOA_Framework.NatureOpt import NatureOpt


# original BA framework
# but only fix the asynchronous Global calculation to the synchronous Global calculation
# the Evaluation is still asynchronous



class BA_orig_fix(NatureOpt):
    def __init__(self, func ,hyperparams_set, budget_factor = 1e4):
        super().__init__(func,budget_factor)
        self.M = hyperparams_set.get('popsize', 20) #
        self.A = hyperparams_set.get('loudness', 1) # initial loudness A
        self.r0 = hyperparams_set.get('pulse_rate', 1) # initial pulse rate r0
        self.alpha = hyperparams_set.get('alpha', 0.97) # to decrease A
        self.gamma = hyperparams_set.get('gamma', 0.1) # to decrease r0
        self.Freq_min = hyperparams_set.get('frequency_min', 0)
        self.Freq_max = hyperparams_set.get('frequency_max', 2)
        
    def __call__(self):
        v = np.zeros((self.M, self.n))  # Velocities

        # Initialize the population/solutions
        Sol = self.Init_X.Init_X(M=self.M, n=self.n, lb_x=self.lb_x, ub_x=self.ub_x)
        Fitness = self.Evaluate_X(X = Sol)

        # Find the best solution of the initial population
        I = np.argmin(Fitness)
        best = Sol[I].copy()
        fmin = copy.copy(Fitness[I])

        # iteration counter
        t = 0

        # Start the iterations -- the Bat Algorithm (BA) -- main loop
        while not self.stop:
            #  Varying loundness (A) and pulse emission rate (r)
            r=self.r0*(1-math.exp(-self.gamma*t))
            A = self.alpha * self.A
            # Loop over all bats/solutions
            for i in range(self.M):
                Freq=self.Freq_min+(self.Freq_max-self.Freq_min)*np.random.rand()
                v[i]=v[i]+(Sol[i]-best)*Freq
                x= Sol[i] + v[i]
                # Check a switching condition
                if np.random.rand()<r:
                    x= best + 0.1 * np.random.randn(self.n) * A
                # Check if the new solution is within the simple bounds
                x = np.clip(x, self.lb_x, self.ub_x)
                fitness_temp = self.fitness_function(x)
                # selection
                if ((fitness_temp <= Fitness[i]) and (np.random.rand() > A)):
                    Sol[i] = x # final new generated pop
                    Fitness[i] = fitness_temp

            # Update the current best solution = global best one
            for i in range(self.M):
                if Fitness[i]<=fmin:
                    best = Sol[i].copy()
                    fmin = copy.copy(Fitness[i])

            t=t+1

