# -*- coding: UTF-8 -*-
#!/usr/local/bin/python
__author__ = 'guyanhua'


import xlwt
file = xlwt.Workbook(encoding = 'ascii')
table = file.add_sheet('mysqltable',cell_overwrite_ok=True)

def table_structure(row,column,vlue,filename):
    vm_table = 0
    vm_nature = 1
    type = 2
    range = 3
    explain = 4
    default = 5
    extra = 6
    table.write(row,column,vlue)
    file.save(filename)