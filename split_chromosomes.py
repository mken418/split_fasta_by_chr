#!/usr/bin/env python

"""
Split a fasta file by chromosome/contig. This script will split a fasta file by the description lines that begin with >.
The name of each contig will only be taken as the first word after the >. 
Example: 
	>chr1  AC:CM000663.2  gi:568336023  LN:248956422  rl:Chromosome  M5:6aef897c3d6ff0c78aff06ac189178dd  AS:GRCh38
	The script will only parse for chr1 as the contig name.
"""

import argparse
import re
import os

parser=argparse.ArgumentParser()


parser.add_argument('-i', type=str, help='Name of fasta file to split by chromosome')
parser.add_argument('-p', type=str, help='prefix for each output file. The output fasta will be named: prefix_contigname.fa')
parser.add_argument('-o', type=str, help='Full path name of the output directory for the output fasta files')

args=parser.parse_args()

if not os.path.exists(args.o):
	os.makedirs(args.o)


fh=open(args.i, 'r')

First=True
for line in fh:
	if line.startswith('>'): #description line
		if First:
			line=line.strip()
			match=re.match(r'>(\S+)\s.+', line)
			contig=match.group(1)
			out_fh=open(args.o+'/'+args.p+'_'+contig+'.fa', 'w')
			out_fh.write('>'+contig+'\n')
			First=False
			continue
		else:
			out_fh.close()
			line=line.strip()
			match=re.match(r'>(\S+)\s.+', line)
			contig=match.group(1)
			out_fh=open(args.o+'/'+args.p+'_'+contig+'.fa', 'w')
			out_fh.write('>'+contig+'\n')
			continue

	out_fh.write(line)
out_fh.close()
fh.close()
