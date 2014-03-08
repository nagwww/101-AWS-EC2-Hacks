#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Terminate an EC2 instance
- Info   : Terminate an EC2 instance
"""

import boto

def term():
    ec2 = conn_default.terminate_instances("i-0ccbc92d")
    print ec2

if __name__ == "__main__":
   conn_default = boto.connect_ec2()
   term()
