#!/usr/bin/python

"""
- author : Nag m
- Hack   : Connect to ec2
- Info   : Connect to ec2
"""

import boto

def connect():
   conn = boto.connect_ec2()
   print conn

if __name__ == "__main__":
    connect()
