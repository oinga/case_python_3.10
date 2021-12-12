import mysql.connector
import config.database as database
import datetime

mydb = mysql.connector.connect(**database.oingadb)
cursor = mydb.cursor()


cursor.execute("""SELECT artist, title FROM music""")
results_data = cursor.fetchall()
for data in results_data:
        music_row = list(data)
        for elements in music_row:
            match elements:
                case 'Dru Hill':
                    print(music_row)
                case 'DMX':
                    print(music_row)    
   

