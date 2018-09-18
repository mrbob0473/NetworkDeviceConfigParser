'''
Created on Aug 26, 2018

@author: jugu
'''
import unittest
from plugins.PluginCommon import PluginTypes
from plugins.parser.ConfigParserPluginBaseClass import ConfigParserPluginBaseClass


class ConfigParserPluginBaseClassTestCase(unittest.TestCase):

    def setUp(self):
        self.testObject = ConfigParserPluginBaseClass()

    def tearDown(self):
        pass

    def testGetPluginType(self):
        self.assertEqual(self.testObject.getPluginType(), PluginTypes.TYPE_PARSER)

    def testLoadConfigFile(self):
        self.testObject.loadConfigFile("ConfigParserPluginBaseClassTestCase.txt")
        self.testFileFirstLine = self.testObject.configFile.readline()
        self.assertEqual(self.testFileFirstLine, "ConfigParserPluginBaseClassTestCase Sample File")

    def testIsMyConfig(self):
        with self.assertRaises(NotImplementedError):
            ConfigParserPluginBaseClass.isMyConfig(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
