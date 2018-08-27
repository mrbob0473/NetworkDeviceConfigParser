'''
Created on Aug 26, 2018

@author: jugu
'''
import unittest
from plugins.PluginCommon import PluginBaseClass


class PluginBaseClassTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetPluginType(self):
        with self.assertRaises(NotImplementedError):
            PluginBaseClass.getPluginType(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
