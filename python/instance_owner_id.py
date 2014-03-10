#!/usr/bin/python

"""
- Author : Nag m
- Hack   : All running EC2 instance security groups
- Info   : All running EC2 instance security groups
"""

import boto

def running():
    ec2 = conn_default.get_all_reservations()
    for instance in ec2:
        print instance.id, instance.owner_id

if __name__ == "__main__":
   conn_default = boto.connect_ec2()
   running()
