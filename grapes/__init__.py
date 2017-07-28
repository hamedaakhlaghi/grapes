from os.path import dirname, join, abspath, basename, exists
import argparse
import sys

import pymlconf
import appdirs


__version__ = '0.1.0'


APP_NAME=basename(sys.argv[0])
HERE = abspath(dirname(__file__))
DATA = abspath(join(HERE, '../data'))
USER_CONFIG_FILE = join(appdirs.user_config_dir(APP_NAME, version=__version__), '%s.yml' % APP_NAME)
settings = pymlconf.DeferredConfigManager()

__builtin_config__ = '''

db:
  uri: sqlite:///%s/dev-data.sqlite

''' % DATA


parser = argparse.ArgumentParser(APP_NAME)
parser.add_argument('-c', '--config-file', required=False, help='The config file')


def main():
    args = parser.parse_args()
    settings.load(builtin=__builtin_config__)
    print('Checking for user\'s config file: %s ...' % USER_CONFIG_FILE, end='')
    if exists(USER_CONFIG_FILE):
        print('Found!')
        settings.load_files(USER_CONFIG_FILE)
    else:
        print('Not found!')
    if args.config_file:
        settings.load_files(args.config_file)
    print(settings.db.uri)
