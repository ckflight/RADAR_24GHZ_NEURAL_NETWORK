import numpy as np
import os

### 
###    Radar stores data as N number of shots where each shot is one fft picture
###    This code parses data from N sub folder of radar folders and combined them
###    together as an one video. Current radar setting was 20ms * 250 shots = 5 sec video
###
###    The code creates radar_(type)_combined file and each rad-xxx_(type) folder is combined
###    in a related txt file. Each xx_u.dat file has 5 type of data as:
###    tick(distance), real, imaginary, db and angle. 
###    Absolute value from real and img numbers are created and stored which is the one that is used.
###

# Now each line has tick, real, img, level_db and angle_deg data
NUMBER_OF_COLUMN_PER_LINE = 5
TICK_COLUMN               = 0
REAL_COLUMN               = 1
IMG_COLUMN                = 2
DB_COLUMN                 = 3
ANGLE_COLUMN              = 4

print("Parse and Combine Started")

tick_array   = []
real_array   = []
img_array    = []
db_array     = []
angle_array  = []
abs_array    = [] # computed from real and img arrays at the end of parsing.

temp_string = ""

NUMBER_OF_TYPE      = 1
NUMBER_OF_FILES     = 30
NUMBER_OF_SHOTS     = 250
shot_counter        = 0
file_counter        = 1
type_counter        = 0 # select number for not running the code over all types

# After implementing this function, i found out that (np.float)("-1.342424e01") is doing it automatically lol.
def string_to_float(str_value):
    
    current_idx = 0
    main_sign = 1.0
    exp_sign = 1
    
    is_main_set = False
    is_frac_set = False
    frac_order_counter = 1  # fractional 10th power counter
    main_part = 0.0         # main number part until '.' char
    frac_part = 0.0         # fractional part until 'e' char
    exp_part = 0            # exponential part after 'e' char
    
    # if number has - sign set 
    if(str_value[current_idx] == '-'):
        main_sign = -1.0
        current_idx = current_idx + 1
           
    while(current_idx < len(str_value)):
        
        current_char = str_value[current_idx]
        
        # if char is '.' then the current index is pointing to main integer part char
        if(current_char == '.' and is_main_set == False):
            current_char = str_value[current_idx - 1]
            main_part = char_to_float(current_char)
            is_main_set = True
        
        # is it moved to fractional part (part after '.' char)
        elif(is_main_set and is_frac_set == False):
            if(current_char != 'e'):
                num = char_to_int(current_char) * pow(10, ((-1)*frac_order_counter))
                frac_part += (np.float)(num)
                frac_order_counter = frac_order_counter + 1    
                
            # the current char is 'e'
            else:
                is_frac_set = True
                
        
        elif(is_frac_set):
            
            if(current_char == '-'):
                exp_sign = -1               
                # send rest to function and get the exponential multiplier
                str_sub = str_value[current_idx+1: current_idx+3]
                exp_part = pow(10, exp_sign * exp_to_int(str_sub))                
                current_idx = len(str_value)
                
            elif(current_char == '+'):
                exp_sign = 1
                # send rest to function and get the exponential multiplier
                str_sub = str_value[current_idx+1: current_idx+3]
                exp_part = pow(10, exp_sign * exp_to_int(str_sub))                                
                current_idx = len(str_value)
                
        current_idx = current_idx + 1    
    
    
    return ((main_sign * (main_part + frac_part)) * exp_part)

def exp_to_int(str_in):
    
    if(len(str_in) == 2):
        int1 = (np.uint8)(str_in[0])
        int2 = (np.uint8)(str_in[1])
    else:
        print("error at exp_to_int function")    
    
    res = ((int1 * 10) + int2)
    return (np.int)(res)
    

def char_to_float(c):
    
    return (np.float)(c)
    
def char_to_int(c):
    
    return (np.uint8)(c)
 
 
while(type_counter < NUMBER_OF_TYPE):
     
    if(type_counter == 0):
        type_string = "_run"    
    elif(type_counter == 1):
        type_string = "_tree"
    elif(type_counter == 2):
        type_string = "_walk"
    elif(type_counter == 3):
        type_string = "_car"
     
    if not os.path.exists("radar" + type_string + "_combined"):
        os.mkdir("radar" + type_string + "_combined")    
     
    file_counter = 1
    print(type_string)
     
    while(file_counter <= NUMBER_OF_FILES):
         
        if(file_counter <= 9):
            file_string = "radar" + type_string + "/rad-00" + str(file_counter) + type_string + "/"
                 
            if not os.path.exists("radar" + type_string + "_combined/rad-00" + str(file_counter) + type_string):
                os.mkdir("radar" + type_string + "_combined/rad-00" + str(file_counter) + type_string)
             
                 
            tick_combined_file  = open("radar" + type_string + "_combined/rad-00" + str(file_counter) + type_string + "/" + "tick_combined_file.txt","w")
            real_combined_file  = open("radar" + type_string + "_combined/rad-00" + str(file_counter) + type_string + "/" + "real_combined_file.txt","w")
            img_combined_file   = open("radar" + type_string + "_combined/rad-00" + str(file_counter) + type_string + "/" + "img_combined_file.txt","w")
            db_combined_file    = open("radar" + type_string + "_combined/rad-00" + str(file_counter) + type_string + "/" + "db_combined_file.txt","w")
            angle_combined_file = open("radar" + type_string + "_combined/rad-00" + str(file_counter) + type_string + "/" + "angle_combined_file.txt","w")
            abs_combined_file   = open("radar" + type_string + "_combined/rad-00" + str(file_counter) + type_string + "/" + "abs_combined_file.txt","w")
             
        else:
            file_string = "radar" + type_string + "/rad-0" + str(file_counter) + type_string + "/"
             
            if not os.path.exists("radar" + type_string + "_combined/rad-0" + str(file_counter) + type_string):
                os.mkdir("radar" + type_string + "_combined/rad-0" + str(file_counter) + type_string)
             
             
            tick_combined_file  = open("radar" + type_string + "_combined/rad-0" + str(file_counter) + type_string + "/" + "tick_combined_file.txt","w")
            real_combined_file  = open("radar" + type_string + "_combined/rad-0" + str(file_counter) + type_string + "/" + "real_combined_file.txt","w")
            img_combined_file   = open("radar" + type_string + "_combined/rad-0" + str(file_counter) + type_string + "/" + "img_combined_file.txt","w")
            db_combined_file    = open("radar" + type_string + "_combined/rad-0" + str(file_counter) + type_string + "/" + "db_combined_file.txt","w")
            angle_combined_file = open("radar" + type_string + "_combined/rad-0" + str(file_counter) + type_string + "/" + "angle_combined_file.txt","w")
            abs_combined_file   = open("radar" + type_string + "_combined/rad-0" + str(file_counter) + type_string + "/" + "abs_combined_file.txt","w")
         
        print(file_string)
         
        shot_counter = 0
         
        while(shot_counter < NUMBER_OF_SHOTS):
         
            #naming : 00-09_u.dat, 10-19, ....
             
            if(shot_counter <= 9):
                shot_string = "0" + str(shot_counter) + "_u.dat"
                 
            else:
                shot_string = str(shot_counter) + "_u.dat"
                         
            radarFile = open(file_string + shot_string,"r")
             
            line_str = " "
             
            while (len(line_str)):        
             
                line_str = radarFile.readline()
                line_str_length = len(line_str)
                #print "new line is: " + line_str + "length of line is: " + str(line_str_length )
                 
                idx = 0
                # each line has NUMBER_OF_DATA_PER_LINE data so count it to decide which number is parsed
                line_data_counter = 0
                 
                if(line_str_length):
                     
                    # start parsing if line is data line
                    if(line_str[idx] != '#' and line_str != "\r\n"):
                         
                        ## loop the entire line to parse
                        while(idx < len(line_str)):            
                             
                            ## add chars while it is number related
                            if(line_str[idx] != ' ' and line_str[idx] != '\t' and line_str[idx] != '\r' and line_str[idx] != '\n'):
                                while(line_str[idx] != ' ' and line_str[idx] != '\t' and line_str[idx] != '\r' and line_str[idx] != '\n'):
                                    temp = line_str[idx]
                                    temp_string = temp_string + temp
                                    idx = idx + 1 
                                 
                            
                                result = (np.float)(temp_string)
                                result = round(result,3)
                                
                                # parse the current string and convert it to float here
                                if(line_data_counter == TICK_COLUMN):# First string number belongs to tick column
                                     
                                    # tick is not needed to combined since it gives same 161 values everytime
                                    tick_combined_file.write((np.str)(result) + "\r\n")
                                    tick_array.append(result)                    
                                     
                                elif(line_data_counter == REAL_COLUMN):
                                    
                                    real_combined_file.write((np.str)(result) + "\r\n")
                                    real_array.append(result)
                                 
                                elif(line_data_counter == IMG_COLUMN):    
                                    
                                    img_combined_file.write((np.str)(result) + "\r\n")
                                    img_array.append(result)
                                     
                                elif(line_data_counter == DB_COLUMN):  
                                    
                                    db_combined_file.write((np.str)(result) + "\r\n")
                                    db_array.append(result)
                                     
                                elif(line_data_counter == ANGLE_COLUMN):   
                                     
                                    angle_combined_file.write((np.str)(result) + "\r\n")
                                    angle_array.append(result)
                                                             
                                line_data_counter = line_data_counter + 1
                                 
                                temp_string = ""# reset string for next number                                
                                     
                            else:
                                idx = idx + 1    
                         
                    else:
                        continue   
               
             
             
             
             
            for i in range(len(tick_array)):    
                x = complex(real_array[i], img_array[i])
                x = round(abs(x),3)
                abs_combined_file.write((np.str)(x) + "\r\n")
                abs_array.append(abs(x))
             
              
            tick_array   = []
            real_array   = []
            img_array    = []
            db_array     = []
            angle_array  = []
            abs_array    = []
             
            shot_counter = shot_counter + 1
             
         
         
        tick_combined_file.close()
        real_combined_file.close()
        img_combined_file.close()
        db_combined_file.close()
        angle_combined_file.close()
        abs_combined_file.close()
         
        file_counter = file_counter + 1        
 
     
    type_counter = type_counter + 1


               
print("Finished")      












