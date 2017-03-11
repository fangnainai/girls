# -*- coding:utf-8 -*-
import MySQLdb
import sys

import time

reload(sys)
sys.setdefaultencoding('utf8')

class DBMan:
    def db_query(self,sql):
        conn = MySQLdb.connect(host='localhost', user='root', passwd='shiWOlp123', port=3306, db='girls', charset='utf8')
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def db_modify(self,sql):
        conn = MySQLdb.connect(host='localhost', user='root', passwd='shiWOlp123', port=3306, db='girls', charset='utf8')
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()



