import cv2
import mysql.connector as con
import time
mydb=con.connect(host="localhost", user='root', passwd='Iotistic6382',database='mydatabase') #establishing the connection between sql and python
mycursor=mydb.cursor(buffered=True)
#mycursor.execute('CREATE DATABASE mydatabase') #creating the database which will store the execution time
start=time.time()
img = cv2.imread(r"C:\Users\Layan\Downloads\yandy316012.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

hsvimg=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('image',hsvimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
end=time.time()
totalTime=end-start
#mycursor.execute("CREATE TABLE execTime (time DOUBLE(24,5))") #create a table within the mydatabase
mycursor.execute("INSERT INTO execTime (time) VALUES (%s)",[totalTime]) #insert the execution time into the table
mydb.commit()#save changes to database
mycursor.execute("SELECT * FROM execTime") #to display all entries in the table
for x in mycursor:
    print(x)