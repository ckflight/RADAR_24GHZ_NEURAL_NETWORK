# Radar Object Type Detection Using Neural Network Algorithm

## Project Details:

 * This repository implements a neural network algorithm. I wrote these Matlab scripts when i received **Machine Learning** certificate course by **Andrew Ng** from **Stanford  University**. Therefore the implementation is highly optimized for best speed results.

### Parse_Combine_Set.py

 * The radar that i used on this project had a different kind of data recording. It recorded file on different .txt files for N number of samples and each .txt file has a specific encoding along with other configuration data of the hardware. Therefore, the data needed to be parsed. This python script parses the data and combines them in one final .txt file. 

### Create_Training_Set.py

 * This python script creates a training set to be used along with the Mathlab scripts.

### Plot_Training_Set.py

 * Plots the training set for visualisation of the each FFT video of the Radar data. Each record video is labeled for indicating if it is walk, run, car etc. The objects can be seen at a specific distance and related frequency. What i mean by the FFT video is that, the radar buffers FFT images during record time with step time between each new FFT image. The combination of each image with a time step is simply a video. Therefore the Matlab plot is not a stationary image but, a video showing the movement of the objects detected by the radar. 
 
 * **Example Screenshot** of the FFT plot is one picture of a video of running person. The peak moves from beginning to end. Run with radar_result folder to see.

### Plot_Waterfall.py

 * Plots the radar data in a waterfall format for different kind of visualisation.
 
 * **Example Screenshot** of the Waterfall plot belongs to a moving car. Doppler shift effect can be seen easily as well. The Doppler shift is the effect that moving objects shift the frequency of the reflected signal. By checking the amount of frequency shift, the speed of the object can be detected. Earlier simpler radars used this principal to detect the speed of the moving objects without Frequency Modulation)

### Matlab Files:

 * Matlab scripts are running Neural Network Front and Back Propagation on the radar files for classification. It detects whether the radar record belongs to a    walking person, running person or stationary object like tree with little movement because of the wind. For each class 30 records are split into 15 training set for Neural Network and 15 test set for measuring the accuracy. It detects each type with 100% accuracy over FFT records with just 15 training examples per class. In each class the movement was at a different pace and direction. For example, for running class: Person was running at a different speed each time and as direction from start point to end in one record and from end point to start in the other one.
 
 1. **main.m**, main matlab script for running the algorithm
 2. **load_data.m** (change folder path) , loads radar_result files
 3. **fmincg.m**, **lrCostFunction.m**, **sigmoid.m** are all Neural Network related files.

Due to the upload size unparsed data of radar is not uploaded to github. I just uploaded parsed and ready to use data in radar_result files in 2 parts in zip file. Put all .txt files under same folder and rename the folder as **radar_result**.

Matlab uses this **radar_result** folder's files for Neural Network classification as well.

![car_watermark](https://user-images.githubusercontent.com/61315249/82326657-d6e34300-99e5-11ea-8004-1b3b01aaef30.png)

![running](https://user-images.githubusercontent.com/61315249/82326898-37728000-99e6-11ea-909c-c5766b5d3f8d.png)

![nn1](https://user-images.githubusercontent.com/61315249/82327504-2ece7980-99e7-11ea-908c-f69e4695effc.png)

![nn2](https://user-images.githubusercontent.com/61315249/82327499-2c6c1f80-99e7-11ea-8b4b-2d39561f3492.png)

