'''
Created on Aug 26, 2018

@author: jugu
'''

from abc import ABCMeta
from plugins.PluginCommon import *


class ConfigParserPluginBaseClass(PluginBaseClass, metaclass=ABCMeta):
    '''
    ConfigParserPluginBaseClass is an abstract bases class that defines the base class
    that every config parser plugin for this application must implement.
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def getPluginType(self):
        return PluginTyps.TYPE_PARSER
