#!/usr/bin/python3

from Database import DBFunctions

# 'changeRecordInfo', 'deleteRecord', 'getRecord', 'newRecord', 'totalrecords'

#print(dir(DBFunctions))

a = DBFunctions('DB', 'info', ['username text', 'age text'])
a.newRecord(['reece', '18'])

b = DBFunctions('DB', 'info2', ['username text', 'date text', 'class text'])
b.newRecord(['john', '2020', 'biology'])

m = a.getRecord('username', 'reece')
n = b.getRecord('username', 'john')


#a.changeRecordInfo('username', 'reece', 'age', '19')

# a.deleteRecord('username', 'reece')