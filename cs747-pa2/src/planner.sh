#!/bin/bash

mdp=$2
algorithm=$4

python3 algorithm.py --mdp $mdp --algorithm $algorithm
