# RADAR_24GHZ_NEURAL_NETWORK

Python Radar record parse, fft video and waterfall plot and Matlab object type detection using neural network classification algorithm. What i mean by FFT video is that, radar buffers FFT images during record time with step time between each new FFT image. Combination of each image with a time step is simply a video.

It detects whether the radar record belongs to a walking person, running person or stationary object like tree with little movement because of wind.

The radar files are parsed and combined in a single .txt files by using PYTHON scripts below.
Then MATLAB is running Neural Network Front and Back Propagation on radar files for classification. For each class 30 records are split into 15 training set for Neural Network and 15 test set for measuring the accuracy. It detects each type with 100% accuracy over FFT records with just 15 training examples per class. In each class movement was at a different pase and direction. For example for running class: Person was running at different speeds each time and as direction from start point to end in one record and from end point to start in other one.

The example Waterfall plot belongs to a moving car. Doppler shifts can be seen easily as well.
The example FFT plot is one picture of a video of running person. The peak moves from beginning to end. Run with radar_result folder to see. 

Due to the upload size unparsed data of radar is not uploaded to github. Therefore i uploaded parsed and ready to use data in radar_result files in 2 parts in zip file. Put all .txt files under same folder named as radar_result.

Matlab uses this radar_result folder's files for Neural Network classification as well.

PYTHON Files:
1.	Run Parse_Combine_Set.py to combine shots, Radar sends record with one file for each fft image for specified range
2.	Run Create_Training_Set.py to create final training set from combined files to use with MATLAB
3.	Use Plot_Training_Set.py to plot radar videos. Each record video is labeled for indicating if it is walk, run, car etc. 
4.  Plot_Waterfall.py to see colormesh of the result. 

MATLAB Files:
1. main.m
2. load_data.m (change folder path) , loads radar_result files
3. fmincg.m, lrCostFunction.m, sigmoid.m are all Neural Network related files.

![car_watermark](https://user-images.githubusercontent.com/61315249/82326657-d6e34300-99e5-11ea-8004-1b3b01aaef30.png)

![running](https://user-images.githubusercontent.com/61315249/82326898-37728000-99e6-11ea-909c-c5766b5d3f8d.png)

![nn1](https://user-images.githubusercontent.com/61315249/82327504-2ece7980-99e7-11ea-908c-f69e4695effc.png)

![nn2](https://user-images.githubusercontent.com/61315249/82327499-2c6c1f80-99e7-11ea-8b4b-2d39561f3492.png)

