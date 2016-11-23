#!/usr/bin/env python

'''
JSON to CSV Converter
Created by Anurag Banerjee.
Copyright 2016. All rights reserved.

USAGE `python json-to-csv.py <JSON FILE>`

Use I/O Redirection for creating resulting files.
`python json-to-csv.py sample.json > sample.csv`

'''

from codecs import open
import json
import sys

def showInfo():
  print "JSON to CSV Converter"
  print "USAGE: json-to-csv.py <JSON FILE>"
  print ""
  print "Use I/O redirection for creating resulting files. Example:"
  print "python ./json-to-csv.py sample.json > sample.csv"

def main():
  if len(sys.argv) != 2 or sys.argv[1].split(".")[-1] != "json":
    showInfo()
    return
  keys = []
  with open(sys.argv[1], 'r', encoding="utf-8") as json_file:
    json_data = json.load(json_file)
        for key in json_data[0]:
          keys.append(key)

        for i in range(len(keys)):
          if (i == 0):
            print keys[i],
          else:
            print ", " + keys[i],
        print

        for i in range(len(json_data)):
          for j in range(len(keys)):
            if (j == 0):
              print json_data[i][keys[j]],
            else:
              print ", " + str(json_data[i][keys[j]]),
        print
if __name__ == '__main__':
  main()