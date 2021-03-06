import sqlite3

# db가 없으면 생성후 접속
# 있으면 접속
#
def createTable():
    try:
        sql = 'create table student(name varchar(20), age int, birth date)'
        db = sqlite3.connect('my.db')
        db.execute(sql)
        db.close()
        print('create success')
    except Exception as err:
        print(err)

# insert, update, delete : 명열을 확정(commit), rollback
def insertTable():
    try:
        # sql = "insert into student(name, age, birth) values('홍길동',20,'1990-10-11')"
        # sql = "insert into student values('홍길동',20,'1990-10-11')"
        sql = "insert into student values(?,?,?)"
        db = sqlite3.connect('my.db')
        data = ('이순신',30,'1980-01-03')
        db.execute(sql, data)
        db.commit()
        db.close()
        print('insert success')
    except Exception as err:
        print(err)

def insertBulk():
    try:
        sql = "insert into student values(?,?,?)"
        db = sqlite3.connect('my.db')
        data = [('김철수1',40,'1970-01-03'),
                ('김철수2',50,'1960-01-03'),
                ('김철수3',60,'1950-01-03')]
        db.executemany(sql, data)
        db.commit()
        db.close()
        print('insert success')
    except Exception as err:
        print(err)

def updateTable():
    try:
        sql = "update student set name='김철수4', age=22 where name='김철수1'"
        db = sqlite3.connect('my.db')
        db.execute(sql)
        db.commit()
        db.close()
        print('update success')
    except Exception as err:
        print(err)

def deleteTable():
    try:
        sql = "delete from student where name='김철수3'"
        db = sqlite3.connect('my.db')
        db.execute(sql)
        db.commit()
        db.close()
        print('delete success')
    except Exception as err:
        print(err)

def selectTable1():
    try:
        sql = "select * from student"
        db = sqlite3.connect('my.db')
        cur = db.cursor() # db관리메모리영역에 접근
        cur.execute(sql)
        dt = cur.fetchall()
        print(dt)
        for n,a,b in dt:
            print(n,a,b)
        db.close()
        print('select success')
    except Exception as err:
        print(err)

def selectTable():
    try:
        sql = "select * from student"
        db = sqlite3.connect('my.db')
        cur = db.cursor() # db관리메모리영역에 접근
        cur.execute(sql)
        for c in cur:
            print(c)
        db.close()
        print('select success')
    except Exception as err:
        print(err)


selectTable()
