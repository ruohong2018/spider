# -*- coding: utf-8 -*-
import MySQLdb

def get_task_from_mysql():
    conn = MySQLdb.connect(
            host = '127.0.0.1',
            port = 3306,
            db = 'linkedin',
            user = 'root',
            passwd = 'bupt123456',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
            )
    cur = conn.cursor()
    print "test point 24"
    collect = []
    try:
        cur.execute("select url, task_type from searchinfo where task_status = 0 limit 1")
        collect = cur.fetchone()
        cur.execute("update searchinfo set task_status = 1 where task_status = 0 limit 1")
        conn.commit()
        print "test point 24.1"
    except:
        conn.rollback()
        print "test point 24.2"
    print "test point 25"
    print collect
    cur.close()
    conn.close()
    return collect
