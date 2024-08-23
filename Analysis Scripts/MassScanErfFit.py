# fit error function to mass scan data

import numpy as np
import scipy as scipy
import matplotlib.pyplot as plt
import pandas as pd
import os

# this defines the fit function
# amp: height from background to full signal
# center: should be center of the ion bunch
# fwhm: put in the conversion from 1/e^2 (FWHM = sqrt(2ln(2))*w)
# bg: background level (the amp/2 corrects the offset from the halfway point to 0)
def erf(x, amp, center, fwhm, bg):
	return (amp/2)*scipy.special.erf((x-center)/(fwhm/np.sqrt(2*np.log(2)))) + (bg+amp/2)
	
os.chdir(os.path.dirname(__file__))
#print('cwd:', os.getcwd())
#os.chdir('20240822')

# import data and shift the t_window by t_delay to get where the edge is relative to the laser trigger (LD Trig)
file = "Data/20240823/2024-08-23_Mass_scan_Al.csv"
data = pd.read_csv(file, sep=',')[1:]
tdelay = 225
tedge = data['t_window'] + tdelay

#Do the fit with curve_fit and make array for plotting fit
params, cov = scipy.optimize.curve_fit(erf, tedge, data['average charge'], p0=[70, 240, 8, 20])
fitx = np.linspace(.98*min(tedge), 1.02*max(tedge),1000)

# Plot data and fit with parameters
plt.figure('Mass Scan')
plt.errorbar(tedge, data['average charge'], yerr = data['std'], ls = '', marker = 'o', color = 'blue')
plt.plot(fitx, erf(fitx, params[0], params[1], params[2], params[3]), 'k-')
plt.xlabel('Delay from LD Trig (us)', fontsize=14)
plt.ylabel('Average Charge (pC)', fontsize=14)
plt.gca().tick_params(axis='both', which='major', labelsize=10)
plt.annotate('Amplitude: {0:.2f}pC\nCenter: {1:.2f}us\nFWHM: {2:.2f}us\nBackground: {3:.2f}pC'.format(params[0],params[1],params[2],params[3]), (.05,.95), xycoords='axes fraction', fontsize=14, ha='left', va='top')
plt.tight_layout()
plt.savefig('20240823_AlMassScan_ErfFit.png')
plt.show()