'''
intro : the code parses the file to catch the street types and look up to
the table of common streets and if not found adds it to a dict of rare street
types with values in it are a set of street names of that type 
'''

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

common_street_names = ['Heights', 'Concourse', 'Mews', 'D', 'Alley', 'Broadway', 'West', 'Circle', 'John', 'Park', 'C', 'Extension', 'Plaza', 'Oval', 'Place', 'Square', 'Row', 'Boulevard', 'North', 'Lane', 'B', 'St', 'Parkway', 'Road', 'Walk', 'Ave', 'Avenue', 'Court', 'Highway', 'East', 'Bowery', 'Terrace', 'A', 'Drive', 'Americas', 'South', 'Street', 'Crescent', 'Slip']
street_types  = defaultdict(set)
street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE) # sequence to match the street type 

filename = "manhatten.osm"

def is_street_name(elem):
    return  (elem.attrib["k"] == "addr:street") #catches the tag with key value "addr:street"

# function below used to look up to the list of common street types
# and if not found adds to a dict "street_types" which is made of rare 
#street names as a set
def audit_street_type(street_types,street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in common_street_names:
            street_types[street_type].add(street_name)
    
# main function to run the whole code     
def audit(filename):
    for event,elem in ET.iterparse(filename,events=("start",)):
        if elem.tag == "way" or elem.tag == "node":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types,tag.attrib["v"])  
    pprint.pprint(dict(street_types))
    
if __name__ == "__main__":
    audit(filename)   