import json
import logger as logging

logger = logging.get_logger("logs", "tools/config.py")


def load_config_file(file):
    with open(file) as json_data_file:
        try:
            data = json.load(json_data_file)
        except Exception as e:
            raise e
    return data


def create_config_iter(conf):
    for key, val in conf.iteritems():
        yield {'name': key, 'properties': val}
