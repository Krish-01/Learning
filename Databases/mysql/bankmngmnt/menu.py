# create database bank

import datetime as dt
import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='MySQL123', database='bank')
cur = conn.cursor()

conn.autocommit = True  # https://dev.mysql.com/doc/refman/5.6/en/innodb-autocommit-commit-rollback.html
"""Auto-commit mode means that when a statement is completed, the method commit is called on that statement 
automatically. """

c = 'N'
while c == 'N':
    print('Menu Items:', end='\n')
    print('1.CREATE BANK ACCOUNT')
    print('2.PERFORM TRANSACTION')
    print('3.CUSTOMER DETAILS')
    print('4.TRANSACTION DETAILS')
    print('5.DELETE ACCOUNT')
    print('6.QUIT')

    n = int(input('Enter your CHOICE: '))
    print()

    if n == 1:
        acc_no = int(input('Enter your ACCOUNT NUMBER: '))
        acc_name = input('Enter your ACCOUNT NAME:')
        ph_no = int(input('Enter your PHONE NUMBER:'))
        add = (input('Enter your place: '))
        cr_amt = int(input('Enter your credit amount: '))
        V_SQLInsert = f"INSERT  INTO customer_details values ('{str(acc_no)}','{acc_name}','{str(ph_no)}','{add}','{str(cr_amt)}') "
        cur.execute(V_SQLInsert)
        print()
        print('Account Created Successfully!!!!!')
        conn.commit()
        break

    if n == 2:
        acct_no = int(input('Enter Your Account Number: '))
        cur.execute(f'select * from customer_details where acct_no={str(acct_no)}')
        data = cur.fetchall()
        count = cur.rowcount
        conn.commit()
        if count == 0:
            print('Account Number Invalid Sorry Try Again Later')
        else:
            print()
            print('1.WITHDRAW AMOUNT')
            print('2.ADD AMOUNT')

            x = int(input('Enter your CHOICE: '))
            print()
            if x == 1:
                wd_amt = int(input('Enter withdrawal amount: '))
                amt_added = 0  # here we are not crediting anything so we need to enter 0 in transaction table as cr_amt
                cur.execute(f'update customer_details set amt=amt-{wd_amt} where acct_no={str(acct_no)}')
                V_SQLInsert = "INSERT  INTO transactions values ({} , '{}' , '{}' , {} , {}) ".format(acct_no,
                                                                                                      dt.datetime.today(),
                                                                                                      dt.datetime.now(),
                                                                                                      wd_amt, amt_added)
                cur.execute(V_SQLInsert)
                conn.commit()
                print('Account Updated Successfully!!!!!')
                break

            if x == 2:
                add_amt = int(input('Enter amount to be added:'))
                amt = 0
                cur.execute(f'update customer_details set amt=amt+{str(add_amt)} where acct_no={str(acct_no)}')
                V_SQLInsert = "INSERT  INTO transactions values ({} , '{}' , '{}' , {} , {})".format(acct_no,
                                                                                                     dt.datetime.today(),
                                                                                                     dt.datetime.now(),
                                                                                                     amt, add_amt)
                cur.execute(V_SQLInsert)
                conn.commit()
                print()
                print('Account Updated Succesfully!!!!!')
                break
    if n == 3:
        acct_no = int(input('Enter your account number:'))
        print()
        cur.execute('select * from customer_details where acct_no=' + str(acct_no))
        if cur.fetchone() is None:
            print()
            print('Invalid Account number')
        else:
            cur.execute('select * from customer_details where acct_no=' + str(acct_no))
            data = cur.fetchall()
            for row in data:
                print('ACCOUNT NO:', acct_no)
                print('ACCOUNT NAME:', row[1])
                print('PHONE NUMBER:', row[2])
                print('ADDRESS:', row[3])
                print('amt: ', row[4])
        break

    if n == 4:
        acct_no = int(input('Enter your account number: '))
        print()
        cur.execute('select * from transactions where acct_no=' + str(acct_no))
        if cur.fetchone() is None:
            print()
            print('Invalid Account number')
        else:
            cur.execute('select * from transactions where acct_no=' + str(acct_no))
            data = cur.fetchall()
            for row in data:
                print('ACCOUNT NO:', acct_no)
                print('DATE:', row[1])
                print('TIME:', row[2])
                print('WITHDRAWAL AMOUNT:', row[3])
                print('AMOUNT ADDED:', row[4])

    if n == 5:
        print('DELETE YOUR ACCOUNT')
        acct_no = int(input('Enter your account number: '))
        cur.execute('select * from customer_details where acct_no=' + str(acct_no))
        if cur.fetchone() is None:
            print('Invalid Account number')
        else:
            cur.execute('delete from customer_details where acct_no=' + str(acct_no))
            print('ACCOUNT DELETED SUCCESSFULLY, OOPS we are sorry, hope you will get '
                  'back soon, we will miss you')

    if n == 6:
        print('DO YO WANT TO EXIT(Y/N)')
        c = input('Enter your choice:')

else:
    print('THANK YOU PLEASE VISIT US AGAIN')
    quit()

"""fetchall() fetches all the rows of a query result. An empty list is returned if there is no record to fetch the 
cursor.fetchone() method returns one row or a single record at a time. It will return None if no more rows / records 
are available. """
