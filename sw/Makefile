
CFLAGS = -g
CC = gcc
LDFLAGS = -lncurses
CPPFLAGS = -I../../../lib/C/common/ -I../lib/C/

all: registers regdump show_stats keysetup

registers:
	$(NF_ROOT)/bin/nf_register_gen.pl --project reference_switch

regdump: regdump.o ../../../lib/C/common/nf2util.o ../../../lib/C/common/nf2util_proxy_common.o ../../../lib/C/common/util.o

show_stats: show_stats.o ../../../lib/C/common/nf2util.o ../../../lib/C/common/nf2util_proxy_common.o ../../../lib/C/common/util.o

keysetup: keysetup.o ../../../lib/C/common/nf2util.o ../../../lib/C/common/nf2util_proxy_common.o ../../../lib/C/common/util.o 

clean :
	rm -f show_stats regdump keysetup *.o

