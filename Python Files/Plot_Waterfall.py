import matplotlib.pyplot as plt
import numpy as np

### For waterfall image:
### x axis needs an array (time interval 250 shots with 20ms step)
### y axis needs an array (distance interval 174 ticks max 18 meters)
### z axis needs an multidimensional array [174][250] where each location is related abs value)

abs_file  = open("radar_car_combined/rad-024_car/" + "abs_combined_file.txt",  "r")
tick_file = open("radar_car_combined/rad-024_car/" + "tick_combined_file.txt", "r")

# Create time array 5 second with 250 points 20ms step
time     = np.linspace(0, 5, 250)

# Create distance array, simply take first 174 value of tick file
distance = np.zeros(174)
for i in range(174):
    current = tick_file.readline()
    distance[i] = current[0:len(current)-1]

# Create abs values array for pcolormesh plot each column is one shots 174 abs values
abs_values = np.zeros([174, 250])
for i in range(250):
    for j in range(174):
        current = abs_file.readline()
        abs_values[j][i] = current[0:len(current)-1]

print(time)
print(len(time))

print(distance)
print(len(distance))



fig, ax = plt.subplots()

cmap = ax.pcolormesh(time, distance, abs_values)
fig.colorbar(cmap)
plt.show(fig)