#!/usr/bin/env python

from scapy.all import *
from scapy.utils import *
import sys

nprint = sys.stdout.write

pkts=rdpcap("udp.pcap")
pkt=pkts[0]

key=[0xde,0xad,0xbe,0xef]
#key=[0x0,0x0,0x0,0x0]
k=0
offset=4

pdu=str(pkt)
i=len(pdu)

for l in range(i):
	if  l and not (l % 16):
		nprint("\n")
	byte = ord(str(pdu[l]))
	k=l%4
	if l > 41:
		b = (byte ^ key[k])
	else:
		b = byte	
	nprint ("%.2x " % b)
