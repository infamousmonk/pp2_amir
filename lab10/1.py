import psycopg2
from psycopg2 import Error
import csv
print('1-Show')
print('2-Update')
print('3-Delete')
print('4-Insert')
option=int(input())
if option==1:
    try:
        connection=psycopg2.connect(user='postgres',password='postgres',host='localhost',port='5432',database='postgres')
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM phonebook')
        print(cursor.fetchall())
    except (Exception,Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
if option==2:
    print('Enter your name')
    name=input()
    print('Enter your phone number')
    number=input()
    try:
        connection=psycopg2.connect(user='postgres',password='postgres',host='localhost',port='5432',database='postgres')
        cursor=connection.cursor()
        cursor.execute('UPDATE phonebook set "number"=%s where "name"=%s',(number,name))
        connection.commit()
        print(cursor.fetchall())
    except (Exception,Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
if option==3:
    print('Whose number you want to delete?')
    name=input()
    try:
        connection=psycopg2.connect(user='postgres',password='postgres',host='localhost',port='5432',database='postgres')
        cursor=connection.cursor()
        cursor.execute('DELETE from phonebook where "n3ame"=%s',(name,))
        connection.commit()
        print(cursor.fetchall())
    except (Exception,Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
if option==4:
    print('1-From console','\r')
    print('2-From csv','\r')
    option2=int(input())
    if option2==1:
        print('Enter your name')
        name=input()
        print('Enter your phone number')
        number=input()
    else:
        print('Enter csv filename')
        csv_name=input()
        csv_name='C:\\Users\\apal0\OneDrive\Desktop\pp2\lab10\\'+csv_name+'.csv'
        names=[]
        numbers=[]
        with open(csv_name,'r',newline='') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                for i in range(0,len(row)):
                    if i==1:
                        numbers.append(row[i])
                    else:   
                        names.append(row[i])
            names.pop(0)
            numbers.pop(0)
    try:
        connection=psycopg2.connect(user='postgres',password='postgres',host='localhost',port='5432',database='postgres')
        cursor=connection.cursor()
        if option2==1:
            cursor.execute('INSERT INTO phonebook VALUES(%s,%s) returning name',(name,number))  # Add 'returning name' to get inserted name
            connection.commit()
        else:
            for i in range(len(names)):
                cursor.execute('INSERT INTO phonebook VALUES(%s,%s) returning name',(names[i],numbers[i]))  # Add 'returning name' to get inserted name
                connection.commit()
        record=cursor.fetchone()  # Fetch the result after the INSERT operation
        print(record)  # Print the result
    except (Exception,Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
