# -*- coding: utf-8 -*-
''' intro to the code : the code below counts the different elements on the 
basis of tag names classified into 3 categories ways,nodes,nd(nodes in ways)
 and tags of the  whole osm file 
'''
import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict
filename = "sample_manhatten.osm"

# function below iterates the counter of differnt tag names stored in a dict
def count_tags(filename):
        tags = defaultdict(int)
        for events,elem in ET.iterparse(filename):
            tags[elem.tag] += 1
        print tags
        return tags


def test():

    tags = count_tags(filename)
    pprint.pprint(tags)
    
if __name__ == "__main__":
    test()   
