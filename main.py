import mysql.connector
c=mysql.connector.connect(
    host="localhost"   ,
    user="root",
    password="mysql",
    database="testdb"
)
cursor=c.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100))")
cursor.execute("Insert into users(name,email) values (%s,%s)",("jeshwanth","jeshwanth@gamil.com"))
c.commit

cursor.execute("Select * from  users")

cursor.fetchall()
c.close() 
