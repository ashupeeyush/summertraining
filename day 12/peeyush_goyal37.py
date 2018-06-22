# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:48:40 2018

@author: Peeyush Goyal
"""

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 50.0, 10000)

print incomes


plt.hist(incomes, 50)
plt.show()

np.mean(incomes)
np.median(incomes)

incomes=np.append(incomes,[10000000])

np.mean(incomes)
np.median(incomes)
plt.hist(incomes, 50)
plt.show()

