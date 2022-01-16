import numpy as np

class Init_X:
    @staticmethod
    def Init_X(M, n, lb_x, ub_x):
        np.random.seed(2)
        X = np.random.uniform(lb_x, ub_x, (M, n))
        return X

