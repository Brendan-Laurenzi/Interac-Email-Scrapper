from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb



class Database:

    def __init__(self):
        self.host = "aws.connect.psdb.cloud"
        self.user = "q7y37kvrmfqc9bqode5v"
        self.password = "pscale_pw_lewwzQrpbT6U6aCm325nvRgY8h0abT4e6vrS9h58NRg"
        self.datebase = "emt_database"
        self.autocommit = True
        self.ssl_mode = "VERIFY_IDENTITY"
        self.ssl = {"ca": "C:\\Users\\brend\\Desktop\\Coding Stuff\\Interac-Email-Scrapper\\cacert.pem"}
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = MySQLdb.connect(
            host = self.host,
            user = self.user,
            passwd =  self.password,
            db = self.datebase,
            autocommit = True,
            ssl_mode = self.ssl_mode,
            ssl = self.ssl
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_update(self, query, params=None):
        self.cursor.execute(query, params) if params else self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount

    def fetch_all(self, table_name):
        query = f"SELECT * FROM {table_name} ORDER BY date DESC"
        return self.execute_query(query)
    
    def fetch_all_confirmed(self, table_name):
        query = f"SELECT * FROM {table_name} WHERE confirmed = FALSE ORDER BY date DESC"
        return self.execute_query(query)
    
    def fetch_all_from_value(self, table_name, value):
        query = f"SELECT * FROM {table_name} WHERE INSTR(name, '{value}') > 0 OR INSTR(amt, '{value}') > 0 OR INSTR(memo, '{value}') > 0 OR INSTR(date, '{value}') > 0 OR INSTR(refID, '{value}') > 0  ORDER BY date DESC"
        return self.execute_query(query)

    def insert_record(self, table_name, columns, values):
        query = f"INSERT IGNORE INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in values])})"
        return self.execute_update(query, values)
    
    def update_column_bool(self, table_name, column_name, new_value, condition):
        query = f"UPDATE {table_name} SET {column_name} = %s WHERE {condition}"
        return self.execute_update(query, (int(new_value),))

    def update_record(self, table_name, update_values, condition):
        set_clause = ', '.join([f"{column} = %s" for column in update_values.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        return self.execute_update(query, list(update_values.values()))

    def delete_record(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        return self.execute_update(query)

    def wipe(self):
        try:
            self.cursor.execute("DROP TABLE received_emts")
            self.cursor.execute("CREATE TABLE received_emts (name VARCHAR(99), amt VARCHAR(99), memo VARCHAR(500), date DATETIME, refID VARCHAR(99) PRIMARY KEY, confirmed BOOLEAN DEFAULT FALSE)") 
            
        except MySQLdb.Error as e:
            print("MySQL Error:", e)
        
        
if __name__ == "__main__":
    db = Database()
    db.connect()
    db.wipe()
    #mostRecentEntry = db.execute_query("SELECT * FROM received_emts ORDER BY date DESC LIMIT 1")
    #entry = ('PHILIP ZYLKA', '23.00', 'N/A', '2023-4-26 5:8:41', 'C1A5c3F9CkCn')
    #db.insert_record("received_emts", ['name', 'amt', 'memo', 'date', 'refID'], entry)
    #print(mostRecentEntry[0][4])

    db.disconnect()
