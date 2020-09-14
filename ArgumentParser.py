#!/bin/python

import argparse
import os

class ArgumentParser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Checks all images for width and ratio and filters them into appropriate sub-directories.')

    def add_arguments(self):
        self.parser.add_argument('path', default=os.getcwd(), nargs='?', help='directory to be used by %(prog)s. Default is current working directory.')
        self.parser.add_argument('-v', '--verbose', action='store_true', help='increase verbosity')

    def get_args(self):
        return self.parser.parse_args()


parser = ArgumentParser()
parser.add_arguments()