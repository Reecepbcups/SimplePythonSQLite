#!/usr/bin/python3
"""
    This is a class which is used to easily create, maintain, remove records
    Simple, fast, and easy to use.

    a = Database('DBNAME.db', 'TableName', ['field1 text', 'field2 text'])
    a.newRecord(['reece', '18'])
    rec1 = a.getRecord('field1', 'reece')
    print(rec1) -> return tuple of info

    a.changeRecordInfo('field1', 'reece', 'field2', '19')
    a.deleteRecord('field1', 'reece')

"""

from os import path
import sqlite3

# Global Variables
DEBUGGING = 1
DEFAULT_ADMIN_PASSWORD = 'pa'
#DATABASE_NAME = 'Credentials.db' #":memory:" # if debuggin

def DEBUG(function, msg):
        print(f"[DBUG] {function}(): {msg}")

class DBFunctions:

    
    def __init__(self, DATABASE_NAME="", TableName="", Feilds=[]):
        '''
        + Initially creates an instance of the DB.

        * obj = DBFunctions('DBNAME.db', 'tablename', ['field1', 'field2'])
            - where fields are sets of data, such as 'usernames'

        ** if you define 3 fields for an object, you must suply 3 fields when
          adding new records.
            (If you need a different amount of fields, create a new DB instance)
        ''' 
        
        # Adds db file extention if not applied
        if '.' not in DATABASE_NAME[-3:]:
            if DEBUGGING: 
                DEBUG('__init__', 'Adding .db file extention due to now being found')
            DATABASE_NAME+='.db'

        # Set init variables and sql access cursor
        self.DATABASE_NAME = DATABASE_NAME
        self.TableName = TableName
        self.Feilds = Feilds
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.c = self.conn.cursor()

        # Checks for default Values and shows the correct syntax
        if self.TableName == "" or self.DATABASE_NAME == "":
            print("\n[!] Correct Syntax: ")
            print("obj = DBFunctions('DBNAME.db', 'TABLENAME', ['field1 text', 'field2 text')\n\n")
            exit()

        # Setup initial DB with table and collum fields
        fieldNamesFormated = ', '.join([f for f in self.Feilds]) # field type, field2 type
        self.c.execute(f"""CREATE TABLE IF NOT EXISTS {self.TableName} ({fieldNamesFormated})""")


    def newRecord(self, properties=[]):
        '''
        Creates a new record. In properties, place the data to match the collums for
        the initial DB setup. 
        ex. obj.newRecord('john', '19') if the fields are set as ['username text', 'age text']
        '''

        if properties == []:
            if DEBUGGING:
                #print('Fields: ' + str(self.Feilds))

                print(f"\n[!] No properties given. EX:")
                print("obj.newRecord(['FIELD1VALUE', 'FIELD2VALUE'])\n")
            return False

        properties = tuple([field for field in properties])

        if DEBUGGING: 
            DEBUG('newRecord', properties)

        fieldFormating = "(" + ("?," * len(properties))[:-1] + ')' # returns (?,?,?)

        with self.conn:
            self.c.execute(f"INSERT INTO {self.TableName} VALUES {fieldFormating}", properties)

        if DEBUGGING:
            DEBUG('newRecord', f'[+] Values {properties} added')

        return True


    def getRecord(self, field="" , _value="", numOfRecords=1, showDebug=True):
        '''Gets information from a collum of a record.

        ex. a.getRecord('usernameField', 'johnsmith')
        returns [('johnsmith', '20', 'OtherData')]

        If there is no record, returns None'''

        with self.conn:
            self.c.execute(f"SELECT * FROM {self.TableName} WHERE {field}=:val", {"val": _value})

        # Return 1 record, or all the records
        if numOfRecords==1:
                recordValues = self.c.fetchone()
        else: 
            recordValues = self.c.fetchall()

        if DEBUGGING and showDebug == True:
            DEBUG('getRecord', f'{recordValues}')

        return recordValues

 
    def deleteRecord(self, field="", _value=""):
        '''Removes a record based on 1 value (ex. a username)'''
        with self.conn:
            self.c.execute(f"DELETE FROM {self.TableName} WHERE {field}=:val", {'val': _value})

        if DEBUGGING:
            DEBUG('deleteRecord', f'[-] {_value.title()} record removed')

        return True


    def changeRecordInfo(self, searchFeild="",searchValue="", valueField="",newValue="" , reason=""):
        '''Change a records information.

        obj.changeRecordInfo('searchCollum', 'data', 'replaceCollum', 'newDataInformation')
        ex. ...cordInfo('users', 'john', 'age', '19')
        '''

        # could just do a for loop here, and go over a list of items if they provide.
        #with conn:
        #        c.execute(f"UPDATE {self.TableName} SET permission=? WHERE username=?", (_perm, _user))


        with self.conn: # Change the password for the user given their username
            self.c.execute(f"""UPDATE {self.TableName} SET 
                {valueField}=:new_val WHERE {searchFeild}=:defCharacteristic""", {'new_val': newValue, "defCharacteristic": searchValue})

        if DEBUGGING:
            DEBUG('changeRecordInfo', 
                f'[+] Updated value ({valueField}) {newValue}  for ({searchFeild}) {searchValue} record')
                


    def totalrecords(self):
        '''Returns records in the objects table'''
        with self.conn:
            self.c.execute(f"SELECT COUNT(*) FROM {self.TableName}")

        total = self.c.fetchall()[0][0]

        if DEBUGGING:
            DEBUG('totalrecords', f'[!] Number of records: {total}')

        return total


if __name__ == "__main__":
    # Initial DB with name, table name, and the feilds of the database
    one = DBFunctions('DB_FOR_TESTING.db', 'logins', ['username text', 'password text', 'date text', 'salt text'])

    # # Insert in a new record
    one.newRecord(['John','password', '12-20-19', '3'])

    #gets a record based on field name and the value you are looking for
    one.getRecord('username', 'John', '*')

    # remove a record
    #one.deleteRecord('username', 'John')

    # Get number of records in the DB
    one.totalrecords()

    # Changes the information for a record
    one.changeRecordInfo('password', 'newPassword', 'username', 'John')

    # Gets the record information and returns it as a tuple
    one.getRecord('username', 'John')

    


    pass