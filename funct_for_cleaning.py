'''
functions defined here to call for cleaning data while writing to csv . 
the file is imported to the writing_to_csv.py to call the functions 
defined here over there 
'''

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "manhatten.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
code_type_re = re.compile(r'\D+', re.IGNORECASE)


mapping = { "Ave":"Avenue",
           "ave":"Avenue",
           "Ave.":"Avenue",
           "Avene":"Avenue",
           "Aveneu":"Avenue",
           "avenue":"Avenue",
           "B":"Boulevard",
           "Blv.":"Boulevard",
           "Broadway.":"Broadway",
           "bus_stop":"Bus_Stop",
           "Ctr":"Center",
           "D":"Drive",
           "Floor)":"Floor",
           "NY":"Newyork",
           "ST":"Street",
           "St":"Street",
           "st":"Street",
           "St.":"Street",
           "Steet":"Street",
           "Streeet":"Street",
           "street":"Street",
           "Plz":"Plaza",
           "Rd":"Road"

            }
# to catch tags with street names as values 
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

# to identify tags with post code values 
def is_post_code(elem):
    return (elem.attrib['k'] == "addr:postcode")

# function to return cleaned street name 
def update_name( mapping,name):

        m = street_type_re.search(name)
    
        street_type = m.group()
        if street_type  in mapping :
            better_name = re.sub(street_type_re, mapping[street_type], name)
            print  name, "=>", better_name
            return better_name
        else :
               return name 
            
            
# function calls the update_name and returns the value
def correct_street_name(elem):
    
    correct_name = update_name(mapping,elem.attrib['v'])
    return correct_name

# function returns the cleaned postal code value
def correct_post_code(elem):
    
        m = code_type_re.match(elem.attrib['v'])
        if m:
            print elem.attrib['v']
            if elem.attrib['v'] [0] == "(" :
                correct_code = elem.attrib['v'][6:]
                print correct_code
                return correct_code
            else:
                correct_code = re.sub(code_type_re,"" , elem.attrib['v'])
                print correct_code 
                return correct_code
        else :
                return   elem.attrib['v']          
           