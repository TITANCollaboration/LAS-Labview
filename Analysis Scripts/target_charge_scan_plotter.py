import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir(os.path.dirname(__file__))

file = "20240814_001_BigScan11mmx11mmFullTarget.txt"

data = np.loadtxt(file, skiprows = 1, delimiter = ",")

mirror_x = data[:,0] 

mirror_z = data[:,1] 

target_x = mirror_x/0.0531

target_z = mirror_z/0.0720

num_pulses = data[:,2]

charge = data[:,3] 

time = data[:,4]

status = data[:,5]

charge_grid = np.reshape(charge, (len(np.unique(mirror_z)), len(np.unique(mirror_x))))

#plot the data as a colour scatter plot
plt.figure()
plt.scatter(mirror_x, mirror_z, c = charge, norm = "log")
plt.colorbar()
#plot the data as an imshow

fig, ax = plt.subplots()
im = ax.imshow(charge_grid, norm = "log",extent = [np.min(mirror_x), np.max(mirror_x), np.max(mirror_z), np.min(mirror_z)])
fig.colorbar(im)

plt.show()
