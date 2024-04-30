from bloodbankmngmt import*
from EroorHand import*


if(__name__=="__main__"):
    while True:
        print("\n============================================================ RRS BLOOD BANK ==================================================================")
        print("\n\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\t\t\t\t\t\t| 1.Admin Login. | 2.User Login. | 3.Exit |")
        print("\t\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n==============================================================================================================================================")
        choice=int(input("\t\t\t\t\tChoose a option :"))

        if choice ==1 :
            obj=BBMngt()
            obj.adminlogin()
        if choice ==1 :   
            while True:
                print("\t\t\t\t\t+----------------------------+")
                print("\t\t\t\t\t1.Display Blood details")
                print("\t\t\t\t\t2.Delete Blood after Expiry")
                print("\t\t\t\t\t3.Update.")
                print("\t\t\t\t\t4.Logout.")
                print("\t\t\t\t\t+----------------------------+")
                choice=int(input("Choose a option :"))

                if choice==1:
                 while True: 
                    print("----------------------------")
                    print("1.Display all details.")
                    print("2.Display Blood bag.")
                    print("3.Back.")
                    print("----------------------------")
                    choice=int(input("Choose a option :"))
                    print("----------------------------")
                    if choice==1:
                        obj=BBMngt()
                        obj.display1p()
                    elif choice==2:
                        #print("----------------------------")   
                        obj=BBMngt()
                        obj.display2p()
                        #print("----------------------------")
                    elif choice==3:   
                        break
                elif choice==2:
                    obj=BBMngt()
                    t=obj.date1()
                    obj.expiry(t)
                 
                elif choice==4:
                    break
        if choice ==2:
                print("\n\t\t\t\t\t\t===========================")
                print("\t\t\t\t\t\t1.Donor Login.")
                print("\t\t\t\t\t\t2.Receiver Login.")
                print("\t\t\t\t\t\t===========================")
                choice=int(input("\t\t\t\t\t\tChoose a option :"))

                if choice==1:
                    obj = BBMngt()
                    print("\n==========================================================================================================================================")
                    name=input("\n\tEnter Your Name : ")
                    age=int(input("\tEnter Your Age : "))
                    bloodgrp=input("\tEnter Your Bloodgroup : ")
                    contact=int(input("\tEnter Your Contact No : "))
                    print("\n==========================================================================================================================================")
                    date,expdate =obj.date()
                    quantity="200 ml"
                    b=bloodbank(name,age,bloodgrp,contact,date,expdate)
                    obj.donordet(b)
                    c=bloodbag(bloodgrp,date,expdate,quantity)
                    obj.addDonor(c)
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(f"\n\t\t\t\t\t\tThank you {name} for donating {bloodgrp} bloodgroup.!")
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
                elif choice==2:
                    obj=BBMngt()
                    print("\n==========================================================================================================================================")
                    bloodgrp=input("\tEnter which Bloodgroup do you want :")
                    print("\n==========================================================================================================================================")
                    obj.Request(bloodgrp)
                    obj.delete(bloodgrp) 
                    #print("\n==========================================================================================================================================")


        elif choice==3:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n\t\t\t\t\t\tThank You for visiting our Blood Bank.!")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break

        
    


