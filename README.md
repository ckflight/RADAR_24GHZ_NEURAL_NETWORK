# RADAR_24GHZ_NEURAL_NETWORK
Object type detection using neural network classification algorithm.

It detects whether the radar record belongs to a walking person, running person, a car or stationary object like tree with little movement because of wind.

PYTHON Files:
1.	Run Parse_Combine_Set to combine shots, Radar sends record with one file for each fft image for specified range
2.	Run Create_Training_Set to create final training set from combined files to use with MATLAB
3.	Use Plot_Training_Set to plot radar videos. Each record video is labeled for indicating if it is walk, run, car etc. (It plots slower than actual record speed)

MATLAB Files:
