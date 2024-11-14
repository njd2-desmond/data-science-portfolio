from scipy.stats import poisson,binom
import pandas as pd
import numpy as np
runs = 2847
balls_faced = 4330
ratio = runs / balls_faced

runs = [0,1,2,3,4,6]
outcomes = [0.3, 0.4, 0.1, 0.02, 0.1, 0.08]

balls = 0
while balls <= 100:
    result = np.random.choice(runs,p=outcomes)
    print(result)
    balls += 1