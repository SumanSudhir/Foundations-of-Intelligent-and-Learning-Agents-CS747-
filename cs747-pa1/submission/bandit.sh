#!/bin/bash

#Echo first argument as ./bandit.sh
echo $2
--instance
in = "$2"
shift 2
#Now first argument is --instance
echo $2
al = "$2"
shift 2
#Now first argument is --algorithm
echo $2
rs = "$2"
shift 2
#Now first argument is --randomSeed
echo $2
ep = "$2"
shift 2
#Now first argument is --epsilon
echo $2
shift 2
hz = "$2"
#Now first argument is --horizon
echo $2
#python algorithm.py --instance ""
