'''
Created on Aug 26, 2018

@author: jugu
'''

from plugins.parser.ConfigParserPluginBaseClass import ConfigParserPluginBaseClass
import re

class ConfigParser(ConfigParserPluginBaseClass):
    '''
    ConfigParser defines a config parser that can be used to parse Cisco IOS configuration
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ConfigParser, self).__init__()

    def __del__(self):
        super(ConfigParser, self).__del__()

    def isMyConfig(self):
        configLikelihood = 0
        '''
        Matching criterias are definced with format:
            (Description, Regexp Pattern, Likelihood value) 
        '''
        configMatchingCriterias = (
            ('IOS Version', '^version\s+\d+\.\d+', 20),
            ('Hostname', '^hostname\s+\w+', 20),
            ('Boot Start Marker', '^boot\-start\-marker', 20),
            ('Boot End Marker', '^boot\-end\-marker', 20),
            ('End', '^end', 20)
        )
        self.configFile.seek(0)
        configLine = self.configFile.readline()
        while configLine != '':
            for matchingCriteria in configMatchingCriterias:
                if re.match(matchingCriteria[1], configLine) is not None:
                    configLikelihood = configLikelihood + matchingCriteria[2]
            configLine = self.configFile.readline()
        if configLikelihood >= 75:
            return True
        else:
            return False
