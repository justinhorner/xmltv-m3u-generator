import xml.etree.ElementTree as ET
import json


class Config(object):
    def __init__(self, xmlFilePath, hdhomerunUrlPrefix, m3uFilename):
        self.xmlFilePath = xmlFilePath
        self.hdhomerunUrlPrefix = hdhomerunUrlPrefix
        self.m3uFilename = m3uFilename


def loadConfig():
    with open('config.json') as json_data_file:
        config = json.load(json_data_file)
        return Config(config['xmlFilePath'], config['hdhomerunUrlPrefix'], config['m3uFilename'])


def buildItemInfo(id, displayName, icon):
    return '#EXTINF:-1, tvg-ID="{0}" tvg-name="{1}" tvg-logo="{2}",{1}\n'.format(id, displayName, icon)


def buildItemUrl(urlPrefix, channel):
    return '{0}{1}\n'.format(urlPrefix, channel)


def buildM3U():
    _config = loadConfig()

    str = '#EXTM3U\n'

    tree = ET.parse(_config.xmlFilePath)
    root = tree.getroot()

    for channel in root.findall('channel'):
        id = channel.get('id')
        displayNames = channel.findall('display-name')
        displayName = displayNames[0].text
        _channel = displayNames[1].text
        icon = channel.find('icon').attrib['src']

        str += buildItemInfo(id, displayName, icon)
        str += buildItemUrl(_config.hdhomerunUrlPrefix, _channel)

    m3uFile = open(_config.m3uFilename, 'w')
    m3uFile.write(str)
    m3uFile.close()

buildM3U()