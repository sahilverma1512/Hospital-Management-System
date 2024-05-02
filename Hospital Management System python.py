from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector    #Can raise a problem 

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")  #add +0+0 to end of 800
        root.config(bg='grey')

        label_title=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg='red',bg='cyan', font='comicsansms 24 bold')
        label_title.pack(side=TOP,fill=X,ipady=10)
    

        #string variable made for functioning of button
         
        self.nameoftablet=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.no_of_tablets=StringVar()
        self.Issue_Date=StringVar()
        self.Expiry_Date=StringVar()

        # self.patientid=StringVar()

#=---------------------------------------CREATING A MENUBAR-==================================================
        

    
    
    
    
    # first frame
     
        data_frame=Frame(self.root,bd=20,relief=RIDGE)
        data_frame.place(x=0,y=95,width=1535,height=400)

        data_frame_left=LabelFrame(data_frame,bd=10,relief=RIDGE,font='comicsans 18 bold',text='Patient Information')
        data_frame_left.place(x=0,y=5,width=950,height=350)

        data_frame_right=LabelFrame(data_frame,bd=10,relief=RIDGE,font='comicsans 18 bold',text='Prescription Data')
        data_frame_right.place(x=960,y=5,width=530,height=350)

    #Button Frames
        button_frame=Frame(root,bd=10, relief=RIDGE)
        button_frame.place(y=485,height=120,width=1530)

    #details frame
        details_frame=Frame(root,bd=10, relief=RIDGE)
        details_frame.place(y=560,height=225,width=1530)



    # ----------------------------------------------------DAta frame of left side----------------------------------------------------------
        
        
        label_name_tablet=Label(data_frame_left,text='Patient Name :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
        label_name_tablet.grid(row=1, column=0)
        patient_name_entry=Entry(data_frame_left,font="arial 12", width=30,textvariable=self.no_of_tablets)
        patient_name_entry.grid(row=1,column=1)

        # Dropdown list of tablets-----------------------------------
        
        # combo_name_tablet=ttk.Combobox(data_frame_left,textvariable=self.nameoftablet , font= ('arial', 12),width=30)
        # combo_name_tablet["values"]=('Corona Vaccine','Artheritis Medicine','Dolo','Combiflame','Paracetamol','ETHER ','HIV PROTEASE INHIBITORS','CHEMOTHERAPY DRUGS','THORAZINE','POLIO VACCINE')
        # combo_name_tablet.grid(row=1,column=1)

        # REFERENCE NUMber # pateint id

        reference_number=Label(data_frame_left,text='Patient Id :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
        reference_number.grid(row=2, column=0)
        reference_number_entry=Entry(data_frame_left,font="arial 12", width=30,textvariable=self.ref)
        reference_number_entry.grid(row=2,column=1)

       # Daily DOse  # AGe
        
        label_dose=Label(data_frame_left,text=' Age :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
        label_dose.grid(row=3, column=0)
        label_dose_entry=Entry(data_frame_left,font='arial 12',width=30,textvariable=self.Dose)
        label_dose_entry.grid(row=3,column=1)

        # No of tablet  #name of tablet

        label_no_of_tablet=Label(data_frame_left,text='Name of tablet :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
        label_no_of_tablet.grid(row=4, column=0)
        # label_no_of_entry=Entry(data_frame_left,font='arial 12',width=30,textvariable=self.no_of_tablets)
        # label_no_of_entry.grid(row=4,column=1)

        combo_name_tablet=ttk.Combobox(data_frame_left,textvariable=self.nameoftablet , font= ('arial', 12),width=28)
        combo_name_tablet["values"]=('Corona Vaccine','Artheritis Medicine','Dolo','Combiflame','Paracetamol','ETHER ','HIV PROTEASE INHIBITORS','CHEMOTHERAPY DRUGS','THORAZINE','POLIO VACCINE')
        combo_name_tablet.grid(row=4,column=1)



        #Issue date # blood pressure

        label_issue_date=Label(data_frame_left,text='Blood Pressure :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
        label_issue_date.grid(row=5, column=0)
        label_issue_date_entry=Entry(data_frame_left,font='arial 12',width=30,textvariable=self.Issue_Date)
        label_issue_date_entry.grid(row=5,column=1)

        #Expiry date  # appointment date

        label_expiry_date=Label(data_frame_left,text='Appointment Date :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
        label_expiry_date.grid(row=6, column=0)
        label_expiry_date_entry=Entry(data_frame_left,font='arial 12',width=30,textvariable=self.Expiry_Date)
        label_expiry_date_entry.grid(row=6,column=1)

        # Patient Id
        
        # label_patient_id=Label(data_frame_left,text='Patient Id :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
        # label_patient_id.grid(row=7, column=0)
        # label_patient_id_entry=Entry(data_frame_left,font='arial 12',width=30)   #textvariable=self.patientid
        # label_patient_id_entry.grid(row=7,column=1)



        #-----------------------------------------==========-SAME COPIED !! WILL CHANGE IT LATER++++++++++_______________________+++++-------------


        # REFERENCE NUMber

    #     reference_number=Label(data_frame_left,text='Reference No :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
    #     reference_number.grid(row=2, column=4)
    #     reference_number_entry=Entry(data_frame_left,font="arial 12", width=30)
    #     reference_number_entry.grid(row=2,column=5)

    #    # Daily DOse 
        
    #     label_dose=Label(data_frame_left,text='Daily Dose :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
    #     label_dose.grid(row=3, column=4)
    #     label_dose_entry=Entry(data_frame_left,font='arial 12',width=30)
    #     label_dose_entry.grid(row=3,column=5)

    #     # No of tablet

    #     label_no_of_tablet=Label(data_frame_left,text='No. of tablets :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
    #     label_no_of_tablet.grid(row=4, column=4)
    #     label_no_of_entry=Entry(data_frame_left,font='arial 12',width=30)
    #     label_no_of_entry.grid(row=4,column=5)

    #     #Issue date

    #     label_issue_date=Label(data_frame_left,text='Issue Date :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
    #     label_issue_date.grid(row=5, column=4)
    #     label_issue_date_entry=Entry(data_frame_left,font='arial 12',width=30)
    #     label_issue_date_entry.grid(row=5,column=5)

    #     #Expiry date

    #     label_expiry_date=Label(data_frame_left,text='Expiry Date :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
    #     label_expiry_date.grid(row=6, column=4)
    #     label_expiry_date_entry=Entry(data_frame_left,font='arial 12',width=30)
    #     label_expiry_date_entry.grid(row=6,column=5)

    #     # Patient Id
        
    #     label_patient_id=Label(data_frame_left,text='Patient Id :- ', font= ('times new roman', 15,'bold') , padx=2,pady=6)
    #     label_patient_id.grid(row=7, column=4)
    #     label_patient_id_entry=Entry(data_frame_left,font='arial 12',width=30)
    #     label_patient_id_entry.grid(row=7,column=5) 

#====================================-===============================================================================================================================
#====================================================================================================================================================================
        

        #----------------------------DATA frame of right side---------------------------------------------

        self.text_prescription=Text(data_frame_right,font='arial 12',width=53,height=15,pady=2) 
        self.text_prescription.place(y=10,x=13)


        # ---------------------------BUTTONS__________________________________________

        button_prescription=Button(button_frame,text='Save',font='arial 15 bold',width=12,padx=10,bg='yellow',fg='black',bd=3,command=self.iprescription_data)
        button_prescription.place(x=80,y=10)
        # button_prescription.grid(row=0,column=4)



        button_data=Button(button_frame,text='Update',font='arial 15 bold',width=12,padx=10,bg='yellow',fg='black',bd=3,command=self.update_data)
        button_data.place(x=360,y=10)
        # button_data.grid(row=0,column=8)



        button_update=Button(button_frame,text='Delete',font='arial 15 bold',width=12,padx=10,bg='yellow',fg='black',bd=3,command=self.delete_data)
        button_update.place(x=650,y=10)
        # button_update.grid(row=0,column=12)




        button_Reset=Button(button_frame,text='Print',font='arial 15 bold',width=12,padx=10,bg='yellow',fg='black',bd=3,command=self.iprint_prescription)
        button_Reset.place(x=950,y=10)
        # button_Reset.grid(row=0,column=16)



        button_Delete=Button(button_frame,text='Reset',font='arial 15 bold',width=12,padx=10,bg='yellow',fg='black',bd=3,command=self.reset_data)
        button_Delete.place(x=1250,y=10)
        # button_Delete.grid(row=0,column=40)
        


# -------------------------------details frame -last frame_____________________________________________________________
        
        #Scroll bAr

        scroll_bar_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_bar_y=ttk.Scrollbar(details_frame,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(details_frame,column=("nameoftablet",'ref','Dose','no_of_tablets','Issue_Date','Expiry_Date'),xscrollcommand=scroll_bar_x.set,yscrollcommand=scroll_bar_y.set)
        scroll_bar_x.pack(side=BOTTOM,fill=X)
        scroll_bar_y.pack(side=RIGHT,fill=Y)

        scroll_bar_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_bar_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet",text='Patient Name')
        self.hospital_table.heading("ref",text='Patient Id')
        self.hospital_table.heading("Dose",text='Age')
        self.hospital_table.heading("no_of_tablets",text='Name of Tablet')
        self.hospital_table.heading("Issue_Date",text='Blood Pressure')
        self.hospital_table.heading("Expiry_Date",text='Appointment Date')
        

        # self.hospital_table.column("Name of tablet",text='name of tablets')
        # self.hospital_table.heading("Name of tablet",text='name of tablets')
        # self.hospital_table.heading("Name of tablet",text='name of tablets')
        # self.hospital_table.heading("Name of tablet",text='name of tablets')
        # self.hospital_table.heading("Name of tablet",text='name of tablets')


        self.hospital_table['show']='headings'
        self.hospital_table.pack(fill=BOTH,expand=True)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

        # By this feature you can change the width of the table content on details frame-------------------



        # self.hospital_table.column("Name of tablet",width=15)    



# FUnctinality of the project____________________________________________________________________________________
        
    def iprescription_data(self):
        if self.nameoftablet.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required") 
        else:
            conn=mysql.connector.connect( host="127.0.0.1",port='3306',username="root",password="123456",database="hmsData")
            my_cursor=conn.cursor()     #data entry in sql hospital is my table name
            my_cursor.execute("insert into hmsMainTable values(%s,%s,%s,%s,%s,%s)"   , (
                                                                                    self.no_of_tablets.get(),
                                                                                    self.ref.get(),
                                                                                    self.Dose.get(),
                                                                                    self.nameoftablet.get(),
                                                                                    self.Issue_Date.get(),
                                                                                    self.Expiry_Date.get()      
                                                                                    ))   
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Succes","Record has been inserted.")
#   ==============Used to reset the data=================================================
            self.reset_data()


# Data not storing in database!!!!!!!!!!!!!!!!! have to add a function to click on button to add data to database


# Update not working properly--===================================================
            
    def update_data(self):
        conn=mysql.connector.connect( host="127.0.0.1",port='3306',username="root",password="123456",database="hmsData")
        my_cursor=conn.cursor()     
        my_cursor.execute("update hmsMainTable set nameoftablet=%s,Dose=%s,no_of_tablets=%s,Issue_Date=%s,Expiry_Date=%s where ref=%s",(
                                                                                                                                self.no_of_tablets.get(),
                                                                                                                                self.Dose.get(),
                                                                                                                                self.nameoftablet.get(),
                                                                                                                                self.Issue_Date.get(),
                                                                                                                                self.Expiry_Date.get(),
                                                                                                                                self.ref.get(), ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Record has been updated successfully.")

    # ===================================================fetch_data=========================================

    def fetch_data(self):
        conn=mysql.connector.connect( host="127.0.0.1",port='3306',username="root",password="123456",database="hmsData")
        my_cursor=conn.cursor()     #data entry in sql hospital is my table name
        my_cursor.execute("select * from hmsMainTable")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


# ========================================================
    def get_cursor(self,event):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.no_of_tablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.nameoftablet.set(row[3])
        self.Issue_Date.set(row[4])
        self.Expiry_Date.set(row[5])



    def iprint_prescription(self):
        if self.nameoftablet.get()=="" or self.ref.get()=="" or self.Dose.get()=="" or self.no_of_tablets.get()=="" or self.Issue_Date.get()=="" or self.Expiry_Date.get()=="":
            messagebox.showwarning("Data Short","Data you have entered is short.")
        else:
            self.text_prescription.insert(END,"     Patient Name :            " + self.no_of_tablets.get()+"\n\n")
            self.text_prescription.insert(END,"     Patient Id :              " + self.ref.get()+"\n\n")
            self.text_prescription.insert(END,"     Age :                     " + self.Dose.get()+"\n\n")
            self.text_prescription.insert(END,"     Name of Tablet :          " + self.nameoftablet.get()+"\n\n")
            self.text_prescription.insert(END,"     Blood Pressure :          " + self.Issue_Date.get()+"\n\n")
            self.text_prescription.insert(END,"     Appointment Date :        " + self.Expiry_Date.get()+"\n\n")
            messagebox.showinfo("Printed","Information is printed in prescription page.")

    
    def delete_data(self):
        conn=mysql.connector.connect( host="127.0.0.1",port='3306',username="root",password="123456",database="hmsData")
        my_cursor=conn.cursor()     
        
        # another method to add sql query

        query="delete from hmsMainTable where ref=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()

        messagebox.showinfo("Deleted","Data has been deleted.")        

    def reset_data(self):
        self.no_of_tablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.nameoftablet.set("")
        self.Issue_Date.set("")
        self.Expiry_Date.set("")


    # -------------------------------------------exit button--------------------------------------------------
        

    # def exit_button(self):
    #     exit= messagebox.askyesno("Hospital Management System","Do you really want to exit ?")
    #     if exit==1:
    #         root.destroy()
    #         return





root=Tk()
# menubar=Menu(root)
# filemenu=Menu(menubar)
# filemenu.add_command(label="Save",command="")
# filemenu.add_separator()
# filemenu.add_command(label="exit",command=root.destroy)
# menubar.add_cascade(label="File",menu=filemenu)
# root.config(menu=menubar)
obj=Hospital(root)
root.mainloop()
