#!/bin/bash

instance=$2
algorithm=$4
randomSeed=$6
epsilon=$8
shift
horizon=$9

python3 algorithm.py --instance $instance --algorithm $algorithm --randomSeed $randomSeed --epsilon $epsilon --horizon $horizon
