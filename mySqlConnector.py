import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


h = os.getenv("HOST")
u = os.getenv("USER")
p = os.getenv("PASSWORD")

mydb=mysql.connector.connect(
    host = h , #192.30.25.45 Normalde bunu bir yerden service hizmeti olarak satın almamız lazım. Onlar tarafından IP adresi verilecektir.
    user = u ,# Kullanıcı adı
    password = p ,# Server'a giriş şifrem
    database ="mydatabase" #Hangi database ile çalışacaksak onu yazabiliriz eğer birden fazla varsa
)

mycursor = mydb.cursor() #mycursor objesi oluşturduk komut verebilmek için mysql'e çünkü mydb ile bağladık

mycursor.execute("SHOW DATABASES") # Databaseleri gösterme
for x in mycursor:
    print(x)



mycursor.execute("CREATE DATABASE mydatabase") # Database oluşturma 

print(mydb)

# Genel olarak Script kullanmaya gerek yok IDE üzerinden rahatça yapabiliriz
