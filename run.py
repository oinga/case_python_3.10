import mysql.connector
import config.database as database
import datetime

mydb = mysql.connector.connect(**database.oingadb)
cursor = mydb.cursor()


cursor.execute("""SELECT artist, title FROM music""")
results_data = cursor.fetchall()
for data in results_data:
    for elements in data:
        match elements:
            case 'Dru Hill':
                print("Artist: " + data[0] + " | " + " Song: " + data[1]) 
            case 'DMX':
                print("Artist: " + data[0] + " | " + " Song: " + data[1]) 
            case 'Boyz II Men':
                print("Artist: " + data[0] + " | " + " Song: " + data[1])       
   

