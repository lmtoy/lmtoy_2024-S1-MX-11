#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-11"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["J154506"] = \
 [ 111655, 111656, 111657, 111659, 111660, 111661, 111663, 111664, 111665, 111669, 111670, 111671,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}

pars1["J154506"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}

pars2["J154506"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
