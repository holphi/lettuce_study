import sqlite3

from os.path import abspath
from module import Student

def getDbConn():
    conn = None
    try:
        connStr = './features/Student.db'
        conn = sqlite3.connect(connStr)
        return conn
    except Exception, ex:
        raise ex

def clearStudentInfo():
    conn = None
    try:
        conn = getDbConn()
        conn.execute('DELETE FROM Student')
        conn.commit()
    except Exception, ex:
        raise ex
    finally:
        if conn is not None:
            conn.close()

def getStudentCount():
    conn = None
    count = -9999
    try:
        conn = getDbConn()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM Student')
        row = cur.fetchone()
        count = int(row[0])
    except Exception, ex:
        raise ex
    finally:
        if conn is not None:
            conn.close()
        return count

def insertStudent(stu):
    if isStudentExist(stu.id):
        return
    conn = None
    sql_statement = 'INSERT INTO Student VALUES(?,?,?,?,?)'
    try:
        conn = getDbConn()
        print conn
        conn.execute(sql_statement, (stu.id, stu.name, stu.gender, stu.year_of_birth, stu.city))
        conn.commit()
    except Exception, ex:
        raise ex
    finally:
        if conn is not None:
            conn.close()

def isStudentExist(id):
    if len(getStudentInfo('id', id))==1:
        return True
    else:
        return False

def getStudentInfo(by, value):
    conn = None
    sql_statement = 'SELECT * FROM Student WHERE %s=?' % by
    result = []
    try:
        conn = getDbConn()
        t = (value, )
        cur = conn.cursor()
        cur.execute(sql_statement, t)
        row = cur.fetchone()
        while row is not None:
            stu = Student(row[0], row[1], row[2], row[3], row[4])
            result.append(stu)
            row = cur.fetchone()
        else:
            return result
    except Exception, ex:
        raise ex
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    stu = Student('20120202', 'Alex', 'Male', 1983, 'Beijing')
    insertStudent(stu)
    print isStudentExist('20120202')