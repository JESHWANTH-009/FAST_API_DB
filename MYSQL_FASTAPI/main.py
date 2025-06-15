"""import mysql.connector
c=mysql.connector.connect(
    host="localhost"   ,
    user="root",
    password="mysql",
    database="testdb"
)
cursor=c.cursor()
                                ##creating table

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100))")
cursor.execute("Insert into users(name,email) values (%s,%s)",("jeshwanth","jeshwanth@gamil.com"))
c.commit

cursor.execute("Select * from  users")

cursor.fetchall()
c.close() """

import mysql.connector
##Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="testdb"
)
cursor = conn.cursor()
## Insert Data
cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)",("JESHWANTH", "jeshwanth@gmai.com"))
conn.commit()
#Read Data
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

## Update Data
cursor.execute("UPDATE users SET name = %s WHERE email = %s",("jeshwanth", "jeshwanth@gmai.com"))
conn.commit()

##Delete Data
cursor.execute("DELETE FROM users WHERE email = %s",("jeshwanth@gmai.com",))  ## here , will select tuple of elelments if not it only selects string of elelmt
conn.commit()

cursor.execute("SELECT * FROM users")
for i in cursor.fetchall():

    print(i)
if  cursor.fetchall() is None:
    print("Empty table")

#closing connection 
conn.close()
