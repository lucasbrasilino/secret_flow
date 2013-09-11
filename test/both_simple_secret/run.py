#!/bin/env python

from NFTest import *
from scapy.utils import rdpcap
from reg_defines_secret_flow import *

phy2loop0 = ('../connections/conn', [])

nftest_init(sim_loop = [], hw_config = [phy2loop0])
nftest_start()

pkts = rdpcap("udp.pcap")
pkt=pkts[0]
secret_pkts = rdpcap("udp-secret.pcap")
secret_pkt=secret_pkts[0]

key = 0xdeadbeef;
nftest_regwrite(SECRET_FLOW_KEY_REG(),key);
nftest_regread_expect(SECRET_FLOW_KEY_REG(),key);


nftest_send_phy('nf2c0', pkt)
nftest_expect_phy('nf2c1', secret_pkt)
if not isHW():
   nftest_expect_phy('nf2c2', secret_pkt)
   nftest_expect_phy('nf2c3', secret_pkt)


nftest_barrier()

total_errors = 0

#tmp = nftest_regread_expect(reg_defines.MAC_GRP_1_TX_QUEUE_NUM_PKTS_SENT_REG(), num_broadcast)
#tmp = nftest_regread_expect(reg_defines.MAC_GRP_2_TX_QUEUE_NUM_PKTS_SENT_REG(), num_broadcast)
#tmp = nftest_regread_expect(reg_defines.MAC_GRP_3_TX_QUEUE_NUM_PKTS_SENT_REG(), num_broadcast)
#tmp = nftest_regread_expect(reg_defines.SWITCH_OP_LUT_NUM_MISSES_REG(), num_broadcast)

nftest_finish()
