'''
Created on Aug 26, 2018

@author: Bob Gu
'''

from abc import ABCMeta
from enum import Enum


class PluginTypes(Enum):
    TYPE_PARSER = 1
    TYPE_OUTPUT = 2


class PluginBaseClass(object, metaclass=ABCMeta):
    '''
    PluginBaseClass is an abstract bases class that defines the base class
    that every plugin for this application must implement.
    '''

    def __init__(self):
        '''
        Constructor
        '''

    # @abc.abstractmethod
    def getPluginType(self):
        raise NotImplementedError('users must define getPluginType to use this base class')

    def getPluginName(self):
        return __name__
