
# SPDX-License-Identifier: Apache-2.0
# Copyright 2021 Open Networking Foundation

from ipaddress import IPv4Address
from grpc_test import *
from collections import namedtuple
import os
import sys
import re
import subprocess

os.environ['no_proxy'] = '*'
#print("Hello")


# Defining main function
def main(ue_ip):
    print("hey there")
    upf_pod = subprocess.run(["kubectl get pod upf-0 -o wide -n omec | awk '{print $6}'"], shell=True, capture_output=True, text=True)
    upf_ip = upf_pod.stdout.strip().split('\n')[1]
    print("UPF IP Address: ",upf_ip)
    client = GrpcTest()
    client.setUp(upf_ip)
    
    pfcp_log = subprocess.run([f"kubectl logs -n omec upf-0 -c pfcp-agent | grep {ue_ip}"], shell=True, capture_output=True, text=True)

    for line in pfcp_log.stdout.strip().split('\n'):
        if "Saved PFCP sessions to local store" in line:
            last_line = line
    #print(last_line)
    #for rule in parse_substrings_between_brackets(last_line):
        #print(rule)
    data = {}
    for info in last_line.split(","):
        #print(info.strip())
        key, value = info.strip().split("=", 1)
        data[key] = value
    #print(data)
    
    qerIDList = list(map(int,data['qerIDs'][1:-1].split(' ')))
    #print(qerIDList)
    far = client.createFAR(
            farID=10003,
            fseID=int(data['F-SEID']),
            fseidIP=3232257044,
            dstIntf=0,
            sendEndMarker=False,
            applyAction=0,
            tunnelType=1,
            tunnelIP4Src= int(IPv4Address('192.168.252.3')),
            tunnelIP4Dst= int(IPv4Address('192.168.251.6')),
            tunnelTEID=1,
            tunnelPort=2152
        )
    '''
    pdrfields = (
            'srcIface',
            'tunnelIP4Dst',
            'tunnelTEID',
            'srcIP',
            'dstIP',
            'srcPort',
            'dstPort',
            'proto',
            'srcIfaceMask',
            'tunnelIP4DstMask',
            'tunnelTEIDMask',
            'srcIPMask',
            'dstIPMask',
            'srcPortMask',
            'dstPortMask',
            'protoMask',
            'precedence',
            'pdrID',
            'fseID',
            'fseidIP',
            'ctrID',
            'farID',
            'qerIDList',
            'needDecap',
            'allocIPFlag'
        )    '''
    pdr = client.createPDR(
            pdrID = 10029,
            fseID = int(data['F-SEID']),
            fseidIP = int(data['F-SEID IP']),
            srcIface = 1,
            srcIfaceMask = 0xFF,
            srcIP = int(IPv4Address('172.250.0.0')),
            srcIPMask = 0xffff0000,
            tunnelIP4Dst = int(IPv4Address('192.168.252.3')),
            tunnelIP4DstMask =  0xFFFFFFFF,
            tunnelTEID = 0,
            tunnelTEIDMask = 0,
            dstIP = int(IPv4Address(ue_ip)),
            dstIPMask = 0xFFFFFFFF,
            precedence = 9,
            ctrID = 0,
            farID = int(data['farID']),
            qerIDList = qerIDList,
            needDecap = 1,
            allocIPFlag=False
        )

    print(pdr)
    #print("del far response:")
    #client.addPDR(pdr, debug=True)
    #client.delPDR(pdr, debug=True)
    #client.delFAR(far, debug=True)
    #print()

def parse_substrings_between_brackets(s):
    bracket_regex = re.compile(r'\[([^\]]*)\]')
    substrings = []

    for match in bracket_regex.finditer(s):
        substrings.append(match.group(1))

    return substrings




# Using the special variable
# __name__
if __name__=="__main__":

    if len(sys.argv) < 2:
        print("Please run program as: setupLAN.py [UE_IP]")
        exit()
    else:
        ue_ip = sys.argv[1]
        main(ue_ip)


    #main()
