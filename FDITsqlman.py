import sqlite3
import tkinter.scrolledtext as tkst
from tkinter import * #For sticky=NSEW
import FDIT

#For use with FDIT
#Table Info: CREATE TABLE FDITtable(actionid INTEGER PRIMARY KEY ASC, action TEXT, fdate DATE, ftime TIME);
#Has to work with tuples at some points hence the (thing,)

database = 'FDIT.db'
table = 'FDITtable'

datatup = (database,)
tabletup = (table,)


conn = sqlite3.connect(database)
# create a Cursor object and call its execute() method to perform SQL commands:
cursor = conn.cursor()

def createDefaultFDITtable():
    print('Recreating Default FDIT Table')
    cursor.execute("CREATE TABLE FDITtable(actionid INTEGER PRIMARY KEY ASC, action TEXT, fdate DATE, ftime TIME);")

def deleteDefaultFDITtable():#Clear table
    print('Deleting Default FDIT Table')
    cursor.execute("DELETE FROM " + table)

def checkTableExist(): #Checks if Database exists and creates it with respective table if it doesn't.
    try:
        cursor.execute("SELECT * FROM " + table)
    except:
        print("Couldn't select from default table, attempting to recreate.")
        createDefaultFDITtable()

def getNumRows():
    numrows = 0
    for row in cursor.execute(("SELECT action, fdate, ftime FROM " + table)):
        numrows += 1
    return numrows

def selectAll():
    for row in cursor.execute(("SELECT * FROM " + table)):
        print(row)
        return row

def fetchAll():
    fetchcursor = conn.cursor()
    fetchcursor.execute(("SELECT * FROM " + table))
    rows = fetchcursor.fetchall()
    for row in rows:
        print(row)
        return row

def minselectAll():
    for row in cursor.execute(("SELECT action, fdate, ftime FROM " + table)):
        return row

def insertNewEntry(action):
    print('Creating new entry')
    print('Action = ' + action)
    ##cursor.execute("INSERT INTO " + table + " (fdate, ftime, action) VALUES(date('now'),time('now'),?)", (action,)) ##Previous with touple
    cursor.execute("INSERT INTO " + table + " (fdate, ftime, action) VALUES(date('now'),time('now'),?)", (action,))
    conn.commit() #Commit Changes to DB

def fetchRow(row): #Selects row with ID of Row
    fetchcursor = conn.cursor()
    fetchcursor.execute(("SELECT * FROM " + table + " WHERE actionid =" + str(row)))
    rows = fetchcursor.fetchall()
    for row in rows:
        print(row)
        return row

def updateTextFeed(TextFeed):#Update text feed
    #Clear text first:
    TextFeed.delete('1.0', END)
    #TextFeed = passed Tkinter Scrolled Text Widget
    # Fill Text Feed with SQL Selection
    for i in range(0, getNumRows()):  ##For number of SQL Entries
        TextFeed.insert('1.0', str(fetchRow(i+1)) + '\n')  ##Append row text to scroll display

def insertNewEntryUpdateFeed(action,feed): #Combines two above functions to only need to pass one argument to buttons command parameter.
    insertNewEntry(action)
    updateTextFeed(feed)

checkTableExist() #Called to see if table exist and then create it if not.