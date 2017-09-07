# -*- coding: utf-8 -*-
''' 
intro : constructing the database from the csv files 
'''

import csv
import sqlite3

db = sqlite3.connect("manhatten.db") 
c = db.cursor()
db.text_factory = str

# making nodes table
c.execute("CREATE TABLE nodes (id,lat,lon,user,uid,version,changeset,timestamp);")
with open ('nodes.csv','rb') as f:
    line = csv.DictReader(f) 
    to_db = [(i['id'], i['lat'], i['lon'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) for i in line]

c.executemany("INSERT INTO nodes (id, lat, lon, user, uid, version, changeset, timestamp)  VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
db.commit()

# making nodes_tags table
c.execute("CREATE TABLE nodes_tags (id, key, value, type);")
with open('nodes_tags.csv','rb') as f:
    line = csv.DictReader(f) 
    to_db = [(i['id'], i['key'], i['value'], i['type']) for i in line]

c.executemany("INSERT INTO nodes_tags (id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
db.commit()

# making ways table
c.execute("CREATE TABLE ways (id, user, uid, version, changeset, timestamp);")
with open('ways.csv','rb') as f:
    line = csv.DictReader(f) 
    to_db = [(i['id'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) for i in line]

c.executemany("INSERT INTO ways (id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", to_db)
db.commit()

# making ways_nodes table
c.execute("CREATE TABLE ways_nodes (id, node_id, position);")
with open('ways_nodes.csv','rb') as f:
    line = csv.DictReader(f) 
    to_db = [(i['id'], i['node_id'], i['position']) for i in line]

c.executemany("INSERT INTO ways_nodes (id, node_id, position) VALUES (?, ?, ?);", to_db)
db.commit()

# making ways_tags table
c.execute("CREATE TABLE ways_tags (id, key, value, type);")
with open('ways_tags.csv','rb') as f:
    line = csv.DictReader(f) 
    to_db = [(i['id'], i['key'], i['value'], i['type']) for i in line]

c.executemany("INSERT INTO ways_tags (id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
db.commit()


