import matplotlib.pyplot as plt
import os
import numpy as np
from scipy.optimize import curve_fit
import scipy.special as sp

def erf(x, a,width, center, offset):
    return a*sp.erf((x-center)*1/width)+offset

os.chdir(os.path.dirname(__file__))
file = "Data/20240822/20240822_t_delay_massScan.csv"

data = np.loadtxt(file, delimiter = ",", skiprows = 1)
t_window = data[:,0] 
avg_charge = data[:,1]
std_charge = data[:,2]

params, covariance = curve_fit(erf, t_window, avg_charge, p0=[70, 15, 31, 6])

print(params)

fig, ax = plt.subplots()
plot_t_windows = np.arange(0,45,0.01)
plot_erf = erf(plot_t_windows, params[0], params[1], params[2], params[3])
ax.plot(plot_t_windows,plot_erf, label = "fit")
ax.scatter(t_window, avg_charge)
ax.errorbar(t_window, avg_charge, yerr = std_charge, linestyle ="")
ax.set_title(file)
ax.set_xlabel()
plt.show()