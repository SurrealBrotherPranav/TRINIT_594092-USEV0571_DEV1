import csv
import requests
import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
UI=tk.Tk()

'''
mydb=mysql.connector.connect(
    host='localhost',                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    user='root',
    password='Password'
)

mycursor=mydb.cursor()
mycursor.execute("DROP database IF EXISTS ngodonation;")
mycursor.execute("create ngodonation;")
mycursor.execute("use donations;")
mycursor.execute("DROP TABLE IF EXISTS donations;")
mycursor.execute('CREATE TABLE donations(DonorName VARCHAR(255),NGOName VARCHAR(255),Donation INTEGER(10),DonationMethod VARCHAR(50),Phone INTEGER(10);')
sqlFormula="INSERT INTO donations (DonorName,NGOName,Donation,DonationMethod,Phone) VALUES (%s,%s,%s,%s,%s);"
'''

def Book():
    Data=(DonorName_in.get(),NGOName_in.get(),Donation_in.get(),Method_in.get(),Phone_in.get())
    if '' in Data:
        Error['text']='Blank Field / Fields'
    else:
        with open("C:\\Users\\Pranav\\Downloads\\ngos_log.csv", 'r') as csv_f:
            r = csv.reader(csv_f)
            details = [i for i in r]
            NGOName1 = [i[0] for i in details[1:]]
            Mission = [i[1] for i in details[1:]]
            History = [i[2] for i in details[1:]]
            Impact = [i[3] for i in details[1:]]
            TotalF = [i[4] for i in details[1:]]
            Fund = [i[5] for i in details[1:]]
            
        #converting from tkinter object into int and str
        DonorName = str(DonorName_in.get())
        NGOName= str(NGOName_in.get())
        Donation=int(Donation_in.get())
        Method= str(Method_in.get())
        Phone = str(Phone_in.get())
        
        s=1;
        while s==1:
            #Details
            i = NGOName1.index(NGOName.lower())
            #appoinment=(DonorName,NGOName,Donation,Method,Phone)
            #mycursor.execute(sqlFormula,appoinment)
            #mydb.commit()
            url = "https://www.fast2sms.com/dev/bulk"
            phno = Phone[i]
            text = str(DonorName) + ", you have a donated a sum of " + str(Donation) +" to NGO " + str(NGOName)
            payload = f"sender_id=FSTSMS&message={text}&language=english&route=p&numbers={phno}"#connecting to website
            headers = {
            'authorization': "T1p5dPJaqxvA4syU0cRkwNHY8uSgnFEW923XfbQrItMlZGzDe7r4ahQFKAn9P5RXbMTIcykLUdzfC8oD", #special API key to send message via fast sms
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            print("Dear",DonorName,", \nMESSAGE SUCCESFULLY SENT!")
            Error['text']='Booked'
            print("Thank you for using this portal to make your donation. GOD BLESS YOU!")
            with open("C:\\Users\\Pranav\\Downloads\\ngos_log.csv", 'r') as csv_f:
                r = csv.reader(csv_f , delimiter=',')
                r=list(r)
            for i in range(1,len(r)):
                if r[i][0]==NGOName:
                    r[i][4]=str(int(r[i][4])+Donation)
                    r[i][5]=str(Donation)
                    break
            with open("C:\\Users\\Pranav\\Downloads\\temp.csv", mode = 'w', newline='') as csv_f:
                csvwriter = csv.writer(csv_f, delimiter=',',quotechar="") 
                csvwriter.writerows(r)
            print(r[0][0]+" "+r[0][1]+" "+r[0][2]+" "+r[0][3]+" "+r[0][4]+" "+r[0][5])
            for i in range(1,len(r)):
                if r[i][0]==NGOName:
                    print(r[i][0]+" "+r[i][1]+" "+r[i][2]+" "+r[i][3]+" "+r[i][4]+" "+r[i][5])
                    break
            s=2;
        UI.destroy()
#labels for boxes

s=input("Do you have any Login ID Password ? (Enter y for yes and n for no)")
'''if(s.lower()=='n'):
if(s.lower()=='y'):
'''
Header=tk.Label(text='AVAILABLE OPTIONS FOR NGOS : \nA\nB\nC\nD\nFill your data in the following fields')
DonorName_label = tk.Label(text="Enter your name : "); DonorName_in = tk.Entry(UI)
NGOName_label=tk.Label(text="Enter your preffered NGO name : ");NGOName_in=tk.Entry(UI)
Donation_label=tk.Label(text="Enter your preffered donation amount : ");Donation_in=tk.Entry(UI)
Method_label=tk.Label(text="Enter your donation method : ");Method_in=tk.Entry(UI)
Phone_label=tk.Label(text="Enter your phone number : ");Phone_in=tk.Entry(UI)
Book_Button=tk.Button(UI,text='Book Donation',command=Book)
Error=tk.Label(UI)

Header.pack()
DonorName_label.pack();DonorName_in.pack()
NGOName_label.pack();NGOName_in.pack()
Donation_label.pack();Donation_in.pack()
Method_label.pack();Method_in.pack()
Phone_label.pack();Phone_in.pack()
Book_Button.pack();Error.pack()
tk.mainloop()
