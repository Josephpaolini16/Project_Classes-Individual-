
from Facilities import facilities 
from Labs import labs   


#  Display the categories, you can choose and access any of these categories by calling their respective classes and methods
class Management:

    def DisplayMenu(self):
        while True:
            menu_input = input("Welcome to Alberta Hospital (AH) Management system\n"
                         "Select from the following options, or select 0 to stop:\n"
                         "1 - 	Facilities\n"
                         "2 - 	Laboratories\n")
                         
            
# Class named "Facility" will be call on this condition
            if menu_input == "1":
                while True:
                    fac = facilities("pat")
                    fac_input = input("Facilities Menu: \n"
                                "1 - Display Facilities list\n"
                                "2 - Add Facility\n"
                                "3 - Back to Main Menu\n>")
                    if fac_input == "1":
                        fac.displayFacilities()
                        print("\nBack to the previous Menu\n")
                    elif fac_input == "2":
                        fac.addFacility()
                        fac.writeListOffacilitiesToFile()
                        print("\nBack to the previous Menu\n")
                    else:
                        Management().DisplayMenu()
#  Class named "Lab" will be call on this condition
            elif menu_input == "2":
                while True:
                    lab = labs(1, 1)
                    lab_input = input("Laboratories Menu\n"
                                "1 - Display laboratories list\n"
                                "2 - Add laboratory\n"
                                "3 - Back to the Main Menu\n>")
                    if lab_input == "1":
                        lab.readLabFile()
                        lab.displayLabs()
                        print("\nBack to the previous Menu\n")
                    elif lab_input == "2":
                        lab.enterLabInfo()
                        lab.formatLabInfo()
                        lab.addLabToFile()
                        print("\nBack to the previous Menu\n")
                    else:
                        Management().DisplayMenu()
            elif menu_input == "0":
                exit()


Management().DisplayMenu()