from BloodBank import *
from datetime import datetime,timedelta
from prettytable import PrettyTable

class BBMngt:
    def addDonor(self,c):
        fp=open("Bloodbag.txt","a")
        fp.write(str(c))
        fp.close()

    def donordet(self,b):
        fp=open("Data.txt","a")
        fp.write(str(b))
        fp.close()

    def quantity(self):
        blood_group_quantities = {}
        # Read from Bloodbag.txt to calculate quantities
        with open("Bloodbag.txt", "r") as fp:
            for line in fp:
                _,blood_group, _, _, quantity = line.strip().split(",")
                quantity = int(quantity)
                # Update the total quantity for the blood group
                if blood_group in blood_group_quantities:
                    blood_group_quantities[blood_group] += quantity
                else:
                    blood_group_quantities[blood_group] = quantity
        # Write the blood group quantities to a file
        with open("BloodGroupQuantities.txt", "w") as fp:
            for blood_group, total_quantity in blood_group_quantities.items():
                fp.write(f"{blood_group}, {total_quantity}\n")
                
                 
    def displayq(self):
        with open("BloodGroupQuantities.txt", "r") as fp:
            for ele in fp:
                print(ele)            

    def display(self):
        with open("Bloodbag.txt","r") as fp:
            for ele in fp:
                print(ele)

    def display2(self):
        with open("Data.txt","r") as fp:
            for ele in fp:
                print(ele)    

    def display1p(self): 
        with open("Data.txt","r") as rp:
            table=PrettyTable(["id","name","age","bloodgrp","contact","date","expdate","unit"])  
            for bl in rp:
                row=bl.strip().split(",")
                if len(row)==8:
                    table.add_row(row)      
                else:
                    pass      
            print(table)   

    def display2p(self):
        with open("Bloodbag.txt","r") as rp:
            table=PrettyTable(["Id","bloodgrp","date","expdate","unit"])  
            for bl in rp:
                row=bl.strip().split(",")
                if len(row)==5:
                    table.add_row(row)      
                else:
                    pass      
            print(table)   

    def displayqp(self): #value must come in table format from Data.txt file
        with open("BloodGroupQuantities.txt","r") as rp:
            table=PrettyTable(["bloodgrp","Quantities(units)"])  
            for bl in rp:
                row=bl.strip().split(",")
                if len(row)==2:
                    table.add_row(row)      
                else:
                    pass      
            print(table)  

    def date(self):
        cdt = datetime.now()
        currentdate = cdt.date()
        expiry_date = currentdate + timedelta(days=+1)
        return currentdate,expiry_date   
    
    def date1(self):
        cd=datetime.now()
        tod=cd.date()
        return tod         
   
                              
    def expiry(self,d):
        data=[]
        isfound=False
        with open("Bloodbag.txt","r") as fp:
            for ele in fp:
                split_text=ele.split(",")  
                if split_text[3] <=str(d):
                    isfound=True
                    pass
                else:
                    data.append(ele)
        if isfound==True:
            with open("Bloodbag.txt","w") as fp:
                for x in data:
                    fp.write(x)
            print("\n\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")    
            print("\t\t\t\tExpired Blood removed from Repository.!")  
            print("\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")   
        else:
            print("\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+") 
            print("\t\t\t\tNo expired Blood group found")          
            print("\n\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+") 

    def adminlogin(self):
        while True:
            print("\n\t+~~~~~~~~~~~ Admin Login ~~~~~~~~~~~+")
            username=input("\n\tEnter Username: ")
            if username== 'r':
                password=int(input("\tEnter Password:"))
                print("\n\t+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")    
                if password==1:
                    print("\n\t+---------------------------+")
                    print("\tLogin Successful.!")  
                    print("\t+---------------------------+") 
                    break
                else:
                    print("\t-----------------------------") 
                    print("\tPlease Enter Correct Password")
                    print("\-----------------------------") 
            else:
                print("\t-----------------------------") 
                print("\tPlease Enter Correct Username:")                 
                print("\t-----------------------------")                   

    def updateun(self, id):
        data = []
        data1 = []
        isfound = False
        ch = input("\tDo you want to change Bloodgroup(y/n) :")
        if ch == 'y':
            nm = input("\tEnter new Bloodgroup to update : ")
            print("\t--------------------------------------------------------")
        if nm in ["A","B","AB","O"]:    
            with open("Data.txt", "r") as fp:
                with open("Bloodbag.txt", "r") as dp:

                    for ele in fp:
                        splitted_text = ele.split(',')
                        if splitted_text[0] == str(id):
                            isfound = True
                            splitted_text[3] = nm
                            ele = ",".join(splitted_text)
                            # add updated string to container
                            data.append(ele)
                        else:
                            data.append(ele)

                    for ele in dp:
                        splitted_text = ele.split(',')
                        if splitted_text[0] == str(id):
                            isfound = True
                            splitted_text[1] = nm
                            ele = ",".join(splitted_text)
                            data1.append(ele)
                        else:
                            data1.append(ele)

                if isfound:
                    with open("Data.txt", "w") as fp:
                        for x in data:
                            fp.write(x)
                    with open("Bloodbag.txt", "w") as dp:
                        for x in data1:
                            dp.write(x)
                    if ch == 'y' :
                        print("\t--------------------------------------------------------")
                        print(f"\t{nm} Blood group has been updated successfully!")
                        print("\t--------------------------------------------------------")     


                else:
                    pass#print("Record not found")
        else:
            print("\tEnter Valid bloodgroup")        

    def manage_blood_bag(self, bloodgrp, units=None):
        blood_group_found = False
        available_units = 0

        with open("Bloodbag.txt", "r") as fp:
            for ele in fp:
                split_text = ele.split(",")
                if split_text[1] == bloodgrp:
                    blood_group_found = True
                    available_units += int(split_text[4])

        if not blood_group_found:
            print("\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
            print(f"\t\t\t\t\t{bloodgrp} Blood group is unavailable. Please visit later!")
            print("\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
            return

        if units is not None:
            if available_units < units:
                print("\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
                print(f"\t\t\t\t\tOnly {available_units} units of {bloodgrp} blood are available.")
                print("\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
                return

            data = []
            units_deleted = 0

            with open("Bloodbag.txt", "r") as fp:
                for ele in fp:
                    split_text = ele.split(",")
                    if split_text[1] == bloodgrp and units_deleted < units:
                        units_deleted += int(split_text[4])
                    else:
                        data.append(ele)

            with open("Bloodbag.txt", "w") as fp:
                for x in data:
                    fp.write(x)

            print(f"\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
            print(f"\t\t\t\t\tSuccessfully donated {units_deleted} unit(s) of {bloodgrp} bloodgroup.")
            print(f"\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
        else:
            print("\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
            print(f"\t\t\t\t\t{bloodgrp} Blood group is available with {available_units} units.")
            print("\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")




