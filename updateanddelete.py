import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db_host = os.getenv("HOST")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
    
connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database='schooldb')
cursor = connection.cursor()

# sql = "UPDATE student SET name = 'Emre' WHERE Id=3"

sql = "DELETE FROM student WHERE Name LIKE '%Emre%'"


try:
    cursor.execute(sql)
    connection.commit() # Eğer databasede değişiklik olacaksa commit kullanmalıyız
    result = cursor.fetchall()
    print(f'{cursor.rowcount} tane kayit değişti')
except mysql.connector.Error as err:
        print('Bir hata oluştu')
finally:
    connection.close()
    print("Database connection koparildi")