from sklearn import impute
import mysql.connector

connect_database = mysql.connector.connect(host = 'localhost',
                                           user = 'root',
                                           password = 'HelloWorld123',
                                           database = 'roadway_vehicles'
                                           )

cur = connect_database.cursor()  #Creating Cursor Object



#Add data to Database
def ADD_DETAILS():

    #inserting into rc_details table
    sql_command = "INSERT INTO rc_details(vehicle_number, owner_name, address, mobile_number, rc_registration_date, rc_expiry_date) VALUES (%s,%s,%s,%s,%s,%s)"

    print("ENTER OWNER DETAILS: ")
    vehicle_number = input("Enter Vehicle Number: ")
    owner_name = input("Enter Owner Name: ")
    address = input("Enter Address: ")
    mobile_number = input("Enter Mobile Number: ")
    rc_registration_date = input("Enter Registration Date (YYYY-MM-DD): ")
    rc_expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ")
    insert_in_values = (vehicle_number, owner_name, address, mobile_number, rc_registration_date, rc_expiry_date)

    cur.execute(sql_command, insert_in_values)

    connect_database.commit()

    print("ENTER CAR DETAILS: ")
    vehicle_manufacturer = input("Enter Vehicle Manufacturer: ")
    vehicle_type = input("Enter Vehicle Type: ")
    vehicle_model = input("Enter Vehicle Model: ")
    vehicle_colour = input("Enter Vehicle Colour: ")
    fuel_type = input("Enter Fuel Type: ")
    seat_capacity = int(input("Enter Seat Capacity: "))
    
    #inserting into car_details table
    sql_command = "INSERT INTO car_details(vehicle_number, vehicle_manufacturer, vehicle_type, model, colour, fuel_type, seat_capacity) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    insert_in_values = (vehicle_number ,vehicle_manufacturer, vehicle_type, vehicle_model, vehicle_colour, fuel_type, seat_capacity)
    
    cur.execute(sql_command, insert_in_values)
    connect_database.commit()

    print()
    print("Inserted Successfully in Database")


#Searching Details of RC
def SEARCH_RC(vehicle_number):

    sql_command = "SELECT * FROM rc_details WHERE vehicle_number = (%s)" 
    cur.execute(sql_command, (vehicle_number,))

    result = cur.fetchall()

    if(len(result) == 0):
        print()
        print("Vehicle Number: ", vehicle_number,"Not Found in Database !!!")
    else:
        print("*****************************************************")
        print()
        print()
        print("Vehicle Number: ",result[0][0])
        print()
        print("------------------------------------------------------")
        print("OWNER DETAILS: ")
        print("------------------------------------------------------")
        print()
        print("Owner Name:        ",result[0][1])
        print("Owner Address:     ",result[0][2])
        print("Mobile Number:     ",result[0][3])
        print("Registration Date: ", result[0][4])
        print("Expiry Date:       ",result[0][5])
        print()

        sql_command = "SELECT * FROM car_details WHERE vehicle_number = (%s)"
        cur.execute(sql_command, (vehicle_number,))
        result = cur.fetchall()

        print("------------------------------------------------------")
        print("CAR DETAILS: ")
        print("------------------------------------------------------")
        print()
        print("Vehicle Manufacturer: ",result[0][1])
        print("Vehicle Type:         ",result[0][2])
        print("Vehicle Model:        ",result[0][3])
        print("Vehicle Colour:       ", result[0][4])
        print("Fuel Type:            ",result[0][5])
        print("Seat Capacity:        ",result[0][6])
        print()
        print("*****************************************************")


    



