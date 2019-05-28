#select fetch one on database mysql from localhost

import mysql.connector
server='localhost'
db='' 
usernaname='' 
password=''
port=8889

conn = mysql.connector.connect(host=server,database=db,user=username,password=password,port=port)

def query_with_fetchone():
    try:
       
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pc_punchdump")
 
        row = cursor.fetchone()
 
        while row is not None:
            print(row)
            row = cursor.fetchone()
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    query_with_fetchone()
