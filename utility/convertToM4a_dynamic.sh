#!/bin/bash

shopt -s expand_aliases
source ~/.bashrc

INPUT_DIR="$1"

for i in "$INPUT_DIR"//*; do
    echo "$i"
    convertToM4A_force "$i"
done