while True:

    print() #for next line
    print() #for next line

    print("1. Admin")
    print("2. Know RC details")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    #Admin Panel
    if(choice == 1):
        print("Admin")
        print()
        
        admin_password = input("Enter Password:  ")
        
        if(admin_password == "admin"):
            print("1. ADD RC DETAILS")
            print("2. Search")
            print("3. Exit")

            admin_choice = int(input("Enter Choice: "))

            if(admin_choice == 1):
                import admin
                admin.ADD_DETAILS()
            elif(admin_choice == 2):
                import admin
                vehicle_number = input("Enter Vehicle Number: ")
                admin.SEARCH_RC(vehicle_number)
            elif(admin_choice == 3):
                exit()
            else:
                print("Wrong Input")            
        

        else:
            print("Wrong Password")
    #end of Admin Panel



    #Image Capturing/Scanning to get vehicle number as stirng 
    elif(choice == 2):
        
        import extractTextFromImage   
        import admin   
        admin.SEARCH_RC(extractTextFromImage.outputText)

    #terminating the program
    elif(choice == 3):
        exit()

    else:
        print()
        print("Wrong Choice Entered")
        print()
        print()
