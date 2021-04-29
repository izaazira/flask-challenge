import sqlite3 as sqlite
import sys, getopt
from config import *

def generate_db():
    conn = sqlite.connect(app.config['DATABASE'])
    print("Opened database successfully")
    conn.execute("DROP TABLE IF EXISTS files;")
    conn.execute("CREATE TABLE files (id INTEGER PRIMARY KEY, name TEXT, path TEXT)")
    print("Table created successfully")
    conn.close()

def list_db():
    con = sqlite.connect(app.config['DATABASE'])
    con.row_factory = sqlite.Row
    cur = con.cursor()
    cur.execute("select * from files")
    rows = cur.fetchall(); 
    for row in rows:
        print(str(row["id"]) + ' -- ' +row["name"] + ' -- ' + row["path"])

def main(argv):
    full_cmd_arguments = sys.argv
    argument_list = full_cmd_arguments[1:]
    short_options = "hdl"
    long_options = ["help", "deploy", "list"]
    try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
    except getopt.error as err:
        # Output error, and return with an error code
        print (str(err))
        sys.exit(2)

    for current_argument, current_value in arguments:
        if current_argument in ("-h", "--help"):
            print('database.py -d --deploy | -v --view')
            sys.exit()
        elif current_argument in ("-d", "--deploy"):
            generate_db()
        elif current_argument in ("-l", "--list"):
            list_db()

if __name__ == "__main__":
    main(sys.argv[1:])