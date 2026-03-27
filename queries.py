import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db_host = os.getenv("HOST")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
    
connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database='schooldb')
cursor = connection.cursor()

#sql = "SELECT * FROM student" # Örneğin biz sadece name ve surname olan kısmı istiyorsak tüm column'ları getirmek mantıksızdır.
# Boşa database'ye yük biner

#sql = "SELECT Name, Surname FROM student" # Bu şekilde sadece istediğimiz column'ları yazdırmış oluruz

# sql = "SELECT * FROM student WHERE Name='İbrahim Emre' and Gender = 'Kadın' "

#sql = "SELECT * FROM student WHERE Name LIKE '%Kenan%'" # bu Name column'u içerisinde herhangi bir yerde Kenan geçen kayıtları getirir başında ve sonundaki % işareti kelimenin öncesinde veya sonrasında bir şey olabileceğini belirtir

sql = "SELECT * FROM student ORDER BY Id DESC" # ORDER BY bir sıralama işlemidir seçtiğimiz column'a göre sıralar DESC eklersek sondan başa doğru ASC eklersen baştan sona doğru sıralar
# 2 tane column seçersek de örneğin name ve number seçtim önce nameye göre sıralar aynı isimleri de number'a göre sıralar





cursor.execute(sql)
try:
    dataShow = cursor.fetchall() # Tüm verileri liste olarak getirir eğer çok büyük bir dataset ise fetchmany() 
    #eğer sadece ilk kayıtı getirmek istersek fetchone() kullanılır
except mysql.connector.Error as err:
    print("Bir hata oluştu")

finally:
    connection.close()
    

print("\nRECORDINGS \n")
for data in dataShow:
    
    print(f' ID: {data[0]}  Student Number: {data[1]}  Name: {data[2]}  Surname: {data[3]}  Birthdate: {data[4]}  Gender: {data[5]}')
print("\nConnection Lost")

# print(dataShow)





