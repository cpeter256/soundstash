from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import sqlite3

try:
    db_file = 'db.sqlite3'
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), db_file)
    conn = sqlite3.connect(db_path)

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


except Exception, e:
    print "ERROR: Caught exception: " + repr(e)
    raise e
    sys.exit(1)

# EOF


#filename = 'json_data'
#file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
#json_file = open(file_path, 'r')
#json_data = json_file.read()

#data = json.loads(json_data)

def libraryView(request):
	return HttpResponse(rows_json, content_type='application/json')

# Create your views here.
