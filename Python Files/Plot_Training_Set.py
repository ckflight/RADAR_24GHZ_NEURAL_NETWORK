import numpy as np
import matplotlib.pyplot as plt

print("Plotting Started")        
 
## This part plots the training-set data results

tick_result_file    = open("radar_result/tick_result.txt","r")
real_result_file    = open("radar_result/real_result.txt","r")
img_result_file     = open("radar_result/img_result.txt","r")
db_result_file      = open("radar_result/db_result.txt","r")
angle_result_file   = open("radar_result/angle_result.txt","r")
abs_result_file     = open("radar_result/abs_result.txt","r")


fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(1, 1, 1)


line     = 0
shot_idx = 0
num_idx  = 0

tick_array = []
abs_array = []

if(line):
    for a in range(line):
        tick_line = tick_result_file.readline()
        abs_line = abs_result_file.readline()
        
# each line is a video 
while(line < 120):
    
    # each line is 174 number times 250 shots (pictures)
    # plot each 174 number and do it 250 times with 20ms delay
    
    tick_line = tick_result_file.readline()
    abs_line = abs_result_file.readline()
        
    tick_line_idx = 0
    abs_line_idx = 0
    tick_last_idx = 0
    abs_last_idx = 0
    
    # each video has 250 pictures
    #while(shot_idx < 250):
    while(shot_idx < 250): # to watch fast
        
        num_idx = 0

        # parse and append to array each 174 number
        while(num_idx < 174):
            
            if(tick_line[tick_line_idx] == ','):
                tick_array.append((np.float)(tick_line[tick_last_idx:tick_line_idx]))
                tick_last_idx = tick_line_idx + 1
                num_idx = num_idx + 1
    
            tick_line_idx = tick_line_idx + 1
        
        
        num_idx = 0
        
        # parse and append to array each 174 number
        while(num_idx < 174):
            
            if(abs_line[abs_line_idx] == ','):
                abs_array.append((np.float)(abs_line[abs_last_idx:abs_line_idx]))
                abs_last_idx = abs_line_idx + 1
                num_idx = num_idx + 1
    
            abs_line_idx = abs_line_idx + 1
        
        
        ax1.clear()
        plt.ylim(0, 30)    # limit y axis between var1 and var2
        plt.xlabel('Distance in mm')
        plt.ylabel('Absolute Value')    
        plt.grid()
        ax1.plot(tick_array, abs_array, 'c')
        
        
        plt.text(120, 25, "Shot: " + str(line), bbox=dict(facecolor = 'red', alpha=0.5))
        if(line < 30):
            plt.text(120, 23, "_Run", bbox=dict(facecolor = 'blue', alpha=0.5))    
        elif(line >= 30 and line < 60):
            plt.text(120, 23, "_Tree", bbox=dict(facecolor = 'green', alpha=0.5))
        elif(line >= 60 and line < 90):
            plt.text(120, 23, "_Walk", bbox=dict(facecolor = 'cyan', alpha=0.5))    
        
             
        plt.pause(0.00001) # 20ms delay is slow for python
        
        tick_array = []
        abs_array = []
        shot_idx = shot_idx + 1 # to play faster add more than 1
    
    
    shot_idx = 0
    line = line + 1    
               
print("Finished")      












