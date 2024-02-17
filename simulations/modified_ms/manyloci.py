#!/usr/bin/env python
# using as argument:  ms 20 5 -t 10 -r 0 1000 -I 2 20 10 -T -M -q 1000 -ej 1.0  1 2 > tree
import sys
import os

default = "ms 40 5 -t 10 -r 0 500 -I 2 20 20 -T -M -q 500 -ej 1.0  1 2 "
if len(sys.argv)<2:
    msarg = default.split()[:]
else:
    msarg = sys.argv[1:]
#print "#", len(sys.argv)
#print "#", sys.argv
#print "#", msarg

loci=long(msarg[2])
index = msarg.index('-I')
#print index,msarg[index],msarg[index+1]
numpop = long(msarg[index+1])
popstring = " ".join(msarg[index+2:index+numpop+2])
index = msarg.index('-q')
sites = msarg[index+1]
ms = " ".join(filter(None, msarg))
#print "@",ms,"@"
os.system(ms+" | grep \"^(\" > gugus")
g = open("gugus","r")
print "#SN"
print "#-1"
print "#"+str(numpop)
print "#"+popstring 
print "#"+str(loci)+" "+sites+" 2.000000"
rl = range(loci)

for i in rl:
    print "# rate among sites for locus 0 (1.000000)"
    print "#="
loc = 0    
for gi in g:
    loc += 1
    print "#$Locus "+str(loc)
    print "#$1.0"
    print gi,

