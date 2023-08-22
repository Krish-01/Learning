import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='MySQL123', database='bank')
cur = conn.cursor()
print('======================================WELCOME TO SQL BANK======================================')

import datetime as dt

print(dt.datetime.now())
print('1.REGISTER')
print('2.LOGIN')

n = int(input('Enter your choice: '))
print()

if n == 1:
    name = input('Enter a Username: ')
    passwd = int(input('Enter a 4 DIGIT Password: '))
    V_SQLInsert = f"INSERT  INTO user_table (passwrd,username) values('{str(passwd)}','{name}')"
    cur.execute(V_SQLInsert)
    conn.commit()
    print('USER Registered successfully')
    import menu

if n == 2:
    def login():
        name = input('Enter your Username:')
        passwd = int(input('Enter your 4 DIGIT Password: '))
        V_Sql_Sel = f"select * from user_table where passwrd='{str(passwd)}' and username= '{name}' "
        cur.execute(V_Sql_Sel)
        if cur.fetchone() is None:
            print('Invalid username or password')
            login()
        else:
            print("login success!!!")
            import menu
    login()
