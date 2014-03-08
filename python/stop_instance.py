#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Stop an EC2 instance
- Info   : Stop an EC2 instance
"""

import boto

def stop():
    ec2 = conn_default.stop_instances("i-0ccbc92d")
    print ec2

if __name__ == "__main__":
   conn_default = boto.connect_ec2()
   stop()
