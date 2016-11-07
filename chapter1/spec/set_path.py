#!/usr/bin/env python
#!coding:utf-8

import os
import sys

# set current dir's parent dir to the pythonpath
get_dir = os.path.dirname
pkg_path = os.path.join(get_dir(get_dir(os.path.abspath(__file__))), 'codes')
sys.path.append(pkg_path)
