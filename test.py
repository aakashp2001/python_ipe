from datetime import datetime
from datetime import date
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="aakash", database="hospital"
)

cursor = mydb.cursor()
query = "SELECT * FROM `hospital`.`appointment` WHERE `patient_phone` = %s"
cursor.execute(query, [8401364728])
app = cursor.fetchall()

for i in app:
    print(i[3]>=date.today())