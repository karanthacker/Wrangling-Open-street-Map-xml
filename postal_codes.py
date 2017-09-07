# -*- coding: utf-8 -*-
'''
intro : program to clean post codes
'''

import xml.etree.cElementTree as ET
import pprint
import re


filename = 'manhatten.osm'

code_type_re = re.compile(r'\D+', re.IGNORECASE) # finding sequence of non digit chars

# finding the post code tag with problematic value and correcting it 
def find_post_code(elem):
    if elem.attrib['k'] == "addr:postcode" :
        m = code_type_re.match(elem.attrib['v'])
        if m:                                  # if post code contains non digit chars at the start 
            print elem.attrib['v']
            if elem.attrib['v'] [0] == "(" :  # correcting phone no. type codes
                correct_code = elem.attrib['v'][6:]
                print correct_code
            else:
                # correcting codes with alphabet chars infront of it 
                correct_code = re.sub(code_type_re,"" , elem.attrib['v']) 
                print correct_code 

# main function calling the sub functions
def audit_postcode(filename):
    for event,elem in ET.iterparse(filename,events=("start",)):
        if elem.tag == "way" or elem.tag == "node":
            for tag in elem.iter("tag"):
                find_post_code(tag)
 
if __name__ == "__main__":
    audit_postcode(filename)
    
