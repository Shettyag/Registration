# Registration

# sample Registration table.

CREATE TABLE Registration (
                              ID INT PRIMARY KEY AUTO_INCREMENT,
                              Name VARCHAR(100) NOT NULL,
                              Email VARCHAR(100) UNIQUE NOT NULL,
                              DateOfBirth DATE NOT NULL,
                              Gender VARCHAR(100) NOT NULL,
                              PhoneNo VARCHAR(100),
                              Address VARCHAR(100),
                              City VARCHAR(100),
                              State VARCHAR(100),
                              Country VARCHAR(100),
                              ZipCode VARCHAR(100)
                           )

#  To run registration.py code 

1. Install the sqlite3 module if it is not already installed. we can install it using:
   pip install pysqlite3
2. Create a new file named registration.py and paste that code into it.
3. run the script using python interpreter
   python registration.py
4. The script will create a new SQLite database file named registration.db and a table named Register in it.

#  implementation of CRUD operations:

1. # Create a record
      db.create_record("rakesh", "rakesh23@example.com", "2000-12-03","Male","097711789","342 st","Hyderabad","Andra","India","451234")
       - this function insert a new record into the database.
   
2. # Read a record
    record = db.read_record(120)
    print("record:", record)
    - this function retrieves the record from the database with the ID of 120 and prints the content of the record.
   
3. # Update a record
    db.update_record(120, "harshan", "harshan@example.com", "2001-05-16","Male","123457799","021 st","Mysore","Karnataka","India","675421")
    
    updated_record = db.read_record(120)
    print("Updated record:", updated_record)
    -  This function is assumed to locate the record with the given ID of 120 and update its fields with the new values.
   
4.  # Delete a record
    db.delete_record(117)
    - This function deletes the record from the database with the ID of 117.
