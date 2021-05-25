import pymysql

def getConnection():
    connect = pymysql.connect(
        host = "den1.mysql4.gear.host",
        user ="auto9",
        password ="$Elmasmejor0910",
        database = "auto9"
    )
    return connect

def create_user_table():
    connect = getConnection()
    create_users = "CREATE TABLE IF NOT EXISTS users (id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100))"
    db_cursor = connect.cursor()
    db_cursor.execute(create_users)
    db_cursor.execute("show tables")
    db_cursor.close()
    connect.close()

def delete_user_table():
    connect = getConnection()
    db_cursor = connect.cursor()
    delete_users = "DROP TABLE USERS"
    db_cursor.execute(delete_users)
    db_cursor.close()
    connect.close()

def create_user(name, email):
    connect = getConnection()
    db_cursor = connect.cursor()
    create_user = "INSERT INTO users (name, email) VALUES ('{}', '{}')".format(name, email)
    db_cursor.execute(create_user)
    connect.commit()
    db_cursor.close()
    connect.close()


create_user("peter", "peter@keyzen.cl")