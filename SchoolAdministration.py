#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv

def info(students) :
    
    with open ('StudentsInfromation.csv' , mode = 'a+' , newline = '') as csvfile :
        a = csv.writer(csvfile)
       
        if csvfile.tell () == 0 :
            a.writerow (["Name","Age","Mobile_Number","Email_ID"])
        a.writerow (students)
        
if __name__ == "__main__" :
    count = 1
    
    while True :
        print ("\nPlease enter the information of student " + str (count) + " in the given format only :\n")
        StudentsInfromation = input ("\nName, Age, Mobile_Number, Email_ID :\n").split (",")
        print(f"\nName : {StudentsInfromation[0]} \nAge : {StudentsInfromation[1]} \nMobile_Number : {StudentsInfromation[2]} \nEmail_ID : {StudentsInfromation[3]}\n")
        
        choice = input ("\nPlease check if the entered information is correct [type yes/no] :\n")
        if choice == 'yes':
            info (StudentsInfromation)
            
            next_choice = input ("\nDo you want to enter information for another student [type yes/no] ?\n")
            if next_choice == 'no':
                print ("\nThank You!\n")
                break
            else:
                count += 1

