import numpy as np
from numba import njit, prange, jit
from UNIOA_Framework.NatureOpt import NatureOpt
from UNIOA_Framework.LevyFlight import Levy

# original MBO framework
# but both Global calculation and Evaluation are asynchronous

class MBO_orig_asyncE_asyncG(NatureOpt):
    def __init__(self, func ,hyperparams_set, budget_factor=1e4):
        super().__init__(func, budget_factor)
        self.M = hyperparams_set.get('popsize', 50)
        self.Keep = hyperparams_set.get('Keep', 2)
        self.maxStepSize = hyperparams_set.get('maxStepSize', 1)
        self.partition = hyperparams_set.get('partition', 5/12)
        self.BAR = hyperparams_set.get('BAR', 5/12)
        self.period = hyperparams_set.get('period', 1.2)

    @staticmethod
    #@njit(parallel=True)
    def migration_opt(func, sorted_pop, sorted_fitness, numButterfly1, numButterfly2, population1, population2, n, period, partition):
        NewPopulation1 = population1.copy()
        NewPopulation1_f = np.zeros(numButterfly1)
        x_g = sorted_pop[0]
        x_g_f = sorted_fitness[0]
        tfs = np.random.rand(numButterfly1, n) * period <= partition
        for i in prange(numButterfly1):
            for j in prange(n):
                if tfs[i, j]:
                    NewPopulation1[i, j] = population1[np.random.randint(numButterfly1), j]
                else:
                    NewPopulation1[i, j] = population2[np.random.randint(numButterfly2), j]
            NewPopulation1_f[i] = func(NewPopulation1[i])
            if NewPopulation1_f[i] < x_g_f:
                x_g = NewPopulation1[i]
                x_g_f = NewPopulation1_f[i]

        return NewPopulation1, NewPopulation1_f, x_g, x_g_f

    @staticmethod
    #@jit(parallel=True)
    def adjusting_opt(func, x_g, x_g_f, genIndex, numButterfly2, population2, maxStepSize,n, partition,budget, BAR,lb_x, ub_x):
        t = genIndex + 1
        scale = maxStepSize / (t * t)
        NewPopulation2 = population2.copy()
        NewPopulation2_f = np.zeros(numButterfly2)
        tfs = np.random.rand(numButterfly2, n) <= partition
        for i in prange(numButterfly2):
            for j in prange(n):
                if tfs[i, j]:
                    NewPopulation2[i, j] = x_g[j]
                else:
                    NewPopulation2[i, j] = population2[np.random.randint(numButterfly2), j]
                    if np.random.rand() > BAR:
                        delataX = Levy(n=n, T=budget)
                        x = NewPopulation2[i, j] + scale * delataX[j]
                        NewPopulation2[i, j] = np.clip(x, lb_x, ub_x)
            NewPopulation2_f[i] = func(NewPopulation2[i])
            if NewPopulation2_f[i] < x_g_f:
                x_g = NewPopulation2[i]
                x_g_f = NewPopulation2_f[i]
        return NewPopulation2, NewPopulation2_f

    def __call__(self):
        numButterfly1 = np.ceil(self.partition*self.M).astype(int)
        numButterfly2 = self.M - numButterfly1

        # initialization
        population = self.Init_X.Init_X(M=self.M, n=self.n, lb_x=self.lb_x, ub_x=self.ub_x)
        # anyway, original code uses the sorted pop in following steps
        fitness = self.Evaluate_X(X = population)
        sorted_fitness = np.sort(fitness)
        I_s = np.argsort(fitness)
        sorted_pop = population[I_s] # for collecting elitists


        genIndex = 0
        while not self.stop:
            # elitism strategy, will use 'keep=2'--------------------------
            chromKeep = np.zeros((self.Keep, self.n))
            costKeep = np.zeros(self.Keep)
            for i in range(self.Keep):
                chromKeep[i] = sorted_pop[i]
                costKeep[i] = sorted_fitness[i]

            # divide into two populations in two lands
            population1 = sorted_pop[0:numButterfly1]
            population2 = sorted_pop[numButterfly1:]

            # migration
            NewPopulation1, NewPopulation1_f, x_g, x_g_f = self.migration_opt(func=self.fitness_function, sorted_pop=sorted_pop, sorted_fitness=sorted_fitness,
                                                                    numButterfly1=numButterfly1, numButterfly2=numButterfly2,
                                                                    population1=population1, population2=population2,
                                                                    n=self.n,
                                                                    period=self.period,
                                                                    partition=self.partition)
            # evaluate new population1
            #NewPop1_fitness = self.Evaluate_X(X = NewPopulation1)


            # adjusting
            NewPopulation2, NewPopulation2_f = self.adjusting_opt(func=self.fitness_function, genIndex=genIndex,
                                                                  x_g=x_g, x_g_f=x_g_f, numButterfly2=numButterfly2,
                                                population2=population2, maxStepSize=self.maxStepSize, n=self.n,
                                                partition=self.partition, budget=self.budget, BAR=self.BAR,
                                                lb_x=self.lb_x, ub_x=self.ub_x)

            # evluate new pop2
            #NewPop2_fitness = self.Evaluate_X(X=NewPopulation2)

            # Combine Population1 with Population2 to generate a new Population
            population = np.concatenate((NewPopulation1, NewPopulation2))
            fitness = np.concatenate((NewPopulation1_f, NewPopulation2_f))
            # Sort from best to worst
            I_s = np.argsort(fitness)
            sorted_pop = population[I_s]
            sorted_fitness = fitness[I_s]

            #      Elitism Strategy     = selection
            # Replace the worst with the previous generation's elites.
            for k3 in range(self.Keep):
                sorted_pop[-(k3+1)] = chromKeep[k3]
                sorted_fitness[-(k3+1)] = costKeep[k3]

            # Sort from best to worst again
            I_s = np.argsort(sorted_fitness)
            sorted_pop = sorted_pop[I_s]
            sorted_fitness = sorted_fitness[I_s]

            genIndex = genIndex + 1
                            
                    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
    