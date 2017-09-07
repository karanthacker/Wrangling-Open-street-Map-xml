# -*- coding: utf-8 -*-
''' 
 intro : this code parses the tag elements with key value "addr:street" to 
 identify diff street types in the street address and to find out most comm
 street types 
 '''
import xml.etree.cElementTree as ET
from collections import defaultdict
import re 

filename   = "manhatten.osm"

street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE) #catch sequence of non white chars at the end of string 
street_types = defaultdict(int)
list1 = [] # TO store common street types 

# below is a function to catch the street types in name and store them into dict with no. of counts
def audit_street_type(street_name,street_types):
    m = street_type_re.search(street_name)
    if m :
        street_type = m.group()
        street_types[street_type] += 1 
        
# arrange the dict alphabetically
def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys,key=lambda s: s.lower())
    for k in keys:
        v = d[k]
        print "%s: %d" %(k,v)

# if the street type has counter value more than 20 it is stored in list 1
def find_common_st_name(names):
    expected_types =[]
    for street in names:
        if names[street] > 20:
            expected_types.append(street)
    return expected_types        
            
# find value of total no. of street names in the file
def total_streets(street_types) :
    total_count = 0
    for count in street_types:
        total_count = total_count + street_types[count] 
    print total_count    

 # main function parsing the file and calling rest of functions            
def test(filename):
    for event,elem in ET.iterparse(filename):
        if (elem.tag == "tag") and (elem.attrib['k']=="addr:street"):
            audit_street_type(elem.attrib['v'],street_types)
    print_sorted_dict(street_types)
    

if __name__ == "__main__":
    test(filename)   
    list1 = find_common_st_name(street_types)
    print list1
    total_streets(street_types)
            