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

                
"""

OUTPUT :

Please enter the information of student 1 in the given format only :


Name, Age, Mobile_Number, Email_ID :
Yugi, 19, 915476254, yugiyugi@gmail.com

Name : Yugi 
Age :  19 
Mobile_Number :  915476254 
Email_ID :  yugiyugi@gmail.com


Please check if the entered information is correct [type yes/no] :
yes

Do you want to enter information for another student [type yes/no] ?
yes

Please enter the information of student 2 in the given format only :


Name, Age, Mobile_Number, Email_ID :
Harry, 25, 988462496, harry@yahoo.com

Name : Harry 
Age :  25 
Mobile_Number :  988462496 
Email_ID :  harry@yahoo.com


Please check if the entered information is correct [type yes/no] :
no

Please enter the information of student 2 in the given format only :


Name, Age, Mobile_Number, Email_ID :
Harry, 25, 988462426, harry@yahoo.co.in

Name : Harry 
Age :  25 
Mobile_Number :  988462426 
Email_ID :  harry@yahoo.co.in


Please check if the entered information is correct [type yes/no] :
yes

Do you want to enter information for another student [type yes/no] ?
no

Thank You!

"""
