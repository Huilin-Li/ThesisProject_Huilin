from UNIOA_Framework.NatureOpt import NatureOpt
import numpy as np
import math

# original MFO framework
# but the Evaluation becomes synchronous

class MFO_orig_syncE(NatureOpt):
    def __init__(self, func ,hyperparams_set, budget_factor = 1e4):
        super().__init__(func, budget_factor)
        self.N = hyperparams_set.get('popsize', 30)
        
    def __call__(self):
        # Initialize the positions of moths
        Moth_pos = np.random.uniform(self.lb_x, self.ub_x, (self.N, self.n))
        # Moth_fitness = self.Evaluate_X(X=Moth_pos)

        Iteration = 0
    
        # Main loop
        while not self.stop:
    
            # Number of flames Eq. (3.14) in the paper
            Flame_no = round(self.N - Iteration * ((self.N - 1) / self.budget))

            for i in range(self.N):
                Moth_pos[i] = np.clip(Moth_pos[i], self.lb_x, self.ub_x)
            Moth_fitness = self.Evaluate_X(X = Moth_pos)


            if Iteration == 0:
                # Sort the first population of moths
                fitness_sorted = np.sort(Moth_fitness)
                I = np.argsort(Moth_fitness)
                sorted_population = Moth_pos[I]
                # Update the flames
                best_flames = sorted_population.copy()
                best_flame_fitness = fitness_sorted.copy()
            else:
                # Sort the moths
                double_population = np.concatenate((previous_population, best_flames), axis=0)
                double_fitness = np.concatenate((previous_fitness, best_flame_fitness), axis=0)
                double_fitness_sorted = np.sort(double_fitness)
                I2 = np.argsort(double_fitness)
                double_sorted_population = double_population[I2]

                fitness_sorted = double_fitness_sorted[0:self.N]
                sorted_population = double_sorted_population[0:self.N]
                # Update the flames
                best_flames = sorted_population.copy()
                best_flame_fitness = fitness_sorted.copy()

            previous_population = Moth_pos.copy()
            previous_fitness = Moth_fitness.copy()

            # a linearly dicreases from -1 to -2 to calculate t in Eq. (3.12)
            a = -1 + Iteration * ((-1) / self.budget)
    
            # Loop counter
            for i in range(0, self.N):
                b = 1
                t = (a - 1) * np.random.rand() + 1
                for j in range(0, self.n):
                    distance_to_flame = abs(sorted_population[i, j] - Moth_pos[i, j])
                    if i <= Flame_no:
                        Moth_pos[i, j] = distance_to_flame * math.exp(b * t) * math.cos(t * 2 * math.pi)+ sorted_population[i, j]
                    else:
                        Moth_pos[i, j] = distance_to_flame * math.exp(b * t) * math.cos(t * 2 * math.pi) + sorted_population[Flame_no, j]
                # check boundary
                # Moth_pos[i] = np.clip(Moth_pos[i], self.lb_x, self.ub_x)
                # Moth_fitness[i] = self.fitness_function(Moth_pos[i])

            #Moth_fitness = self.Evaluate_X(X=Moth_pos)
            Iteration = Iteration + 1