import csv
import sqlite3

class storage(object):
    def cd1(self):
        con = sqlite3.connect('Recommendations.db')
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS data1
                                (names text, email text, role text, businessline text, location text, client text, dashboard text, useractivity int)''')


        with open('recommendation_engine_users.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                mylist = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]]
                #print(row[0]+" "+row[1]+" "+row[2]+row[3]+" "+row[4]+" "+row[5]+row[6]+" "+row[7])
                cur.executemany('''INSERT INTO data1 VALUES
                        (?,?,?,?,?,?,?,?)''', (mylist,))

        con.commit()

        # sql = "select * from data1"

        # cur.execute(sql)

        # db = cur.fetchall()

        # print(db[12][3])
        #for row in cur.execute('''SELECT * FROM data'''):
        #    print(row)

    def cd2(self):
        con = sqlite3.connect('Insights.db')
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS data2
                                (propertyAddress text, insight1 text, insight2 text, driver text, account text, criticality text)''')


        with open('property_insights_extended.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                mylist = [row[0],row[1],row[2],row[3],row[4],row[5]]
                #print(row[0]+" "+row[1]+" "+row[2]+row[3]+" "+row[4]+" "+row[5]+row[6]+" "+row[7])
                cur.executemany('''INSERT INTO data2 VALUES
                        (?,?,?,?,?)''', (mylist,))

        con.commit()


    @staticmethod
    def fetch1(ind1, ind2):
        con = sqlite3.connect('Recommendations.db')
        cur = con.cursor()

        sql = "select * from data1"

        cur.execute(sql)

        db = cur.fetchall()

        print(db[ind1][ind2])
    
    def fetch2(self,ind1, ind2):
        con = sqlite3.connect('Insights.db')
        cur = con.cursor()

        sql = "select * from data2"

        cur.execute(sql)

        db = cur.fetchall()

        print(db[ind1][ind2])

    