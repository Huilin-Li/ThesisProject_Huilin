import numpy as np
from UNIOA_Framework.NatureOpt import NatureOpt

# original PSO framework
# but only fix the asynchronous Global calculation to the synchronous Global calculation
# the Evaluation is still asynchronous


class PSO_orig_fix(NatureOpt):
    def __init__(self, func, hyperparams_set, budget_factor=1e4):
        super().__init__(func, budget_factor)
        self.M = hyperparams_set.get('popsize', 25)


    def __call__(self):
        X = np.random.uniform(self.lb_x, self.ub_x, (self.M, self.n))
        fitness = self.Evaluate_X(X=X)
        v = np.random.uniform(-1, 1, (self.M, self.n))
        X_i_p = X.copy()
        X_i_p_Fit = fitness.copy()
        g_ind = np.argmin(fitness)
        g = X[g_ind]
        g_fit = fitness[g_ind]


        while not self.stop:
            for i in range(self.M):
                v[i] = 0.73 * v[i] + np.random.uniform(0, 1.49) * (X_i_p[i] - X[i]) + np.random.uniform(0, 1.49) * (g - X[i])
                new_x = X[i] + v[i]
                X[i] = np.clip(new_x, self.lb_x, self.ub_x)
                fitness[i] = self.fitness_function(X[i])

                if fitness[i] < X_i_p_Fit[i]:
                    X_i_p[i] = X[i]
                    X_i_p_Fit[i] = fitness[i]

            for i in range(self.M):
                if fitness[i] < g_fit:
                    g = X[i]
                    g_fit = fitness[i]













