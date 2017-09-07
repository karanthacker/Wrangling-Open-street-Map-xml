# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
 finding out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""
filename = "manhatten.osm"

def get_user(element):
    id = element.attrib['uid']  
    return id 

#  function parsing the osm 
def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if "uid" in element.attrib: # finding user id in the element
            id = get_user(element)
            users.add(id)          # adding to set of unique users
        
            

    return users

# main function calling the process_map function
def test():

    users = process_map(filename)
    pprint.pprint(users)



if __name__ == "__main__":
    test()
