#!/usr/bin/python

import json
import boto
import boto.ec2


ec2_connections = {}

def aws_connection(connection_type, region, account_id):
    sts = boto.connect_sts()
    role = sts.assume_role('arn:aws:iam::' + account_id + ':role/BaseRole', 'baserole')

    if connection_type == 'ec2':
        return boto.ec2.connect_to_region(region,
                                          aws_access_key_id=role.credentials.access_key,
                                          aws_secret_access_key=role.credentials.secret_key,
                                          security_token=role.credentials.session_token)


if __name__ == "__main__":

    account="232323222222"
    region="eu-west-1"

    ec2_connections[region] = aws_connection("ec2", region, account)
    sg = ec2_connections[region].get_all_security_groups(group_ids='sg-xyzxyz')[0]
    with open('srccidr.json') as data_file:
        data = json.load(data_file)
        for i in data["rules"]:
            print "[+]Adding the rule for cidr", i["cidr_ip"], ""
            try:
                sg.authorize(ip_protocol=i["ip_protocol"], from_port=i["from_port"], to_port=i["to_port"], cidr_ip=i["cidr_ip"],  dry_run=False)
                print " - Successfully Added"
            except ec2_connections[region].ResponseError, e:
                print " - Issue adding", e.code

