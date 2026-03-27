import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db_host = os.getenv("HOST")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
    
connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database='schooldb')
cursor = connection.cursor()

# sql = "SELECT COUNT(*) FROM student" # COUNT kaç tane kayıt olduğunu saymak için yapılır.

# sql = "SELECT AVG(StudentNumber) FROM student" # İstediğimiz column'un ortalamasını alır

# sql = "SELECT SUM(Id) FROM student" # Seçtiğimiz column'u toplar

# sql = "SELECT MAX(studentnumber) FROM STUDENT" # Seçtiğimiz column'daki maximum değeri gösterir

# sql = "SELECT MIN(studentnumber) FROM student" # Seçtiğimiz column'daki minimum değeri gösterir

sql = "SELECT * FROM student WHERE StudentNumber= (SELECT MAX(studentnumber) FROM STUDENT)" # Burada mantık şu Her değerini istiyorum peki istediğim değer ne en büyük okul numaralı öğrenci
# koşul kelimem neydi where studentnumber= maksimu öğrenci numarasını veren sorgu. Bu şekilde düşüneceğiz

try:
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f'Record: {result[0]}')
except mysql.connector.Error as err:
        print('Bir hata oluştu')
finally:
    connection.close()
    print("Database connection koparildi")


