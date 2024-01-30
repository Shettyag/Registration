import sqlite3

class RegistrationDB:
    def __init__(self, db_name='registration.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Register (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                Name TEXT NOT NULL,
                                Email TEXT UNIQUE NOT NULL,
                                DateOfBirth DATE NOT NULL,
                                Gender TEXT NOT NULL,
                                PhoneNo TEXT,
                                Address TEXT,
                                City TEXT,
                                State TEXT,
                                Country TEXT,
                                ZipCode TEXT
                                
                            )''')
        self.conn.commit()

    def create_record(self, name, email, dob, gender, phoneno, address, city, state, country, zipcode):
        try:
            self.cursor.execute('''INSERT INTO Register (Name, Email, DateOfBirth, Gender, PhoneNo, Address, City, State, Country, ZipCode)
                                VALUES (?, ?, ?, ? ,?, ?, ?, ? ,?, ?)''', (name, email, dob, gender,phoneno, address, city, state, country, zipcode))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error creating record:", e)
            return False

    def read_record(self, id=None):
        try:
            if id is None:
                self.cursor.execute('''SELECT * FROM Register''')
            else:
                self.cursor.execute('''SELECT * FROM Register WHERE ID = ?''', (id,))
                record = self.cursor.fetchone()
                return record
            record = self.cursor.fetchone()
            return record
        except sqlite3.Error as e:
            print("Error reading records:", e)
            return None

    def update_record(self, id, name, email, dob, gender, phoneno, address, city, state, country, zipcode):
        try:
            self.cursor.execute('''UPDATE Register
                                SET Name = ?, Email = ?, DateOfBirth = ?, Gender = ?, PhoneNo = ?, Address = ?, City = ?, State = ?, Country = ?, ZipCode = ?
                                WHERE ID = ?''', (name, email, dob, gender, phoneno, address, city, state, country, zipcode, id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error updating record:", e)
            return False

    def delete_record(self, id=None):
        try:
            if id is None:
                self.cursor.execute('''DELETE FROM Register''')
            else:
                self.cursor.execute('''DELETE FROM Register WHERE ID = ?''', (id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error deleting record:", e)
            return False

    def close_connection(self):
        self.conn.close()

# Example
if __name__ == "__main__":
    db = RegistrationDB()
  
    # Create a record
    db.create_record("rakesh", "rakesh23@example.com", "2000-12-03","Male","097711789","342 st","Hyderabad","Andra","India","451234")

    # Read a record
    record = db.read_record(120)
    print("record:", record)


    # Update a record
    db.update_record(120, "harshan", "harshan@example.com", "2001-05-16","Male","123457799","021 st","Mysore","Karnataka","India","675421")
    
    updated_record = db.read_record(120)
    print("Updated record:", updated_record)

    # Delete a record
    db.delete_record(117)    
    
    db.close_connection()

