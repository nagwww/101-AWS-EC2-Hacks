#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Create a connection to EC2 Region
- Info   : Create a connection to EC2 Region
"""

import boto.ec2

def connect():
    print conn

if __name__ == "__main__":
   conn = boto.ec2.connect_to_region("us-west-2")
   connect()
