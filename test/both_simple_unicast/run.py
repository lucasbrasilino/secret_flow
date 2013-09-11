#!/bin/env python

from NFTest import *
from scapy.utils import rdpcap

phy2loop0 = ('../connections/conn', [])

nftest_init(sim_loop = [], hw_config = [phy2loop0])
nftest_start()

pkts = rdpcap("udp.pcap")
pkt=pkts[0]

nftest_send_phy('nf2c0', pkt)
nftest_expect_phy('nf2c1', pkt)
if not isHW():
   nftest_expect_phy('nf2c2', pkt)
   nftest_expect_phy('nf2c3', pkt)

nftest_barrier()

total_errors = 0

nftest_finish()
