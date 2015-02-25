# -*- coding: UTF-8 -*-
#!/usr/local/bin/python
__author__ = 'guyanhua'

import MySQLdb
import Xlwt_use
import openpyxl
import code_select

wo  =  0
mm = ''
num = 4
print code_select.listbb
try:
    conn= MySQLdb.connect(
        host='192.168.1.48',
        port = 3306,
        user='root',
        passwd='1234',
        db ='vmdai_test',
        )
    cur=conn.cursor()
    for m in range (1,len(code_select.listbb)-num+1):
        if len(str(code_select.listbb[m])) == 1:
            mm = "00"+str(code_select.listbb[m])
        if len(str(code_select.listbb[m])) == 2:
            mm = "0"+str(code_select.listbb[m])
        if len(str(code_select.listbb[m])) == 3:
            mm = str(code_select.listbb[m])
        sql = "INSERT INTO `activity_code` (`user_id`, `loan_id`, `activity_id`, `money`, `code`, `ip`, `status`, `created_at`, `updated_at`, `code_type`) VALUES (7074, 1, 2, 0.0000, '"+mm+"', '58.247.114.162', 1, '2015-01-07 11:00:08', '2015-01-07 14:28:40', 1)"
        wo = wo+1
        cur.execute(sql)
    print "插入的条数 = ",wo
    #cur.execute(sql)
    #info = cur.fetchmany(aa)
    cur.close()
    conn.commit()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
