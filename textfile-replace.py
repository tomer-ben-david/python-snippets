#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:29:21 2018

@author: tomer.bendavid
"""

import fileinput
import re

with fileinput.FileInput("/Users/tomer.bendavid/Downloads/tmp.txt") as file:
    for line in file:
        print(re.search('\/.*?\/(.*?)\s*.*', line).group(1))
#        print(line)