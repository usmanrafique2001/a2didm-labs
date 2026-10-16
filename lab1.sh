#!/bin/bash
# Lab 1: hash sensitivity
echo -n "model weight v1" | sha256sum
echo -n "model weight v2" | sha256sum
echo -n "model weight v3" | sha256sum
echo -n "model weight v1" | sha256sum   # run again: same hash (deterministic)

echo "checkpoint data" > ckpt.txt
sha256sum ckpt.txt
sed -i 's/data/dat4/' ckpt.txt
sha256sum ckpt.txt                       # one word changed: completely different hash
