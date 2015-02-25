# -*- coding: UTF-8 -*-
#!/usr/local/bin/python
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
        db ='vmdai_online',
        )
    cur=conn.cursor()
    aa = cur.execute('select code from activity_code where status != 2')
    info = cur.fetchmany(aa)
    print '已使用的总获奖码个数',aa
    listaa = []
    listbb = []
    listcc = []
    for n in range(0,aa):
        #print int(str(info[n])[2:5])
        listaa.append(int(str(info[n])[2:5]))
    print '已使用的获奖码 = ',listaa
    for n in range(1,1000):
        if listaa.count(n)!=1 and listaa.count(n)!=0:
            listcc.append(n)
    print "重复获奖码个数",len(listcc)
    print '重复获奖码 = ',listcc
    for n in range(1,1000):
        if n in listaa:
            1 == 1
        else:
            listbb.append(n)
    print "没使用的获奖码个数",len(listbb)
    print "没使用的获奖码 = ",listbb
    cur.close()
    conn.commit()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
