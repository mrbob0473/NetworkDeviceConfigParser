'''
Created on Aug 26, 2018

@author: jugu
'''

from abc import ABCMeta
from plugins.PluginCommon import *
import mmap
import os


class ConfigParserPluginBaseClass(PluginBaseClass, metaclass=ABCMeta):
    '''
    ConfigParserPluginBaseClass is an abstract bases class that defines the base class
    that every config parser plugin for this application must implement.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.configFilePath = None
        self.configFile = None

    def __del__(self):
        if self.configFile is not None:
            self.configFile.close()

    # @abc.abstractmethod
    def isMyConfig(self):
        raise NotImplementedError('users must define isMyConfig to use this base class')

    def getPluginType(self):
        return PluginTypes.TYPE_PARSER

    def loadConfigFile(self, configFilePath):
        if not os.path.isfile(configFilePath):
            raise FileNotFoundError(configFilePath)
        else:
            self.configFilePath = configFilePath
            self.configFile = open(configFilePath, 'r')
