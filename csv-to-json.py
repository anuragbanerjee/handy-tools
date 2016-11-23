#!/usr/bin/env python

'''
CSV to JSON Converter
Created by Anurag Banerjee.
Copyright 2016. All rights reserved.

USAGE `python csv-to-json.py <CSV FILE>`

Use I/O Redirection for creating resulting files.
`python csv-to-json.py sample.csv > sample.json`

'''

from codecs import open
import json
import sys

def showInfo():
  print "CSV to JSON Converter"
  print "USAGE: csv-to-json.py <CSVFILE>"
  print ""
  print "Use I/O redirection for creating resulting files. Example:"
  print "python ./csv-to-json.py sample.csv > sample.json"

def main():
  if len(sys.argv) != 2 or sys.argv[1].split(".")[-1] != "csv":
    showInfo()
    return
  result_json = []
  with open(sys.argv[1], 'r', encoding="utf-8") as csv:
    lines = csv.readlines()
    fields = [field.rstrip() for field in lines[0].split(",")]
    entryId = 0;
    for l in lines[1:]:
      try:
        entry = result_json[entryId]
      except IndexError:
        result_json.append({})
        entry = result_json[-1]
      for id, val in enumerate(l.split(",")):
        result_json[entryId][fields[id]] = val.rstrip()
      else:
        entryId+=1


  print json.dumps(
    result_json,
    encoding="utf-8",
    indent=4,
    separators=(',', ': '),
    ensure_ascii=False
  ).encode("utf-8")

if __name__ == '__main__':
  main()