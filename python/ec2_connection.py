#!/usr/bin/python

"""
test
- Author: Nag m
- Hack   : Create a connection to EC2 
- Info   : Create a connection to EC2 ( The default is always us-east-1 even if region is passed to it)
"""

import boto

def connect():
    print conn
    print conn_default

if __name__ == "__main__":
   conn = boto.connect_ec2("us-west-2")
   conn_default = boto.connect_ec2()
   connect()
