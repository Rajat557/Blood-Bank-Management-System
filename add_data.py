def Request1(self, bloodgrp, units):
            available_units = 0
            with open("Bloodbag.txt", "r") as fp:
                for ele in fp:
                    split_text = ele.split(",")
                    if split_text[1] == bloodgrp :
                     available_units+=int(split_text[4])

                    elif split_text[1] == bloodgrp:
                        print("\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
                        print(f"\t\t\t\t\t\t{bloodgrp} Blood group is available!")
                        print("\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
                        break
                    
                    else:
                        print("\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
                        print(f"\t\t\t\t\t{bloodgrp} Blood group is unavailable. Please visit later!")
                        print("\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
                        break
                
def delete1(self, bloodgrp, units):
        total_units_available = 0
        with open("Bloodbag.txt", "r") as fp:
            for ele in fp:
                split_text = ele.split(",")
                if split_text[1] == bloodgrp:
                    total_units_available += int(split_text[4])

        if total_units_available < units:
            print("\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
            print(f"\t\t\t\t\tOnly {total_units_available} units of {bloodgrp} blood are available.")
            print("\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
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

        print(f"\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
        print(f"\t\t\t\t\tSuccessfully deleted {units_deleted} unit(s) of {bloodgrp} blood.")
        print(f"\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")

""""def Request(self,bloodgrp):
            available=False
            with open("Bloodbag.txt","r") as fp:
                for ele in fp:
                    split_text=ele.split(",")
                    if split_text[1]==bloodgrp:
                        print("\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
                        print(f"\t\t\t\t\t\t{bloodgrp} Blood group is available.!")
                        print("\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
                        available=True
                        break

            if not available:
                        print("\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
                        print(f"\t\t\t\t\t\t {bloodgrp} Blood group is unavailable.Please visit later.!")
                        print("\t\t\t\t\t+-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-+")
                    
        def delete(self,bloodgrp):
            data=[]
            isfound=False
            with open("Bloodbag.txt","r") as fp:
                for ele in fp:
                    split_text=ele.split(",")
                    if split_text[1]==bloodgrp and not isfound:
                        isfound=True
                        
                    else:
                        data.append(ele)
        
            if isfound==True:
                with open ("Bloodbag.txt","w") as fp:
                    for x in data:
                        fp.write(x)
                    #print()    
            else:
            pass  #print("\t\t\t\t\t\tBlood group not found")"""          