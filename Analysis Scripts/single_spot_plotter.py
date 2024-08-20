import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__))
first_file = 40
last_file = 49

fileIDs = np.arange(first_file,last_file+1,1)

avg_charge = {}
for fileID in fileIDs:
    file = "Data\\20240819\\20240819_CuAlTi18_0"+str(fileID)+"IonDetection_FC3_TargetCenter.csv"
    data = np.loadtxt(file, skiprows = 2, delimiter =",")
    num_pulses = data[:,0] 
    laser_power = data[:,1]
    charge = data[:,2]
    charge = charge*1e12 # convert from C to pC
    time = data[:,3]
    status = data[:,4]
    avg_charge[fileID] = (np.mean(charge/laser_power/num_pulses)) #this is in units pC/uJ (per pulse)


# up/down steering with SEL1/3
up_down_tuning = [None]*10
up_down_tuning[0] = {"top":-1700,"left":-1700,"bottom":-1700,"right":-1700} #File 40 
up_down_tuning[1] = {"top":-1710,"left":-1700,"bottom":-1690,"right":-1700} #File 41
up_down_tuning[2] = {"top":-1720,"left":-1700,"bottom":-1680,"right":-1700} #File 42
up_down_tuning[3] = {"top":-1730,"left":-1700,"bottom":-1670,"right":-1700} #File 43
up_down_tuning[4] = {"top":-1740,"left":-1700,"bottom":-1660,"right":-1700} #File 44
up_down_tuning[5] = {"top":-1700,"left":-1700,"bottom":-1700,"right":-1700} #File 45
up_down_tuning[6] = {"top":-1690,"left":-1700,"bottom":-1710,"right":-1700} #File 46
up_down_tuning[7] = {"top":-1680,"left":-1700,"bottom":-1720,"right":-1700} #FIle 47
up_down_tuning[8] = {"top":-1670,"left":-1700,"bottom":-1730,"right":-1700} #File 48
up_down_tuning[9] = {"top":-1660,"left":-1700,"bottom":-1740,"right":-1700} #File 49

plt.figure()
plt.scatter([SEL["top"] for SEL in up_down_tuning], [avg_charge[file] for file in fileIDs])
plt.ylim(0,0.06)
plt.title("File 2024-08-19 40-49 up/down tuning")
plt.xlabel("Split Einzel Lens Top Voltage (V)")
plt.ylabel("Average Charge per Pulse (pC/uJ)")

# Common voltage tuning
first_file = 50
last_file = 57

fileIDs = np.arange(first_file,last_file+1,1)

fileIDs = np.delete(fileIDs,list(fileIDs).index(51))
print(fileIDs)
avg_charge = {}
for fileID in fileIDs:
    file = "Data\\20240819\\20240819_CuAlTi18_0"+str(fileID)+"IonDetection_FC3_TargetCenter.csv"
    data = np.loadtxt(file, skiprows = 2, delimiter =",")
    num_pulses = data[:,0] 
    laser_power = data[:,1]
    charge = data[:,2]
    charge = charge*1e12 # convert from C to pC
    time = data[:,3]
    status = data[:,4]
    avg_charge[fileID] = (np.mean(charge/laser_power/num_pulses)) #this is in units pC/uJ (per pulse)

Common_voltage_tuning = [None]*7
Common_voltage_tuning[0] = {"top":-1725,"left":-1725,"bottom":-1725,"right":-1725} #File 50

# File 51 bad!

Common_voltage_tuning[1] = {"top":-1750,"left":-1750,"bottom":-1750,"right":-1750} #File 52
Common_voltage_tuning[2] = {"top":-1650,"left":-1650,"bottom":-1650,"right":-1650} #File 53
Common_voltage_tuning[3] = {"top":-1600,"left":-1600,"bottom":-1600,"right":-1600} #File 54
Common_voltage_tuning[4] = {"top":-1550,"left":-1550,"bottom":-1550,"right":-1550} #File 55
Common_voltage_tuning[5] = {"top":-1625,"left":-1625,"bottom":-1625,"right":-1625} #File 56
Common_voltage_tuning[6] = {"top":-1650,"left":-1650,"bottom":-1650,"right":-1650} #File 57

plt.figure()
plt.scatter([SEL["top"] for SEL in Common_voltage_tuning], [avg_charge[file] for file in fileIDs])
plt.title("File 2024-08-19 50-57 Common SEL Voltage tuning")
plt.xlabel("Split Einzel Lens Top Voltage (V)")
plt.ylabel("Average Charge per Pulse (pC/uJ)")
plt.show()






