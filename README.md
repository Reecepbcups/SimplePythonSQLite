# SimplePythonSQLite
An easier way to use SQLite for Python applications

# Example:
```py
from Database_V2 import DBFunctions

# Creates contacts.db with the table name 'contacts'
contacts = DBFunctions('contacts.db', 'contact', 
    ['ContactID INT primary key', 
    'FirstName char(50)', 
    'LastName char(50)', 
    'PhoneNumber char(15)', 
    'EmailAddress char(50)']
)

contacts.newRecord(['1', 'Reece', 'Wilkerson', '111-222-3333', 'reece@email.com'])
contacts.newRecord(['2', 'Alice', 'LastAAAA', '111-222-4444', 'alice@email.edu'])
contacts.newRecord(['3', 'Bob', 'LastBBBB', '111-222-5555', 'bob@email.edu'])
contacts.newRecord(['4', 'Cathy', 'LastCCCC', '111-222-6666', 'cathy@email.edu'])
contacts.newRecord(['5', 'David', 'LastDDDD', '111-222-7777', 'david@email.edu'])

# Gets all First, Last, and Email addresses from records
customRecords = contacts.getCustomRecords(['FirstName', "LastName", "EmailAddress"])
for personRecord in customRecords:
  print(personRecord)
  
# Update record
contacts.changeRecordInfo('FirstName', 'Alice', 'EmailAddress', 'alice_changed@newscool.edu')

# Delete last record - is popped off
lastRecord = contacts.deleteLastRecord('ContactID'))
print(f"{lsatRecord} was deleted")
```
