#!/usr/bin/env python

'''
Batch Rename Extensions
Created by Anurag Banerjee.
Copyright 2016. All rights reserved.

USAGE `python batch-rename-extensions.py <DIRECTORY>`

'''

import os, sys

folder, newExtension = sys.argv[1:];

if os.path.isdir(folder):
	files = os.listdir(folder);
	for filename in files:
		if "." not in filename: continue;
		extension = filename.split(".")[-1];
		name = filename[:(len(extension) * -1)];
		oldfile = folder + "/" +filename
		newfile = folder + "/" + name + newExtension
		os.rename(oldfile, newfile)