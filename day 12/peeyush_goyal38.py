# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:59:50 2018

@author: Peeyush Goyal
"""

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(150.0, 20.0, 1000)
print incomes
plt.hist(incomes, 100)

print np.std(incomes)
print np.var(incomes)
 