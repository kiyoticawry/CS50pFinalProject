# Habitual Tracker
    #### Video Demo:  https://youtu.be/x2suBwpqh_s
    #### Description:
This is a simple program that takes in a CSV file in a format of (date,scale) yyyy-mm-dd,int 0 - 9 and then produces either a heatmap, a bar or a plotted line in a graph. However due to limitations in the cs50 codespace it will only save a png file showcasing the data instead of show() Nonetheless the user Still needs to have actual data for the program to work with. The user could manually type in his data or run a program that makes it WHENEVER he does a habit of his choosing. Do note that Scale is not a measurement of anything other than whether the User has done a habit or a task. A habit adding 1 to the scale and a task adding 0.5 to it Yet, the user can still decide any sort of scale measurement on his own so long as it is an int between 0 - 9.

Initially the program will prompt the user to type in the name of the CSV file which has to be in the same directory as the program. A None CSV file will be rejected, If the data is something other than yyy-mm-dd,int 0 - 9 then the program will crash. It also does not show the entire data for bar and plotted line, only the last 28 days since showing all the data makes it very unreadable. You cannot also decide what month you would like to see but only the last 28 days. These are missing features due the limited time and contraints when making this project

There is also a shortcut where the User could just give the following arguments: habitualtracker.py (nameofcsv.csv) h|b|L
    Allowing to bypass the need of greetings and to instantly produce the desired result

This program is also tailored to the specific problems I encountered in making the data, If you have multiple days repeating the program will add the scale of all those days, If you have some days missing then the program will add those days with a scale of 0.0 as it implies you didn’t do any habit or task. You will then be prompted the name for the CSV file which it will be saved before being actually processed

Lastly, the program doesnt do any math, It only fixes/plots the data as to be seen in heatmap or bar or plotted line on a PNG
    
    
    

