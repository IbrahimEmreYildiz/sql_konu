import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


h = os.getenv("HOST")
u = os.getenv("USER")
p = os.getenv("PASSWORD")

mydb=mysql.connector.connect(
    host = h, #192.30.25.45 Normalde bunu bir yerden service hizmeti olarak satın almamız lazım. Onlar tarafından IP adresi verilecektir.
    user = u ,# Kullanıcı adı
    password = p # Server'a giriş şifrem
)

print(mydb)