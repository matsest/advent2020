#!/bin/bash

for d in */; do 
  echo "day $d"
  cd "$d" || 'not found'
  ./main.py
  cd .. 
  echo
done
