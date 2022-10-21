# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import random

def f_x(x):
       return np.exp(-x) * x * (x**2 - x - 1)

x = np.linspace(-1,4, 1000)#Plot the curve
plt.plot(x, f_x(x))
plt.show()
