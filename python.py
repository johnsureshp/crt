python
import csv
f = open("student.csv","a",newline1="")
a=csv.write(f)
a.writerow(['student ID','rollno','name','mobile no'])
studentid = int(input("enter the student id  "))
rollno = int(input("enter the roll no "))
name = input("enter the name ")
mobile = int(input("enter the mobile number"))
a.writerow([studentid,rollno,name,mobile])
print("student record saved")

