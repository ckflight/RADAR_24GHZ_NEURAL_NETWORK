import os


print("Create Training-set Started")
          
##
##    This code creates one final radar_result folder 
##    which has final result txt files of previously combined shot txt files
##    Each shot has one column and separated comma.
##
##


NUMBER_OF_ROWS      = 174*250   # 174 ticks (radar max dist. sets number of data at each shot) and 250 shots
NUMBER_OF_TYPE      = 4         # 4 types of movement recorded with radar run, walk, tree
NUMBER_OF_FILES     = 30        # Each type has 30 records
NUMBER_OF_TXT       = 6         # 6 data type tick, real, img, db, angle and abs.
file_counter        = 1
type_counter        = 3
txt_counter         = 0
row_counter         = 0
 



# Create file if not exists
if not os.path.exists("radar_result"):
    os.mkdir("radar_result")
             
# open files in append mode so at each write it will continue from last write point     
tick_result_file  = open("radar_result/" + "tick_result.txt","a")
real_result_file  = open("radar_result/" + "real_result.txt","a")
img_result_file   = open("radar_result/" + "img_result.txt","a")
db_result_file    = open("radar_result/" + "db_result.txt","a")
angle_result_file = open("radar_result/" + "angle_result.txt","a")
abs_result_file   = open("radar_result/" + "abs_result.txt","a")

while(type_counter < NUMBER_OF_TYPE):
 
    if(type_counter == 0):
        type_string = "_run"    
    elif(type_counter == 1):
        type_string = "_tree"
    elif(type_counter == 2):
        type_string = "_walk"
    elif(type_counter == 3):
        type_string = "_car"
    
    
    print(type_string)
 
    while(file_counter <= NUMBER_OF_FILES):
         
        if(file_counter <= 9):        
            current_folder_string = "radar" + type_string + "_combined/" + "rad-00" + str(file_counter) +  type_string
        else:
            current_folder_string = "radar" + type_string + "_combined/" + "rad-0" + str(file_counter) +  type_string
         
        print(file_counter)
         
        # 5 txt files each will be opened and their 43500 values will be written to one column of final txt
        while(txt_counter < NUMBER_OF_TXT):
             
            if(txt_counter == 0):
                current_read_txt = open(current_folder_string + "/" + "tick_combined_file.txt", 'r')
                current_write_txt = tick_result_file     
             
            elif(txt_counter == 1):
                current_read_txt = open(current_folder_string + "/" + "real_combined_file.txt", 'r')
                current_write_txt = real_result_file
                 
            elif(txt_counter == 2):
                current_read_txt = open(current_folder_string + "/" + "img_combined_file.txt", 'r')
                current_write_txt = img_result_file
                 
            elif(txt_counter == 3):
                current_read_txt = open(current_folder_string + "/" + "db_combined_file.txt", 'r')
                current_write_txt = db_result_file
                 
            elif(txt_counter == 4):
                current_read_txt = open(current_folder_string + "/" + "angle_combined_file.txt", 'r')
                current_write_txt = angle_result_file
            
            elif(txt_counter == 5):
                current_read_txt = open(current_folder_string + "/" + "abs_combined_file.txt", 'r')
                current_write_txt = abs_result_file              
             
            while(row_counter < NUMBER_OF_ROWS):
                 
                current_line_number = current_read_txt.readline()
                 
                length = len(current_line_number)
                 
                if(length):
                     
                    current_line_number = current_line_number[0:length-1] # delete /n from string
                 
                    current_write_txt.write(current_line_number + ",")
 
                    row_counter = row_counter + 1
                     
                else:

                    print("Numb of rows: " + str(row_counter))
                     
                    row_counter = NUMBER_OF_ROWS
         
             
            current_write_txt.write("\r\n")
          
            row_counter = 0
         
            txt_counter = txt_counter + 1
         
        
        txt_counter = 0
        
        file_counter = file_counter + 1
     
     
    file_counter = 1
     
    type_counter = type_counter + 1


print("Finished")      












