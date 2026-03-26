import os
from dotenv import load_dotenv
import mysql.connector

# executemany kullanmamızın sebebi her seferinde connection yapmaya gerek yok en son tek seferde birden çok kaydı gönderebiliriz
load_dotenv()
def insertStudents(liste):

    db_host = os.getenv("HOST")
    db_user = os.getenv("USER")
    db_password = os.getenv("PASSWORD")
    
    connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database='schooldb')
    cursor = connection.cursor()

    sql = "INSERT INTO student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES(%s, %s, %s, %s, %s)"
    values = liste

    

    try:
        cursor.executemany(sql, values)
        connection.commit() # Burada database'ye işlemi yollamak için kullanılır diyebiliriz.
        print(f'{cursor.rowcount} tane satir eklendi.') #rowcount kaç satır eklendiğini söyleyecek
        print(f'Son eklenen kaydin id numarasi {cursor.lastrowid} dir.') # lastrowid son eklenen kaydın id numarasını söyler
    except mysql.connector.Error as err:
        print('Bir hata oluştu')
    finally:
        connection.close()
        print("Database connection koparildi")


should_continue = True
liste = []
while True:
    studentNumber = int(input("Öğrenci numarasi: "))
    name = input("Name: ")
    surname = input("Surname: ")
    birthdate = input("Doğum tarihi(YYYY-MM-DD): ")
    gender = input("Gender(Erkek/Kadin): ")
    liste.append((studentNumber, name, surname, birthdate, gender))
    


    while True:
        try:
            result = input("Devam etmek istiyor musunuz? (e/h): ")
    
            if result == "e":
                print("Devam ediliyor.")
                break
                
            elif result == "h":
                should_continue = False
                break
            else:
                print("Lütfen belirtilen harflerden birini giriniz.")
        except ValueError:
            print("Lütfen belirtilen harflerden birini giriniz.")
    if should_continue == False:
        insertStudents(liste)
        print("Kayitlariniz gonderiliyor")
        print(liste)
        break
    

    





