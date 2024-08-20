import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir(os.path.dirname(__file__))

file = "20240819_059_CuAlTi18_CoarseScan_FC3_500um_1DScan_X.csv"

#target_id = "CuAlTi_18"

#get target id
fline=open(file).readline().rstrip()
spline = fline.split(",")
target_id = spline[1]

#skip header and column headers
data = np.loadtxt(file, skiprows = 2, delimiter = ",")

mirror_x = data[:,0] 

mirror_z = data[:,1] 

target_x = mirror_x/0.0521
target_x = target_x-target_x[0]

target_z = mirror_z/0.0725
target_z = target_z-target_z[0]

num_pulses = data[:,2]

avg_laser_energy = data[:,3]

charge = data[:,4]*1e12 

charge_per_pulse_per_energy = charge/num_pulses/avg_laser_energy

time = data[:,5]

status = data[:,6]

charge_grid = np.reshape(charge_per_pulse_per_energy, (len(np.unique(mirror_z)), len(np.unique(mirror_x))))

#plot the data as a colour scatter plot
set_s = 100/np.sqrt(np.min([len(np.unique(mirror_x)), len(np.unique(mirror_z))]))

#Mirror coords
plt.figure()
plt.title(file[:12] + " " + target_id)
plt.xlabel("Mirror x (mm)")
plt.ylabel("Mirror z (mm)")
plt.scatter(mirror_x, mirror_z, c = charge_per_pulse_per_energy, norm = "log", s=set_s)
plt.colorbar(label = "Charge per pulse per energy (pC/uJ)")
plt.legend()
#plt.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_mirror_scatter.png")

#Target coords
plt.figure()
plt.title(file[:12] + " " + target_id)
plt.xlabel("Target x (mm)")
plt.ylabel("Target z (mm)")
plt.scatter(target_x, target_z, c = charge_per_pulse_per_energy, norm = "log", s=set_s)
plt.colorbar(label = "Charge per pulse per energy (pC/uJ)")
plt.legend()
#plt.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_target_scatter.png")


#plot the data as an imshow

#mirror coords

# linear scaling
fig, ax = plt.subplots()
ax.set_title(file[:12] + " " + target_id)
ax.set_xlabel("Mirror x (mm)")
ax.set_ylabel("Mirror z (mm)")
im = ax.imshow(charge_grid,extent = [np.min(mirror_x), np.max(mirror_x), np.max(mirror_z), np.min(mirror_z)])
fig.colorbar(im, label = "Charge per pulse per energy (pC/uJ)")
fig.legend()
try:
    fig.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_linear_mirror_imshow.png")
except OSError as exc:
    os.mkdir("plots/"+file[:12])
    fig.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_linear_mirror_imshow.png")

# log scaling 
fig, ax = plt.subplots()
ax.set_title(file[:12] + " " + target_id)
ax.set_xlabel("Mirror x (mm)")
ax.set_ylabel("Mirror z (mm)")
im = ax.imshow(charge_grid, norm = "log",extent = [np.min(mirror_x), np.max(mirror_x), np.max(mirror_z), np.min(mirror_z)])
im.set_clim(0.001, 0.03) #set scale to remove outliers 
fig.colorbar(im, label = "Charge per pulse per energy (pC/uJ)")
fig.legend()
fig.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_log_mirror_imshow.png")

#target coords

# linear scaling
fig, ax = plt.subplots()
ax.set_title(file[:12] + " " + target_id)
ax.set_xlabel("Target x (mm)")
ax.set_ylabel("Target z (mm)")
im = ax.imshow(charge_grid,extent = [np.min(target_x), np.max(target_x), np.max(target_z), np.min(target_z)])
fig.colorbar(im, label = "Charge per pulse per energy (pC/uJ)")
fig.legend()
fig.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_linear_target_imshow.png")

# log scaling
fig, ax = plt.subplots()
ax.set_title(file[:12] + " " + target_id)
ax.set_xlabel("Target x (mm)")
ax.set_ylabel("Target z (mm)")
im = ax.imshow(charge_grid, norm = "log",extent = [np.min(target_x), np.max(target_x), np.max(target_z), np.min(target_z)])
fig.colorbar(im, label = "Charge per pulse per energy (pC/uJ)")
fig.legend()
fig.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_log_target_imshow.png")
plt.show()
