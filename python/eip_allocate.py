#!/usr/bin/python

"""
-author : Nag m
- Hack   : Allocate an EIP Address
- Info   : Allocate an EIP Address
"""

import boto

def eip():
    print conn_default
    add = conn_default.allocate_address()
    print add

if __name__ == "__main__":
   conn_default = boto.connect_ec2()
   eip()
