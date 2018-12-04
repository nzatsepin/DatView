#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# datview/scripts/datupdate.py
# Update dat file
# Author Natasha Stander

import sys
import os
import argparse
import copy

sys.path.append(os.path.dirname(sys.path[0]))
from api.groupmgr import GroupMgr

parser=argparse.ArgumentParser(description='Read in a dat file and apply a group file to it.')
parser.add_argument('--group',default=None,required=True,help='The group file output by groupgen.py (groupcfg.txt), keeps files smaller and numeric by enuemrating strings')
parser.add_argument('--cols',default=None,nargs='+',help='The group columns to include in the output. If not provided, does all possible based on columns in datfile.')
parser.add_argument('--concatint',action='append',default=[],nargs='+',help='Concatenate integer columns with --. Useful for grouping on multiple values. Values are converted to integers before concatenation so there is no 0 padding. These columns are not output unless specifically added to --cols.')
parser.add_argument('--datfile',type=open,default=sys.stdin,help='the dat file')
parser.add_argument('--outfile',type=argparse.FileType('w'),default=sys.stdout,help='Output file name. Script does not support in-place editing.')
args=parser.parse_args()

groupmgr=GroupMgr(args.group,True)

dfile=args.datfile
out=args.outfile

cols=dfile.readline().split()
outcols=copy.deepcopy(cols)
allcols = copy.deepcopy(cols)

for row in args.concatint:
    allcols.append('--'.join(row))

possible = groupmgr.groups()
if args.cols is not None:
    possible = set(possible) & set(args.cols)
keptgroups=[]
for col in sorted(possible):
    if col in cols:
        outcols[cols.index(col)]=GroupMgr.prefix + col
        keptgroups.append(col)
    elif args.cols is not None or groupmgr.matchcol(col) in allcols:
        gcol=GroupMgr.prefix + col
        if gcol not in cols:
            outcols.append(gcol)
        keptgroups.append(col)

print(*outcols,sep='\t',file=out)
while True:
    line=dfile.readline()
    if not line:
        break

    values=line.split()
    cur = {}
    cur.update(zip(cols,values))

    for row in args.concatint:
        l=[]
        valid=True
        for v in row:
            if v in cur and cur[v] is not None:
                l.append(str(int(cur[v])))
            else:
                valid=False
        if valid:
            cur['--'.join(row)]='--'.join(l)    
    
    for g in keptgroups:
        gcol = GroupMgr.prefix + g
        v = groupmgr.match(g,cur.get(groupmgr.matchcol(g),-1))
        if v is not -1:
            cur[gcol] = v # Allow keeping existing value on regrouping if new value not found.

    for col in outcols:
        if col in cur and cur[col] is not None:
            print(cur[col],end='\t',file=out)
        else:
            print(-1,end='\t',file=out)
    print('\n',end='',file=out)






