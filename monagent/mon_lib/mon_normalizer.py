from util import json
import os

class MonNormalizer(object):

    def __init__(self, logger, mapping_file_path):
        self.logger = logger
        self.mapping_file_path = mapping_file_path
        self.metric_map = self.__get_metric_map()

    def is_initialized(self):
        return self.metric_map != None

    def normalize_name(self, key):
        name = key
        if name in self.metric_map:
            name = self.encode(self.metric_map[name])
        else:
            name = self.encode(name)
        return name

    def encode(self, string):
        return_str = string
        if isinstance(string, basestring):
            return_str = string.encode('ascii','ignore')
        return return_str

    def __get_metric_map(self):
        json_data = None
        try:
            json_data = open(self.mapping_file_path, 'r')
            data = json.loads(json_data.read())
            json_data.close()
            return data
        except IOError as e:
            self.logger.error("I/O error while loading metric mapping file({0}): {1}".format(e.errno, e.strerror))
        except ValueError as v:
            self.logger.error("Value error while decoding JSON from metric mapping file({0}): {1}".format(v.errno, v.strerror))
        except:
            self.logger.error("Unable to process metric mapping file...")

        if json_data:
            json_data.close()
        return None