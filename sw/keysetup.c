#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <net/if.h>

#include "nf2.h"
#include "nf2util.h"

#include "reg_defines_secret_flow.h"

#define PATHLEN		80

#define DEFAULT_IFACE	"nf2c0"

/* Global vars */
static struct nf2device nf2;

/* Function declarations */
int main(int argc, char *argv[])
{
	unsigned int value;
	unsigned int write_value=0;
	int opt = -1;
	short int s_flag = 0;
	char *value_buff = NULL;

	nf2.device_name = DEFAULT_IFACE;

	// Open the interface if possible
	if (check_iface(&nf2))
	{
		exit(1);
	}
	if (openDescriptor(&nf2))
	{
		exit(1);
	}

	while ((opt = getopt (argc, argv, "s:")) != -1)
		{
			switch (opt) 
				{
					case 's': value_buff = optarg; break;
				}
		}

	if (value_buff != NULL)
		{
			sscanf(value_buff, "%x", &write_value);
			printf("Saving key value: %x\n", write_value);
			writeReg(&nf2, SECRET_FLOW_KEY_REG, write_value); 
		};

	readReg(&nf2, SECRET_FLOW_KEY_REG, &value);
	printf("Key register value: %x\n",value); 

	closeDescriptor(&nf2);

	return 0;
}
