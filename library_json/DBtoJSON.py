# DBtoJSON.py
# Author: Vasudev Ram - http://www.dancingbison.com
# Copyright 2014 Vasudev Ram
# DBtoJSON.py is a program to DEMOnstrate how to read 
# SQLite database data and convert it to JSON.

import sys
import sqlite3
import json

try:

    conn = sqlite3.connect('example.db')

    # This enables column access by name: row['column_name']
    conn.row_factory = sqlite3.Row

    curs = conn.cursor()

    # Create table.
    curs.execute('''DROP TABLE IF EXISTS stocks''')
    curs.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a few rows of data.
    curs.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.0)")
    curs.execute("INSERT INTO stocks VALUES ('2007-02-06','SELL','ORCL',200,25.1)")
    curs.execute("INSERT INTO stocks VALUES ('2008-03-06','HOLD','IBM',200,45.2)")

    # Commit the inserted rows.
    conn.commit()

    # Now fetch back the inserted data and write it to JSON.
    curs.execute("SELECT * FROM stocks")
    recs = curs.fetchall()

    print "DB data as a list with a dict per DB record:"
    rows = [ dict(rec) for rec in recs ]
    print rows

    print

    print "DB data as a single JSON string:"
    rows_json = json.dumps(rows)
    print rows_json

except Exception, e:
    print "ERROR: Caught exception: " + repr(e)
    raise e
    sys.exit(1)

# EOF