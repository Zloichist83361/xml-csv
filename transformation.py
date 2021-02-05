import sys
import argparse

from part_xml import parse_xml


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path')

    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace =parser.parse_args(sys.argv[1:])
    parse_xml(namespace.path)