import numpy as np
from UNIOA_Framework.NatureOpt import NatureOpt


# -------------------------------------------------------------------------------------------
# The file is a translation of Crow-Optimizer\cite{1,2} from MatLab to Python.
# This Python version code suits our specific experiment cases in IOHanalyzer\cite{3}.
# The execution logic is same as the original implementation in \cite{2}.
# -------------------------------------------------------------------------------------------
# References:
# [1]A. Askarzadeh, ‘A novel metaheuristic method for solving constrained engineering optimization problems: Crow search algorithm’, Computers & Structures, vol. 169, pp. 1–12, Jun. 2016, doi: 10.1016/j.compstruc.2016.03.001.
# [2]https://nl.mathworks.com/matlabcentral/fileexchange/57867-crow-search-algorithm-for-constrained-optimization?focused=6496133&s_tid=gn_loc_drop&tab=function
# [3]C. Doerr, H. Wang, F. Ye, S. van Rijn, and T. Bäck, ‘IOHprofiler: A Benchmarking and Profiling Tool for Iterative Optimization Heuristics’, arXiv:1810.05281 [cs], Oct. 2018, Accessed: Sep. 19, 2021. [Online]. Available: http://arxiv.org/abs/1810.05281
# -------------------------------------------------------------------------------------------

class PSO_SEP(NatureOpt):
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

                if fitness[i] < g_fit:
                    g = X[i]
                    g_fit = fitness[i]













