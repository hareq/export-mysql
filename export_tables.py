__author__ = 'guyanhua'

import MySQLdb
import Xlwt_use
import openpyxl


try:
    conn= MySQLdb.connect(
        host='192.168.1.48',
        port = 3306,
        user='root',
        passwd='1234',
        db ='vmdai_test',
        )
    cur=conn.cursor()
    aa = cur.execute('show tables')
    info = cur.fetchmany(aa)
    row = 1
    for n in range(0,aa):
        Xlwt_use.table_structure(row,0,info[n],"a.xls")
        sql = 'show columns from '+ str(info[n])[2:len(str(info[n]))-3]
        bb = cur.execute(sql)
        infobb = cur.fetchmany(bb)
        row = row+1
        for m in range(0,bb):
            Xlwt_use.table_structure(row,1,infobb[m][0],"a.xls")
            Xlwt_use.table_structure(row,2,infobb[m][1],"a.xls")
            Xlwt_use.table_structure(row,3,infobb[m][2],"a.xls")
            Xlwt_use.table_structure(row,4,infobb[m][3],"a.xls")
            Xlwt_use.table_structure(row,5,infobb[m][4],"a.xls")
            Xlwt_use.table_structure(row,6,infobb[m][5],"a.xls")
            row = row+1
    cur.close()
    conn.commit()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
