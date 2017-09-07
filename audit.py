# -*- coding: utf-8 -*-

"""
- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    
-  the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "manhatten.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)




# UPDATE THIS VARIABLE
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


           

# finding tags with street name as vcalue 
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

# main function doing iterative parsing and calling the update function
def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    update_name(mapping, tag.attrib['v'])
    osm_file.close()
    return street_types

# checking for the street type to be in mapping 
# and if there replacing it in the name with better street type 
def update_name( mapping,name):

        m = street_type_re.search(name)
    
        street_type = m.group()
        if street_type  in mapping :
            #the below line finds the part to be replaced with the maping street type 
            # from the street name string 
            better_name = re.sub(street_type_re, mapping[street_type], name)
            print  name, "=>", better_name
        else :
               return name 
            

        return better_name






if __name__ == '__main__':
    audit(OSMFILE)