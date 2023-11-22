from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb

def connect_to_db():
    connection = MySQLdb.connect(
    host = "aws.connect.psdb.cloud",
    user = "q7y37kvrmfqc9bqode5v",
    passwd =  "pscale_pw_lewwzQrpbT6U6aCm325nvRgY8h0abT4e6vrS9h58NRg",
    db = "emt_database",
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY",
    ssl = {
        "ca": "C:\\Users\\brend\\Desktop\\Coding Stuff\\Interac-Email-Scrapper\\cacert.pem"
        }
    )
    return connection

class Database:

    def wipe():
        connection = connect_to_db()
        try:
            cursor = connection.cursor()
            cursor.execute("DROP TABLE received_emts")
            cursor.execute("CREATE TABLE received_emts (name VARCHAR(99), amt VARCHAR(99), memo VARCHAR(500), date DATETIME, refID VARCHAR(99) PRIMARY KEY)") 
            
        except MySQLdb.Error as e:
            print("MySQL Error:", e)

        finally:
            cursor.close()
            connection.close()


    def get_all_emt_data():
        connection = connect_to_db()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM received_emts")

            emt_data = []
            for x in cursor:
                emt_data.append(list(x))

        except MySQLdb.Error as e:
            print("MySQL Error:", e)

        finally:
            cursor.close()
            connection.close()
            return emt_data
        
    
    def insert_data_list(data_list):
        connection = connect_to_db()
        try:
            cursor = connection.cursor()

            add_emt = ("INSERT IGNORE INTO received_emts(name, amt, memo, date, refID) VALUES (%(name)s, %(amt)s, %(memo)s, %(date)s, %(refID)s)")
            for data in data_list:
                formated_data = {
                    'name': data[0],
                    'amt': data[1],
                    'memo': data[2],
                    'date': data[3],
                    'refID': data[4],
                }
                print(data)
                cursor.execute(add_emt, formated_data)

            connection.commit()

        except MySQLdb.Error as e:
            print("MySQL Error:", e)

        finally:
            cursor.close()
            connection.close()
        
if __name__ == "__main__":
    Database.wipe()
