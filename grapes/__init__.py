from os.path import dirname, join, abspath, basename
import argparse
import sys


__version__ = '0.1.0'


HERE = abspath(dirname(__file__))
DATA = abspath(join(HERE, '../data'))

__builtin_config__ = '''

db:
  uri: sqlite:///%s/dev-data.sqlite

''' % DATA


parser = argparse.ArgumentParser(basename(sys.argv[0]))
parser.add_argument('-c', '--config-file', required=False, help='The config file')

def main():
    args = parser.parse_args()
    print(__builtin_config__)
