import random
import calendar
import time
import sqlite3 as sqlite
from flask import send_file
from config import *


class ProgrammingChallenge:

    switcher = {
        0: ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(10,20))),
        1: ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(random.randint(10,20))),
        2: random.randint(0,999999999),
        3: random.uniform(999999999.0,0.0)
    }

    def __init__(self):
        print("In Programming Challenge")

    def generate_report(self,request_filename):

        try:
            
            con = sqlite.connect(app.config['DATABASE'])
            cur = con.cursor()
            cur.execute("SELECT * FROM files where id=?",(request_filename,))
            row = cur.fetchone()
            cur.close()
                

            file_read = open(row[2], 'r')
            lines = file_read.readlines()
            for line in lines:
                split = line.replace(" ","").split(',')

                countAlpha = 0
                countAlphaNum =0
                countIsDigit = 0
                countIsFloat = 0
                for i in range(len(split)):
                    if (split[i].isalpha()):
                        countAlpha+=1
                    elif (split[i].isdigit()):
                        countIsDigit+=1
                    elif (split[i].isalnum()):
                        countAlphaNum+=1
                    else:
                        countIsFloat+=1

        except Exception as e:
            return {
            'message' : str(e),
            "code" : 400
            }

        return {
            "isalpha" : countAlpha,
            "isalphanum" : countAlphaNum,
            "isdigit" : countIsDigit,
            "isfloat" : countIsFloat
            }

    def generate_random_data(self):
        random_text = ''
        try:
            while len(random_text) < 2000000:
                random_text += (str(self.switcher.get(random.randint(0,3),"None")) + ',') 
            
            filename = str(calendar.timegm(time.gmtime()))
            path = app.config['storage'] + filename + '.txt' 

            write_file = open(path,'w')
            write_file.writelines(random_text)
            write_file.close()

            with sqlite.connect(app.config['DATABASE']) as conn:
                cur = conn.cursor()
                data = ("Generate data " + filename, path)
                cur.execute("INSERT INTO files (name,path) VALUES (?,?)",data)
                conn.commit()

        except Exception as e:
            conn.rollback()
            return {
            'message' : str(e),
            "code" : 400
            }

        finally:
            conn.close()         

        return {
            'message' : "Success",
            "code" : 200
            }

    def download_report(self,request_filename):
        try:
            conn = sqlite.connect(app.config['DATABASE'])
            cur = conn.cursor()
            cur.execute("SELECT * FROM files where id=?",(request_filename,))
            row = cur.fetchone()
            request_filename = row[2]
        except:
            return jsonify({
                'message' : "Error",
                "code" : 400
            })
        finally:
            conn.close()         
            
        return send_file(request_filename, as_attachment=True)

    

        
