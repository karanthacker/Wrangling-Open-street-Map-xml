# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""

Before you process the data and add it into your database, you should check the
"k" value for each "<tag>" and see if there are any potential problems.

We have provided you with 3 regular expressions to check for certain patterns
in the tags.we would like to change the data
model and expand the "addr:street" type of keys to a dictionary like this:
{"address": {"street": "Some value"}}
So, we have to see if we have such tags, and if we have any tags with
problematic characters.

Please complete the function 'key_type', such that we have a count of each of
four tag categories in a dictionary:
  "lower", for tags that contain only lowercase letters and are valid,
  "lower_colon", for otherwise valid tags with a colon in their names,
  "problemchars", for tags with problematic characters, and
  "other", for other tags that do not fall into the other three categories.
"""

# types of sequences to be searched using re lib.
lower = re.compile(r'^([a-z]|_)*$') #for lower case letter
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$') #for collon
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]') # for prob chars


def key_type(element, keys):
   
    if element.tag == "tag":
        # if the element is named tag search it for the possible types
        if lower.search(element.attrib['k']):
            keys['lower'] = keys['lower'] + 1
        elif lower_colon.search(element.attrib['k']):
            keys['lower_colon'] = keys['lower_colon'] + 1
        elif problemchars.search(element.attrib['k']):
            print element.attrib['k']
            keys['problemchars'] = keys['problemchars'] + 1
        else:
            keys['other'] = keys['other'] + 1
        pass
    return keys
        
    return keys



def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys



def test():
    # You can use another testfile 'map.osm' to look at your solution
    # Note that the assertion below will be incorrect then.
    # Note as well that the test function here is only used in the Test Run;
    # when you submit, your code will be checked against a different dataset.
    keys = process_map('manhatten.osm')
    pprint.pprint(keys)


if __name__ == "__main__":
    test()
