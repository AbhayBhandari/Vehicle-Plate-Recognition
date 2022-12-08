CREATE DATABASE roadway_vehicles;
USE roadway_vehicles;

CREATE TABLE rc_details(
	vehicle_number varchar(10) PRIMARY KEY,
    owner_name varchar(32) NOT NULL,
    address varchar(100) NOT NULL,
    mobile_number varchar(10) NOT NULL,
    rc_registration_date date NOT NULL,
    rc_expiry_date date NOT NULL
    );
    
CREATE TABLE car_details(
	vehicle_number varchar(10) PRIMARY KEY,
    vehicle_manufacturer varchar(20)  NOT NULL,
    vehicle_type varchar(20) NOT NULL,
    model varchar(10) NOT NULL,
    colour varchar(10) NOT NULL,
    fuel_type varchar(10) NOT NULL,
    seat_capacity INT NOT NULL,
    FOREIGN KEY(vehicle_number) REFERENCES rc_details(vehicle_number) ON DELETE CASCADE
    );
    
    
    
    
    
    
    