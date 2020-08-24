#!/usr/bin/env python3.6
# coding: utf-8

import unittest
import sys
import os

ROOT_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
    tests = unittest.TestLoader().discover(ROOT_PATH, "*.py")
    result = unittest.TextTestRunner().run(tests)
    if not result.wasSuccessful():
        sys.exit(1)
