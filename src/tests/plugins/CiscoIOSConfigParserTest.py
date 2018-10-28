'''
Created on Oct 27, 2018

@author: jugu
'''
import unittest
from plugins.PluginCommon import PluginTypes
from plugins.parser.CiscoIOSConfigParser import ConfigParser

class CiscoIOSConfigParser(unittest.TestCase):

    def setUp(self):
        self.testObject = ConfigParser()
        self.testObject.loadConfigFile("CiscoIOSConfigParserTestCase.txt")

    def testIsMyConfig(self):
        self.testObject.isMyConfig()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
