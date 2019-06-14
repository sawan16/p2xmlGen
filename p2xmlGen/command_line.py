#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:13:00 2019

@author: sawan
"""

import sys
import os, os.path
from io import open
import glob, time

from lark import Lark
from lark.indenter import Indenter

class PythonIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

def _read(fn, *args):
    kwargs = {'encoding': 'iso-8859-1'}
    with open(fn, *args, **kwargs) as f:
        return f.read()

if len(sys.argv)<3:
	print("Please Provide source and target file name correctly....")
	exit()

kwargs = dict(rel_to=__file__, postlex=PythonIndenter(), start='file_input')


python_parser3 = Lark.open('updated_python3.lark',parser='lalr', **kwargs)
#print(type(python_parser3))
tree = python_parser3.parse(_read(sys.argv[1]) + '\n')

fl = open(sys.argv[2],'w')
fl.write(str(tree))
fl.close()

print(tree)