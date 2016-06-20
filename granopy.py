import xml.etree.cElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom
import requests


class Track:
    title = None
    year = None
    genre = None
    artist = None


    tracks = []

    def __init__(self, title):
        self.title = title


class Artist:
    def __init__(self, album_title):
        self.name = album_title

class Album:
    def __init__(self, name):
        self.name = name

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def test_xml():
    top = ET.Element('QUERIES')
    return top

xml = test_xml()
print(prettify(xml))