import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir(os.path.dirname(__file__))

file = "20240815_003 CuAlTi18 250um 10mmx12mm.csv"

target_id = "CuAlTi_18" #test

data = np.loadtxt(file, skiprows = 1, delimiter = ",")

mirror_x = data[:,0] 

mirror_z = data[:,1] 

target_x = mirror_x/0.0521
target_x = target_x-target_x[0]

target_z = mirror_z/0.0725
target_z = target_z-target_z[0]

num_pulses = data[:,2]

charge = data[:,3] 

charge_per_pulse = charge/num_pulses

time = data[:,4]

status = data[:,5]

charge_grid = np.reshape(charge_per_pulse, (len(np.unique(mirror_z)), len(np.unique(mirror_x))))

#plot the data as a colour scatter plot

#Mirror coords
plt.figure()
plt.title(file[:12] + " " + target_id)
plt.xlabel("Mirror x (mm)")
plt.ylabel("Mirror z (mm)")
plt.scatter(mirror_x, mirror_z, c = charge_per_pulse, norm = "log", s=len(mirror_x)/35)
plt.colorbar(label = "Charge per pulse (C)")
plt.legend()
#plt.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_mirror_scatter.png")

#Target coords
plt.figure()
plt.title(file[:12] + " " + target_id)
plt.xlabel("Target x (mm)")
plt.ylabel("Target z (mm)")
plt.scatter(target_x, target_z, c = charge_per_pulse, norm = "log", s=len(mirror_x)/35)
plt.colorbar(label = "Charge per pulse (C)")
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
fig.colorbar(im, label = "Charge per pulse (C)")
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
fig.colorbar(im, label = "Charge per pulse (C)")
fig.legend()
fig.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_log_mirror_imshow.png")

#target coords

# linear scaling
fig, ax = plt.subplots()
ax.set_title(file[:12] + " " + target_id)
ax.set_xlabel("Target x (mm)")
ax.set_ylabel("Target z (mm)")
im = ax.imshow(charge_grid,extent = [np.min(target_x), np.max(target_x), np.max(target_z), np.min(target_z)])
fig.colorbar(im, label = "Charge per pulse (C)")
fig.legend()
fig.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_linear_target_imshow.png")

# log scaling
fig, ax = plt.subplots()
ax.set_title(file[:12] + " " + target_id)
ax.set_xlabel("Target x (mm)")
ax.set_ylabel("Target z (mm)")
im = ax.imshow(charge_grid, norm = "log",extent = [np.min(target_x), np.max(target_x), np.max(target_z), np.min(target_z)])
fig.colorbar(im, label = "Charge per pulse (C)")
fig.legend()
fig.savefig("plots/"+file[:12]+"/"+file[:12]+"_plot_log_target_imshow.png")
plt.show()
