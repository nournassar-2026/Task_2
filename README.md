This task is about merging and cleaning data files.
firstly in the inner merge type the number of rows are 49 while in the left merge type they where 86.
Cleaning of the files dropped the raws with NAN values and changed the negative amount in the amount_cad column to 0.
After the cleaning both merged files have the same number of rows, which is 47.
The main script calls the two functions : clean.py and merge.py .
The script answers the three questions :  ① Which researcher has the highest total citations?
-Claire   Davidson
citations   9999
 ② Which field received the most total funding? 
 Field with most funding:
Machine Learning: $880,000.00
 ③ Who joined earliest and is still active?
 -Earliest joined active researcher: Name: Jiyeon Park Joined year: 2008
 * The data has been saved to the file: output/clean_research_data_inner.csv