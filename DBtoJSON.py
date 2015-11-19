# DBtoJSON.py

import sys
import sqlite3
import json

f = open("json_data2", "w")

try:

    conn = sqlite3.connect('db.sqlite3')

    # This enables column access by name: row['column_name']
    conn.row_factory = sqlite3.Row

    curs = conn.cursor()


    # Now fetch back the inserted data and write it to JSON.
    curs.execute("SELECT * FROM library_Sound")
    recs = curs.fetchall()

	# convert to a dict
    rows = [ dict(rec) for rec in recs ]

    print "DB data as a single JSON string:"
    rows_json = json.dumps(rows)
    print rows_json

    #write the json_string out to a file
    f.write(rows_json)
    f.close()

except Exception, e:
    print "ERROR: Caught exception: " + repr(e)
    raise e
    sys.exit(1)

# EOF
